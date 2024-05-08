from tkinter  import* #GUI develop , easy to learn
from tkinter import ttk #Theme for GUI, stylish toolkit here
from PIL import ImageTk,Image   #Used for image handling in the app
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    #call construction
    def __init__(self,root):
        self.root=root                       #Root window of TKinter
        #set window geometry 
        self.root.geometry("1530x790+0+0")         #Width x Height + "+", "-"
        self.root.title("Face Recognition System")
        
        #=========varaible======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        
        
        #first image
        img1=Image.open(r"college_images\studentpyimg.jpg")
        img1=img1.resize((450,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
       
        f_lbl=Label(self.root,image=self.photoimg1)                
        f_lbl.place(x=0,y=0,width=450,height=130)
         
          #second image
        img2=Image.open(r"college_images\studentpyimg3.jpg")
        img2=img2.resize((450,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
       
        f_lbl=Label(self.root,image=self.photoimg2)                
        f_lbl.place(x=400,y=0,width=450,height=130)
         
        
        #third image
        img3=Image.open(r"college_images\studentpyimg2.jpg")
        img3=img3.resize((450,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
       
        f_lbl=Label(self.root,image=self.photoimg3)                
        f_lbl.place(x=850,y=0,width=450,height=130)
        
        
        #bg image
        imgbg=Image.open(r"college_images\imgbg4.png")
        imgbg=imgbg.resize((1530,710),Image.LANCZOS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)
       
        bg_img=Label(self.root,image=self.photoimgbg)                
        bg_img.place(x=0,y=130,width=1330,height=530)
       
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        #bd=border
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=19,y=56,width=1230,height=460)
        back_button = Button(
            self.root,
            text="Back",
            command=self.root.destroy,  # Closes the current Toplevel window
            font=("times new roman", 15, "bold"),
            bg="purple",
            fg="white",
        )
        back_button.place(x=10, y=10, width=100, height=30)
        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Helvetica", 12,"bold"))
        left_frame.place(x=5,y=5,width=600,height=450)
        
        #third image
        img_left=Image.open(r"college_images\frame.jpg")
        img_left=img_left.resize((560,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
       
        f_lbl=Label(left_frame,image=self.photoimg_left)                
        f_lbl.place(x=0,y=0,width=595,height=110)
        
        #current course
        current_course=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Helvetica", 12,"bold"))
        current_course.place(x=12,y=100,width=570,height=95)
        
        #Department 
        
        dep_label=Label(current_course,text="Deparatment:",font=("times new roman", 11,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",11,"bold"), state="readonly",width=20)
        dep_combo["values"]=("Select Deparatment","Computer Science","BBA","EE","Robotics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        
        
        #Course
        course_label=Label(current_course,text="Course:",font=("times new roman", 11,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",9,"bold"), state="readonly",width=23)
        course_combo["values"]=("Select Course","Artifical Intelligence","Data Science","Machine Learning","Deep Learning")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=8,sticky=W)
        
        #Year
        year_label=Label(current_course,text="Year:",font=("times new roman", 11,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=0,sticky=W)
        
        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",11,"bold"), state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=1,pady=0,sticky=W)
        
        
        #Semesters
        semester_label=Label(current_course,text="Semester:",font=("times new roman", 11,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",9,"bold"), state="readonly",width=23,height=10)
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=8,sticky=W)
        
        #class student information
        class_student=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Helvetica", 12,"bold"))
        class_student.place(x=8,y=200 ,width=584,height=225)
        
        #Student ID
        sid_label=Label(class_student,text="Student ID:",font=("times new roman", 11,"bold"),bg="white")
        sid_label.grid(row=0,column=0,padx=8,sticky=W)
        
        #entry field
        studentID_entry=ttk.Entry(class_student,textvariable=self.var_id,width=18,font=("Times New Roman",11,"bold"))
        studentID_entry.grid(row=0,column=1,padx=0,sticky=W)
        
        #Student name
        studentname_label=Label(class_student,text="Student Name:",font=("times new roman", 11,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=2,sticky=W)
        
        studentname_entry=ttk.Entry(class_student,textvariable=self.var_name,width=18,font=("Times New Roman",11,"bold"))
        studentname_entry.grid(row=0,column=3,padx=5,sticky=W)
        
        #Gender
        gender_label=Label(class_student,text="Gender:",font=("times new roman", 11,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=2,sticky=W)
        
        # gender_entry=ttk.Entry(class_student,textvariable=self.var_gender,width=18,font=("Times New Roman",11,"bold"))
        # gender_entry.grid(row=1,column=1,padx=0,sticky=W)
        gender_combo=ttk.Combobox(class_student,textvariable=self.var_gender,font=("times new roman",9,"bold"), state="readonly",width=21)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=1,pady=0,sticky=W)
        
        
        
        #Roll No
        rollno_label=Label(class_student,text="DOB:",font=("times new roman", 11,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=2,sticky=W)
        
        rollno_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=18,font=("Times New Roman",11,"bold"))
        rollno_entry.grid(row=1,column=3,padx=5,pady=0,sticky=W)
        
        
         #Email 
        email_label=Label(class_student,text="Email:",font=("times new roman", 11,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=8,sticky=W)
        
        email_entry=ttk.Entry(class_student,textvariable=self.var_email,width=18,font=("Times New Roman",11,"bold"))
        email_entry.grid(row=2,column=1,padx=0,pady=1,sticky=W)
        
        #Phone No
        phoneno_label=Label(class_student,text="Phone No:",font=("times new roman", 11,"bold"),bg="white")
        phoneno_label.grid(row=2,column=2,padx=2,sticky=W)
        
        phoneno_entry=ttk.Entry(class_student,textvariable=self.var_phoneno,width=18,font=("Times New Roman",11,"bold"))
        phoneno_entry.grid(row=2,column=3,padx=5,pady=1,sticky=W)
        
        #Address
        address_label=Label(class_student,text="Address:",font=("times new roman", 11,"bold"),bg="white")
        address_label.grid(row=3,column=0,padx=8,pady=0,sticky=W)
        
        address_entry=ttk.Entry(class_student,textvariable=self.var_address,width=18,font=("Times New Roman",11,"bold"))
        address_entry.grid(row=3,column=1,padx=0,pady=2,sticky=W)
        
        # #Teacher Name
        teachername_label=Label(class_student,text="Teacher Name:",font=("times new roman", 11,"bold"),bg="white")
        teachername_label.grid(row=3,column=2,padx=2,sticky=W)
        
        teachername_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=18,font=("Times New Roman",11,"bold"))
        teachername_entry.grid(row=3,column=3,padx=5,pady=1,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0,padx=10)
        
        radiobtn1=ttk.Radiobutton(class_student,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=4,column=1,padx=10)
        
        
        
        #make button frame
        btn_frame=Frame(class_student,bd=2, relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=125,width=560,height=38)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="purple",fg="white")  
        save_btn.grid(row=0,column=0)     
        
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=13,font=("times new roman",13,"bold"),bg="indigo",fg="white")  
        update_btn.grid(row=0,column=1)    
        
        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=13,font=("times new roman",13,"bold"),bg="indigo",fg="white")  
        delete_btn.grid(row=0,column=2)   
        
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=13,font=("times new roman",13,"bold"),bg="purple",fg="white")  
        reset_btn.grid(row=0,column=3)  
        
         #make button frame for photo
        btn_frame2=Frame(class_student,bd=2, relief=RIDGE,bg="white")
        btn_frame2.place(x=10,y=158,width=560,height=38)
        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo Sample",width=28,font=("times new roman",13,"bold"),bg="teal",fg="white")  
        take_photo_btn.grid(row=0,column=0) 
        
        update_photo_btn=Button(btn_frame2,text="Update Photo Sample",width=27,font=("times new roman",13,"bold"),bg="dark cyan",fg="white")  
        update_photo_btn.grid(row=0,column=1)        
        
          
        
        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Helvetica", 12,"bold"))
        right_frame.place(x=620,y=5,width=600,height=450)
        
        img_right=Image.open(r"college_images\studentimg.jpg")
        img_right=img_right.resize((560,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
       
        f_lbl=Label(right_frame,image=self.photoimg_right)                
        f_lbl.place(x=0,y=0,width=595,height=110)
        
        #===============Search System=======================
        
        search_system=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Helvetica", 12,"bold"))
        search_system.place(x=8,y=95 ,width=584,height=60)
        
        search_label=Label(search_system,text="Search By:",font=("times new roman", 12,"bold"),bg="purple",fg="white")
        search_label.grid(row=0,column=0,padx=2,sticky=W)
        
        search_combo=ttk.Combobox(search_system,font=("times new roman",9,"bold"), state="readonly",width=20)
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        
        search_entry=ttk.Entry(search_system,width=18,font=("Times New Roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=0,sticky=W)
        
        search_btn=Button(search_system,text="Search",width=10,font=("times new roman",11,"bold"),bg="dark cyan",fg="white")  
        search_btn.grid(row=0,column=3,padx=1)   
        
        showall_btn=Button(search_system,text="Show All",width=9,font=("times new roman",11,"bold"),bg="teal",fg="white")  
        showall_btn.grid(row=0,column=4) 
        
        showall_btn=Button(search_system,text="Show All",width=9,font=("times new roman",11,"bold"),bg="teal",fg="white")  
        showall_btn.grid(row=0,column=4,padx=2) 
        #====================Table Frame===================
        table_frame=Frame(right_frame,bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=6,y=160,width=587,height=260)
        
        #scroll bar
        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Dept","Course","Year","Semester","ID","Name","Gender","DOB","Email","PhoneNo","Address","Teacher","PhotoSample"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("PhotoSample",text="Photo Sample Status")
        self.student_table["show"]="headings"
        
        #set column width
        self.student_table.column("Dept",width=80)
        self.student_table.column("Course",width=80)
        self.student_table.column("Year",width=80)
        self.student_table.column("Semester",width=80)
        self.student_table.column("ID",width=80)
        self.student_table.column("Name",width=80)
        self.student_table.column("Gender",width=80)
        
        self.student_table.column("DOB",width=80)
        self.student_table.column("Email",width=80)
        self.student_table.column("PhoneNo",width=80)
        self.student_table.column("Address",width=80)
        self.student_table.column("Teacher",width=80)
        self.student_table.column("PhotoSample",width=80)
      
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
      #=================Function declartion==============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get( )=="":
          messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
              #connect database
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phoneno.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()      
                                                                                            
                                                                                                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Sucessfully",parent=self.root)
            except Exception as es:
              messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
     #==============Fetch data==========
    def fetch_data(self):  
      conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()
      
      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        conn.commit()
      conn.close()
    #=============get cursor========
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]
      
      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),
      self.var_id.set(data[4]),
      self.var_name.set(data[5]),
      self.var_gender.set(data[6]),
      self.var_dob.set(data[7]),
      self.var_email.set(data[8]),
      self.var_phoneno.set(data[9]),
      self.var_address.set(data[10]),
      self.var_teacher.set(data[11]),
      self.var_radio1.set(data[12])
    #update FUNCTION
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get( )=="":
          messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      
      else:
          try:
            update=messagebox.askyesno("update","Do You want to update this student details",parent=self.root)
            if update>0:
              conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
              my_cursor=conn.cursor()
              my_cursor.execute("Update student set Dep=%s,Course=%s, Year=%s,Semester=%s,Name=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,PhotoSample=%s where ID=%s",(
                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                          self.var_name.get(),
                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                          self.var_phoneno.get(),
                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                          self.var_id.get()      
                                                                                            
                                                                                                                                                                                          ))
            else:
                if not update:
                  return
            messagebox.showinfo("Success","Student Details Successfully update Completed",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
          except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     
    # delete function      
    def delete_data(self):
      if self.var_id.get()=="":
        messagebox.showerror("Error","Student ID must be required!",parent=self.root)
      else:
           try:
              delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
              if delete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                sql="delete from student where ID=%s"
                val=(self.var_id.get(),)
                my_cursor.execute(sql,val)
              else:
                if not delete:
                  return
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
           except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #reset function
    def reset_data(self):
      self.var_dep.set("Select Department") 
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester") 
      self.var_id.set("")
      self.var_name.set("")
      self.var_gender.set("Male") 
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phoneno.set("") 
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")
    #==================    Generate data set or take photo samples==========================
    def generate_dataset(self):
      if self.var_id.get()=="":
        messagebox.showerror("Error","Student ID must be required!",parent=self.root)
      else:
           try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                sid=0
                for x in myresult:
                  sid+=1
                my_cursor.execute("Update student set Dep=%s,Course=%s, Year=%s,Semester=%s,Name=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,PhotoSample=%s where ID=%s",(
                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                          self.var_name.get(),
                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                          self.var_phoneno.get(),
                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                          self.var_id.get()==sid+1    
                                                                                            
                                                                                                                                                                                          ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #===============load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                  faces=face_classifier.detectMultiScale(gray,1.3,5)
                  #scaling factor=1.3
                  #minimum neighbour=5
                  for (x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                  ret,myframe=cap.read()
                  if face_cropped(myframe) is not None:
                    img_id+=1
                    face=cv2.resize(face_cropped(myframe),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(sid)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255,0),2)
                    cv2.imshow("Cropped Face",face)
                  if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!")
           except Exception as es:
             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  
                  
      
                
                  
                  
             
             
             
      
               
           
          
      


   
   
   
   
        
        
#call main (object)
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() #close main loop