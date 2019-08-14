#!/usr/bin/python3
from tkinter import * 
from tkinter import font
import sqlite3
from tkinter import messagebox as ms

root = Tk()
root.geometry('400x350')
root.title("Login/Register")

myfont = font.Font(size=12)
header = font.Font(size=14)

userName=StringVar()
passWord=StringVar()



# = = = = =  Functions  = = = = = = 
# Registartion
class database:
	def __init__(self):
		print("Connection Estabilished")
		user1=userName.get()
		pass1=passWord.get()
		conn = sqlite3.connect('Form-4.db')
		with conn:
			cursor=conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS UsersBase (userName TEXT NOT NULL, passWord TEXT NOT NULL) ')
		find_user = ('SELECT * FROM UsersBase WHERE userName = ?')
		cursor.execute(find_user, [(userName.get())])
		if cursor.fetchall():
			print("Error!, User taken")
			ms.showerror('Error', 'User Is taken, or empty')
		else:
			print("Success!, User Created")
			cursor.execute('INSERT INTO UsersBase (Username, Password) VALUES(?,?)',(user1,pass1,))
			ms.showinfo('Success!', 'User Created')
		conn.commit()
		
		



# Login
def log_db():
	print("user logged")



# Labels: Username Password
reg_header = Label(root, text="Registration", font=header, fg="green", bg="white")
reg_header.grid(column=1, row=0, pady=8)
Label_username = Label(root, text="Username: ", font=myfont)
Label_username.grid(row=1, sticky=E, padx=8)
Label_password = Label(root, text="Password: ", font=myfont)
Label_password.grid(row=2, sticky=E, padx=8)
#Entries
Entry_username = Entry(root, textvar=userName)
Entry_username.grid(column=1, row=1)
Entry_password = Entry(root, show="*", textvar=passWord)
Entry_password.grid(column=1, row=2)
# Register Button 
Btn_reg = Button(root, text="Registration", command=database, anchor=N)
Btn_reg.grid(column=1, row=3)

# ========== User Login 
login_header = Label(root, text="Login to System ", font=header, fg="green", bg="white")
login_header.grid(column=1, row=4, pady=15)

login_user = Label(root, text="Login: ", font=myfont)
login_user.grid(column=0, row=5, sticky=E, padx=8)
login_pass = Label(root, text="Pass: ", font=myfont)
login_pass.grid(column=0, row=6, sticky=E, padx=8)

login_entry = Entry(root)
login_entry.grid(column=1, row=5)
pass_entry = Entry(root, show="*")
pass_entry.grid(column=1, row=6)


def NewPage():
	print("New Page")
	root2 = Toplevel(root)
	root2.title('User Logged In')
	root2.geometry("400x350")
	root2.resizable(0,0)
	root2.config(bg = 'grey')
	r2_label_1 = Label(root2, text="username is: ").grid(row=0)

Btn_login = Button(root, text="Log in", command=NewPage, anchor=N)
Btn_login.grid(column=1, row=7)

root.mainloop()
