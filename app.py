from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='123456',  # Replace with your MySQL password
        database='registration'  # Replace with your database name
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM New_user WHERE email = %s or username = %s', (email, username))
        existing_user = cursor.fetchone()

        if existing_user:
            if existing_user[3] == email:
                flash('Email already exists!. Please use a different email.', 'danger')
            elif existing_user[2] == username:
                flash('Username already exists!. Please use a different username.', 'danger')
        else:            
            try:
                cursor.execute('INSERT INTO New_user (full_name, username, email, password) VALUES (%s, %s, %s, %s)', (full_name,username, email, hashed_password))
                connection.commit()
                flash('Registration successful! You can now login.', 'success')
            except mysql.connector.Error as err:
                flash(f'Error: {err}', 'danger')
            finally:
                cursor.close()
                connection.close()

        return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login_input = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM New_user WHERE username = %s OR email = %s', (login_input, login_input))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user and check_password_hash(user[4], password):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email/username or password', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)