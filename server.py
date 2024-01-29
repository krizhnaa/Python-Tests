from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(0, 10)
    current_year = datetime.now().year
    return render_template('index.html', random_num=random_num, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)


