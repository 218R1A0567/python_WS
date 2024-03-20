from tkinter import *
from tkinter import ttk
import random as rn

gss = Tk()
gss.title("GUESS_THE_NUMBER")
gss.geometry("300x300")

var1 = rn.randint(1, 10)
var2 = StringVar()
n = 3

def guess():
    global n

    if var2.get().isdigit():
        guessed_number = int(var2.get())

        if guessed_number == var1:
            res1.config(text='***YOU GUESSED CORRECT***')
            gss.after(1300, gss.destroy)
        elif n == 0:
            res1.config(text='*GAME OVER*')
            gss.after(1500, gss.destroy)
        else:
            res.config(text='RETRY',)
            cnt.config(text=f"REMAINING ATTEMPTS: {n - 1}")
            n -= 1
            var2.set("")
            if guessed_number > var1:
                res1.config(text='Your guess is Greater than actual')
            else:
                res1.config(text='Your guess is Lesser than actual')
    else:
        res1.config(text='Enter a valid number')



l1 = ttk.Label(gss, text='GUESS THE NUMBER', width=110)
e1 = ttk.Entry(gss, textvariable=var2, width=8)
b1 = ttk.Button(gss, text='GUESS!', command=guess)
res = ttk.Label(gss, text='')
res1 = ttk.Label(gss, text='')
cnt = ttk.Label(gss, text=f"REMAINING ATTEMPTS: {n}")

l1.place(x=25, y=120)
e1.place(x=165, y=120)
res.place(x=95, y=90)
cnt.place(x=85, y=50)
b1.place(x=95, y=160)
res1.place(x=65, y=200)

gss.mainloop()
