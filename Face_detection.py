from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class face_detection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1580x790+0+0")
        self.root.title("Face Detector")

        title_lbl=Label(self.root,text="Face Detection",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #left image
        img_left=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f23.webp")
        img_left=img_left.resize((760,720))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=47,width=760,height=720)
        
        #right image
        img_right=Image.open(r"C:\Users\saksh\Downloads\face_detection\college_images\f19.jpg")
        img_right=img_right.resize((770,720))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=760,y=47,width=770,height=720)

        #Button
        b1=Button(f_lbl,text="Detect Face",command=self.detect_face,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1.place(x=260,y=635,width=240,height=43)
        
    #Attendance
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #Face Detection
    def detect_face(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"

                my_cursor.execute("select Department from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = str(d[0]) if d else "Unknown"

                if confidence > 71:
                    cv2.putText(img,f"ID: {i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord = [x,y,w,h]

            return coord
        
        def detect(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=detect(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Detection",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=face_detection(root)
    root.mainloop()
