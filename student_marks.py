from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()  # main window

root.title('Example')  # window title
root.geometry('500x500')  # window size

get_Name = StringVar()
get_Class = StringVar()
marks_ = IntVar()

# Colours.
col1 = '#020f12'
col2 = '#05d7ff'
col3 = '#65e7ff'
col4 = 'BLACK'

# Submit button function
def Submit():
    # These are inputs provided by the user in the text field and scale.
    name = get_Name.get()  # Name of the Student.
    class_ = get_Class.get()  # Class of the Student.
    marks = marks_.get()  # Marks obtained by the Student.

    formatted_output = f"{name} , {class_} , {marks}\n"

    with open("output.txt", "a") as file:
        file.write(formatted_output)

    get_Name.set("")
    get_Class.set("")
    marks_.set(0)

# Labels
namel = ttk.Label(root, text='Name')
class1 = ttk.Label(root, text='Class')
Marks = ttk.Label(root, text='Marks')

# Text Fields, Buttons, Scale.
nameE = ttk.Entry(root, textvariable=get_Name, font=('calibre', 10, 'normal'))
classE = ttk.Entry(root, textvariable=get_Class, font=('calibre', 10, 'normal'))
MarksE = ttk.Scale(root, orient=HORIZONTAL, from_=1, to=100, variable=marks_)

# Load the image
image = Image.open(r"C:\Users\akshi\OneDrive\Desktop\python_WS\s1.jpg")
# Resize the image with LANCZOS resampling
image = image.resize((image.width // 8, image.height // 8), Image.LANCZOS)
# Create PhotoImage
photo = ImageTk.PhotoImage(image)

Sub = ttk.Button(root, image=photo, command=Submit)

# Placing all the components that are created in the main window.
# We used place() function for organizing things in the main window.
namel.place(x=10, y=0)
class1.place(x=10, y=50)
nameE.place(x=90, y=10)
classE.place(x=90, y=60)
Marks.place(x=10, y=100)
MarksE.place(x=90, y=90)
Sub.place(x=110, y=150)

# Create a style for the button
style = ttk.Style()
style.configure("Custom.TButton", padding=10, font=("Arial", 16, "bold"), background=col2, foreground=col4,
                activebackground=col3, activeforeground=col4, highlightthickness=2, highlightbackground=col2,
                highlightcolor='WHITE', width=7, height=2, border=0, cursor='hand1')

root.mainloop()
