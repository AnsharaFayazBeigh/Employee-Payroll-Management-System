

from tkinter import *

from tkinter import messagebox

import pymysql



def login():

    username=entry1.get()

    password=entry2.get()



    if(username=="" and password==""):

        messagebox.showinfo("","Blank not Allowed")

    elif(username=="Jai" and password=="1234"):

        messagebox.showinfo("","Login Success")   
        next == "C:\Users\ansha\OneDrive\Desktop\EMPLOYEES\employees.py":

    else:

        messagebox.showinfo("","incorrect username and password")    



root=Tk()

root.title("LOGIN")

root.geometry("1199x600+100+50")



global entry1

global entry2



Label(root,text="Username").place(x=450,y=20)

Label(root,text="Password").place(x=450,y=70)



entry1=Entry(root,bd=4)

entry1.place(x=600,y=20)



entry2=Entry(root,bd=4)

entry2.place(x=600,y=70)



Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=500,y=120)



def check_connection(self):

        try:

             con=pymysql.connect(host='localhost',user='root',password='',db='emps')

             cur=con.cursor()

             cur.execute("select * from payroll_system")

             rows=cur.fetchall()

             #print(rows)

        except Exception as ex:

             messagebox.showerror("Error",f'Error due to: {str(ex)}')    



root.mainloop()

