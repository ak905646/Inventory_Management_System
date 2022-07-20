import os
import sqlite3
import time
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1560x790+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white",bd = 2)

        # ===title===

        self.icon_title = PhotoImage(file = "images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w",padx = 20 ).place(x=0,y=0,relwidth=1,height=70)

        # === button log out ====#

        btn_logout = Button(self.root,text = "Logout" ,font = ("times new roman",15,"bold"),bg = "yellow",cursor="hand2",command=self.logout)
        btn_logout.place(x=1370,y=10,height = 49,width = 120)

        # ======clock===== #

        self.lbl_clock = Label(self.root, text="Welcome to Inventory Mangement System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS ", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # ===left menu ===#

        '''Frames are nothing but a window that is placed inside a window '''
        self.menu_logo = Image.open("images/menu_im.png")
        self.menu_logo = self.menu_logo.resize((200,200),Image.ANTIALIAS)
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        LeftMenu = Frame(self.root,bd=2,relief = RIDGE,bg="white")
        LeftMenu.place(x=0,y=100,width = 200,height = 569)

        lbl_menuLogo = Label(LeftMenu,image=self.menu_logo)
        lbl_menuLogo.pack(side = TOP,fill=X)

         #== menu Buttons === #

        label_menu = Label(LeftMenu,text = "Menu",font=("times new roman",20),bg="#009688")
        label_menu.pack(side = TOP,fill = X)

        self.menu_icon = PhotoImage(file="images/side.png")
        btn_employee = Button(LeftMenu, text="Employee", image = self.menu_icon, compound = LEFT, padx = 10, command = self.employee,
                              font=("times new roman", 20, "bold"), bg="white",bd = 3,cursor="hand2",anchor="w")
        btn_employee.pack(side = TOP,fill = X)

        btn_supplier = Button(LeftMenu, text="Supplier", image=self.menu_icon, compound=LEFT, padx=5,command=self.supplier,
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",anchor="w")
        btn_supplier.pack(side=TOP, fill=X)

        btn_category = Button(LeftMenu, text="Category", image=self.menu_icon, compound=LEFT, padx=5,command=self.category,
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",anchor="w")
        btn_category.pack(side=TOP, fill=X)

        btn_product = Button(LeftMenu, text="Products", image=self.menu_icon, compound=LEFT, padx=5,command=self.product,
                             font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",anchor="w")
        btn_product.pack(side=TOP, fill=X)

        btn_sales = Button(LeftMenu, text="Sales", image=self.menu_icon, compound=LEFT, padx=5,command=self.sales,
                           font=("times new roman", 20, "bold"),
                           bg="white", bd=3, cursor="hand2",anchor="w")
        btn_sales.pack(side=TOP, fill=X)

        btn_exit = Button(LeftMenu, text="Exit", image=self.menu_icon, compound=LEFT, padx=5,
                          font=("times new roman", 20, "bold"),command=self.exit,
                          bg="white", bd=3, cursor="hand2",anchor="w")
        btn_exit.pack(side=TOP, fill=X)

        #==content===#

        self.lbl_employee = Label(self.root, text="Total Employee\n [ 0 ]",font=("goudy old style", 20, "bold"),bg="#33bbf9", fg="white",bd = 5,relief = RIDGE)
        self.lbl_employee.place(x=300,y=150,width = 300 ,height=150)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n [ 0 ]",font=("goudy old style", 20, "bold"),bg="#ff5722", fg="white",bd = 5,relief = RIDGE)
        self.lbl_supplier.place(x=675,y=150,width = 300 ,height=150)

        self.lbl_category = Label(self.root, text="Total Category\n [ 0 ]",font=("goudy old style", 20, "bold"),bg="#009688", fg="white",bd = 5,relief = RIDGE)
        self.lbl_category.place(x=1050,y=150,width = 300 ,height=150)

        self.lbl_product = Label(self.root, text="Total Product\n [ 0 ]",font=("goudy old style", 20, "bold"),bg="#607d8b", fg="white",bd = 5,relief = RIDGE)
        self.lbl_product.place(x=475,y=425,width = 300 ,height=150)

        self.lbl_sales = Label(self.root, text="Total Sales\n [ 0 ]",font=("goudy old style", 20, "bold"),bg="#ffc107", fg="white",bd = 5,relief = RIDGE)
        self.lbl_sales.place(x=875,y=425,width = 300 ,height=150)


        #==Footer===#

        self.lbl_footer = Label(self.root,
                               text="IMS - Inventory Management System \n For any technical issues :-  Contact: +91 9525857792 , Email: ak905646@gmail.com",
                               font=("times new roman", 14), bg="#4d636d", fg="white")
        self.lbl_footer.pack(side = BOTTOM,fill = X)

        self.update_data()
    #==============================================================================#

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def exit(self):
        self.new_win.destroy()

    def update_data(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            total_employee = len(cur.fetchall())
            self.lbl_employee.config(text=f"Total Employee\n [ {str(total_employee)} ]")
            cur.execute("select * from category")
            total_category = len(cur.fetchall())
            self.lbl_category.config(text=f"Total Category\n [ {str(total_category)} ]")
            cur.execute("select * from product")
            total_product = len(cur.fetchall())
            self.lbl_product.config(text=f"Total Products\n [ {str(total_product)} ]")
            cur.execute("select * from supplier")
            total_supplier = len(cur.fetchall())
            self.lbl_supplier.config(text=f"Total Suppliers\n [ {str(total_supplier)} ]")
            total_sales = len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales\n [ {str(total_sales)} ]")

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Mangement System \t\t Date: {str(date_)} \t\t Time: {str(time_)}")
            self.lbl_clock.after(200, self.update_data)
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system('python login.py')

if __name__=="__main__":
    root = Tk()
    obj1 = IMS(root)
    root.mainloop()
