from flask import Flask, render_template, request
from joblib import load
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("app.html")
    else:
        model = load("model/model.joblib")
        age = model.predict(request.form.to_dict(flat=False)["content"])[0][0]
        type = model.predict(request.form.to_dict(flat=False)["content"])[0][1]
        return render_template("app.html", age=age, type=type)


if __name__ == "__main__":
    app.run(debug=True)