from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'John'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ash'},
            'body': 'Beautiful day in New York!'
        },
        {
            'author': {'username': 'Kevin'},
            'body': 'Great time at Aponia!'
        },
        {
            'author': {'username': 'Rogers'},
            'body': 'Aponia rules!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
