import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("V1rU2 F0uND", "Alert! A maliciuos software has been found on your device!")
button = tk.Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)
root.mainloop()