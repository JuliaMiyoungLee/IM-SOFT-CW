# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
__main__
127.0.0.1 - - [04/Oct/2022 08:57:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [04/Oct/2022 08:57:38] "GET /favicon.ico HTTP/1.1" 404 -

QCC:
0. Not too sure...
1. Base folder for Ubuntu.
2. It would print to a file in the route that was given, in this case "\". Maybe.
3. It would print the name of the folder it's in, in this case __main__.
4. The file will contain the return string, "No hablo queso!".
5. In java you can run non static functions by calling them with Object.function().
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''