# from flask import Flask, request, redirect, url_for, render_template, flash
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_bootstrap import Bootstrap
# import mysql.connector

# app = Flask(__name__)
# app.secret_key = 'temporary_key'
# Bootstrap(app)  # Initialize Flask-Bootstrap

# # Function to connect to AWS RDS MySQL database
# def get_db_connection():
#     return mysql.connector.connect(
#         host='clonedb.cvcweiusacog.us-east-1.rds.amazonaws.com',  
#         user='admin',
#         password='Flaskdb69',
#         database='clone_db'
#     )

# # Home Route
# @app.route('/')
# def home():
#     return render_template('home.html')

# # Registration Route
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = generate_password_hash(request.form['password'])

#         try:
#             conn = get_db_connection()
#             cursor = conn.cursor()
#             cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
#             conn.commit()
#             flash('Registration successful! Please log in.', 'success')
#         except mysql.connector.Error as err:
#             flash(f'Error: {err}', 'danger')
#         finally:
#             conn.close()

#         return redirect(url_for('login'))
#     return render_template('register.html')

# # Login Route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         try:
#             conn = get_db_connection()
#             cursor = conn.cursor()
#             cursor.execute('SELECT password FROM users WHERE username = %s', (username,))
#             result = cursor.fetchone()
#         except mysql.connector.Error as err:
#             flash(f'Error: {err}', 'danger')
#             return render_template('login.html')
#         finally:
#             conn.close()

#         if result and check_password_hash(result[0], password):
#             flash('Login successful!', 'success')
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials. Please try again.', 'danger')
#             return redirect(url_for('login'))

#     return render_template('login.html')

# # Dashboard Route
# @app.route('/dashboard')
# def dashboard():
#     # Example URLs for course material from S3
#     course_urls = [
#         "https://clonebucket23.s3.us-east-1.amazonaws.com/Internshala+Assignment+(1).pdf",
#         "https://clonebucket23.s3.us-east-1.amazonaws.com/web+security+issues+and+tranpost+layer.pdf"
#     ]
#     return render_template('dashboard.html', course_urls=course_urls)

# # Logout Route
# @app.route('/logout')
# def logout():
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('login'))

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(_name_)
app.secret_key = 'temporary_key'

def get_db_connection():
    return mysql.connector.connect(
        host='flashdb.c7g4csqm6jl5.us-east-1.rds.amazonaws.com',
        user='admin',
        password='Flaskdb69',
        database='flashdb'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, password_hash) VALUES (%s, %s)',
            (username, hashed_password)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE username = %s', (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result and check_password_hash(result[0], password):
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')


# Dashboard Route (after login)
@app.route('/dashboard')
def dashboard():
    course_urls = [
        'https://clonebucker1.s3.us-east-1.amazonaws.com/python_code.pdf',
        'https://clonebbucket.s3.amazonaws.com/PYTHON%2BPhttps://clonebucker1.s3.us-east-1.amazonaws.com/PYTHON%2BPROGRAMMING%2BNOTES.pdf'
    ]
    
    return render_template('dashboard.html', course_urls=course_urls)

# Home Route (Landing Page)

@app.route('/')

def home():

    return render_template('home.html')



# Logout

@app.route('/logout')

def logout():

    return redirect(url_for('login'))



if _name_ == '_main_':

    app.run(host="0.0.0.0", port=5000,debug=True)