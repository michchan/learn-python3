from tkinter import *

window = Tk()

def kg_to_others():
    kg = float(input_value.get())
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    text_grams.insert(END, grams)
    text_pounds.insert(END, pounds)
    text_ounces.insert(END, ounces)
    
input_value = StringVar()
input_label = Label(window, text="Kg")
entry = Entry(window, textvariable=input_value)
convert_button = Button(window, text="Convert", command=kg_to_others)
text_grams = Text(window, height=1, width=20)
text_pounds = Text(window, height=1, width=20)
text_ounces = Text(window, height=1, width=20)

input_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
convert_button.grid(row=0, column=2)
text_grams.grid(row=1, column=0)
text_pounds.grid(row=1, column=1)
text_ounces.grid(row=1, column=2)

window.mainloop()