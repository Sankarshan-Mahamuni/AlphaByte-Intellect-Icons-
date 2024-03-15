from flask import render_template, request, redirect, url_for, session
from app import app

# Hardcoded password for testing
PASSWORD = "testpassword123"

@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        password = request.form['password']
        if password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('orientation'))
        else:
            return "Invalid password. Please try again."
    return render_template('signin.html')

@app.route('/orientation')
def orientation():
    return render_template('orientation.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('signin'))