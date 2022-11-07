from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session and 'password' in session:
        return render_template('login.html')
    return render_template('login.html', problem = 'bad')
    # elif 'username' not in session and 'password' not in session:
    #     return render_template('login.html', problem = 'juju')
    # elif 'username' not in session:
    #     return render_template('login.html', problem = 'bad username')
    # elif 'password' not in session:
    #     return render_template('login.html', problem = 'bad password')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return render_template('response.html', username = 'username')
    # return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return 'byebye'

if __name__ == "__main__":
    app.debug = True
    app.run()
