import tkinter as tk  # Python 3
from tkinter import Canvas


root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.image = tk.PhotoImage(file='image/ant.png')
label = tk.Label(root, image=root.image, bg='white')
root.overrideredirect(True)
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
label.pack()
a = Canvas()
label.mainloop()
