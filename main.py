from flask import Flask, request, render_template

app=Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def login():
    return render_template('user-signup.html')
 

@app.route("/verify", methods=["POST"])
def verify():
    username = request.form['username']
    password = request.form['password']
    password_ver = request.form['password_ver']
    email = request.form['email']

    username_error = ''
    if len(username) < 3: 
        username_error = "Username must be longer than 2 charaters"
    elif len(username) > 20:
        username_error = "Username must be shorter than 20 characters"
    elif ' ' in username:
        username_error = "Username must not contain spaces"
    
    password_error= ''
    if password == '':
        password_error = "Please enter a password"
    elif ' ' in password:
        password_error = "Password must not contain spaces"
    elif len(password) < 3: 
        password_error = "Password must be longer than 2 charaters"
    elif len(password) > 20:
        password_error = "Password must be shorter than 20 characters"

    password_ver_error =''
    if password != password_ver:
        password_ver_error = "Passwords must be the same"
    
    email_error=''
    if len(email) > 0:
        if ' ' in email:
            email_error = "Email must not contain spaces"
        elif email.count("@") < 1 or email.count("@") > 1:
            email_error = "Email must contain a valid email address"
        elif email.count(".") < 1 or email.count(".") > 1:
            email_error = "Email must not contain more then 1 period"

    
    if  not username_error and not password_error and not password_ver_error and not email_error:
        return render_template('welcome.html', username = username)

    else:
        return render_template('user-signup.html', 
        username = username, 
        email = email, 
        user_error = username_error,
        password_error = password_error,
        password_ver_error = password_ver_error,
        email_error = email_error)


app.run()