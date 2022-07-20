import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import create_db


class productClass:

    cat_list = ["Select"]
    sup_list = ["Select"]

    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x550+220+140")
        self.root.title("Inventory Management System")
        self.root.config(bg="white",bd=5)
        self.root.focus_force()

        frame1 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        frame1.place(x=10,y=10,height=520,width=500)

        product_lbl=Label(frame1,text="Manage Product Details",font=("goudy old style",25),bg="#0f4d7d")
        product_lbl.pack(side=TOP,fill=X)

    #====Variables========#

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


    #======Details To Fill=======
        self.fetch_cat_sup()
        category_lbl = Label(frame1,text="Category",font=("goudy old style",20),bg="white").place(x=40,y=60)
        category_txt = ttk.Combobox(frame1,value=self.cat_list, textvariable = self.var_cat,state="readonly", justify='center',font=("goudy old style", 15))
        category_txt.place(x=190,y=60,width=220,height=35)
        category_txt.current(0)

        supplier_lbl = Label(frame1, text="Supplier", font=("goudy old style", 20), bg="white").place(x=40, y=120)
        supplier_txt = ttk.Combobox(frame1, value=self.sup_list,textvariable = self.var_sup, state="readonly",justify='center', font=("goudy old style", 15))
        supplier_txt.place(x=190, y=120,width=220,height=35)
        supplier_txt.current(0)

        name_lbl = Label(frame1, text="Name", font=("goudy old style", 20), bg="white").place(x=40, y=180)
        name_txt = Entry(frame1,bg="lightyellow",textvariable=self.var_name,font=("goudy old style", 20)).place(x=190, y=180,width=220,height=35)

        price_lbl = Label(frame1, text="Price", font=("goudy old style", 20), bg="white").place(x=40, y=240)
        price_txt = Entry(frame1, bg="lightyellow", textvariable = self.var_price,font=("goudy old style", 20)).place(x=190, y=240, width=220,height=35)

        quantity_lbl = Label(frame1, text="Quantity", font=("goudy old style", 20), bg="white").place(x=40, y=300)
        quantity_txt = Entry(frame1, bg="lightyellow", textvariable = self.var_quantity,font=("goudy old style", 20)).place(x=190, y=300, width=220,height=35)

        status_lbl = Label(frame1, text="Status", font=("goudy old style", 20), bg="white").place(x=40, y=360)
        status_txt = ttk.Combobox(frame1, value=("Active", "Inactive"),textvariable = self.var_status, state="readonly",justify='center', font=("goudy old style", 15))
        status_txt.place(x=190, y=360, width=220,height=35)
        status_txt.current(0)

        #====Buttons======

        btn_save = Button(frame1, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3",fg="white", cursor="hand2",command=self.add)
        btn_save.place(x=40, y=440, width=80, height=35)

        btn_update = Button(frame1, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",cursor="hand2",command=self.update)
        btn_update.place(x=140, y=440, width=80, height=35)

        btn_delete = Button(frame1, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.delete)
        btn_delete.place(x=240, y=440, width=80, height=35)

        btn_clear = Button(frame1, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.clear)
        btn_clear.place(x=340, y=440, width=80, height=35)

        #=======Frame 2 Started==========#

        searchFrame = LabelFrame(self.root, text="Search Product", bg="white", font=("goudy old style", 12, "bold"),bd=2, relief=RIDGE)
        searchFrame.place(x=560, y=10, width=620, height=70)

        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_searchby,value=("Select", "Category", "Supplier", "Name"), state="readonly",
                                  justify='center', font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=220, y=10, width=200)

        btn_search = Button(searchFrame, text="Search", font=("goudy old style", 15, "bold"), fg="white", bg="#4caf50",cursor="hand2",command=self.search)
        btn_search.place(x=445, y=5, width=150, height=35)

        #===================Tree view==============

        pro_frame = Frame(self.root, bd=3, relief=RIDGE,bg="white")
        pro_frame.place(x=560, y=100, width=620, height=427)

        
        scrolly = Scrollbar(pro_frame, orient=VERTICAL)
        scrollx = Scrollbar(pro_frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(pro_frame, columns=("pid", "name", "category", "supplier", "price", "qty","status"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("pid", text="Product ID")
        self.productTable.heading("name", text="Name")
        self.productTable.heading("category", text="Category")
        self.productTable.heading("supplier", text="Supplier")
        self.productTable.heading("price", text="Price")
        self.productTable.heading("qty", text="Quantity")
        self.productTable.heading("status", text="Status")

        self.productTable["show"] = "headings"  # To remove the first column which was blank

        self.productTable.column("pid", width=80)
        self.productTable.column("name", width=100)
        self.productTable.column("category", width=100)
        self.productTable.column("supplier", width=100)
        self.productTable.column("price", width=100)
        self.productTable.column("qty", width=100)
        self.productTable.column("status",width=100)

        self.productTable.pack(fill=BOTH, expand=1)
        self.show()

        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        # self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)  # when we click on the data it will reflect
        # on their respective areas

    #===========code for dataBases started=========#
    def fetch_cat_sup(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        cur.execute("select name from supplier")
        sup_name = cur.fetchall()
        cur.execute("select name from category")
        cat_name = cur.fetchall()
        self.cat_list = ["Select"]
        self.sup_list = ["Select"]
        for item in cat_name:
            self.cat_list.append(item[0])
        for item in sup_name:
            self.sup_list.append(item[0])
        self.cat_list = tuple(self.cat_list)
        self.sup_list = tuple(self.sup_list)

    def add(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get()=="" or self.var_sup.get()=="Select" or self.var_cat.get()=="Select":
                messagebox.showerror("Error"," Product Name and the details must be required",parent=self.root)
            else:
                cur.execute("select * from product where name=? and supplier=?",(self.var_name.get(),self.var_sup.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This product is already registered, try different", parent=self.root)
                else:
                    cur.execute("Insert into product(name,category,supplier,price,qty,status) values(?,?,?,?,?,?)",(
                                    self.var_name.get(),
                                    self.var_cat.get(),
                                    self.var_sup.get(),
                                    self.var_price.get(),
                                    self.var_quantity.get(),
                                    self.var_status.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Product added Successfully",parent=self.root)
                    self.show()
                    self.clear()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            for item in self.productTable.get_children():
                self.productTable.delete(item)

            for row in rows:
                self.productTable.insert('',END,values=row)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_name.set(row[1])
        self.var_cat.set(row[2])
        self.var_sup.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from the list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product Id", parent=self.root)
                else:
                    # "pid", "name", "category", "supplier", "price", "qty", "status"
                    cur.execute("update product set name=?,category=?,supplier=?,price=?,qty=?,status=? where pid=?",
                                (
                                    self.var_name.get(),
                                    self.var_cat.get(),
                                    self.var_sup.get(),
                                    self.var_price.get(),
                                    self.var_quantity.get(),
                                    self.var_status.get(),
                                    self.var_pid.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                    self.show()
                    self.clear()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.var_pid.set("")
        self.var_name.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("")
        self.show()


    def delete(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select Product from the list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    ans=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if(ans==True):
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Product Deleted Successfully",parent=self.root)
                        self.show()
                    else:
                        messagebox.showwarning("Cancelled","Employee not deleted",parent=self.root)
                    self.clear()
                    con.close()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    # self.var_searchby = StringVar()     "Select", "Category", "Supplier", "Name"
    # self.var_searchtxt = StringVar()
    def search(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if(self.var_searchby.get()=="Select"):
                messagebox.showerror("Error","Select search by option",parent=self.root)

            elif(self.var_searchtxt.get()==""):
                messagebox.showerror("Error","Search Input should be required",parent=self.root)
            else:
                    cur.execute("select * from product where "+self.var_searchby.get()+" like '%"+self.var_searchtxt.get()+"%'")

                    rows = cur.fetchall()
                    if(len(rows)==0):
                        messagebox.showerror("Error","No Record Found",parent=self.root)
                    else:
                        self.productTable.delete(*self.productTable.get_children())
                        for row in rows:
                            self.productTable.insert('', END, values=row)  # starting from start to end
        except EXCEPTION as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()