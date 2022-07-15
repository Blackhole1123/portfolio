from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash, g, session, abort
from waitress import serve
from static import blog, errors

app = Flask(__name__)
app.secret_key = '(1yHf(#e4P$*_#MK'

@app.route('/')
def index():
    return render_template('index.html')

#sitemap
@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')

#initialize the blueprint
app.register_blueprint(blog.blog, url_prefix='/blog')
app.register_blueprint(errors.errors)

app.run(host="0.0.0.0", port='8080', debug=True)