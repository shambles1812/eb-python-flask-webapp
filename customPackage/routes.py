from flask import render_template, url_for, flash, redirect
from customPackage.forms import RegistrationForm, RetrieveForm
from customPackage.models import User, Information
from customPackage import app , db , bcrypt
from flask_login import login_user, current_user, logout_user


@app.route("/")
@app.route("/home")
def home(): 
    return render_template('home.html', title= 'Home')
@app.route("/register", methods=['GET', 'POST'] )
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password= hashed_password,
                    information= form.info.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Data stored for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
@app.route("/retrieve", methods = ['GET', 'POST'])
def retrieve():
    form = RetrieveForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
             flash('Retrieving Unsuccessful. Please check your credentials', 'danger')
    return render_template('retrieve.html', title= 'Retrieve', form = form )
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
