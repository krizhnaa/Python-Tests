from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=225, height=150)
window.config(padx=40, pady=40)

input = Entry()
input.grid(row=0, column=1)
input.config(width=10)

label1 = Label()
label1.config(text="Miles", font=("Arial", 12))
label1.grid(row=0, column=2)

label2 = Label()
label2.config(text="is equal to", font=("Arial", 12))
label2.grid(row=1, column=0)

label3 = Label()
label3.config(font=("Arial", 12))
label3.grid(row=1, column=1)

label4 = Label()
label4.config(text="Km", font=("Arial", 12))
label4.grid(row=1, column=2)

def button_clicked():
    miles = int(input.get())
    km = miles * 1.6
    label3["text"] = km
#
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)
#
# button = Button(text="Don't", command=button_clicked)
# button.grid(row=1, column=2)













window.mainloop()