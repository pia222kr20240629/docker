from flask import Flask, request, render_template_string, redirect, url_for
import psycopg2
app = Flask(__name__)

DATABASE_URL = 'postgresql://postgres:password@db:5432/mydatabase'

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts ORDER BY created_at DESC')
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string('''
        <h1>board</h1>
        <a href="{{ url_for('register')}}">signUp</a>
        <a href="{{ url_for('post_message')}}">new content</a>
        <ul>
            {% for post in posts  %}
                <li><strong>{{ post[1] }}</strong> - {{ post[2}} <br> {{ post[3] }}  </li>
            {% endfor %}
        </ul>
    ''', posts=posts)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (username, password) VALUES({username}, {password)}")
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_templage_string('''
        <h1>signIn</h1>
        <form method='post'>
            username: <input type="text" name="username" required><br>
            password: <input type="text" name="password" required><br>
            <input type="submit" value="signIn">
        </form>
        <a href="{{ url_for('index'}}">return to Home</a>

    ''')

@app.route('/post', method=['GET','POST'])
def post_message():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO posts(title,content) VALUES({title}, {content})")
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_templage_string('''
        <h1>new content</h1>
        <form method = 'post'>
            title: <input type="text" name="title" required><br>
            content: <textarea name="content" required></textarea><br>
            <input type="submit" value = "new content">
        </form>
        <a href = "{{url_for('index')}}"> return to Home </a>
    ''')

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

    


