from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class Login:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title('LOGIN SYSTEM')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False,False)
        
        # ==================BUTTON SIGNUP =========================
        
        def createAccount():
        # =====================CREATE AN ACCOUNT ======================================== 
            self.registerScreen = Toplevel(self.root)
            self.registerScreen.title("USER REGISTRATION")
            self.registerScreen.geometry("925x500+300+200")
            self.registerScreen.configure(bg="#fff")
            self.registerScreen.resizable(False,False)
            self.register_image = Image.open("./cart.png")
            self.size = self.register_image.resize((300, 350))
            self.size_img = ImageTk.PhotoImage(self.size)
            Label(self.registerScreen,image = self.size_img,bg="#fff").place(x=100,y=30)
            self.frame = Frame(self.registerScreen,width=300,height=500,bg="#fff")
            self.frame.place(x=480,y=40)
            
            #=================REGISTRATION TEXT==============================================
            self.registration_label = Label(self.frame,text="REGISTRATION FORM",bg="#fff",fg="#57a1f8",font=("Microsoft YaHei UI Light",13,"bold"))
            self.registration_label.place(x=10,y=10)
            
            # ====================MOUSE EVENT PLACEHOLDER FIELD=====================
            
            def on_enter(e):
                self.fname.delete(0,"end")
        
        
            def on_leave(e):
                name = self.fname.get()
                if name =='':
                    self.fname.insert(0,"First Name")
            
            #==================FIRST NAME FIELD===============================
            self.fname = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
            self.fname.place(x=30,y=70)
            self.fname.insert(0,"First Name")
            self.fname.bind("<FocusIn>",on_enter)
            self.fname.bind("<FocusOut>",on_leave)
            # ===============TEXT BORDER BOTTOM======================
            
            self.border_bottom = Frame(self.frame,width=300,height=1,bg="grey")
            self.border_bottom.place(x=30,y=100)
            
            
            # ====================LAST NAME PLACEHOLDER FIELD=====================
            
            def on_enter(e):
                self.lname.delete(0,"end")
        
        
            def on_leave(e):
                name = self.lname.get()
                if name =='':
                    self.lname.insert(0,"Last Name")
            
            #==================FIRST NAME FIELD===============================
            self.lname = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
            self.lname.place(x=30,y=130)
            self.lname.insert(0,"Last Name")
            self.lname.bind("<FocusIn>",on_enter)
            self.lname.bind("<FocusOut>",on_leave)
             # ===============TEXT BORDER BOTTOM======================
            self.border_bottom = Frame(self.frame,width=300,height=1,bg="grey")
            self.border_bottom.place(x=30,y=160)
            
            
            
            # ====================EMAIL PLACEHOLDER FIELD=====================
            
            def on_enter(e):
                self.email.delete(0,"end")
        
        
            def on_leave(e):
                name = self.email.get()
                if name =='':
                    self.email.insert(0,"Email")
            
            #==================EMAIL NAME FIELD===============================
            self.email = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
            self.email.place(x=30,y=190)
            self.email.insert(0,"Email")
            self.email.bind("<FocusIn>",on_enter)
            self.email.bind("<FocusOut>",on_leave)
             # ===============TEXT BORDER BOTTOM======================
            self.border_bottom = Frame(self.frame,width=300,height=1,bg="grey")
            self.border_bottom.place(x=30,y=220)
            
            
            # ====================DEPARTMENT PLACEHOLDER FIELD=====================
            
            def on_enter(e):
                self.department.delete(0,"end")
        
        
            def on_leave(e):
                name = self.department.get()
                if name =='':
                    self.department.insert(0,"Department")
            
            #==================DEPARTMENT NAME FIELD===============================
            self.department = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
            self.department.place(x=30,y=250)
            self.department.insert(0,"Department")
            self.department.bind("<FocusIn>",on_enter)
            self.department.bind("<FocusOut>",on_leave)
             # ===============TEXT BORDER BOTTOM======================
            self.border_bottom = Frame(self.frame,width=300,height=1,bg="grey")
            self.border_bottom.place(x=30,y=280)
            
            
            
            # ====================PASSWORD PLACEHOLDER FIELD=====================
            
            def on_enter(e):
                self.password.delete(0,"end")
        
        
            def on_leave(e):
                name = self.password.get()
                if name =='':
                    self.password.insert(0,"Password")
            
            #==================FIRST NAME FIELD===============================
            self.password = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
            self.password.place(x=30,y=310)
            self.password.insert(0,"Password")
            self.password.bind("<FocusIn>",on_enter)
            self.password.bind("<FocusOut>",on_leave)
             # ===============TEXT BORDER BOTTOM======================
            self.border_bottom = Frame(self.frame,width=300,height=1,bg="grey")
            self.border_bottom.place(x=30,y=340)
            
            
            #===================== REGISTER BUTTON SIGN_UP=================================
            
            self.button = Button(self.frame,width=35,pady=7,text="CREATE AN ACCOUNT",bg='#57a1f8',fg="#fff",border=0,)
            self.button.place(x=40,y=390)
            
            self.registerScreen.mainloop()

        
        
        
        
        
        #================USER VALIDATION==================================================

        def submit():
            username = self.username.get()
            password = self.password.get()
            
            if username == 'admin' and password == '1234':
                messagebox.showinfo("Login successfully")
            else:
                messagebox.showerror("Wrong Credentials")
                
        
        
        
        
        # ====================USERNAME PLACEHOLDER FIELD=====================
            
        def on_enter(e):
            self.username.delete(0,"end")
        
        
        def on_leave(e):
            name = self.username.get()
            if name =='':
                self.username.insert(0,"Username")
        
        
        
        
    
        
        
        
        # =================SIDE IMAGE SECTION===============================
        self.image = Image.open("cart.png")
        self.resize_image = self.image.resize((300, 350))
        self.img = ImageTk.PhotoImage(self.resize_image)
        Label(self.root,image = self.img,bg="#fff").place(x=100,y=30)

        # =============LOGIN FRAME========================
        self.frame = Frame(self.root,width=350,height=400,bg="#fff")
        self.frame.place(x=480,y=30)
        
        
        # ===========HEADER TEXT===============================
        self.header = Label(self.frame,text="USER LOGIN",fg="#57a1f8",bg="#fff",font=("Microsoft YaHei UI Light",16,"bold"))
        self.header.place(x=30,y=30)
        
        # =======================USER ENTRY======================
        self.username = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
        self.username.place(x=30,y=80)
        self.username.insert(0,"Username")
        self.username.bind("<FocusIn>",on_enter)
        self.username.bind("<FocusOut>",on_leave)
        
        # ===============TEXT BORDER BOTTOM======================
        self.border_bottom = Frame(self.frame,width=250,height=1,bg="grey")
        self.border_bottom.place(x=30,y=110)

        
        # ==================PASSWORD SECTION======================
        # ====================PASSWORD PLACEHOLDER FIELD=====================
            
        def on_enter(e):
            self.password.delete(0,"end")
        
        
        def on_leave(e):
            password = self.password.get()
            if password =='':
                self.password.insert(0,"Password")
        self.password = Entry(self.frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10))
        self.password.place(x=30,y=130)
        self.password.insert(0,"Password")
        self.password.bind("<FocusIn>",on_enter)
        self.password.bind("<FocusOut>",on_leave)
        
        # ===============TEXT BORDER BOTTOM======================
        self.border_bottom = Frame(self.frame,width=250,height=1,bg="grey")
        self.border_bottom.place(x=30,y=160)
        
        
        
        # ================BUTTON SUBMIT===========================
        self.button = Button(self.frame,width=35,pady=7,text="Sign in",bg='#57a1f8',fg="#fff",border=0,command=submit)
        self.button.place(x=35,y=190)
        
        
        # =============================DONT HAVE AN ACCOUNT=========================================
        self.forget_password = Label(self.frame,text="Don't have an account ?",fg="black",bg="#fff",font=("Microsoft YaHei UI Light",9))
        self.forget_password.place(x=65,y=250)
        # =====================SIGNUP TEXT BUTTON==========================
        self.signup = Button(self.frame,text="Sign up",fg="#57a1f8",bg="#fff", border=0, cursor="hand2" ,font=("Microsoft YaHei UI Light",9),command=createAccount)
        self.signup.place(x=215,y=250)

        # ====================== OR LABEL=================================
        self.label_or = Label(self.frame,text="OR",fg="black",bg="#fff",font=("Microsoft YaHei UI Light",9,"bold")).place(x=150,y=290)
        # =================SOCIAL MEDIAL ICONS=============================
        self.facebook_icon = Image.open("facebook.png")
        self.resize_icon = self.facebook_icon.resize((30, 30))
        self.facebook_img = ImageTk.PhotoImage(self.resize_icon)
        Label(self.frame,image = self.facebook_img,bg="#fff",cursor="hand2").place(x=90,y=340)
        
        self.google_icon = Image.open("google.png")
        self.resize_icon_google = self.google_icon.resize((30, 30))
        self.google_img = ImageTk.PhotoImage(self.resize_icon_google)
        Label(self.frame,image = self.google_img,bg="#fff",cursor="hand2").place(x=200,y=340)
    
    
if __name__ == '__main__':
    root = Tk()
    obj  = Login(root)
    root.mainloop()