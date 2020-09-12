from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formasindex.html")

@app.route("/hello", methods=["POST"])
def hello():
    #giriş sayfası olan formsindex.html'den aldığımız ve name içine koyduğumuz isim bilgisini 
    # çekiyoruz. Çektikten sonra aşağıda name olarak çağırıp hello.html içine sokuyoruz.
    name = request.form.get("name")
    return render_template("hello.html",name=name)

