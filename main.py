from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from datetime import datetime as dt
from post import Post
from form import Form, LoginForm
from flask_wtf import CSRFProtect
import requests
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
CSRFProtect(app)
Bootstrap5(app)

API_URL = "https://api.npoint.io/8bd73f4fedbaf037a112"

def fetch_posts():
    blogs = requests.get(API_URL).json()
    posts = []
    for blog in blogs:
        post = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
        posts.append(post)
    return posts

@app.route("/")
def homepage():
    posts = fetch_posts()
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone_number.data
        message = form.message.data
        return render_template("submit.html", name=name, email=email, phone=phone, message=message)
    return render_template("contact.html", form=form)

@app.route("/post/<int:num>")
def get_post(num):
    posts = fetch_posts()
    return render_template("post.html", posts=posts, num=num)

@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # Add the login logic here
        if email == "admin@skynet.com" and password == "123456":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)

@app.context_processor
def inject_current_year():
    return {"current_year": dt.now().year}


if __name__ == "__main__":
    app.run(debug=True)