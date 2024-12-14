from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database Initialization
def init_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_or_mobile TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    connection.close()

# Route to the Sign-Up page (Home Page)
@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email_or_mobile = request.form['email_or_mobile'].strip()
        password = request.form['password'].strip()
        email_error = None
        password_error = None

        # Email or Mobile Validation
        email_or_mobile_pattern = r'^([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})|([0-9]{10})$'
        if not email_or_mobile:
            email_error = "Email or Mobile Number is required."
        elif not re.match(email_or_mobile_pattern, email_or_mobile):
            email_error = "Invalid Email or Mobile Number format."

        # Password Validation
        if not password:
            password_error = "Password is required."
        elif len(password) < 6:
            password_error = "Password must be at least 6 characters long."

        if email_error or password_error:
            flash('Please correct the errors before submitting.', 'error')
            return render_template('signup.html', email_error=email_error, password_error=password_error)

        hashed_password = generate_password_hash(password)
        try:
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO users (email_or_mobile, password_hash) VALUES (?, ?)', (email_or_mobile, hashed_password))
            connection.commit()  # Commit changes before closing the connection
            connection.close()
            flash('Sign-Up Successful! Welcome!', 'success')
            return redirect(url_for('login'))  # Redirect to the Login page
        except sqlite3.IntegrityError as e:
            flash(f'Error: {str(e)}', 'error')

    return render_template('signup.html')

# Route to the Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_mobile = request.form['email_or_mobile'].strip()
        password = request.form['password'].strip()
        email_error = None
        password_error = None

        # Email or Mobile Validation
        email_or_mobile_pattern = r'^([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})|([0-9]{10})$'
        if not email_or_mobile:
            email_error = "Email or Mobile Number is required."
        elif not re.match(email_or_mobile_pattern, email_or_mobile):
            email_error = "Invalid Email or Mobile Number format."

        # Password Validation
        if not password:
            password_error = "Password is required."
        elif len(password) < 6:
            password_error = "Password must be at least 6 characters long."

        if email_error or password_error:
            flash('Please correct the errors before submitting.', 'error')
            return render_template('login.html', email_error=email_error, password_error=password_error)

        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE email_or_mobile = ?', (email_or_mobile,))
        user = cursor.fetchone()
        connection.close()

        if user and check_password_hash(user[0], password):
            flash('Login Successful!', 'success')
            return redirect(url_for('welcome'))  # Correct redirection to the Welcome page
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')

# Route to the Welcome page
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
