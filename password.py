from tkinter import*
import string
import random

cal=Tk()
cal.geometry("480x300")
cal.title("password Generator App")

def gen():
    num=int(e1.get())
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    Password = s[0:num]

    Label(cal,text = "Password :",font = "time 15 bold").place(x=30,y=250)

    Label(cal, text = Password, font = "time 15 bold",width=24,bg="white").place(x=150,y=250)

Label(cal, text="Password Generator APP", font = "time 15 bold").place(x=30,y=30)

Label(cal, text="Enter Password Length", font = "time 15 bold").place(x=30,y=90)

e1 = Entry(cal,width = 46,bd = 2,font = "time 13 bold")
e1.place(x=30,y=133)

Button(cal,text="Generator Password",fg="white",bg="steelblue",font="time 15 bold",width=34,command=gen).place(x=30,y=180)

cal.mainloop()
