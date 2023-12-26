import tkinter

window = tkinter.Tk()
window.title("Gui Window")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Bro WTF", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "Lol I changed it"
my_label.config(text="Lololol")
















window.mainloop()