import pymysql
from tkinter import *
from functools import partial
# from home import *
# import subprocess
import os

def validatePoliceLogin(username, password):
	#rowId = 0
	db = pymysql.connect(host="localhost", user="root", password="",database="criminaldb")
	cursor = db.cursor()
	print("database connected")
	police = username.get()
	password = password.get()
	query = "SELECT * FROM policetable WHERE username=%s and password = %s"
	tkWindow.destroy()
	try:
		if(cursor.execute(query, (police,password)) != 0):
			db.commit()
			# rowId = cursor.lastrowid
			print("Successfull Login")
			# subprocess.call(['python', 'home.py'])
			os.system('python home.py')
			
			# subprocess.call(['python', 'home.py'])
			# execfile('./home.py')
			# root.mainloop()
			# tkWindow.destroy()
		else:
			print("Login Failed")
			os.system('python App.py')
	except:
		db.rollback()
	return

def validateAdminLogin(username, password):
	#rowId = 0
	db = pymysql.connect(host="localhost", user="root", password="",database="criminaldb")
	cursor = db.cursor()
	print("database connected")
	admin = username.get()
	passs = password.get()
	query = "SELECT * FROM admintable WHERE admin_username=%s and admin_password = %s"
	tkWindow.destroy()
	try:
		if(cursor.execute(query, (admin,passs)) != 0):
			db.commit()
			rowId = cursor.lastrowid
			print("Successfull Login")
			# subprocess.call(['python', 'home.py'])
			os.system('python admin_dashboard.py')
			
			# subprocess.call(['python', 'home.py'])
			# execfile('./home.py')
			# root.mainloop()
			# tkWindow.destroy()
		else:
			print("Login Failed")
			os.system('python App.py')
	except:
		db.rollback()
	return

#window
tkWindow = Tk()  
tkWindow.geometry('1000x750')  
tkWindow.title('ISWRTISICCUFC')

#username label and text entry box
policeLabel = Label(tkWindow, text="Police Username").grid(row=0, column=0)
policeUsername = StringVar()
usernameEntry1 = Entry(tkWindow, textvariable=policeUsername).grid(row=0, column=1)  

#password label and password entry box
policepasswordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
policepassword = StringVar()
passwordEntry1 = Entry(tkWindow, textvariable=policepassword, show='*').grid(row=1, column=1)  

#username label and text entry box
adminLabel = Label(tkWindow, text="Admin Username").grid(row=0, column=2)
adminUsername = StringVar()
usernameEntry2 = Entry(tkWindow, textvariable=adminUsername).grid(row=0, column=3)  

#password label and password entry box
adminpasswordLabel = Label(tkWindow,text="Password").grid(row=1, column=2)  
adminpassword = StringVar()
passwordEntry2 = Entry(tkWindow, textvariable=adminpassword, show='*').grid(row=1, column=3) 

validatePoliceLogin = partial(validatePoliceLogin, policeUsername, policepassword)
validateAdminLogin = partial(validateAdminLogin, adminUsername, adminpassword)
# login button
loginButton1 = Button(tkWindow, text="Login as Police", command=validatePoliceLogin).grid(row=4, column=0)  
loginButton2 = Button(tkWindow, text="Login as Admin", command=validateAdminLogin).grid(row=4, column=3)
tkWindow.mainloop()