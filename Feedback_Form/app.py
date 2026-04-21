from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")                          # ✅ new root route
def index():
    return redirect(url_for("feedback"))

@app.route("/home", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")
        return redirect(url_for("thankyou", name=name, message=message))
    return render_template("home.html")

@app.route("/thankyou")
def thankyou():
    name = request.args.get("name")
    message = request.args.get("message")
    return render_template("thankyou.html", name=name, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)