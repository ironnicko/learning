from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", content=['Nikhil', "Harini"])

@app.route("/nowhere")    
def nowhere():
    return render_template("application.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
@app.route("/example")
def example():
    return render_template("example.html")
    
@app.route("/<usr>")
def user(usr):
    return f"<h1>Hello {usr}!</h1>"

@app.route("/admin/")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
