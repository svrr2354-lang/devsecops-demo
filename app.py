from flask import Flask, request, render_template_string, g
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'demo.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )''')
        # Insert dummy admin if not exists
        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
            db.commit()

@app.route('/')
def home():
    return render_template_string("""
        <div style='text-align: center; margin-top: 50px;'>
            <h1>🏦 Vulnerable Bank Demo</h1>
            <a href="/login" style='font-size: 20px;'>Login Here</a>
        </div>
    """)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # ------------------------------------------------------------------
        # VULNERABILITY LAB: SQL Injection
        # We are intentionally using an f-string to insert user input.
        # This allows the 'OR 1=1' hack to work.
        # ------------------------------------------------------------------
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        # Print the exact query to the terminal so you can see the hack
        print(f"\n[⚠️ DEBUG] SQL Query Executed: {query}\n") 

        cursor = get_db().cursor()
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                message = f'✅ Login successful! Welcome, {user[1]}. Access Granted.'
            else:
                message = '❌ Login failed. Invalid credentials.'
        except Exception as e:
            message = f"Database Error: {e}"

    return render_template_string("""
        <div style='text-align: center; margin-top: 50px;'>
            <h1>Login</h1>
            <form method="POST">
                Username: <input name="username" size="40"><br><br>
                Password: <input name="password" type="password" size="40"><br><br>
                <button type="submit">Login</button>
            </form>
            <p style="font-weight:bold; font-size: 18px;">{{message}}</p>
            <a href="/">Back to home</a>
        </div>
    """, message=message)

if __name__ == '__main__':
    # Initialize DB only if it doesn't exist
    if not os.path.exists(DATABASE):
        init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)