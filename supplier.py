import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import create_db


class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x550+220+140")
        self.root.title("Inventory Management System")
        self.root.config(bg="white",bd=5)
        self.root.focus_force()

    #=======ALL variable ==== #

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()


        self.var_sup_invoice = StringVar()
        self.var_contact= StringVar()
        self.var_name= StringVar()

    ##========= Search Frame =========##

        # searchFrame = LabelFrame(self.root,text = "Search Supplier",bg = "white",font=("goudy old style",12,"bold"),bd=2,relief= RIDGE)
        # searchFrame.place(x=730,y=80,width = 600,height = 70)

    #====options====#

        lbl_search = Label(self.root,text="Invoice no.",bg="white",justify='center',font=("goudy old style",15))
        lbl_search.place(x=730,y=80)

        txt_search = Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=840,y=80,width=170,height=32)

        btn_search = Button(self.root, text="Search",font=("goudy old style",15,"bold"),fg="white", bg="#4caf50",cursor="hand2",command=self.search)
        btn_search.place(x=1030,y=80,height=32,width=90)

    #====Title=====#

        title = Label(self.root,text="Supplier Details",font = ("goudy old style",20,"bold"),bg = "#0f4d7d",fg = "white")
        title.place(x=125,y=10,width=1000,height=40)

    #===Content====#

        #==== Row1 ====

        lbl_sup_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=130, y=80)

        txt_sup_invoice = Entry(self.root, textvariable = self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=250, y=80,width=180)


        # ==== Row2 ====

        lbl_name = Label(self.root, text="SupplierName", font=("goudy old style", 15), bg="white").place(x=130, y=120)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),bg="lightyellow").place(x=250, y=120,width=180)

        # ==== Row3 ====

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=130, y=160)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15),bg="lightyellow").place(x=250, y=160,width=180)

        #==== Row4 =====

        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=130, y = 200)

        self.txt_desc = Text(self.root,font=("goudy old style", 15),bg="lightyellow")
        self.txt_desc.place(x=250, y=200,width = 465,height = 90)

        #==buttons ====

        btn_save = Button(self.root, text="Save",command=self.add,font=("goudy old style", 15,"bold"), bg="#2196f3", fg="white",cursor="hand2")
        btn_save.place(x=250, y=370, width=100,height=45)

        btn_update = Button(self.root, text="Update", font=("goudy old style", 15,"bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        btn_update.place(x=370, y=370, width=100,height=45)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15,"bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        btn_delete.place(x=490, y=370, width=100,height=45)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15,"bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        btn_clear.place(x=610, y=370, width=100,height=45)

        #==Tree View is use to show the data===#
        # ===Employee Details====#


        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=730,y = 130,width = 395,height = 400)

        scrolly = Scrollbar(emp_frame,orient = VERTICAL)
        scrollx = Scrollbar(emp_frame,orient = HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame,columns = ("invoice","name","contact","desc"),
                                          yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command = self.supplierTable.xview)
        scrolly.config(command = self.supplierTable.yview)

        self.supplierTable.heading("invoice",text = "Invoice No")
        self.supplierTable.heading("name",text = "Name")
        self.supplierTable.heading("contact",text = "Contact")
        self.supplierTable.heading("desc",text = "Description")


        self.supplierTable["show"]="headings" #To remove the first column which was blank


        self.supplierTable.column("invoice",width=80)
        self.supplierTable.column("name",width=90)
        self.supplierTable.column("contact",width=80)
        self.supplierTable.column("desc",width=150)

        self.supplierTable.pack(fill = BOTH,expand = 1)

        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)       #when we click on the data it will reflect
                                                                            # on their respective areas

        self.show()





    #======Working with database=====#




    def add(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Invoice no. is already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,description) values(?,?,?,?)",(
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0',END),))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added Successfully",parent=self.root)
                    self.show()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)


    def show(self):
         con = sqlite3.connect(r'ims.db')
         cur = con.cursor()
         try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            # self.supplierTable.delete(*self.supplierTable.get_children())
            for item in self.supplierTable.get_children():
                self.supplierTable.delete(item)
            for row in rows:
                self.supplierTable.insert('',END,values=row) #starting from start to end
         except EXCEPTION as ex:
             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=self.supplierTable.item(f)
        row=content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert('1.0',row[3])


    def update(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No Must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,description=? where invoice=?",
                                (
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0',END),
                                    self.var_sup_invoice.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no Must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
                else:
                    ans=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if(ans==True):
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
                    else:
                        messagebox.showwarning("Cancelled","Supplier not deleted",parent=self.root)
                    self.show()
                    con.close()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.show()

    # self.var_searchby = StringVar()     ("Select","Email","Name","Contact")
    # self.var_searchtxt = StringVar()'''
    def search(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if(self.var_searchtxt.get()==""):
                messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if(row==None):
                    messagebox.showerror("Error","No Record Found",parent=self.root)
                else:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)  # starting from start to end
        except EXCEPTION as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()