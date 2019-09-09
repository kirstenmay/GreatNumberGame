from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "SecretsOfDojo"

@app.route("/")
def index():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    if 'attempt' not in session:
        session['attempt'] = 0
    print('*'*40, session['num'])
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session['guess'] = int(request.form['guess'])
    if session['guess'] > session['num']:
        session['alert'] = "High"
        session['attempt'] += 1
        return redirect("/")
    elif session['guess'] < session['num']:
        session['alert'] = "Low"
        session['attempt'] += 1
        return redirect("/")
    elif session['guess'] == session['num']:
        session['alert'] = "Correct"
        session['attempt'] += 1
        return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)