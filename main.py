from flask import Flask, render_template, request, redirect, url_for
from waitress import serve

app = Flask('app')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

serve(app, host='192.168.1.70', port=8080)
