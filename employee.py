import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import create_db




class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x550+220+140")
        self.root.title("Inventory Management System")
        self.root.config(bg="white",bd=5)
        self.root.focus_force()

    #=======ALL variable ==== #

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()


        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact= StringVar()
        self.var_name= StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()


    ##========= Search Frame =========##

        searchFrame = LabelFrame(self.root,text = "Search Employee",bg = "white",font=("goudy old style",12,"bold"),bd=2,relief= RIDGE)
        searchFrame.place(x=300,y=20,width = 600,height = 70)

    #====options====#

        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_searchby,value = ("Select","Emp ID","Email","Name","Contact"),state="readonly",justify='center',font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width = 180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=200,y=10,width=200)

        btn_search = Button(searchFrame, text="Search",font=("goudy old style",15,"bold"),fg="white", bg="#4caf50",cursor="hand2",command=self.search)
        btn_search.place(x=410,y=5,width = 150,height = 37)

    #====Title=====#

        title = Label(self.root,text="Employee Details",font = ("goudy old style",15),bg = "#0f4d7d",fg = "white")
        title.place(x=125,y=100,width=1000)

    #===Content====#

        #==== Row1 ====

        lbl_emp_id = Label(self.root, text="Emp ID", font=("goudy old style", 15), bg="white").place(x=130, y=150)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15), bg="white").place(x=490, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=845, y=150)

        txt_emp_id = Entry(self.root, textvariable = self.var_emp_id, font=("goudy old style", 15), bg="lightyellow").place(x=210, y=150)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,value=("Select", "Male", "Female", "Other"), state="readonly", justify='center',
                                  font=("goudy old style", 15))
        cmb_gender.place(x=567, y=150 ,width=200)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable =self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=920, y=150)

        # ==== Row2 ====

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=130, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15), bg="white").place(x=490, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("goudy old style", 15), bg="white").place(x=845, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),bg="lightyellow").place(x=210, y=190)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15),bg="lightyellow").place(x=567, y=190)
        txt_contact = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 15),bg="lightyellow").place(x=920, y=190)

        # ==== Row3 ====

        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="white").place(x=130, y=230)
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 15), bg="white").place(x=480, y=230)
        lbl_usertype = Label(self.root, text="UserType", font=("goudy old style", 15), bg="white").place(x=830, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15),bg="lightyellow").place(x=210, y=230)
        txt_password = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 15),bg="lightyellow").place(x=567, y=230)


        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, value=("Select", "Admin","Employee"), state="readonly", justify='center',
                          font=("goudy old style", 15))
        cmb_utype.place(x=920, y=230, width=200)
        cmb_utype.current(0)

        #==== Row4 =====

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=130, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="white").place(x=650, y=270)

        self.txt_address = Text(self.root,font=("goudy old style", 15),bg="lightyellow")
        self.txt_address.place(x=210, y=270,width = 400,height = 60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 15), bg="lightyellow").place(x=720, y=270)

        #==buttons ====

        btn_save = Button(self.root, text="Save",command=self.add,font=("goudy old style", 15,"bold"), bg="#2196f3", fg="white",cursor="hand2")
        btn_save.place(x=650, y=310, width=100,height=35)

        btn_update = Button(self.root, text="Update", font=("goudy old style", 15,"bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        btn_update.place(x=775, y=310, width=100,height=35)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15,"bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        btn_delete.place(x=905, y=310, width=100,height=35)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15,"bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        btn_clear.place(x=1030, y=310, width=100,height=35)

        #==Tree View is use to show the data===#
        # ===Employee Details====#


        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y = 360,relwidth = 1,height = 180)

        scrolly = Scrollbar(emp_frame,orient = VERTICAL)
        scrollx = Scrollbar(emp_frame,orient = HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame,columns = ("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),
                                          yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command = self.EmployeeTable.xview)
        scrolly.config(command = self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid",text = "EMP ID")
        self.EmployeeTable.heading("name",text = "Name")
        self.EmployeeTable.heading("email",text = "Email")
        self.EmployeeTable.heading("gender",text = "Gender")
        self.EmployeeTable.heading("contact",text = "Contact")
        self.EmployeeTable.heading("dob",text = "DOB")
        self.EmployeeTable.heading("doj",text = "DOJ")
        self.EmployeeTable.heading("pass",text = "Password")
        self.EmployeeTable.heading("utype",text = "User Type")
        self.EmployeeTable.heading("address",text = "Address")
        self.EmployeeTable.heading("salary",text = "Salary")


        self.EmployeeTable["show"]="headings" #To remove the first column which was blank


        self.EmployeeTable.column("eid",width=100)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=150)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=150)
        self.EmployeeTable.column("salary",width=100)

        self.EmployeeTable.pack(fill = BOTH,expand = 1)

        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)       #when we click on the data it will reflect
                                                                            # on their respective areas



        self.show()





    #======Working with database=====#




    def add(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Employee ID is already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                    self.var_emp_id.get(),
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_pass.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0',END),
                                    self.var_salary.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Employee added Successfully",parent=self.root)
                    self.show()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)


    def show(self):
         con = sqlite3.connect(r'ims.db')
         cur = con.cursor()
         try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            # self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for item in self.EmployeeTable.get_children():
                self.EmployeeTable.delete(item)
            for row in rows:
                self.EmployeeTable.insert('',END,values=row) #starting from start to end
         except EXCEPTION as ex:
             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert('1.0',row[9])
        self.var_salary.set(row[10])


    def update(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",
                                (
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_pass.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0',END),
                                    self.var_salary.get(),
                                    self.var_emp_id.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    ans=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if(ans==True):
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Deleted Successfully",parent=self.root)
                        self.clear()
                    else:
                        messagebox.showwarning("Cancelled","Employee not deleted",parent=self.root)
                    self.show()
                    con.close()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.show()

    # self.var_searchby = StringVar()     ("Select","Email","Name","Contact")
    # self.var_searchtxt = StringVar()
    def search(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if(self.var_searchby.get()=="Select"):
                messagebox.showerror("Error","Select search by option",parent=self.root)

            elif(self.var_searchtxt.get()==""):
                messagebox.showerror("Error","Search Input should be required",parent=self.root)

            elif (self.var_searchby.get() == "Emp ID"):
                    cur.execute("select * from employee where eid=?", (self.var_searchtxt.get(),))
            else:
                    cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")


            if(self.var_searchby.get()!="Select" and self.var_searchtxt.get()!=''):
                rows = cur.fetchall()
                if(len(rows)==0):
                    messagebox.showerror("Error","No Record Found",parent=self.root)
                else:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)  # starting from start to end
        except EXCEPTION as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()