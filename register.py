from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

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
        b1=Button(frame,image=self.photoimage_1,borderwidth=0,cursor="hand2")
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
               
           








if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()