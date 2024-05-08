from tkinter  import* #GUI develop , easy to learn
from tkinter import ttk #Theme for GUI, stylish toolkit here
from PIL import ImageTk,Image   #Used for image handling in the app
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    #call construction
    def __init__(self,root):
        self.root=root                       #Root window of TKinter
        #set window geometry 
        self.root.geometry("1530x790+0+0")         #Width x Height + "+", "-"
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="pink",fg="purple")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        back_button = Button(
            self.root,
            text="Back",
            command=self.root.destroy,  # Closes the current window to return to the main page
            font=("times new roman", 15, "bold"),
            bg="purple",
            fg="white",
        )
        back_button.place(x=10, y=10, width=100, height=30)  # Position the "Back" button

        
        img_top=Image.open(r"college_images\help.jpg")
        img_top=img_top.resize((1320,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)                
        f_lbl.place(x=0,y=55,width=1320,height=700)
        
        dev_lbl=Label(f_lbl,text="Email: humeraashykh@gmail.com",font=("times new roman",20,"bold"),bg="pink")
        dev_lbl.place(x=410,y=280)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() #close main loop