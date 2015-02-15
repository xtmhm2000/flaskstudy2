from flask import render_template
from app.main import main
@main.route('/2')
@main.route('/index2')
def index2():
    return 'Hello,word'
