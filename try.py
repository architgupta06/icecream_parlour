from tkinter import Tk, Entry, Button

def print_text():
    text = entry.get()
    print(text)

root = Tk()

entry = Entry(root)
entry.pack()

button = Button(root, text="Print", command=print_text)
button.pack()

root.mainloop()
