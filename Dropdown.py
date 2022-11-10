from tkinter import ttk
from tkinter import *
import tkinter as tk

def dropdown_opened():
    print("The drop-down has been opened!")


main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(
    values=["Python", "C", "C++", "Java"],
    postcommand=dropdown_opened
)

Tela_filtrar = PhotoImage(file="Tela_filtrar.png")
lab_tela1 = Label(main_window, image=Tela_filtrar)
lab_tela1.pack()
combo.place(x=50, y=50)
main_window.mainloop()