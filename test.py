from tkinter import *

window = Tk()
window.title("Gui Window")
window.minsize(width=500, height=300)

my_label = Label(text="Bro WTF", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "Lol I changed it"
my_label.config(text="Lololol")


def button_clicked():
    my_label["text"] = "CLickeddd"

button = Button(text="Click Me", command=button_clicked)
button.pack()













window.mainloop()