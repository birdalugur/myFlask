from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello/<username>')
def say_hello(username):
    return f'Hello {username} !'


if __name__ == '__main__':
    app.run()
