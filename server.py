from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gr = gender_response.json()
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    ar = age_response.json()
    return render_template('index.html', gr=gr, ar=ar)


if __name__ == "__main__":
    app.run(debug=True)


