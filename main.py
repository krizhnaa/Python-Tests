# from flask import Flask
#
# app = Flask(__name__)
# print(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# if __name__ == "__main__":
#     app.run()

import time


def decorator_func(function):
    def wrapper_function():
        time.sleep(1)
        function()
        time.sleep(1)
        function()
    return wrapper_function


@decorator_func
def say_krish():
    print("Krishhh")


say_krish()