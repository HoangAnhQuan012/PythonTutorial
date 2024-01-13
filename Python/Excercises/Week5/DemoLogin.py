from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/success/<name>/<age>/<address>")
def success(name, age, address):
    return "Welcome %s, you are %s years old and you live at %s" % (name, age, address)

@app.route("/show", methods = ["POST", "GET"])
def show():
    if request.method == "POST":
        name = request.form["txtname"]
        age = request.form["txtage"]
        address = request.form["txtaddress"]
        return redirect(url_for("success", name = name, age = age, address = address))
    else:
        name = request.args.get("txtname")
        age = request.args.get("txtage")
        address = request.args.get("txtaddress")
        return redirect(url_for("success", name = name))
    
if __name__ == "__main__":
    app.run(debug=True)
