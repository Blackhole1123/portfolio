from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash, g, session, abort
from waitress import serve
from static import blog

app = Flask('app')
@app.route('/')
def index():
    return render_template('index.html')

#initialize the blueprint
app.register_blueprint(blog.blog, url_prefix='/blog')

app.run(host='0.0.0.0', port='8080', debug=True) 