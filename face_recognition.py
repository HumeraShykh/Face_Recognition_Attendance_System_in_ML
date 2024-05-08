import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import cv2
import numpy as np
import mysql.connector
import os
from datetime import datetime

class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = tk.Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="purple",
        )
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # "Back" button
        back_button = tk.Button(
            self.root,
            text="Back",
            command=self.root.destroy,  # Closes the current Toplevel window
            font=("times new roman", 15, "bold"),
            bg="purple",
            fg="white",
        )
        back_button.place(x=10, y=10, width=100, height=30)

        # Images for the GUI
        img_top = Image.open("college_images/facedetector.jpeg").resize((500, 545), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = tk.Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=55, width=500, height=545)

        img_bottom = Image.open("college_images/face5.JPG").resize((800, 545), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = tk.Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=500, y=55, width=800, height=545)

        # Button to start face recognition
        b1_1 = tk.Button(
            f_lbl2,
            text="FACE RECOGNITION",
            cursor="hand2",
            font=("times new roman", 13, "bold"),
            bg="purple",
            fg="white",
            command=self.face_recog,
        )
        b1_1.place(x=295, y=480, width=200, height=35)

    def face_recog(self):
        # Load the face cascade and recognizer
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        def recognize(img):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            faces = faceCascade.detectMultiScale(
                gray_image,
                scaleFactor=1.1,
                minNeighbors=10,  # Increase minNeighbors for more accurate detection
                minSize=(30, 30),
            )

            # Confidence threshold to reduce misidentifications
            confidence_threshold = 85

            for (x, y, w, h) in faces:
                roi_gray = gray_image[y : y + h, x : x + w]  # Region of interest for the face
                id, confidence = clf.predict(roi_gray)  # Predict the face ID and confidence
                confidence_percentage = int(100 * (1 - confidence / 300))

                if confidence_percentage >= confidence_threshold:
                    try:
                        # Connect to the MySQL database
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="root",
                            database="face_recognition",
                        )
                        my_cursor = conn.cursor()

                        # Fetch the name based on the ID
                        my_cursor.execute(f"SELECT ID, Name FROM student WHERE ID = {id}")
                        result = my_cursor.fetchone()

                        if result:
                            student_id = result[0]
                            student_name = result[1]

                            # Display the name and ID on the screen
                            cv2.putText(
                                img,
                                f"Name: {student_name}, ID: {student_id}",
                                (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (255, 255, 255),
                                2,
                            )

                            # Record attendance
                            my_cursor.execute(
                                "INSERT INTO attendance (student_id, student_name) VALUES (%s, %s)",
                                (student_id, student_name),
                            )
                            conn.commit()  # Commit the transaction

                        else:
                            cv2.putText(
                                img,
                                "Unknown",
                                (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 0, 255),
                                2,
                            )

                        conn.close()  # Close the connection
                    except mysql.connector.Error as err:
                        print(f"Database error: {err}")
                        cv2.putText(
                            img,
                            "Database Error",
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                                2,
                            )
                else:
                    cv2.putText(
                        img,
                        "Unknown",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2,
                    )

        # Start video capture
        video_cap = cv2.VideoCapture(0)  # Use the default webcam
        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            recognize(img)  # Recognize faces
            cv2.imshow("Face Recognition", img)  # Display the video stream

            # Exit when 'Esc' key is pressed
            if cv2.waitKey(1) & 0xFF == 27:
                break

        video_cap.release()  # Release the webcam
        cv2.destroyAllWindows()

# Main entry point for the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Face_recognition_System(root)
    root.mainloop()
