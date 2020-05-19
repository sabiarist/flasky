from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/redirect')
def redirect():
    return redirect('http://senfood.pe.hu/')


# creates a response object and then sets a cookie in it
@app.route('/response')
def response():
    response = make_response("<h1> This document carries a cookie! </h1>")
    response.set_cookie('answer', '42')
    return response


def load_user(id):
    pass


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


if __name__ == '__main__':
    app.run()
