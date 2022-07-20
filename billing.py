from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import time
import sqlite3
import os
import tempfile


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1560x790+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white",bd = 2)


        #==variables====
        self.cart_list=[]
        self.var_search = StringVar()


        # ===title===

        self.icon_title = PhotoImage(file = "images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w",padx = 20 ).place(x=0,y=0,relwidth=1,height=70)

        # === button log out ====#

        btn_logout = Button(self.root,text = "Logout" ,font = ("times new roman",15,"bold"),bg = "yellow",cursor="hand2",command=self.logout)
        btn_logout.place(x=1370,y=10,height = 49,width = 120)

        # ======clock===== #

        self.lbl_clock = Label(self.root, text="Welcome to Inventory Mangement System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS ", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #-------Product Frame-----#

        ProductFrame1 = Frame(self.root,bd = 4,relief = RIDGE,bg = "white")
        ProductFrame1.place(x=6,y=110,width = 410,height=620)

        Ptitle = Label(ProductFrame1,text="All Products",font = ("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #====Product Frame2 ==== For searching the product=======

        ProductFrame2 = Frame(ProductFrame1, bd=4, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        Lbl_search = Label(ProductFrame2,text="Search Product | By Name ",font = ("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_name = Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)

        txt_search = Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=135,y=50,width=150,height=25)
        btn_search = Button(ProductFrame2,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=290,y=50,height=25,width=95)

        btn_show_all = Button(ProductFrame2, text="Show All", font=("goudy old style", 15, "bold"), bg="#083531",fg="white", cursor="hand2",command=self.show).place(x=290, y=10, height=25, width=95)

        # ====Product Frame3 ==== For details of the product=======

        ProductFrame3 = Frame(ProductFrame1,bd = 4,relief= RIDGE,bg="white")
        ProductFrame3.place(x=2,y=140,width = 398,height = 425)

        scrolly = Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=('pid','name','price','qty','status'),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="Product Id")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Quantity")
        self.product_Table.heading("status",text="Status")

        self.product_Table['show'] = 'headings'

        self.product_Table.column("pid",width=75)
        self.product_Table.column("name",width=75)
        self.product_Table.column("price",width=75)
        self.product_Table.column("qty",width=75)
        self.product_Table.column("status",width=75)

        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note = Label(ProductFrame1,text="Note: Enter 0 quantity to remove the product from the cart",font=("goudy old style",12),bg="white",fg = "red").pack(side="bottom",fill=X)

        #======Customer Frame====
        self.var_contact = StringVar()
        self.var_Cname = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=600, height=70)

        Ctitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)

        lbl_name = Label(CustomerFrame,text="Name",font=("times new roman",13),bg="white").place(x=5,y=30)
        txt_name = Entry(CustomerFrame,textvariable=self.var_Cname,font=("times new roman",13),bg="lightyellow").place(x=60,y=33,width=200)


        lbl_contact = Label(CustomerFrame, text="Contact No", font=("times new roman", 13), bg="white").place(x=280, y=30)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13),bg="lightyellow").place(x=370, y=33, width=200)

        #=====Calculator and cart frame======

        Cal_Cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420, y=190, width=600, height=380)

                #======Calculator Frame==========
        self.var_cal_input = StringVar()

        Cal_Frame = Frame(Cal_Cart_Frame, bd=4, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=320, height=360)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=26,bd=10,relief=RIDGE,state='readonly',justify='right')
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),bd=5,width=5,pady=15,cursor='hand2',command=lambda : self.get_input('7')).grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),bd=5,width=5,pady=15,cursor='hand2',command=lambda : self.get_input('8')).grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),bd=5,width=5,pady=15,cursor='hand2',command=lambda : self.get_input('9')).grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),bd=5,width=5,pady=15,cursor='hand2',command=lambda : self.get_input('+')).grid(row=1,column=3)

        btn_4 = Button(Cal_Frame, text='4', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('4')).grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('5')).grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('6')).grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text='-', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('-')).grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('1')).grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('2')).grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('3')).grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text='*', font=('arial', 15, 'bold'), bd=5, width=5, pady=15, cursor='hand2',command=lambda : self.get_input('*')).grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0', font=('arial', 15, 'bold'), bd=5, width=5, pady=16, cursor='hand2',command=lambda : self.get_input('0')).grid(row=4, column=0)
        btn_c = Button(Cal_Frame, text='C', font=('arial', 15, 'bold'), bd=5, width=5, pady=16, cursor='hand2',command=self.clear_cal).grid(row=4, column=1)
        btn_eq = Button(Cal_Frame, text='=', font=('arial', 15, 'bold'), bd=5, width=5, pady=16, cursor='hand2',command=self.perform_cal).grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text='/', font=('arial', 15, 'bold'), bd=5, width=5, pady=16, cursor='hand2',command=lambda : self.get_input('/')).grid(row=4, column=3)


        #=====Cart Frame=============

        Cart_Frame = Frame(Cal_Cart_Frame, bd=4, relief=RIDGE, bg="white")
        Cart_Frame.place(x=330, y=10, width=260, height=360)

        self.lbl_cart_title = Label(Cart_Frame,text = "Cart      Total Products : [0]",font=("times new roman",15),bg="lightgray")
        self.lbl_cart_title.pack(side=TOP,fill=X)


        scrollx_cart = Scrollbar(Cart_Frame,orient=HORIZONTAL)
        scrolly_cart = Scrollbar(Cart_Frame,orient=VERTICAL)
        self.Cart_table = ttk.Treeview(Cart_Frame,columns=("pid","product","qty",'price'),xscrollcommand=scrollx_cart.set,yscrollcommand=scrolly_cart.set)
        scrollx_cart.pack(side=BOTTOM,fill=X)
        scrolly_cart.pack(side=RIGHT,fill=Y)
        scrollx_cart.config(command=self.Cart_table.xview)
        scrolly_cart.config(command=self.Cart_table.yview)
        self.Cart_table.heading('pid',text="PID")
        self.Cart_table.heading('product',text="Product")
        self.Cart_table.heading('qty',text="Quantity")
        self.Cart_table.heading('price',text="Price")

        self.Cart_table['show']="headings"

        self.Cart_table.column('pid',width=40)
        self.Cart_table.column('product',width=100)
        self.Cart_table.column('qty',width=60)
        self.Cart_table.column('price',width=50)

        self.Cart_table.bind("<ButtonRelease-1>",self.get_data_cart_table)

        self.Cart_table.pack(fill=BOTH,expand=1)

        #====ADD CART Visits Frame====

        add_cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        add_cart_Frame.place(x=420, y=580, width=600, height=150)

            #===variables====
        self.var_pid = StringVar()
        self.var_Pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()


        lbl_p_name = Label(add_cart_Frame,text="Product Name",font=("times new roman",15),bg="white").place(x=20,y=10)
        txt_p_name = Entry(add_cart_Frame,textvariable = self.var_Pname,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=10,y=45,width=150)

        p_price = Label(add_cart_Frame,text="Price Per Quantity",font=("times new roman",15),bg="white").place(x=230,y=10)
        txt_p_price = Entry(add_cart_Frame,textvariable = self.var_price, font=("times new roman", 15), bg="lightyellow",state = "readonly").place(x=230, y=45, width=150)

        p_qty = Label(add_cart_Frame,text="Quantity",font=("times new roman",15),bg="white").place(x=470,y=10)
        txt_p_qty = Entry(add_cart_Frame,textvariable = self.var_qty, font=("times new roman", 15), bg="lightyellow").place(x=440, y=45, width=150)

        self.lbl_instock = Label(add_cart_Frame,text="In Stock ",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=105)

        btn_clear = Button(add_cart_Frame,text="Clear",font=("times new roman",15),bg="lightgray",cursor="hand2",command=self.clear).place(x=200,y=90,height=40,width=150)

        btn_add_update = Button(add_cart_Frame,text="Add/Update",font=("times new roman",15),bg="orange",cursor="hand2",command=self.add_update_cart).place(x=400,y=90,height=40,width=150)

        #========Billl Area=======

        BillFrame = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        BillFrame.place(x=1025, y=110, width=490, height=460)

        Btitle = Label(BillFrame, text="Customer Bill", font=("goudy old style", 20, "bold"), bg="maroon",fg="white").pack(side=TOP, fill=X)
        scrolly_bill = Scrollbar(BillFrame,orient=VERTICAL)
        scrolly_bill.pack(side=RIGHT,fill=Y)
        self.txt_bill_area = Text(BillFrame,yscrollcommand=scrolly_bill.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly_bill.config(command=self.txt_bill_area.yview)

        #=======Billing Buttons=========

        Bill_Button_Frame = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Bill_Button_Frame.place(x=1025, y=580, width=490, height=150)

        self.lbl_amount = Label(Bill_Button_Frame,text='Bill Amount\n[0]',font=('goudy old style',15,"bold"),bg='#3f51b5',bd=2,relief=RIDGE,fg='white',width=14,height=3)
        self.lbl_amount.grid(row=0,column=1)

        self.lbl_discount = Label(Bill_Button_Frame, text='Discount\n[5%]', font=('goudy old style', 15, "bold"),bg='#8bc34a', bd=2,relief=RIDGE,fg='white', width=14, height=3)
        self.lbl_discount.grid(row=0, column=2)

        self.lbl_net_pay = Label(Bill_Button_Frame, text='Net Pay\n[0]', font=('goudy old style', 15, "bold"),bg='#607d8b', bd=2,relief=RIDGE,fg='white', width=14, height=3)
        self.lbl_net_pay.grid(row=0, column=3)


        btn_print = Button(Bill_Button_Frame,text="Print",font=('goudy old style',15,'bold'),bg='lightgreen',cursor='hand2').place(x= 5,y= 80, height = 55, width=150)


        btn_clear_all = Button(Bill_Button_Frame,text="Clear All",font=('goudy old style',15,'bold'),bg='gray',fg='white',cursor='hand2',command=self.clear_all).place(x= 165,y= 80, height = 55, width=150)


        btn_generate_bill = Button(Bill_Button_Frame,text="Generate Bill\nSave Bill",font=('goudy old style',15,'bold'),bg='#009688',fg='white',cursor='hand2',command=self.generate_bill).place(x= 325,y= 80, height = 55, width=150)

        #======footer====================

        self.lbl_footer = Label(self.root,text="IMS - Inventory Management System \n For any technical issues :-  Contact: +91 9525857792 , Email: ak905646@gmail.com",font=("times new roman", 14), bg="#4d636d", fg="white",pady=5)
        self.lbl_footer.place(x=0,y=740,width=1532)

        self.show()
        self.update_clock()
    #=======Functions for calculator========

    def get_input(self,num):
        x_num = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(x_num)
    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    #=========Others Functions======

            #self.product_Table = ttk.Treeview(ProductFrame3, columns=('pid', 'name', 'price', 'qty', 'status')
    def show(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status != 'Inactive'")
            rows = cur.fetchall()
            for item in self.product_Table.get_children():
                self.product_Table.delete(item)

            for row in rows:
                self.product_Table.insert('', END, values=row)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            if(self.var_search.get()==""):
                messagebox.showerror("Error","Search Input should be required",parent=self.root)
            else:
                    cur.execute("select pid,name,price,qty,status from product where name like '%"+self.var_search.get()+"%' and status!='Inactive'")
                    rows = cur.fetchall()
                    if(len(rows)==0):
                        messagebox.showerror("Error","No Product Found",parent=self.root)
                    else:
                        self.product_Table.delete(*self.product_Table.get_children())
                        for row in rows:
                            self.product_Table.insert('', END, values=row)  # starting from start to end
        except EXCEPTION as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # self.product_Table = ttk.Treeview(ProductFrame3, columns=('pid', 'name', 'price', 'qty', 'status')
    def get_data(self,ev):
        f = self.product_Table.focus()
        content = self.product_Table.item(f)
        row=content['values']
        self.var_pid.set(row[0])
        self.var_Pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text='In Stock [' + str(row[3]) + ']')
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def clear(self):
        self.var_Pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        for item in self.Cart_table.get_children():
            self.Cart_table.delete(item)
        self.cart_list=[]
        self.lbl_amount.config(text='Bill Amount\n[0]')
        self.lbl_net_pay.config(text='Net Pay\n[0]')
        self.lbl_cart_title.config(text="Cart      Total Products : [0]")
        self.lbl_instock.config(text="In Stock")
        self.var_Cname.set('')
        self.var_contact.set('')

    def add_update_cart(self):
        if (self.var_pid.get() == ''):
            messagebox.showerror('Error', 'Please select the product', parent=self.root)
        elif(self.var_qty.get()==''):
            messagebox.showerror('Error','Quantity is required',parent = self.root)
        elif(int(self.var_stock.get())<int(self.var_qty.get())):
            messagebox.showerror('Error','Please reduce the no of quantity of product')
        else:
            price_cal = float(int(self.var_qty.get())*float(self.var_price.get()))
            # print(price_cal)
            # columns=("pid","product","qty",'price')
            flag=False
            index=-1
            for item in self.cart_list:
                index= index + 1
                if(item[0]==self.var_pid.get()):
                    flag=True
                    conf=messagebox.askyesno('Confirmation',"Product already present, Do you really want to update the product")
                    if(conf==True):
                        if(self.var_qty.get()=='0'):
                            self.cart_list.pop(index)
                        else:
                            item[2] = int(self.var_qty.get())
                            item[3] = price_cal
                    break

            if(flag==False):
                cart_data=[self.var_pid.get(),self.var_Pname.get(),self.var_qty.get(),price_cal,self.var_stock.get()]
                self.cart_list.append(cart_data)

            self.show_cart()
            self.update_bill()

    def update_bill(self):
        self.bill_amt =  0
        # columns=("pid","product","qty",'price')
        for item in self.cart_list:
            self.bill_amt = self.bill_amt + float(item[3])
        net_pay = self.bill_amt*0.95
        self.lbl_amount.config(text='Bill Amount\n[Rs: '+str(self.bill_amt)+']')
        self.lbl_net_pay.config(text='Net Pay\n[Rs: '+str(net_pay)+']')
        self.lbl_cart_title.config(text = "Cart      Total Products : ["+str(len(self.cart_list))+"]")

    def show_cart(self):
        try:
            for item in self.Cart_table.get_children():
                self.Cart_table.delete(item)
            for row in self.cart_list:
                self.Cart_table.insert('', END, values=row)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    #columns=("pid","product","qty",'price')
    def get_data_cart_table(self,ev):
        f=self.Cart_table.focus()
        content=self.Cart_table.item(f)
        row=content['values']
        self.var_pid.set(row[0])
        self.var_Pname.set(row[1])
        self.var_qty.set(row[2])
        pofo=int(float(row[3])/float(row[2]))
        self.var_price.set(pofo)
        self.var_stock.set(row[4])
        self.lbl_instock.config(text="In Stock ["+self.var_stock.get()+"]")

#===========Billing functions==================


    def generate_bill(self):
        if(self.var_Cname.get()=="" or self.var_contact.get()==""):
            messagebox.showerror('Error','Customer details are required')
        elif(len(self.cart_list)==0):
            messagebox.showerror('Error',"Please select the product first")
        else:
            invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
            # =====Top Bill=====
            self.bill_top(invoice)
            #=======Middle Bill=======
            self.bill_middle()
            #=======Bottom Billl=====
            self.bill_bottom()

            #====Saving the generated file======
            bill_text = self.txt_bill_area.get('1.0',END)
            file_obj = open('bill/'+str(invoice)+'.txt','w')
            file_obj.write(bill_text)
            file_obj.close()
            messagebox.showinfo('Saved','Your Bill has been Saved in bill folder',parent=self.root)

    def bill_top(self,invoice):
        bill_top = f'''
\t\t\t XYZ - Inventory
\tPhone No : 9525857792          Patna-801110
==================================================
Customer Name : {self.var_Cname.get()}
Ph No. : {self.var_contact.get()}
Bill No. : {str(invoice)}\t\t\t\t Date : {str(time.strftime("%d/%m/%Y"))}
{str("="*51)}
Product Name\t\t\tQuantity\t\tPrice
'''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top)


    def bill_middle(self):
    # columns=("pid","product","qty",'price')
        try:
            middle = ""
            middle=middle+"===================================================\n"
            con = sqlite3.connect(r'ims.db')
            cur = con.cursor()
            for item in self.cart_list:
                middle=middle+item[1]+"\t\t\t"+str(item[2])+"\t\t"+str(item[3])+"\n"
                self.txt_bill_area.insert(END, middle)

            # =======updating the product table======================#

                new_qty = int(item[4])-int(item[2])
                new_status = 'Active'
                if(new_qty==0):
                    new_status = 'Inactive'
                the_pid = item[0]
                cur.execute('update product set qty=? ,status=? where pid=?',(new_qty,new_status,the_pid))
                con.commit()
            con.close()
            self.show()

        except EXCEPTION as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)



    def bill_bottom(self):
        self.update_bill()
        bottom=f'''
{str("="*51)}
Bill Amount\t\t\tRs. {str(self.bill_amt)}
Discount\t\t\tRs. {str(self.bill_amt*0.05)}
Net Pay\t\t\tRs. {str(self.bill_amt*0.95)}
{str("=" * 51)}
'''
        self.txt_bill_area.insert(END,bottom)

    def clear_all(self):
        self.clear()
        self.txt_bill_area.delete('1.0',END)

    def update_clock(self):
        date_ = time.strftime("%I:%M:%S")
        time_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Mangement System \t\t Date: {str(date_)} \t\t Time: {str(time_)} ")
        self.lbl_clock.after(200,self.update_clock)

    def logout(self):
        self.root.destroy()
        os.system('python login.py')

if __name__=="__main__":
    root = Tk()
    obj1 = BillClass(root)
    root.mainloop()
