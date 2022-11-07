##DICOS:
- You can have just the submit form as a button to redirect you!!
- Made sure to check for empty responses, but since the form username and password start off as empty strings, there is no need to worry!
```
session['username'] = request.form['username']
```
This seems to set the session username to the username that was inputted. Then,
```
if 'username' in session
```
checks to see if there is a value for the 'username' key in the Session object.
- It's helpful to think of a session object as a dictionary object.
