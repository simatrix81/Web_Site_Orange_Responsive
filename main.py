from flask import Flask, render_template,url_for


app = Flask(__name__)
app.secret_key = "website"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Kimiz")
def about():
    return render_template("about.html")

@app.route("/Nedir")
def product():
    return render_template("product.html")

@app.route("/Contact_Us")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #app.run(debug="True")   