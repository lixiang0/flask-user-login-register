from flask import Flask,request,render_template,flash,session
from user import User
import functools

app=Flask(__name__)
app.secret_key = '123123'
u=User()# 用户示例

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error=None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif username=='user':
            error='duplicate name.'

        if error is None:
            u.username = username
            u.password = password
            return render_template('login.html')

        flash(error)

    return render_template('register.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error=None
        if username != u.username:
            error = 'Incorrect username.'
        elif password != u.password:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = username

            return render_template('index.html')

        flash(error)

    return render_template('login.html')


@app.route('/index', methods=['GET'])
def index():
    if 'user_id' in session:
        if session['user_id'] is not None:
            return render_template('index.html')
    else:
        return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')
if __name__ == "__main__":


    app.run(host='0.0.0.0', port=8085, debug=True)