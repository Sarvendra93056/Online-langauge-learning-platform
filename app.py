from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
    conn.close()

    if user:
        session['user'] = username
        return redirect('/dashboard')
    return "Invalid Login ❌"

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect('/')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0

        if request.form['q1'].lower() == "hola":
            score += 1
        if request.form['q2'].lower() == "adios":
            score += 1

        return render_template('quiz.html', score=score)

    return render_template('quiz.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

app.run(debug=True)