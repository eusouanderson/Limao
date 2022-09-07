from tkinter import *


def window():
    global screen , window
    window = Tk()
    window.colormapwindows()
    window.geometry('490x500+400+100')
    window.resizable(True, True)
    window.title('BlackDev')
    screen = Label(window, text='', bd=5, borderwidth=10, font=50, takefocus=True, )
    screen.grid(row=6, column=1)
    # window.wm_resizable(width=False, height=False)
    wi = 15
    Button(window, foreground='red', width=wi, borderwidth=10)
    bt1 = Button(window, foreground='red', text='Cadastrar Produto', image='', width=wi, borderwidth=5, command=bot1)
    bt2 = Button(window, foreground='red', text='Apagar Produto', image='', width=wi, borderwidth=5, command=bot2)
    bt3 = Button(window, foreground='red', text='Editar Produto', image='', width=wi, borderwidth=5, command=bot3)
    bt4 = Button(window, foreground='red', text='Calcular', image='', width=wi, borderwidth=5, command=bot4)
    bt5 = Button(window, foreground='red', text='Valores', image='', width=wi, borderwidth=5, command=bot5)
    bt6 = Button(window, foreground='red', text='Ferramentas', image='', width=wi, borderwidth=5, command=bot6)
    bt1.grid(row=0, column=0)
    bt2.grid(row=1, column=0)
    bt3.grid(row=2, column=0)
    bt4.grid(row=3, column=0)
    bt5.grid(row=4, column=0)
    bt6.grid(row=5, column=0)
    window.mainloop()


def bot1():
    cProdu = Tk()
    cProdu.colormapwindows()
    cProdu.geometry('400x150+450+250')
    cProdu.title('Cadastrando Produto')
    screen['text'] = 'Cadastrando Produto... '
    cProdu_button = Button(cProdu, text="Cadastrar", command='')
    cProdu_button.pack(fill='x', expand=False, pady=5)
    cProdu_button.focus()
    cProdu_entry = Entry(cProdu, bd=5)
    cProdu_entry.pack(fill='x', expand=True)
    cProdu_entry.focus()

    return window()
def bot2():
    screen['text'] = 'Apagando Produto...'


def bot3():
    screen['text'] = 'Editando Produto...'


def bot4():
    screen['text'] = 'Calculando Produto...'

def bot5():
    screen['text'] = 'Valores Produto...'


def bot6():
    screen['text'] = 'Ferramentas...'

window()