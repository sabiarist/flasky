from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def indice(name):
    return "<h1> Bonjour, {}! </h1>".format(name)


app.add_url_rule('/home/<name>', 'indice', indice)


if __name__ == '__main__':
    app.run()
