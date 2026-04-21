from flask import Flask, redirect, request, url_for, session, render_template

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()  # DEBUG

    if username == "admin" and password == "123":
        return redirect(url_for("welcome"))
    else:
        return "Invalid credentials"


@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("welcome.html", name=session["user"])
    else:
        return redirect(url_for("login.html"))


@app.route("/logout")
def logout():
    return redirect(url_for("login.html"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)