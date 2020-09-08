#flask'ın kendisini ve bir yardımcı elemanı olan rendertempate'i içeri aktardık. render template adı üstünde 
#template içindekileri renderlayacak.
from flask import Flask, render_template

#app diye belirttiğimiz ifadeyi aşağıda route belirtirken kulllanıyoruz.
app= Flask(__name__)

@app.route("/")
def index():
    #flask bu uygulamanın olduğu yerde "templates" isimli bir dosya arar. içinde index.html adlı dosyayı açar.
    return render_template("index.html")

#headline: index.html dosyasına girip o sayfayı /headline sayfasına bağlarken sayfa içerisindeki {{headline}},
#içeriğini buradaki headline içeriğiyle değiştirerek return etmiş olduk.
@app.route("/headline")
def headline():
    headline = "Hello World???"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

#route adı üstünde sayfa üzerinde gezinebileceğimiz url ve iç sayfaları oluşturuyor. örneğin burada url 
#yanına faruk gelirse sayfada selamlar faruk yazması gerekiyor.
@app.route("/faruk")
def faruk():
    return "Selamlar, Faruk!!!"

#burada yaptığımız değişiklik ise url'ye eklenen kısım her ne ise o kısmın kopyalanıp websayfası içerisinde
#bir dönüt olarak geri döndürülmesi.
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Selamlar, {name}!"