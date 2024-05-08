from tkinter  import* #GUI develop , easy to learn
from tkinter import ttk #Theme for GUI, stylish toolkit here
from PIL import ImageTk,Image   #Used for image handling in the app
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    #call construction
    def __init__(self,root):
        self.root=root                       #Root window of TKinter
        #set window geometry 
        self.root.geometry("1530x790+0+0")         #Width x Height + "+", "-"
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="pink",fg="purple")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        img_top=Image.open(r"Dev.png")
        img_top=img_top.resize((1320,200),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
       
        f_lbl=Label(self.root,image=self.photoimg_top)                
        f_lbl.place(x=0,y=55,width=1320,height=200)
        
        
        
        ##frame
        main_frame=Frame(self.root,bd=2,bg="black")
        main_frame.place(x=200,y=255,width=900,height=400)
        
        
        #Developer info
        dev_lbl=Label(main_frame,text="Three brilliant minds, Humera, Nancy, and Sudaish",font=("times new roman",20,"bold"),bg="pink")
        dev_lbl.place(x=140,y=5)
        dev_lbl=Label(main_frame,text="Collaborated to create this innovative face recognition attendance system",font=("times new roman",18,"bold"),bg="purple")
        dev_lbl.place(x=70,y=50)
        
        img_top1=Image.open(r"college_images\laptop.jpg")
        img_top1=img_top1.resize((900,370),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
       
        f_lbl=Label(main_frame,image=self.photoimg_top1)                
        f_lbl.place(x=0,y=87,width=900,height=370)
    # Add a "Back" button to return to the main page
        back_button = Button(
            self.root,
            text="Back",
            command=self.root.destroy,  # Closes this Toplevel window to return to the main page
            font=("times new roman", 15, "bold"),
            bg="purple",
            fg="white",
        )
        back_button.place(x=10, y=10, width=100, height=30)  # Position the back button at the top-left corner

        
    #call main (object)
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop() #close main loop