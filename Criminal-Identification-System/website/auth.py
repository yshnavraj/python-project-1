from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import os
import pymysql
import win32api

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        policeId = request.form.get('policeId')
        password = request.form.get('password')
        db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
        cursor = db.cursor()
        print("database connected")
        query = "SELECT * FROM policetable where policeId = '%s' and password = '%s';" % (policeId, password)

        try:
            if(cursor.execute(query)):
                db.commit()
                print("Police Login Successful")
                os.system('Python home.py')
                return render_template("dashboard2.html", user=current_user)
            else:   
                flash('Incorrect Credentials', category='error')
        except:
            db.rollback()
            print("Login Failed")
        db.close()
        print("connection closed")
    return render_template("login.html", user=current_user)

    #     if user:
    #         if check_password_hash(user.password, password):
    #             flash('Logged out successfully!', category='success')
    #             login_user(user, remember=True)
    #             # return redirect(url_for('views.home'))
    #             os.system('Python home.py')
    #             return render_template("dashboard2.html", user=current_user)
    #         else:
    #             flash('Incorrect password, try again.', category='error')
    #     else:
    #         flash('Email does not exist.', category='error')

    # return render_template("login.html", user=current_user)
    # os.system('Python Criminal-Identification-System/j.py')
    # return

    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     user = User.query.filter_by(email=email).first()
    #     if user:
    #         if check_password_hash(user.password, password):
    #             flash('Logged out successfully!', category='success')
    #             login_user(user, remember=True)
    #             # return redirect(url_for('views.home'))
    #             os.system('Python home.py')
    #             return render_template("dashboard2.html", user=current_user)
    #         else:
    #             flash('Incorrect password, try again.', category='error')
    #     else:
    #         flash('Email does not exist.', category='error')

#     return render_template("login.html", user=current_user)
    # os.system('Python Criminal-Identification-System/j.py')
    # return

@auth.route('/logout')
@login_required
def logout():
    # logout_user()
    return redirect(url_for('auth.policeLogin'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        print(email)
        print(password)
        db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
        cursor = db.cursor()
        print("database connected")
        query = "SELECT * FROM admintable where admin_username = '%s' and admin_password = '%s';" % (email, password)

        # user = User.query.filter_by(email=email).first()
        # if user:
        try:
            if(cursor.execute(query)):
                db.commit()
                print("Admin Login Successfull")
                return render_template("dashboard.html", user=current_user)
            else:
                flash('Incorrect Credentials', category='success')
        except:
            db.rollback()
    return render_template("sign_up.html", user=current_user)
        # if (email=="Admin" and password=="Admin123"):
        #     flash('Logged out successfully!', category='success')
        #     # login_user(user, remember=True)
        #     # return redirect(url_for('views.home'))
        #     return render_template("dashboard.html", user=current_user)
        #     #os.system('Python home.py')
        # else:
        #     flash('Incorrect password, try again.', category='error')
        # # else:
        # #     flash('Email does not exist.', category='error')

   # return render_template("login.html", user=current_user)
    

@auth.route('/addpolice', methods=['GET', 'POST'])
def addpolice():
    if request.method == 'POST':
        batch = request.form.get('batchIDNumber')
        name = request.form.get('fullName')
        policeId = request.form.get('policeId')
        password = request.form.get('createPassword')
        print(name, batch, policeId, password)
        # print(batch)
        # print(policeId)
        # print(password)
        db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
        cursor = db.cursor()
        print("database connected")
        # query = "INSERT INTO policetable (police_id, name, batch, policeId, password) VALUES(0, %s, %s, %s, %s)"
        query = "INSERT INTO policetable VALUES(0, '%s', '%s', '%s', '%s');" % (name, batch, policeId, password)

        # record = (0, name, batch, policeId, password)

        try:
            cursor.execute(query)
            db.commit()
            print("Police Added")
            flash("Police Added Successfully", category='success')
            win32api.MessageBox(0, 'Police Added Successfully', 'Message', 0x00001000) 
        except:
            db.rollback()
            print("Police Insertion Failed")
            flash("User couldn't be added", category='error')
            win32api.MessageBox(0, "User couldn't be added", 'Message', 0x00001000)
        db.close()
        print("connection closed")
        return render_template("dashboard.html", user=current_user)
                
@auth.route('/removepolice', methods=['GET', 'POST'])
def removepolice():
    if request.method == 'POST':
        policeId = request.form.get('policeId')
        db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
        cursor = db.cursor()
        print("database connected")
        # query = "INSERT INTO policetable (police_id, name, batch, policeId, password) VALUES(0, %s, %s, %s, %s)"
        query = "DELETE FROM policetable where policeId like '%s';" % policeId 

        try:
            if(cursor.execute(query)):
                db.commit()
                print("Police Removed")
                flash("Police Removed Successfully", category='success')
                win32api.MessageBox(0, "User removed Successfully", 'Message', 0x00001000)
            else:
                win32api.MessageBox(0, "User couldn't be removed", 'Message', 0x00001000)
        except:
            db.rollback()
            print("Police Not Removed")
            flash("User couldn't be removed", category='error')
        db.close()
        print("connection closed")
        return render_template("dashboard.html", user=current_user)

@auth.route('/policeLogin', methods=['GET', 'POST'])
def policeLogin():
    if request.method == 'POST':
        policeId = request.form.get('policeId')
        password = request.form.get('password')
        db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
        cursor = db.cursor()
        print("database connected")
        query = "SELECT * FROM policetable where policeId = '%s' and password = '%s';" % (policeId, password)

        try:
            cursor.execute(query)
            db.commit()
            print("Police Login Successful")
        except:
            db.rollback()
            print("Login Failed")
        db.close()
        print("connection closed")
    return render_template("dashboard2.html", user=current_user)