from flask import Flask, render_template, request
from model import check_sentiment
a = Flask(__name__)
@a.route("/")
def home():
    return render_template("index.html")
@a.route("/result", methods = ['POST'])
def result():
    if request.method == "POST":
        f = request.form["input"]
        newinput = f"""{f}"""
        predection = check_sentiment(newinput)
        return render_template("resultpage.html", pred=predection)
if __name__ == '__main__':
    a.run(debug=True)