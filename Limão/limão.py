from datetime import date
from tkinter import *
from tkinter.messagebox import showerror, showinfo


def clicked_bt1():
    print(name, conect1, conect)


conect = []
conect1 = []
name = []


def loginCadastro():
    def cadastrar():
        global conect, conect1, nome
        logine = email_entry1.get()
        loginp = password_entry1.get()
        loginr = password_entry2.get()

        nome = nome_entry.get()
        name.append(nome)
        print(name)
        conect.append(logine)
        conect1.append(loginp)
        print(list(conect), list(conect1))

        if loginp == loginr:

            with open('cadastro.txt', 'w') as f:
                f.write('Login: {} Senha: {}\n'.format(conect, conect1))
            showinfo(title='Informação', message='Cadastrado com sucesso!')
            master1.destroy()
        else:
            showerror(title='Informação', message='Senha não confere !')
            master1.destroy()
            return loginCadastro()

    master1 = Tk()
    icon = PhotoImage(master=master1, file='icon.png')
    master1.wm_iconphoto(True, icon)
    master1.config(bg='#5d8aa8')
    master1.title('Cadastro')
    master1.geometry('290x500+510+100')  # largura x altura dist esq + dist top
    master1.wm_resizable(width=False, height=False)
    login1 = Frame(master1)
    login1.config(bg='#5d8aa8')
    login1.pack(padx=30, pady=30, fill='x', expand=True)
    # Nome
    nome_entry = Label(login1, text='Nome :', bg='#5d8aa8')
    nome_entry.pack(fill='x', expand=True)

    nome_entry = Entry(login1, bd=5)
    nome_entry.pack(fill='x', expand=True)
    nome_entry.focus()

    email_label1 = Label(login1, text='Endereço de Email :', bg='#5d8aa8')
    email_label1.pack(fill='x', expand=True)

    email_entry1 = Entry(login1, bd=5)
    email_entry1.pack(fill='x', expand=True)
    email_entry1.focus()

    # Password
    password_label1 = Label(login1, text='Senha :', bg='#5d8aa8')
    password_label1.pack(fill='x', expand=True)

    password_entry1 = Entry(login1, bd=5, show='*')
    password_entry1.pack(fill='x', expand=True)

    # Password Repeat
    password_label2 = Label(login1, text='Redefinir Senha:', bg='#5d8aa8')
    password_label2.pack(fill='x', expand=True)

    password_entry2 = Entry(login1, bd=5, show='*')
    password_entry2.pack(fill='x', expand=True)

    # Botão Cadastrar
    login_button1 = Button(
        login1,
        text='Cadastrar',
        bd=5,
        width=15,
        borderwidth=5,
        activeforeground='red',
        padx=10,
        pady=5,
        command=cadastrar,
    )
    login_button1.pack(fill='x', expand=False, pady=10)


# Login
vr = Tk()
icon = PhotoImage(master=vr, file='icon.png')
vr.wm_iconphoto(True, icon)
vr.title('Login')
vr.config(bg='#5d8aa8')
vr.geometry('490x500+400+100')  # largura x altura dist esq + dist top
vr.wm_resizable(width=False, height=False)

# Adicionando Imagens
layout = PhotoImage(file='')

# Layout
labelLayout = Label(vr, image=layout)
labelLayout.place(x=0, y=0)

# Conf de Botoes
bt1 = Button(
    vr,
    bd=5,
    text='Abrir',
    command=clicked_bt1,
    width=5,
    borderwidth=5,
    activeforeground='red',
    padx=5,
)
bt1.place(width=70, height=30, x=37, y=34)
bt2 = Button(
    vr,
    text='Cadastrar',
    bd=5,
    command=loginCadastro,
    width=5,
    borderwidth=5,
    activeforeground='red',
    padx=5,
)
bt2.place(width=70, height=30, x=385, y=34)


def clicked_login():
    logine = email_entry.get()
    loginp = password_entry.get()
    print(logine, loginp)
    if logine == conect[0] and loginp == conect1[0]:
        showinfo(title='Informação', message='Logado com sucesso!')
        vr.destroy()
        return window()
    else:
        showerror(title='Erro', message='Login informado errado! ')


# Email
login = Frame(vr)
login.config(bg='#5d8aa8')

login.pack(padx=3, pady=30, fill='x', expand=True)

email_label = Label(
    login, text='Endereço de Email:', background='white', bg='#5d8aa8'
)
email_label.pack(fill='x', expand=True)

email_entry = Entry(login, bd=5)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# Password
password_label = Label(login, text='Senha:', background='white', bg='#5d8aa8')
password_label.pack(fill='x', expand=True)

password_entry = Entry(login, bd=5, show='*')
password_entry.pack(fill='x', expand=True)

# Botão Login
login_button = Button(
    login,
    text='Logar',
    bd=5,
    command=clicked_login,
    width=15,
    borderwidth=5,
    activeforeground='red',
    padx=5,
)

login_button.pack(fill='x', expand=True, pady=10)


def window():
    global screen, screen1, screen2, screen3, screen4, screen5
    window = Tk()
    window.config(bg='#5d8aa8')
    window.colormapwindows()
    # window.attributes('-fullscreen', True)
    window.geometry('900x400')
    window.title('Menu')
    screen = Label(
        window,
        text='Cadastrando Produto',
        font=('Times', 20),
        bd=5,
        relief='ridge',
        borderwidth=10,
        width=50,
        height=1,
        compound='left',
    )
    screen1 = Label(
        window,
        text='Cadastrando Produto',
        font=('Times', 20),
        bd=5,
        relief='ridge',
        borderwidth=10,
        width=50,
        height=1,
        compound='left',
    )
    screen2 = Label(
        window,
        text='Cadastrando Produto',
        font=('Times', 20),
        bd=5,
        relief='ridge',
        borderwidth=10,
        width=50,
        height=1,
        compound='left',
    )
    screen3 = Label(
        window,
        text='Cadastrando Produto',
        font=('Times', 20),
        bd=5,
        relief='ridge',
        borderwidth=10,
        width=50,
        height=1,
        compound='left',
    )
    screen4 = Label(
        window,
        text='Cadastrando Produto',
        font=('Times', 20),
        bd=5,
        relief='ridge',
        borderwidth=10,
        width=50,
        height=1,
        compound='left',
    )
    screen5 = Label(
        window,
        text='Cadastrando Produto',
        font=('Times', 20),
        bd=5,
        relief='ridge',
        borderwidth=10,
        width=50,
        height=1,
        compound='left',
    )

    window.title('Menu')
    # window.wm_resizable(width=False, height=False)
    wi = 15
    Button(
        window,
        foreground='red',
        width=wi,
        borderwidth=10,
        activeforeground='red',
        padx=5,
    )
    bott1 = Button(
        window,
        foreground='blue',
        text='Cadastrar Produto',
        image='',
        width=wi,
        borderwidth=5,
        activeforeground='red',
        padx=5,
        command=botCadastrar,
    )
    bott2 = Button(
        window,
        foreground='blue',
        text='Apagar Produto',
        image='',
        width=wi,
        borderwidth=5,
        activeforeground='red',
        padx=5,
        command=bot2,
    )
    bott3 = Button(
        window,
        foreground='blue',
        text='Editar Produto',
        image='',
        width=wi,
        borderwidth=5,
        activeforeground='red',
        padx=5,
        command=bot3,
    )
    bott4 = Button(
        window,
        foreground='blue',
        text='Calcular',
        image='',
        width=wi,
        borderwidth=5,
        activeforeground='red',
        padx=5,
        command=bot4,
    )
    bott5 = Button(
        window,
        foreground='blue',
        text='Valores',
        image='',
        width=wi,
        borderwidth=5,
        activeforeground='red',
        padx=5,
        command=bot5,
    )
    bott6 = Button(
        window,
        foreground='blue',
        text='Ferramentas',
        image='',
        width=wi,
        borderwidth=5,
        activeforeground='red',
        padx=5,
        command=bot6,
    )
    bott7 = Button(
        window,
        text='Sair',
        image='',
        width=wi,
        borderwidth=5,
        padx=5,
        command=exit,
        background='red',
        foreground='blue',
    )
    bott1.grid(row=0, column=0)
    bott2.grid(row=0, column=1)
    bott3.grid(row=0, column=2)
    bott4.grid(row=0, column=3)
    bott5.grid(row=0, column=4)
    bott6.grid(row=0, column=5)
    bott7.grid(row=0, column=6)
    # bvindo()
    window.mainloop()


def botCadastrar():
    global cProdu_label, cProdu_entry, cProduv_entry, cProdu
    cProdu = Tk()
    cProdu.colormapwindows()
    cProdu.geometry('490x250+400+100')
    cProdu.title('Cadastrando Produto')
    screen['text'] = ''

    # Nome do produto

    cProdu_label = Label(
        cProdu,
        text='Nome do Produto',
        bd=5,
        borderwidth=5,
        font=50,
        takefocus=True,
    )
    cProdu_label.pack()
    cProdu_entry = Entry(cProdu, border=5)
    cProdu_entry.pack(expand=True, padx=10, pady=10, fill='x')

    # Valores

    cProduv_label = Label(
        cProdu,
        text='Valor',
        bd=5,
        borderwidth=5,
        font=50,
        takefocus=True,
    )
    cProduv_label.pack()
    cProduv_entry = Entry(cProdu, border=5)
    cProduv_entry.pack(expand=True, padx=10, pady=10, fill='x')

    # Botão Cadastrar
    cProdu_button = Button(
        cProdu,
        text='Cadastrar',
        foreground='blue',
        image='',
        width=15,
        borderwidth=10,
        activeforeground='red',
        padx=5,
        command=cprod,
    )
    cProdu_button.pack(expand=True, pady=5, padx=5)
    cProdu_button.focus()
    return window


def bvindo():
    data_atual = date.today()
    data_em_texto = '0{} / 0{} / {}'.format(
        data_atual.day, data_atual.month, data_atual.year
    )
    print(data_em_texto)
    screen.grid(row=10, column=2, padx=5, pady=5)
    screen['text'] = 'Bem Vindo', name[0], data_em_texto[0:]


def cprod():
    produtos = []

    produtos.append(('Produto:', cProdu_entry.get()))
    produtos.append(('Valor: R$', cProduv_entry.get()))
    print(produtos)
    screen['text'] = 'Ultimo Cadastrado', produtos
    screen.place(x=10, y=50)
    with open('produtos.txt', 'w') as f:
        f.write(f'{produtos}')
    screen1['text'] = 'Ultimo Cadastrado', produtos
    screen1.place(x=10, y=105)
    screen2['text'] = 'Ultimo Cadastrado', produtos
    screen2.place(x=10, y=160)
    screen3['text'] = 'Ultimo Cadastrado', produtos
    screen3.place(x=10, y=215)
    screen4['text'] = 'Ultimo Cadastrado', produtos
    screen4.place(x=10, y=270)
    screen5['text'] = 'Ultimo Cadastrado'
    screen5.place(x=10, y=325)

    return produtos
    cProdu.destroy()


def bot2():
    screen1['text'] = 'Bot 2'
    screen.place(x=10, y=50)


def bot3():
    screen1['text'] = 'Bot 2'


def bot4():
    screen['text'] = 'Calculando Produto...'

    return


def bot5():
    screen['text'] = 'Valores Produto...'

    return


def bot6():
    screen['text'] = 'Ferramentas...'

    return


def exit():
    login.quit()


window()


login.mainloop()
