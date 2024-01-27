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

# import time
#
#
# def decorator_func(function):
#     def wrapper_function():
#         time.sleep(1)
#         function()
#         time.sleep(1)
#         function()
#     return wrapper_function
#
#
# @decorator_func
# def say_krish():
#     print("Krishhh")
#
#
# say_krish()

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper_function():
    function()
    print(f"{function.__name__} run speed : {time.time() - current_time}")
  return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()