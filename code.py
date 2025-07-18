import tkinter as tk
from tkinter import messagebox

# Mock course data
courses = [
    {"id": 1, "title": "Python Programming", "instructor": "John Doe", "price": "$49.99"},
    {"id": 2, "title": "Web Development", "instructor": "Jane Smith", "price": "$59.99"},
    {"id": 3, "title": "Machine Learning", "instructor": "Alice Johnson", "price": "$79.99"},
]

# Function to display course details when selected
def show_course_details():
    selected_item = course_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        course = courses[index]
        messagebox.showinfo("Course Details", f"Title: {course['title']}\nInstructor: {course['instructor']}\nPrice: {course['price']}")

# Function to enroll in a course
def enroll_in_course():
    selected_item = course_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        course = courses[index]
        messagebox.showinfo("Enrollment", f"You have enrolled in the course: {course['title']}")

# Create the main window
root = tk.Tk()
root.title("Online Course Platform")

# Create and populate the course listbox
course_listbox = tk.Listbox(root)
for course in courses:
    course_listbox.insert(tk.END, course["title"])

# Create "Course List" label
course_label = tk.Label(root, text="Course List")
course_label.pack()

# Create a scrollbar for the course listbox
course_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
course_scrollbar.config(command=course_listbox.yview)
course_listbox.config(yscrollcommand=course_scrollbar.set)

# Create "Show Details" and "Enroll" buttons
show_details_button = tk.Button(root, text="Show Details", command=show_course_details)
enroll_button = tk.Button(root, text="Enroll", command=enroll_in_course)

# Pack the widgets
course_listbox.pack(fill=tk.BOTH, expand=True)
course_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
show_details_button.pack()
enroll_button.pack()

root.mainloop()
