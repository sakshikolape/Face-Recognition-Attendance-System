from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk 
from student import  Student
import tkinter
import os
from train import Train
from Face_detection import face_detection
from attendance import Attendance

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
        img1=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f4.jfif")
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
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()