import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = Tk()

# config the root window
root.geometry("490x560+500+100")
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a month:")
label.pack(fill=X, padx=144, pady=100)

categoria = ['Basquete', 'Futebol', 'Treinador', 'Patrocínio', 'Paratletas', 'Natação']
# create a combobox
#selected_month = StringVar()
month_cb = ttk.Combobox(root, width=20)

# get first 3 letters of every month name
month_cb['values'] = [categoria[m] for m in range(0, 6)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=X, padx=200, pady=0)


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    '''showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )'''
    label = Label(root, text=f'You selected {selected_month.get()}!')
    label.place(width=206, height=17, x=155, y=392)

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()