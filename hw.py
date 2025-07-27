import tkinter as tk
root = tk.Tk()
root.title("Length App")
root.geometry('400x400')
frame = tk.Frame(master=root, height=200, width=360, bg="#d0efff")
lbl1 = tk.Label(frame, text = "Enter length in inches", bg ="#3895D3", fg = 'white', width=24)
length_entry = tk.Entry(frame)
def display():
    length = float(length_entry.get())
    output_caculate = length * 2.54
    message =   "length in centimeter:"
    textbox.insert(tk.END, message)
    textbox.insert(tk.END, output_caculate)
textbox = tk.Text(bg="#BEBEBE", fg="black")
button = tk.Button(text = "Convert", command=display, bg = "red")
frame.place(x=20)
lbl1.place(x=20, y=20)
length_entry.place(x=195, y=20)
button.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()