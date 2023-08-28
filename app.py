from flask import Flask, url_for, render_template, redirect, request, flash, session
import requests
import json
import urllib.parse
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)  # Set session lifetime

API_URL = "https://opentdb.com/api.php"  # Centralize API URL


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sort", methods=['POST'])
def sort():
    dict_data = request.form
    encoded_data = urllib.parse.urlencode(dict_data)
    return redirect(url_for('newexam', encoded_data=encoded_data))


@app.route("/newexam/<encoded_data>")
def newexam(encoded_data):
    dict_data = urllib.parse.parse_qs(encoded_data)
    dict_data["type"] = "multiple"
    
    try:
        response = requests.get(API_URL, params=dict_data)
        response.raise_for_status()
        data = response.json()
        question_bank = data["results"]
    except requests.exceptions.RequestException:
        return render_template("error.html")
    
    name = dict_data.get("name", [""])[0]  # Use get to avoid KeyError
    session['username'] = name
    session['loggedin'] = True
    # Save questions to a JSON file
    with open(name + '.json', 'w') as f:
        json.dump(question_bank, f)
    
    return render_template("start.html", questions=question_bank, name=name)


@app.route("/startexam/<name>")
def startexam(name):
    try:
        with open(name + '.json', 'r') as f:
            question_bank = json.load(f)
        if not question_bank:
            flash('Insufficient questions')
            return redirect(url_for('index'))
        return render_template('exam.html', questions=question_bank, session=session, name=name)
    except FileNotFoundError:
        flash('File not found')
        return redirect(url_for('index'))


@app.route('/endsession', methods=['POST'])
def endsession():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
