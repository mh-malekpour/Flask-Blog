from flask import session
from . import admin


@admin.route('/')
def index():
    return "Hello from admin Index"
    

@admin.route('/login')
def login():
    session['name'] = 'mohammad hossein'
    print(session.get('name'))
    # session.clear()
    return 'Login Page'