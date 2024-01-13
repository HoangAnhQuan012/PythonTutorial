from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/registerForm")
def Employee():
    return render_template("RegisterForm.html")

@app.route("/register", methods = ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("Show.html", result = result)
    
if __name__ == "__main__":
    app.run(debug=True)