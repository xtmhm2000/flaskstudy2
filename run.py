from app import create_app
if __name__ == '__main__':
    app1=create_app()
    app1.run(debug=True)
#
#
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'
#
# if __name__ == '__main__':
#     app.run(debug=True)