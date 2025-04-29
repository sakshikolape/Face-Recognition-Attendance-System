from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from student import  Student
import tkinter
import os
from train import Train
from Face_detection import face_detection
from attendance import Attendance
from main import Face_Recognition_system

def main1():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\saksh\Downloads\face_detection\college_images\login.png")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\abc4.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        messagebox.showinfo("Info","Your Email is Username")

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=250,width=270)

        #icon images
        img2=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\abc3.webp")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_img2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\img12.webp")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=393,width=25,height=25)
        
        #Login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=150)

        #Forget Password Button
        forgetbtn=Button(frame,text="Forgot Password",command=self.forget_password_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=16,y=380,width=150)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()==""or self.txtpassword.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="User1"and self.txtpassword.get()=="1234":
            messagebox.showinfo("Success","Welcome To Our Software")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpassword.get()
                                                                            ))
            row=my_cursor.fetchone()
            #print Row
            if row==None:
                messagebox.showerror("Error","Invalid Username And Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_system(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #Reset Password 
    def reset_pass(self):
        if self.combo_security.get()=="select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and security=%s and sec_ans=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,Please login with new password",parent=self.root2)
                self.root2.destroy()


    #Forget Password Window
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Birth Place" ,"Your Father's Name","Your Favourite Color")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)

                sec_ans=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                sec_ans.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",13))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",13))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #Variables
        self.var_fname=StringVar()
        self.var_l_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security=StringVar()
        self.var_sec_ans=StringVar()
        self.var_password=StringVar()
        self.var_con_pass=StringVar()
        
        #Background Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\saksh\Downloads\face_detection\college_images\background_image.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left Image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\saksh\Downloads\face_detection\college_images\left_image.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=600,height=550)

        #Main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=650,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #Label and Entry

        #Row_1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=350,y=100)

        self.txt_l_name=ttk.Entry(frame,textvariable=self.var_l_name,font=("times new roman",13))
        self.txt_l_name.place(x=350,y=130,width=250)
        
        #Row_2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=350,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13))
        self.txt_email.place(x=350,y=200,width=250)
        
        #Row_3
        security=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security.place(x=50,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_security,font=("times new roman",13,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Birth Place" ,"Your Father's Name","Your Favourite Color")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)

        sec_ans=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        sec_ans.place(x=350,y=240)
        
        self.txt_sec_ans=ttk.Entry(frame,textvariable=self.var_sec_ans,font=("times new roman",13))
        self.txt_sec_ans.place(x=350,y=270,width=250)

        #Row_4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=310)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",13))
        self.txt_password.place(x=50,y=340,width=250)
        
        con_pass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        con_pass.place(x=350,y=310)
        
        self.txt_con_pass=ttk.Entry(frame,textvariable=self.var_con_pass,font=("times new roman",13))
        self.txt_con_pass.place(x=350,y=340,width=250)

        #check Button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Terms & Conditions",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=390)

        #Buttons
        img=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\register-now.jpg")
        img=img.resize((200,100))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=30,y=420,width=200)

        img_1=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\for_login.jpg")
        img_1=img_1.resize((200,50))
        self.photoimage_1=ImageTk.PhotoImage(img_1)
        b1=Button(frame,image=self.photoimage_1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=360,y=445,width=200)
        
    #Function Declaration

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_security.get()=="Select":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_password.get()!=self.var_con_pass.get():
            messagebox.showerror("Error","Both Passwords must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute( query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists,Please try another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                        self.var_l_name.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security.get(),
                                                                                        self.var_sec_ans.get(),
                                                                                        self.var_password.get()
                                                                                       
                                                                                       ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()

class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1580x790+0+0")
        self.root.title("Face Recognition System")

        #Image_1
        img=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f1.jfif")
        img=img.resize((500,150))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #Image_2
        img1=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f14.jfif")
        img1=img1.resize((550,150))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        #Image_3
        img2=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f3.jfif")
        img2=img2.resize((599,150))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=600,height=150)

        #Background_Image
        img3=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f2.jfif")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE DETECTION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student_Details_Button
        img4=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f5.png")
        img14=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=400,height=200)
        
        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=300,width=400,height=40)
        
        #Face_Detect_Button
        img5=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f13.jfif")
        img15=img5.resize((1530,710))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=575,y=100,width=400,height=200)
        
        b1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=575,y=300,width=400,height=40)
       
        #Attendance_Button
        img6=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f14.jfif")
        img16=img6.resize((1530,710))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1050,y=100,width=400,height=200)
        
        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1050,y=300,width=400,height=40)
        
        #Data_Button
        img7=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f9.webp")
        img17=img7.resize((1530,710))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=400,width=400,height=200)
        
        b1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=600,width=400,height=40)

        #Photos_Button
        img8=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f10.png")
        img18=img8.resize((1530,710))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=575,y=400,width=400,height=200)
        
        b1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=575,y=600,width=400,height=40) 

        #Exit_Button
        img9=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f12.png")
        img19=img9.resize((1530,710))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b1.place(x=1050,y=400,width=400,height=200)
        
        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1050,y=600,width=400,height=40)

   #function for open Photos button  
    def open_img(self):
        os.startfile("Data")
    
    #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_detection(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Detection","Are you sure want to Exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


if __name__=="__main__":
    main1()