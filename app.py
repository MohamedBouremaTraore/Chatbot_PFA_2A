from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'This project aim to create a chateboot for a virtual bank using flask'


if __name__ == '__main__':
    app.run()
