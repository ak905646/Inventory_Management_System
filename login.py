from tkinter import *
from PIL import ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os


class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1550x790+0+0")
        self.root.config(bg="#fafafa")
    #===========Variables=========
        self.username = StringVar()
        self.password = StringVar()

    #=========Images==============
        self.phone_image=ImageTk.PhotoImage(file="Images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=250,y=90)

        self.loginFrame=Frame(self.root,bd=2,relief=RIDGE,bg="#fafafa")
        self.loginFrame.place(x=805,y=130,width=400,height=550)

        title=Label(self.loginFrame,text="Login System",font=("Elephant",30,"bold"),bg="#fafafa").place(x=0,y=30,relwidth=1)

        lbl_username=Label(self.loginFrame,text="Employee ID",font=('times new roman',15),bg='white',fg="#767171").place(x=70,y=130)
        txt_username=Entry(self.loginFrame,textvariable=self.username,font=('times new roman',15),bg='lightyellow').place(x=70,y=160,width=250,height=30)

        lbl_password = Label(self.loginFrame, text="Password", font=('times new roman', 15), bg='white',fg="#767171").place(x=70, y=210)
        txt_password = Entry(self.loginFrame,textvariable=self.password, font=('times new roman', 15), bg='lightyellow').place(x=70, y=240,width=250,height=30)

        btn_login=Button(self.loginFrame,text="Log In",font=("times new roman",20,'bold'),bg='#00B0f0',fg="white",activebackground="#00B0f0",activeforeground="white",cursor='hand2',command=self.login).place(x=70,y=320,width=250,height=40)

        hr=Label(self.loginFrame,bg="lightgray").place(x=70,y=420,width=250,height=2)
        lbl_or=Label(self.loginFrame,text="OR",font=('times new roman',15),bg='white',fg="#767171").place(x=185,y=407)

        btn_forget=Button(self.loginFrame,text='Forget Password ?',font=('times new roman',13),bg="white",fg="#00759E",bd=0,activebackground='white',activeforeground='#00759E',cursor='hand2',command=self.forgot).place(x=140,y=460)

#=================Phone animation====================

        self.lbl_animation=Label(self.root,bg="lightgray")
        self.lbl_animation.place(x=418,y=193,width=239,height=429)
        self.im1=ImageTk.PhotoImage(file='Images/im1.png')
        self.im2=ImageTk.PhotoImage(file='Images/im2.png')
        self.im3=ImageTk.PhotoImage(file='Images/im3.png')

        self.animate()

#==========Backend Functions=====================

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_animation.config(image=self.im)
        self.lbl_animation.after(1500,self.animate)

    def login(self):
        con=sqlite3.connect(r'ims.db')
        cur=con.cursor()
        try:
            if (self.username.get() == '' or self.password.get() == ''):
                messagebox.showerror("Error", 'All Fields are required',parent=self.root)
            else:
                cur.execute('select * from employee where eid = ? and pass = ?',(self.username.get(),self.password.get()))
                user_data=cur.fetchone()
                if(user_data==None):
                    messagebox.showerror('Error',"Invalid username or password")
                else:
                    self.root.destroy()
                    if(user_data[8]=='Admin'):
                        os.system('python dashboard.py')
                    elif (user_data[8]=='Employee'):
                        os.system('python billing.py')

        except EXCEPTION as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)





    def forgot(self):
        pass


if __name__=="__main__":
    root = Tk()
    obj1 = login_system(root)
    root.mainloop()