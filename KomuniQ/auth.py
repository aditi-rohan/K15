from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# login route
@auth.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit() and :
        flash("")
    return render_template("login.html")

# logout route
@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

# reset password route
@auth.route('/reset_password')
def reset_password():
    return "<h1>Reset Password</h1>"