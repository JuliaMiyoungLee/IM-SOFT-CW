"""QR CODE GENERATORS: JEFFREY ZOU, JULIA LEE, WILLIAM
SoftDEV
K19 Session
11-07-2022
time spent: 1 hr - ish?
"""


from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'sje938__`+sdf??/sdie'

@app.route('/')
def index():
    if 'username' in session and 'password' in session:
        return render_template('login.html')
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if request.form['username'] == 'QRGENz' and request.form['password'] == 'Coolests':
            return render_template('response.html', username = 'QRGENz')
        elif request.form['username'] != 'QRGENz' and request.form['password'] != 'Coolests':
            return render_template('login.html', problem = 'bad juju')
        elif request.form['username'] != 'QRGENz':
            return render_template('login.html', problem = 'bad user')
        elif request.form['password'] != 'Coolests':
            return render_template('login.html', problem = 'bad pass')
    # return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('login.html', problem = 'You have been logged out')

if __name__ == "__main__":
    app.debug = True
    app.run()
