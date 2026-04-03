from flask import Flask, Request, redirect, Response, url_for,session

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def login():
    if Request.methods == "POST":
        userName = Request.form.get("username")
        password = Request.form.get("password")

        if userName == "admin" and password == "123":
            session["user"] = userName
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid Credentials, Try again", mimetype="text/plain")
    return '''
            <h2> Login Page</h2>
            <form method = "POST">
            username: <input type = "text" name="username"><br>
            password: <input type = "text" name = "password"><br>
            <input type = "submit" name = "Login">
            '''    