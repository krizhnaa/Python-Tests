from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/blog")
def home():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blogs = blog_response.json()
    return render_template('index.html', blogs=blogs)

# blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
# blogs = blog_response.json()
# print(blogs)

if __name__ == "__main__":
    app.run(debug=True)


