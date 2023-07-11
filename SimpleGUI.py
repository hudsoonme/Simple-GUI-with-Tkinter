import tkinter as tk

def button_clicked():
    label.config(text="Button clicked!")

window = tk.Tk()
button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack()
label = tk.Label(window, text="Hello, World!")
label.pack()
window.mainloop()