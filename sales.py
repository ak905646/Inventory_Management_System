import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os


class salesClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x550+220+140")
        self.root.title("Inventory Management System")
        self.root.config(bg="white",bd=5)
        self.root.focus_force()
    #=======Variables========#

        self.var_invoice=StringVar()
        self.bill_list = []


        #==Title====

        sales_lbl = Label(self.root, text="View Customer Bill", font=("goudy old style", 30), bg="#184a45")
        sales_lbl.pack(side=TOP, fill=X)

        lbl_invoice=Label(self.root,text="Invoice No.",font=("title new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("title new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)

        btn_search=Button(self.root,text="Search",font=("title new roman",15),bg="#2196f3",fg="white",cursor="hand2",command = self.search).place(x=360,y=100,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",font=("title new roman",15),bg="lightgray",cursor="hand2",command = self.clear).place(x=480,y=100,width=110,height=28)


        sales_frame = Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=150,width=220,height=350)


        scrolly = Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list = Listbox(sales_frame,font=("goudy old style", 15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)

        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

    #========Bill Area============#

        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=320, y=150, width=500, height=350)

        bill_area_lbl = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange")
        bill_area_lbl.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        scrollx2 = Scrollbar(bill_frame,orient=HORIZONTAL)
        self.bill_area = Text(bill_frame, font=("goudy old style", 13), bg="lightyellow", yscrollcommand=scrolly2.set,xscrollcommand=scrollx2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrollx2.pack(side=BOTTOM,fill=X)
        scrolly2.config(command=self.bill_area.yview)
        scrollx2.config(command=self.bill_area.xview)
        self.bill_area.pack(fill=BOTH, expand=1)

        #===Image========#

        self.im1 = Image.open("images/cat2.jpg")
        self.im1 = self.im1.resize((450, 300), Image.ANTIALIAS)
        self.im1 = ImageTk.PhotoImage(self.im1)
        self.lb1_im1 = Label(self.root, image=self.im1, bd=0)
        self.lb1_im1.place(x=820, y=140)

        self.show()
        #========Functions========

    def show(self):
        self.sales_list.delete(0,END)
        self.bill_list.clear()
        # print(os.listdir('../IMS'))     This function will print whatever in the bill folder
            # print(i.split('.'),i.split('.')[-1]) This function is used to get the extension of element..if it is type of txt we
            #will add this is to our list.
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        fp = open('bill/'+file_name,'r')
        fd = fp.read()
        self.bill_area.delete('1.0',END)
        self.bill_area.insert('1.0',fd)
        fp.close()

    def search(self):
        if self.var_invoice.get=='':
            messagebox.showerror("Error","Invoice no. should be required")
        else:
            # print(self.bill_list)
            # print(self.var_invoice.get())
            if(self.var_invoice.get() in self.bill_list):
                fp = open('bill/' + self.var_invoice.get() + '.txt', 'r')
                fd = fp.read()
                self.bill_area.delete('1.0', END)
                self.bill_area.insert('1.0', fd)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice NO.")
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
        self.var_invoice.set('')

if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()