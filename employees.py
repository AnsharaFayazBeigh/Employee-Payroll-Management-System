from tkinter import*
from tkinter import messagebox, ttk
import os
import tempfile
import time
import pymysql  # after installation of pymysql in vscode terminal

class EmployeeSystem(): 
    root=None
    def __init__(self,root):
        self.root=root
        self.root.title("EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="EMPLOYEE PAYROLL MANAGEMENT SYSTEM", font=(
            "times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10)
        title.place(x=0, y=0, relwidth=1)
        btn_emp = Button(self.root, text="All Employee's ", command=self.employee_frame, font=(
            "times new roman", 13), bg="gray", fg="black")
        btn_emp.place(x=1000, y=5, height=32, width=120)

# Frame1
 # ====Variables====
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_experience = StringVar()
        self.var_gender = StringVar()
        self.var_contactid = StringVar()
        self.var_joblocation = StringVar()
        self.var_doj = StringVar()
        self.var_dob = StringVar()
        self.var_age = StringVar()
        self.var_proofid = StringVar()
        self.var_email = StringVar()
        self.var_status = StringVar()
        self.var_address = StringVar()

        Frame1= Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=750, height=620)
        title2 = Label(Frame1, text="EMPLOYEE DETAILS", font=(
            "times new roman", 25, "bold"), bg="lightgray", fg="black", anchor="w", padx=10)
        title2.place(x=0, y=0, relwidth=1)

        lbl_code = Label(Frame1, text="Employee Code:", font=(
            "times new roman", 23), bg="white", fg="black")
        lbl_code.place(x=10, y=70)
        self.txt_code = Entry(Frame1, font=("times new roman", 15),
                              textvariable=self.var_emp_code, bg="lightyellow", fg="black")
        self.txt_code.place(x=235, y=78, width=200)
        btn_search = Button(Frame1, text="Search", command=self.search, font=(
            "times new roman", 20), bg="gray", fg="black")
        btn_search.place(x=470, y=72, height=40)

        # Row1
        lbl_designation = Label(Frame1, text="Designation:", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_designation.place(x=10, y=120)
        txt_designation = Entry(Frame1, font=(
            "times new roman", 15), textvariable=self.var_designation, bg="lightyellow", fg="black")
        txt_designation.place(x=170, y=125, width=200)

        lbl_doj = Label(Frame1, text="D.O.J :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_doj.place(x=390, y=120)
        txt_doj = Entry(Frame1, font=("times new roman", 15),
                        textvariable=self.var_doj, bg="lightyellow", fg="black")
        txt_doj.place(x=520, y=125)

        # Row2
        lbl_name = Label(Frame1, text="Name :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_name.place(x=10, y=170)
        txt_name = Entry(Frame1, font=("times new roman", 15),
                         textvariable=self.var_name, bg="lightyellow", fg="black")
        txt_name.place(x=170, y=175, width=200)

        lbl_dob = Label(Frame1, text="D.O.B :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_dob.place(x=390, y=170)
        txt_dob = Entry(Frame1, font=("times new roman", 15),
                        textvariable=self.var_dob, bg="lightyellow", fg="black")
        txt_dob.place(x=520, y=175)

        # Row3
        lbl_exp = Label(Frame1, text="Experience :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_exp.place(x=10, y=220)
        txt_exp = Entry(Frame1, font=("times new roman", 15),
                        textvariable=self.var_experience, bg="lightyellow", fg="black")
        txt_exp.place(x=170, y=225, width=200)

        lbl_age = Label(Frame1, text="Age :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_age.place(x=390, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15),
                        textvariable=self.var_age, bg="lightyellow", fg="black")
        txt_age.place(x=520, y=225)

        # Row4
        lbl_gender = Label(Frame1, text="Gender :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_gender.place(x=10, y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15),
                           textvariable=self.var_gender, bg="lightyellow", fg="black")
        txt_gender.place(x=170, y=275, width=200)

        lbl_id = Label(Frame1, text="Proof ID :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_id.place(x=390, y=270)
        txt_id = Entry(Frame1, font=("times new roman", 15),
                       textvariable=self.var_proofid, bg="lightyellow", fg="black")
        txt_id.place(x=520, y=275)

        # Row5
        lbl_contact = Label(Frame1, text="Contact No :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_contact.place(x=10, y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15),
                            textvariable=self.var_contactid, bg="lightyellow", fg="black")
        txt_contact.place(x=170, y=325, width=200)

        lbl_email = Label(Frame1, text="Email :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_email.place(x=390, y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15),
                          textvariable=self.var_email, bg="lightyellow", fg="black")
        txt_email.place(x=520, y=325)

        # Row6
        lbl_hired = Label(Frame1, text="Job Location:", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_hired.place(x=10, y=370)
        txt_hired = Entry(Frame1, font=("times new roman", 15),
                        textvariable=self.var_joblocation, bg="lightyellow", fg="black")
        txt_hired.place(x=170, y=375, width=200)

        lbl_status = Label(Frame1, text="Status :", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_status.place(x=390, y=370)
        txt_status = Entry(Frame1, font=("times new roman", 15),
                           textvariable=self.var_status, bg="lightyellow", fg="black")
        txt_status.place(x=520, y=375)

        # Row7
        lbl_address = Label(Frame1, text="Address:", font=(
            "times new roman", 20), bg="white", fg="black")
        lbl_address.place(x=10, y=422)
        self.txt_address = Text(Frame1, font=(
            "times new roman", 15), bg="lightyellow", fg="black")
        self.txt_address.place(x=170, y=425, width=550, height=150)

        # Frame2
        # ====Variables====
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_bsalary = StringVar()
        self.var_totaldays = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_conveyance = StringVar()
        self.var_netsalary = StringVar()

        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=580, height=300)

        title3 = Label(Frame2, text="EMPLOYEE SALARY DETAILS", font=(
            "times new roman", 25, "bold"), bg="lightgray", fg="black", anchor="w", padx=10)
        title3.place(x=0, y=0, relwidth=1)

        lbl_month = Label(Frame2, text="Month:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_month.place(x=10, y=60)
        txt_month = Entry(Frame2, font=("times new roman", 15),
                          textvariable=self.var_month, bg="lightyellow", fg="black")
        txt_month.place(x=90, y=62, width=100)

        lbl_year = Label(Frame2, text="Year:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_year.place(x=210, y=60)
        txt_year = Entry(Frame2, font=("times new roman", 15),
                         textvariable=self.var_year, bg="lightyellow", fg="black")
        txt_year.place(x=260, y=62, width=100)

        lbl_salary = Label(Frame2, text="B.Salary:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_salary.place(x=380, y=60)
        txt_salary = Entry(Frame2, font=("times new roman", 15),
                           textvariable=self.var_bsalary, bg="lightyellow", fg="black")
        txt_salary.place(x=460, y=62, width=100)

        # Row1
        lbl_days = Label(Frame2, text="Total Days:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_days.place(x=10, y=100)
        txt_days = Entry(Frame2, font=("times new roman", 15),
                         textvariable=self.var_totaldays, bg="lightyellow", fg="black")
        txt_days.place(x=170, y=100, width=100)

        lbl_absent = Label(Frame2, text="Absent:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_absent.place(x=300, y=100)
        txt_absent = Entry(Frame2, font=("times new roman", 15),
                           textvariable=self.var_absent, bg="lightyellow", fg="black")
        txt_absent.place(x=400, y=100, width=100)

        # Row2
        lbl_medical = Label(Frame2, text="Medical:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_medical.place(x=10, y=145)
        txt_medical = Entry(Frame2, font=("times new roman", 15),
                            textvariable=self.var_medical, bg="lightyellow", fg="black")
        txt_medical.place(x=170, y=145, width=100)

        lbl_pf = Label(Frame2, text="P.F:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_pf.place(x=300, y=145)
        txt_pf = Entry(Frame2, font=("times new roman", 15),
                       textvariable=self.var_pf, bg="lightyellow", fg="black")
        txt_pf.place(x=400, y=145, width=100)

        # Row3
        lbl_conveyance = Label(Frame2, text="Conveyance:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_conveyance.place(x=10, y=190)
        txt_conveyance = Entry(Frame2, font=(
            "times new roman", 15), textvariable=self.var_conveyance, bg="lightyellow", fg="black")
        txt_conveyance.place(x=170, y=190, width=100)

        lbl_netsalary = Label(Frame2, text="Net Salary:", font=(
            "times new roman", 16), bg="white", fg="black")
        lbl_netsalary.place(x=300, y=190)
        txt_netsalary = Entry(Frame2, font=("times new roman", 15),
                              textvariable=self.var_netsalary, bg="lightyellow", fg="black")
        txt_netsalary.place(x=400, y=190, width=100)

        btn_calculate = Button(Frame2, text="Calculate", command=self.calculate, font=(
            "times new roman", 23), bg="gray", fg="orange")
        btn_calculate.place(x=150, y=223, height=32, width=120)
        self.btn_save = Button(Frame2, text="Save", command=self.add, font=(
            "times new roman", 23), bg="gray", fg="green")
        self.btn_save.place(x=280, y=223, height=32, width=120)
        btn_clear = Button(Frame2, text="Clear", command=self.clear, font=(
            "times new roman", 23), bg="gray", fg="black")
        btn_clear.place(x=410, y=223, height=32, width=120)

        self.btn_update = Button(Frame2, text="Update", state=DISABLED, command=self.update, font=(
            "times new roman", 23), bg="gray", fg="blue")
        self.btn_update.place(x=150, y=260, height=35, width=160)
        self.btn_delete = Button(Frame2, text="Delete", state=DISABLED, command=self.delete, font=(
            "times new roman", 23), bg="gray", fg="red")
        self.btn_delete.place(x=340, y=260, height=35, width=200)

        # Frame3
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=380, width=580, height=310)

        # Calculator -- Frame --
        self.var_txt = StringVar()
        self.var_operator = ''

        def btn_click(num):
            self.var_operator = self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator = ''

        Cal_Frame=Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        Cal_Frame.place(x=2, y=2, width=247, height=300)

        txt_result = Entry(Cal_Frame, bg="lightyellow", textvariable=self.var_txt, font=(
            "times new roman", 20, "bold"), justify=RIGHT)
        txt_result.place(x=0, y=0, relwidth=1, height=52)

        # Row1

        btn_7 = Button(Cal_Frame, text='7', command=lambda: btn_click(
            7), font=("times new roman", 15, "bold"))
        btn_7.place(x=0, y=52, width=60, height=60)
        btn_8 = Button(Cal_Frame, text='8', command=lambda: btn_click(
            8), font=("times new roman", 15, "bold"))
        btn_8.place(x=61, y=52, width=60, height=60)
        btn_9 = Button(Cal_Frame, text='9', command=lambda: btn_click(
            9), font=("times new roman", 15, "bold"))
        btn_9.place(x=122, y=52, width=60, height=60)
        btn_div = Button(Cal_Frame, text='/', command=lambda: btn_click('/'),
                         font=("times new roman", 15, "bold"))
        btn_div.place(x=183, y=52, width=60, height=60)

        # Row2

        btn_4 = Button(Cal_Frame, text='4', command=lambda: btn_click( 4), font=("times new roman", 15, "bold"))
        btn_4.place(x=0, y=112, width=60, height=60)
        btn_5 = Button(Cal_Frame, text='5', command=lambda: btn_click(
            5), font=("times new roman", 15, "bold"))
        btn_5.place(x=61, y=112, width=60, height=60)
        btn_6 = Button(Cal_Frame, text='6', command=lambda: btn_click(
            6), font=("times new roman", 15, "bold"))
        btn_6.place(x=122, y=112, width=60, height=60)
        btn_mlt = Button(Cal_Frame, text='*', command=lambda: btn_click('*'),
                         font=("times new roman", 15, "bold"))
        btn_mlt.place(x=183, y=112, width=60, height=60)

        # Row3

        btn_1 = Button(Cal_Frame, text='1', command=lambda: btn_click(
            1), font=("times new roman", 15, "bold"))
        btn_1.place(x=0, y=172, width=60, height=60)
        btn_2 = Button(Cal_Frame, text='2', command=lambda: btn_click(
            2), font=("times new roman", 15, "bold"))
        btn_2.place(x=61, y=172, width=60, height=60)
        btn_3 = Button(Cal_Frame, text='3', command=lambda: btn_click(
            3), font=("times new roman", 15, "bold"))
        btn_3.place(x=122, y=172, width=60, height=60)
        btn_diff = Button(Cal_Frame, text='-', command=lambda: btn_click('-'),
                          font=("times new roman", 15, "bold"))
        btn_diff.place(x=183, y=172, width=60, height=60)

        # Row4

        btn_0 = Button(Cal_Frame, text='0', command=lambda: btn_click(
            0), font=("times new roman", 15, "bold"))
        btn_0.place(x=0, y=232, width=60, height=60)
        btn_point = Button(Cal_Frame, text='.', command=lambda: btn_click(
            '.'), font=("times new roman", 15, "bold"))
        btn_point.place(x=45, y=232, width=60, height=60)
        btn_sum = Button(Cal_Frame, text='+', command=lambda: btn_click('+'),
                         font=("times new roman", 15, "bold"))
        btn_sum.place(x=90, y=232, width=60, height=60)
        btn_equ = Button(Cal_Frame, text='=', command=result,
                         font=("times new roman", 15, "bold"))
        btn_equ.place(x=135, y=232, width=60, height=60)
        btn_clear = Button(Cal_Frame, text='C', command=clear_cal,
                           font=("times new roman", 15, "bold"))
        btn_clear.place(x=183, y=232, width=60, height=60)

        # Salary Frame

        sal_frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_frame.place(x=250, y=2, width=325, height=300)
        title_sal = Label(sal_frame, text="    SALARY RECEIPT ", font=(
            "times new roman", 20, "bold"), bg="lightgray", fg="black", anchor="w", padx=10)
        title_sal.place(x=0, y=0, relwidth=1)

        sal_frame2 = Frame(sal_frame, bg="white", bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=30, relwidth=1, height=230)

        self.sample=f'''            COMTECH INFO SOLUTIONS\n                            PVT LTD\n            Top Floor, Khidmat Complex,\n               Regal Lane, Srinagar, J&K
-------------------------------------------------
Employee ID\t\t:  
Salary Of\t\t:  MON-YYYY
Generated on\t\t:  DD-MM-YYYY
-------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Basic Salary\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Conveyance\t\t:  Rs.----
Net_salary\t\t:  Rs.-----
-------------------------------------------------
This is a computer-generated slip, not
required any signature
    '''
  #

        scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(sal_frame2, font=(
            "times new roman", 13), bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END, self.sample)

        self.btn_print = Button(sal_frame, text="Print", state=DISABLED, command=self.print, font=(
            "times new roman", 23), bg="gray", fg="blue")
        self.btn_print.place(x=200, y=262, height=30, width=90)

        self.check_connection()

        # All Functions Start here

    def search(self):
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', db='emps(comtech)')
            cur = con.cursor()
            cur.execute("select * from payroll_system where emp_id=%s",
                        (self.var_emp_code.get()))
            row = cur.fetchone()
            # print(rows)
            if row==None:
                messagebox.showerror(
                    "Error", "Invalid Employee ID, please try with another employee ID", parent=self.root)
            else:
                # print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_experience.set(row[3])
                self.var_gender.set(row[4])
                self.var_contactid.set(row[5])
                self.var_joblocation.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_age.set(row[9])
                self.var_proofid.set(row[10])
                self.var_email.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END, row[13])

                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_bsalary.set(row[16])
                self.var_totaldays.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_conveyance.set(row[21])
                self.var_netsalary.set(row[22])
                file_ = open('salary_receipts/'+str(row[23]), 'r')
                self.txt_salary_receipt.delete('1.0', END)
                for i in file_:
                    self.txt_salary_receipt.insert(END, i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')
                self.btn_print.config(state=NORMAL)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def delete(self):
        
        if self.var_emp_code.get() == '':
            messagebox.showerror("Error", "Employee ID is required")
        else:
            try:
                con = pymysql.connect(
                    host='localhost', user='root', password='', db='emps(comtech)')
                cur = con.cursor()
                cur.execute(
                    "select * from payroll_system where emp_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(rows)
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid Employee ID, please try with another employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?")
                    # print(op)
                    if op is True:
                        cur.execute(
                            "delete from payroll_system where emp_id=%s", (self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo(
                            "Success", "Employee ID deleted successfully", parent=self.root)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def clear(self):
        
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_experience.set('')
        self.var_gender.set('')
        self.var_contactid.set('')
        self.var_joblocation.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_age.set('')
        self.var_proofid.set('')
        self.var_email.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0', END)

        self.var_month.set('')
        self.var_year.set('')
        self.var_bsalary.set('')
        self.var_totaldays.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_conveyance.set('')
        self.var_netsalary.set('')
        self.txt_salary_receipt.delete('1.0', END)
        self.txt_salary_receipt.insert(END, self.sample)

    def add(self):
        
        if self.var_emp_code.get == '' or self.var_netsalary.get() == '' or self.var_name.get == '':
            messagebox.showerror("Error", "Employee details are required")
        else:
            try:
                con = pymysql.connect(
                    host='localhost', user='root', password='', db='emps(comtech)')
                cur = con.cursor()
                cur.execute(
                    "select * from payroll_system where emp_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(rows)
                if row is not None:
                    messagebox.showerror(
                        "Error", "This Employee ID is already available in our record, try again with a new ID", parent=self.root)
                else:
                    cur.execute("insert into payroll_system values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.var_emp_code.get(),
                                    self.var_designation.get(),
                                    self.var_name.get(),
                                    self.var_experience.get(),
                                    self.var_gender.get(),
                                    self.var_contactid.get(),
                                    self.var_joblocation.get(),
                                    self.var_doj.get(),
                                    self.var_dob.get(),
                                    self.var_age.get(),
                                    self.var_proofid.get(),
                                    self.var_email.get(),
                                    self.var_status.get(),
                                    self.txt_address.get('1.0', END),
                                    self.var_month.get(),
                                    self.var_year.get(),
                                    self.var_bsalary.get(),
                                    self.var_totaldays.get(),
                                    self.var_absent.get(),
                                    self.var_medical.get(),
                                    self.var_pf.get(),
                                    self.var_conveyance.get(),
                                    self.var_netsalary.get(),
                                    self.var_emp_code.get()+".txt"
                                )
                                )
                con.commit()
                con.close()
                file_ = open('salary_receipts/' +str(self.var_emp_code.get())+".txt", 'w')
                file_.write(self.txt_salary_receipt.get('1.0', END))
                file_.close()
                messagebox.showinfo("Success", "Record Added Successfully")
                self.btn_print.config(state=NORMAL)

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def update(self):
        if self.var_emp_code.get== '' or self.var_netsalary.get()== '' or self.var_name.get== '':
            messagebox.showerror("Error", "Employee details are required")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='emps(comtech)')
                cur = con.cursor()
                cur.execute("select * from payroll_system where emp_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(rows)
                if row == None:
                    messagebox.showerror("Error", "This Employee ID is invalid, try again with a valid Employee ID", parent=self.root)
                else:
                    cur.execute("UPDATE `payroll_system` SET `designation`=%s,`name`=%s,`experience`=%s,`gender`=%s,`contact_id`=%s,`job_location`=%s,`d.o.j`=%s,`d.o.b`=%s,`age`=%s,`proof_id`=%s,`email`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`b_salary`=%s,`tot_days`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`conveyance`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `emp_id`=%s",
                    (

                      self.var_designation.get(),
                      self.var_name.get(),
                      self.var_experience.get(),
                      self.var_gender.get(),
                      self.var_contactid.get(),
                      self.var_joblocation.get(),
                      self.var_doj.get(),
                      self.var_dob.get(),
                      self.var_age.get(),
                      self.var_proofid.get(),
                      self.var_email.get(),
                      self.var_status.get(),
                      self.txt_address.get('1.0', END),
                      self.var_month.get(),
                      self.var_year.get(),
                      self.var_bsalary.get(),
                      self.var_totaldays.get(),
                      self.var_absent.get(),
                      self.var_medical.get(),
                      self.var_pf.get(),
                      self.var_conveyance.get(),
                      self.var_netsalary.get(),
                      self.var_emp_code.get()+".txt",
                      self.var_emp_code.get()
                      )
                      )
                con.commit()
                con.close()
                file_ = open('salary_receipts/'+str(self.var_emp_code.get())+".txt", 'w')
                file_.write(self.txt_salary_receipt.get('1.0', END))
                file_.close()
                messagebox.showinfo("Success", "Record Updated Successfully")

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def calculate(self):
        
        if self.var_month.get() == '' or self.var_year.get() == '' or self.var_bsalary.get() == '' or self.var_totaldays.get() == '' or self.var_absent.get() == '':
            messagebox.showerror("Error", "All fields are required")
        else:
            per_day = int(self.var_bsalary.get())/int(self.var_totaldays.get())
            work_day = int(self.var_totaldays.get())-int(self.var_absent.get())
            sal = per_day*work_day
            deduct = int(self.var_medical.get())+int(self.var_pf.get())
            addition = int(self.var_conveyance.get())
            net_sal = sal-deduct+addition
            self.var_netsalary.set(str(round(net_sal, 2)))

            # ---- Update the receipt
            new_sample = f'''            COMTECH INFO SOLUTIONS\n                  PVT LTD\n            Top Floor,Khidmat Complex,\n             Regal Lane, Srinagar, J&K
-----------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
---------------------------------------------------
Total Days\t\t:  {self.var_totaldays.get()}
Total Present\t\t:  {str(int(self.var_totaldays.get())-int(self.var_absent.get()))}
Total Absent\t\t:  {self.var_absent.get()}
Basic Salary\t\t:  Rs.{self.var_bsalary.get()}
Medical\t\t        :  Rs.{self.var_medical.get()}
PF\t\t        :  Rs.{self.var_pf.get()}
Conveyance\t\t:  Rs.{self.var_conveyance.get()}
Net_salary\t\t:  Rs.{self.var_netsalary.get()}
------------------------------------------------------
This is a computer-generated slip, not
required any signature
'''

            self.txt_salary_receipt.delete('1.0', END)
            self.txt_salary_receipt.insert(END, new_sample)

    def check_connection(self):
        
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', db='emps(comtech)')
            cur = con.cursor()
            cur.execute("select * from payroll_system")
            rows = cur.fetchall()
            # print(rows)
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def show(self):
        
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', db='emps(comtech)')
            cur = con.cursor()
            cur.execute("select * from payroll_system")
            rows = cur.fetchall()
            # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('', END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def employee_frame(self):
        
        self.root2 = Toplevel(self.root)
        self.root2.title("EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title = Label(self.root, text="ALL EMPLOYEE DETAILS", font=(
            "times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10)
        title.pack(side=TOP, fill=X)
        self.root2.focus_force()

        scrolly = Scrollbar(self.root2, orient=VERTICAL)
        scrollx = Scrollbar(self.root2, orient=HORIZONTAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)

        self.employee_tree = ttk.Treeview(self.root2, columns=('emp_id', 'designation', 'name', 'experience', 'gender', 'contact_id', 'job_location', 'd.o.j', 'd.o.b', 'age', 'proof_id', 'email',
                                          'status', 'address', 'month', 'year', 'b_salary', 'tot_days', 'absent', 'medical', 'pf', 'conveyance', 'net_salary', 'salary_receipt'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.employee_tree.heading("emp_id", text='Emp-ID')
        self.employee_tree.heading("designation", text='Designation')
        self.employee_tree.heading("name", text='Name')
        self.employee_tree.heading("experience", text='Experience')
        self.employee_tree.heading("gender", text='Gender')
        self.employee_tree.heading("contact_id", text='Contact')
        self.employee_tree.heading("job_location", text='Job-Location')
        self.employee_tree.heading("d.o.j", text='D.O.J')
        self.employee_tree.heading("d.o.b", text='D.O.B')
        self.employee_tree.heading("age", text='Age')
        self.employee_tree.heading("proof_id", text='ID')
        self.employee_tree.heading("email", text='Email')
        self.employee_tree.heading("status", text='Status')
        self.employee_tree.heading("address", text='Address')
        self.employee_tree.heading("month", text='Month')
        self.employee_tree.heading("year", text='Year')
        self.employee_tree.heading("b_salary", text='Basic Salary')
        self.employee_tree.heading("tot_days", text='Total Days')
        self.employee_tree.heading("absent", text='Absent')
        self.employee_tree.heading("medical", text='Medical')
        self.employee_tree.heading("pf", text='PF')
        self.employee_tree.heading("conveyance", text='Conveyance')
        self.employee_tree.heading("net_salary", text='Net Salary')
        self.employee_tree.heading("salary_receipt", text='Salary Receipt')
        self.employee_tree['show'] = 'headings'

        self.employee_tree.column("emp_id", width=50)
        self.employee_tree.column("designation", width=200)
        self.employee_tree.column("name", width=100)
        self.employee_tree.column("experience", width=100)
        self.employee_tree.column("gender", width=50)
        self.employee_tree.column("contact_id", width=100)
        self.employee_tree.column("job_location", width=100)
        self.employee_tree.column("d.o.j", width=100)
        self.employee_tree.column("d.o.b", width=100)
        self.employee_tree.column("age", width=100)
        self.employee_tree.column("proof_id", width=100)
        self.employee_tree.column("email", width=150)
        self.employee_tree.column("status", width=100)
        self.employee_tree.column("address", width=500)
        self.employee_tree.column("month", width=100)
        self.employee_tree.column("year", width=100)
        self.employee_tree.column("b_salary", width=100)
        self.employee_tree.column("tot_days", width=100)
        self.employee_tree.column("absent", width=100)
        self.employee_tree.column("medical", width=100)
        self.employee_tree.column("pf", width=100)
        self.employee_tree.column("conveyance", width=100)
        self.employee_tree.column("net_salary", width=100)
        self.employee_tree.column("salary_receipt", width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH, expand=1)
        self.show()

        self.root2.mainloop()

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')


root=Tk()
obj=EmployeeSystem(root)
root.mainloop()
