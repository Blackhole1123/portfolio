from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
import json

blog = Blueprint(
    "blog",
    __name__,
    template_folder="./templates",
    static_folder="./static",
    url_prefix="/blog",
)

def recent_posts():
    o = open("posts.json", "r")
    posts = o.readlines()
    o.close()
    posts = [json.loads(post) for post in posts]
    posts.reverse()
    return posts

@blog.route("/")
def blog_home():
    return render_template("blog.html", posts=recent_posts())

@blog.route("/<name>")
def post(name):
    return render_template(f"blogposts/{name}.html")