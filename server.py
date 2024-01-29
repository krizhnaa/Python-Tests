from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gr = gender_response.json()['gender']
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    ar = age_response.json()['age']
    return render_template('index.html', name=name, gr=gr, ar=ar)

# name = "Angela"
# gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
# gr = gender_response.json()['gender']
# age_response = requests.get(url=f"https://api.agify.io?name={name}")
# ar = age_response.json()['age']
# print(gr)
# print(ar)

if __name__ == "__main__":
    app.run(debug=True)


