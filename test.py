import tkinter as tk

window = tk.Tk()
window.title("GUI")
window.minsize(500, 300)

labell = tk.Label(text="Hey Tkinter", font=("Arial", 24))
labell.pack()



window.mainloop()