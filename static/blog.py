from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
import json, os

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
    print(posts[:5])
    return posts[:5]

@blog.route("/")
def blog_home():
    return render_template("blog.html", posts=recent_posts())

@blog.route("/post/<name>")
def post(name):
    fn = f'{name}.html'
    # if fn is not in the folder templates/blogposts, abort
    if fn not in os.listdir("./templates/blogposts"):
        return render_template('blog-error.html', error="Post not found")
    return render_template(f"blogposts/{name}.html")

@blog.route("/api/<name>")
def post_api(name):
    name = name.replace("-", " ")
    name = name.lower()
    o = open("posts.json", "r")
    posts = o.readlines()
    o.close()
    posts = [json.loads(post) for post in posts]
    for post in posts:
        pn = post["name"]
        pn = pn.lower()
        if pn == name:
            return post
    notfound = {"error": "Post not found"}
    return notfound

@blog.route('/category/<category>')
def category(category):
    o = open("posts.json", "r")
    posts = o.readlines()
    o.close()
    posts = [json.loads(post) for post in posts]
    posts = [post for post in posts if category in post["categories"]]
    posts.reverse()
    if len(posts) == 0:
        return render_template("blog-error.html", message="No posts found")
    return render_template("blog.html", posts=posts)