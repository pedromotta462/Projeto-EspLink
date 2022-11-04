import tkinter as tk
# Import the package if saved in a different .py file else paste 
# the ScrollableImage class right after your imports.
from scrollimage import ScrollableImage   

root = tk.Tk()
root.title("Tela de login")
root.geometry("490x560+500+100")
root.iconbitmap(default="ico.ico")
root.resizable(width=1, height=1)
# PhotoImage from tkinter only supports:- PGM, PPM, GIF, PNG format.
# To use more formats use PIL ImageTk.PhotoImage
img = tk.PhotoImage(file="teste.png")

image_window = ScrollableImage(root, image=img, scrollbarwidth=15, 
                               width=490, height=560)
image_window.pack()

root.mainloop()