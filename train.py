from tkinter  import* #GUI develop , easy to learn
from tkinter import ttk #Theme for GUI, stylish toolkit here
from PIL import ImageTk,Image   #Used for image handling in the app
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

import pickle
from face_recognition import Face_recognition_System

#ttile
class Train:
    #call construction
    def __init__(self,root):
        self.root=root                       #Root window of TKinter
        #set window geometry 
        self.root.geometry("1530x790+0+0")         #Width x Height + "+", "-"
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="RED")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        img_top=Image.open(r"college_images\collage.png")
        img_top=img_top.resize((1320,200),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
       
        f_lbl=Label(self.root,image=self.photoimg_top)                
        f_lbl.place(x=0,y=55,width=1320,height=200)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="purple",fg="white")
        b1_1.place(x=0,y=239,width=1320,height=60)
        
        img_bottom=Image.open(r"college_images\imgg.jpg")
        img_bottom=img_bottom.resize((1320,330),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
       
        f_lbl=Label(self.root,image=self.photoimg_bottom)                
        f_lbl.place(x=0,y=300,width=1320,height=330)
        back_button = Button(
            self.root,
            text="Back",
            command=self.root.destroy,  # Closes this Toplevel window to return to the main page
            font=("times new roman", 15, "bold"),
            bg="purple",
            fg="white",
        )
        back_button.place(x=10, y=10, width=100, height=30)
  
  
    def train_classifier(self):     
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            #uint== datatype
            id=int(os.path.split(image)[1].split('.')[1])
            #C:\Users\user\Desktop\Face_Recognition_System_Ai_Semester_Project\data== 0 index
            #user.1.1.jpg== index 1
            #C:\Users\user\Desktop\Face_Recognition_System_Ai_Semester_Project\data\user.1.1.jpg
            
            
            #append faces
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #================Train the classifier and save===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        

        
        
        
        
#call main (object)
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop() #close main loop