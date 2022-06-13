from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route('/hi')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello/<username>')
def say_hello(username):
    return f'Hello {username} !'


@app.route('/')
def index():
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return Response('<pre>' + r.text + '</pre>')


if __name__ == '__main__':
    app.run()
