from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/')
def main():
    return open('./web/index.html', 'r', encoding='utf-8').read()


@app.route('/solution')
def solution():
    return open('./solution/web/index.html', 'r', encoding='utf-8').read()


@app.route('/solution/red')
def solution_red():
    return open('./solution/web/red.html', 'r', encoding='utf-8').read()


@app.route('/solution/orange')
def solution_orange():
    return open('./solution/web/orange.html', 'r', encoding='utf-8').read()


@app.route('/solution/yellow')
def solution_yellow():
    return open('./solution/web/yellow.html', 'r', encoding='utf-8').read()


@app.route('/solution/green')
def solution_green():
    return open('./solution/web/green.html', 'r', encoding='utf-8').read()


@app.route('/solution/blue')
def solution_blue():
    return open('./solution/web/blue.html', 'r', encoding='utf-8').read()


@app.route('/solution/purple')
def solution_purple():
    return open('./solution/web/purple.html', 'r', encoding='utf-8').read()


@app.route('/solution/black')
def solution_black():
    return open('./solution/web/black.html', 'r', encoding='utf-8').read()


@app.route('/solution/unknown')
def solution_unknown():
    return open('./solution/web/unknown.html', 'r', encoding='utf-8').read()


@app.route('/api/problem/<pid>')
def api_problem(pid):
    return jsonify(
        json.load(open(f'./solution/data/problem/{pid}.json', 'r', encoding='utf-8'))
    )


@app.route('/api/solution/<pid>')
def api_solution(pid):
    return jsonify(
        json.load(open(f'./solution/data/solution/{pid}.json', 'r', encoding='utf-8'))
    )


if __name__ == '__main__':
    app.run(
        port=8700,
        host='0.0.0.0',
    )

