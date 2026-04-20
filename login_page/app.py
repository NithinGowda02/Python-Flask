from flask import Flask, redirect, request, Response, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return "Invalid credentials"

    return '''
        <h2>Login Page</h2>
        <form method="POST">
            USERNAME : <input type="text" name="username"><br><br>
            PASSWORD : <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>WELCOME {session["user"]}!</h2>
            <a href="/logout">Logout</a>
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)