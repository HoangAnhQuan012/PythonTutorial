from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/loginForm')
def success():
    return render_template('LoginForm.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        result = request.form
        return render_template("showInfo.html", result = result)
    
if __name__ == '__main__':
    app.run(debug = True)