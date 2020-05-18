from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://senfood.pe.hu/')


# creates a response object and then sets a cookie in it
@app.route('/response')
def response():
    response = make_response("<h1> This document carries a cookie! </h1>")
    response.set_cookie('answer', '42')
    return response


@app.route('/user')
def user():
    user_agent = request.headers.get('User-Agent')
    return '<p> Your browser is {} </p>'.format(user_agent)


def load_user(id):
    pass


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name) 


def name(name):
    return "<h1> Bonjour, {}! </h1>".format(name)


app.add_url_rule('/user/<name>', 'name', name)

if __name__ == '__main__':
    app.run()
