from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(el_value.get()) * 1.6
    text1.insert(END, miles)

btn1 = Button(window, text="Execute", command=km_to_miles)
btn1.grid(row=0, column=0)

el_value=StringVar()
entry1 = Entry(window, textvariable=el_value)
entry1.grid(row=0, column=1)

text1 = Text(window, height=1, width=20)
text1.grid(row=0, column=2)

window.mainloop()