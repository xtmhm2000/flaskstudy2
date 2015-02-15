from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main

@main.route('/')
@main.route('/index')
def index():
    return 'Hello,word'