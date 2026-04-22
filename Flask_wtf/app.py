from flask import Flask, redirect, render_template, flash, request, url_for
from forms import RegistrationForm


app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/", methods = ["GET", "POST"])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name} You registered Successfully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form = form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)