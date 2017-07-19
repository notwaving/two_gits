from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return render_template("welcome.html")


app.run(debug=True) # enables helpful terminal messages to identify errors
