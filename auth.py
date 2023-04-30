from flask import  Blueprint, render_template, request, flash, url_for,redirect
from .models  import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 


auth = Blueprint('auth', __name__)

@auth.route('/login' ,methods=['GET','POST'])
def login():
    data =  request.form
    print(data)
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return render_template('login.html')
@auth.route('/register', methods=['GET','POST'])
def register():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username= username,  password = generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("register.html")  # Add this return statement
