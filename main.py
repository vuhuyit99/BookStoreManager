from flask import render_template, request, redirect, url_for, jsonify, send_file, session
from BookStoreManager.models import *

from flask_login import login_user
from BookStoreManager import app, login
import hashlib
# from saleapp import decorator
# import json
import flask_admin

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.loginname == username.strip(),
                             User.password == password.strip()).first()
        if user:
            login_user(user=user)
    return redirect("/admin")

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    app.run(debug=True, port=5000)