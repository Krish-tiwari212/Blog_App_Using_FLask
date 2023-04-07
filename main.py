from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    c = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    c = c.json()
    return render_template("index.html", lis=c)
@app.route("/post/<num>")
def posts(num):
    c = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    c = c.json()
    return render_template("post.html", lis=c,n=num)
if __name__ == "__main__":
    app.run(debug=True)
