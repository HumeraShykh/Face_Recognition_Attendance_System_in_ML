import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
import pandas as pd
from datetime import datetime
import os

# Attendance GUI class
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Attendance System")

        # Background color
        self.root.configure(bg="light pink")

        # Frame for GUI components
        frame = tk.LabelFrame(
            self.root,
            text="Attendance Data",
            font=("Arial", 15, "bold"),
            bg="light pink",
        )
        frame.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        # Treeview for displaying attendance data
        self.attendance_tree = ttk.Treeview(
            frame,
            columns=("ID", "Name", "Last Attendance"),
            show="headings",
        )

        self.attendance_tree.heading("ID", text="ID")
        self.attendance_tree.heading("Name", text="Name")
        self.attendance_tree.heading("Last Attendance", text="Last Attendance")

        self.attendance_tree.column("ID", width=80, anchor=tk.CENTER)
        self.attendance_tree.column("Name", width=200, anchor=tk.W)
        self.attendance_tree.column("Last Attendance", width=200, anchor=tk.CENTER)

        self.attendance_tree.pack(fill=tk.BOTH, expand=True)

        # Frame for buttons
        button_frame = tk.Frame(self.root, bg="light pink")
        button_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

        # Buttons
        refresh_button = tk.Button(
            button_frame,
            text="Refresh",
            command=self.load_attendance_data,
            font=("Arial", 12, "bold"),
            bg="light pink",
        )
        refresh_button.pack(side=tk.LEFT, padx=20, expand=True, fill=tk.X)

        export_button = tk.Button(
            button_frame,
            text="Export to CSV",
            font=("Arial", 12, "bold"),
            command=self.export_to_csv,
            bg="light pink",
        )
        export_button.pack(side=tk.LEFT, padx=20, expand=True, fill=tk.X)

        back_button = tk.Button(
            button_frame,
            text="Back",
            command=self.root.destroy,
            font=("Arial", 12, "bold"),
            bg="light pink",
        )
        back_button.pack(side=tk.RIGHT, padx=20, expand=True, fill=tk.X)

        exit_button = tk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            font=("Arial", 12, "bold"),
            bg="light pink",
        )
        exit_button.pack(side=tk.RIGHT, padx=20, expand=True, fill=tk.X)

        # Load the existing attendance data
        self.load_attendance_data()

    def load_attendance_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="face_recognition",
            )
            my_cursor = conn.cursor()

            # Fetch unique attendance records, ordered by attendance time
            my_cursor.execute(
                """
                SELECT student_id, student_name, MAX(attendance_time)
                FROM attendance
                GROUP BY student_id, student_name
                ORDER BY MAX(attendance_time) DESC
                """
            )
            records = my_cursor.fetchall()

            # Clear existing data
            self.attendance_tree.delete(*self.attendance_tree.get_children())

            # Append unique records to the Treeview
            for record in records:
                if all(record):  # Check if all values in the record are non-empty
                    self.attendance_tree.insert("", tk.END, values=(record[0], record[1], record[2]))

            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to the database: {err}")

    def export_to_csv(self):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save CSV",
        )

        if save_path:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()

                # Fetch unique attendance records for export
                my_cursor.execute(
                    """
                    SELECT student_id, student_name, MAX(attendance_time)
                    FROM attendance
                    GROUP BY student_id, student_name
                    ORDER BY MAX(attendance_time) DESC
                    """
                )
                records = my_cursor.fetchall()

                # Filter out invalid or empty records
                valid_records = [record for record in records if all(record)]


                # Convert to DataFrame and save to CSV
                df = pd.DataFrame(valid_records, columns=["ID", "Name", "Last Attendance"])
                df.to_csv(save_path, index=False)

                conn.close()

                messagebox.showinfo("Export Successful", "Attendance data exported successfully.")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error exporting to CSV: {err}")

# Main entry point for the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Attendance(root)
    root.mainloop()
