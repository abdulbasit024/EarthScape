from flask import render_template, redirect, url_for, flash, request
from urllib.parse import urlparse
from flask_login import login_user, logout_user, current_user
from app import db
from app.models import User
from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
            
        login_user(user)
        return redirect(url_for('main.index'))
        
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'analyst') # Allow simplified role selection for demo
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken')
            return redirect(url_for('auth.register'))
            
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')
