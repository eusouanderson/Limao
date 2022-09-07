from tkinter import *

def window():
    window = Tk()
    window.colormapwindows()
    window.geometry('490x500+400+100')
    window.resizable(True, True)
    window.title('BlackDev')
    #window.wm_resizable(width=False, height=False)
    wi = 15
    Button(window, foreground='red', width=wi, borderwidth=10)
    bt1 = Button(window, foreground='red', image='', width=wi, borderwidth=5, command='')
    bt2 = Button(window, foreground='red', image='', width=wi, borderwidth=5, command='')
    bt3 = Button(window, foreground='red', image='', width=wi, borderwidth=5, command='')
    bt4 = Button(window, foreground='red', image='', width=wi, borderwidth=5, command='')
    bt5 = Button(window, foreground='red', image='', width=wi, borderwidth=5, command='')
    bt6 = Button(window, foreground='red', image='', width=wi, borderwidth=5, command='')
    bt1.grid(row=0, column=0)
    bt2.grid(row=1, column=0)
    bt3.grid(row=2, column=0)
    bt4.grid(row=3, column=0)
    bt5.grid(row=4, column=0)
    bt6.grid(row=5, column=0)
    window.mainloop()


