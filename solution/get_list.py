import requests
import json


def get_headers():
    h = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    }
    return h


def get_list(tp, pg):
    print(f'Getting type={tp} page={pg}')
    response = requests.get(
        url=f'https://www.luogu.com.cn/problem/list?type={tp}&page={pg}&_contentOnly=1',
        headers=get_headers(),
    )
    if response.status_code == 200:
        try:
            js = json.loads(response.text)['currentData']['problems']['result']
            return js
        except:
            return []
    return []


tps = ['P', 'B', 'CF', 'SP', 'AT', 'UVA']
start = {}

result = []

if __name__ == '__main__':
    start['P'] = 1
    start['B'] = 1
    start['CF'] = 1
    start['SP'] = 1
    start['AT'] = 1
    start['UVA'] = 1
    for tp in tps:
        errors = 0
        for i in range(start[tp], 500):
            r = get_list(tp, i)
            if len(r) == 0:
                print('ERROR!')
                errors += 1
                if errors >= 5:
                    break
                continue
            for x in r:
                result.append(x)
            errors = 0
            with open('./problem_data.json', 'w') as f:
                f.write(json.dumps(result))
