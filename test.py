from tkinter import *

window = Tk()
window.title("Gui Window")
window.minsize(width=500, height=300)

my_label = Label(text="Text thanee", font=("Ariel", 24, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    display_this = input.get()
    my_label["text"] = display_this


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button = Button(text="Don't", command=button_clicked)
button.grid(row=0, column=2)

input = Entry()
input.grid(row=2, column=3)












window.mainloop()