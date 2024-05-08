
from tkinter  import* #GUI develop , easy to learn
from tkinter import ttk
import tkinter.messagebox #Theme for GUI, stylish toolkit here
from PIL import ImageTk,Image   #Used for image handling in the app
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_recognition_System
from developer import Developer
from attendance import attendance
from help import Help
from datetime import datetime
from time import strftime
import pickle
class Face_Recognition_System:
    #call construction
    def __init__(self,root):
        self.root=root                       #Root window of TKinter
        #set window geometry 
        self.root.geometry("1530x790+0+0")         #Width x Height + "+", "-"
        self.root.title("Face Recognition System")
        
        #put images   r is used for not to convert backslash to forward slash
        img=Image.open(r"college_images\img1.jpg")
        #set size     ANTILIAS= convert high level image into low level image
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        #set image on window so make label
        f_lbl=Label(self.root,image=self.photoimg)                #create a Label widget
        #to show on window 
        f_lbl.place(x=0,y=0,width=500,height=130)


        #first image
        img1=Image.open(r"college_images\img1.jpg")
        img1=img1.resize((450,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
       
        f_lbl=Label(self.root,image=self.photoimg1)                
        f_lbl.place(x=0,y=0,width=450,height=130)
         
         #second image
        img2=Image.open(r"college_images\img2.jpg")
        img2=img2.resize((150,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
       
        f_lbl=Label(self.root,image=self.photoimg2)                
        f_lbl.place(x=451,y=0,width=150,height=130)
        
        #third image
        img3=Image.open(r"college_images\img3.png")
        img3=img3.resize((150,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
       
        f_lbl=Label(self.root,image=self.photoimg3)                
        f_lbl.place(x=600,y=0,width=150,height=130)
       
        #forth image
        img4=Image.open(r"college_images\img4.jpg")
        img4=img4.resize((150,130),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
       
        f_lbl=Label(self.root,image=self.photoimg4)                
        f_lbl.place(x=750,y=0,width=150,height=130)
        
        #fifth image
        img5=Image.open(r"college_images\img5.jpg")
        img5=img5.resize((450,130),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
       
        f_lbl=Label(self.root,image=self.photoimg5)                
        f_lbl.place(x=900,y=0,width=450,height=130)
        
        #bg image
        imgbg=Image.open(r"college_images\imgbg4.png")
        imgbg=imgbg.resize((1530,710),Image.LANCZOS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)
       
        bg_img=Label(self.root,image=self.photoimgbg)                
        bg_img.place(x=0,y=130,width=1330,height=530)
        
        
        #label title    fg=foreground 
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        #====================TIME=============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl, font = ('times new roman', 14, "bold"),background='white',foreground='purple')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
         
        #create image student button
        img6=Image.open(r"college_images\studentimg.jpg")
        img6=img6.resize((180,180),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=80,width=181,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=150,y=230,width=181,height=30)
        
        
        #create image Detect Face button
        img7=Image.open(r"college_images\facedetector.jpeg")
        img7=img7.resize((180,180),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.face_data)
        b1.place(x=420,y=80,width=181,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=420,y=230,width=181,height=30)
        
        
        
        #create Attendance  Face button
        img8=Image.open(r"college_images\attendance.jpg")
        img8=img8.resize((180,180),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.attendance_data)
        b1.place(x=680,y=80,width=181,height=150)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=680,y=230,width=181,height=30)
        
        #create Help button
        img9=Image.open(r"college_images\HelpDesk.png")
        img9=img9.resize((180,180),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.help_data)
        b1.place(x=940,y=80,width=181,height=150)
        
        b1_1=Button(bg_img,text="Help Base",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=940,y=230,width=181,height=30)
        
        
        #Train face button
        img10=Image.open(r"college_images\trainimg.jpg")
        img10=img10.resize((180,180),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=280,width=181,height=170)
          
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=150,y=420,width=181,height=30)
        
        #Photos face button
        img11=Image.open(r"college_images\photos.jpg")
        img11=img11.resize((180,181),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_img)
        b1.place(x=420,y=280,width=180,height=170)
          
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=420,y=420,width=181,height=30)
        
        #Developer face button
        img12=Image.open(r"college_images\developer.jpg")
        img12=img12.resize((180,181),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.developer_data)
        b1.place(x=680,y=280,width=180,height=170)
          
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=680,y=420,width=181,height=30)
        
        
        #Exit  button
        img13=Image.open(r"college_images\Exit.png")
        img13=img13.resize((180,181),Image.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        
        b1=Button(bg_img,image=self.photoimg13,cursor="hand2",command=self.iExit)
        b1.place(x=940,y=280,width=180,height=170)
          
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=940,y=420,width=181,height=30)
    
    def open_img(self):
        os.startfile("data")
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit this project?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return 
        #=================Function Button================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition_System(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
        
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        

#call main (object)
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop() #close main loop

