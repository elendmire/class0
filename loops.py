from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    names = ["Alice", "Bob", "Faruk"]
    return render_template("loopindex.html", names= names)

