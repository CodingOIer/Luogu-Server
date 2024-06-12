import os
import requests
import json

cookie = '__client_id=x; _uid=x;'

data = {}


def get_headers(cookie=None):
    if cookie != None:
        h = {
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
    else:
        h = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
    return h


def check_problem(pid):
    try:
        with open(f'./data/solution/{pid}.json', 'r') as f:
            js = json.load(f)
        if js['acceptSolution']:
            return 1
        return 2
    except:
        return 0


def get_problem_information(pid):
    response = requests.get(
        url=f'https://www.luogu.com.cn/problem/{pid}?_contentOnly=1',
        headers=get_headers(),
    )
    if response.status_code == 200:
        js = json.loads(response.text)['currentData']
        with open(f'./data/problem/{pid}.json', 'w') as f:
            f.write(json.dumps(js))


def get_solution_information(pid):
    response = requests.get(
        url=f'https://www.luogu.com.cn/problem/solution/{pid}?_contentOnly=1',
        headers=get_headers(cookie),
    )
    if response.status_code == 200:
        js = json.loads(response.text)['currentData']
        with open(f'./data/solution/{pid}.json', 'w') as f:
            f.write(json.dumps(js))


if __name__ == '__main__':
    start = input()
    try:
        os.makedirs('./data/problem')
        os.makedirs('./data/solution')
    except:
        pass
    with open('./problem_data.json', 'r') as f:
        data = json.load(f)
    begin = True
    for x in data:
        if begin:
            if x['pid'] == start:
                begin = False
            continue
        print(f"Getting information {x['pid']}")
        r = check_problem(x['pid'])
        if r == 0:
            print(f'{x["pid"]} first get')
            get_problem_information(x['pid'])
            get_solution_information(x['pid'])
        elif r == 1:
            print(f'{x["pid"]} get information of solution again')
            get_solution_information(x['pid'])
        else:
            print(f'{x["pid"]} have done')
