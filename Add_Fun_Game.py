from tkinter import *
from tkinter import ttk
import random as rn

gm = Tk()

gm.title('Add_Fun')
gm.geometry("500x500")

var1 = rn.randint(1, 500)
var2 = StringVar()
res = rn.randint(500, 1000)

def submit():
    user_answer = int(var2.get()) if var2.get().isdigit() else 0
    
    if var1 + user_answer == res:
        result_label.config(text="CORRECT")
        gm.after(1500, gm.destroy)  # Close the window after 1500 milliseconds
    else:
        result_label.config(text="TRY AGAIN")
        var2.set("")

l1 = ttk.Label(gm, text=var1)
l2 = ttk.Label(gm, text='+')
l3 = ttk.Label(gm, text='=')
rsl = ttk.Label(gm, text=res)

e1 = ttk.Entry(gm, textvariable=var2, width=5)
b1 = ttk.Button(gm, text='Submit', command=submit)

result_label = ttk.Label(gm, text="", font=("Helvetica", 16))  # Label to display result message

l1.place(x=50, y=50)
l2.place(x=100, y=50)
e1.place(x=150, y=50)
l3.place(x=210, y=50)
rsl.place(x=230, y=50)
b1.place(x=100, y=100)
result_label.place(x=100, y=150)  # Place the result label

gm.mainloop()
