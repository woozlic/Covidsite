from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html', sidebar=True)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html', sidebar=False)