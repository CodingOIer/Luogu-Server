import json


def make_index(red, orange, yellow, green, blue, purple, black, unknown):
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>总览 | CodingOIer's 洛谷题解站</title>
</head>

<body>
    <center>
        <h1>总览 | <a href="https://www.luogu.com.cn/user/754324" target="_blank">CodingOIer</a>'s 洛谷题解站</h1>
        <h2>爬了洛谷的所有题目，由于工程量较大，预计 1 周更新一次。</h2>
        <h2>数据库已经达到了 800MiB</h2>
        <a href="solution/red" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(254, 76, 97); color: white;">入门（共 {red} 道）</h3>
        </a>
        <a href="solution/orange" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(243, 156, 17); color: white;">普及−（共 {orange} 道）</h3>
        </a>
        <a href="solution/yellow" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(255, 193, 22); color: white;">普及/提高−（共 {yellow} 道）</h3>
        </a>
        <a href="solution/green" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(82, 196, 26); color: white;">普及+/提高（共 {green} 道）</h3>
        </a>
        <a href="solution/blue" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(52, 152, 219); color: white;">提高+/省选−（共 {blue} 道）</h3>
        </a>
        <a href="solution/purple" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(157, 61, 207); color: white;">省选/NOI−（共 {purple} 道）</h3>
        </a>
        <a href="solution/black" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(14, 29, 105); color: white;">NOI/NOI+/CTSC（共 {black} 道）
            </h3>
        </a>
        <a href="solution/unknown" target="_blank">
            <h3 style="width: 300px; height: 30px; background: rgb(191, 191, 191); color: white;">暂无评定（共 {unknown} 道）</h3>
        </a>
    </center>
</body>

</html>"""


cnt = []

red = ''
orange = ''
yellow = ''
green = ''
blue = ''
purple = ''
black = ''
unknown = ''

if __name__ == '__main__':
    with open('./problem_data.json') as f:
        data = json.load(f)
    for _ in range(8):
        cnt.append(0)
    for x in data:
        print(f'Updating {x["pid"]}')
        try:
            with open(f'./data/solution/{x["pid"]}.json', 'r') as f:
                temp = json.load(f)
            if not temp['acceptSolution']:
                continue
            print(f'Find {x["pid"]} can submit solution')
            pid = temp['problem']['pid']
            name = temp['problem']['pid'] + ' ' + temp['problem']['title']
            diff = temp['problem']['difficulty']
            cnt[diff] += 1
            if diff == 0:
                unknown += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 1:
                red += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 2:
                orange += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 3:
                yellow += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 4:
                green += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 5:
                blue += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 6:
                purple += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
            elif diff == 7:
                black += f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_black">{name}</a><br>'
        except:
            print(f'Failed to get information of {x["pid"]}')
    with open('./web/index.html', 'w', encoding='utf-8') as f:
        f.write(make_index(cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], cnt[6], cnt[7], cnt[0])
        )
    with open('./web/red.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + red
        )
    with open('./web/orange.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + orange
        )
    with open('./web/yellow.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + yellow
        )
    with open('./web/green.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + green
        )
    with open('./web/blue.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + blue
        )
    with open('./web/purple.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + purple
        )
    with open('./web/black.html', 'w', encoding='utf-8') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + black
        )
    with open('./web/unknown.html', 'w') as f:
        f.write(
            '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer's 洛谷题解站</title>
</head>'''
            + unknown
        )

