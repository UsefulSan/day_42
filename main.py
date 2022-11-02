from flask import render_template, request
from app import *


# @app.route('/users/<id>')
# def users(id):
#     return render_template(
#         'index.html',
#         name=id,
#     )


@app.route('/')
def index():
    return 'Hello'


@app.route('/users/')
def get_users():
    users = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    term = request.args.get('term')
    users = filter(lambda x: term in x, users)
    return render_template('users/users.html',
                           users=users,
                           search=term)


if __name__ == '__main__':
    app.run(debug=True)
