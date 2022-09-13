from tkinter import *
from tkinter.messagebox import showinfo, showerror
from datetime import date


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
    master1.title('Cadastro')
    master1.geometry('290x500+510+100')  # largura x altura dist esq + dist top
    master1.wm_resizable(width=False, height=False)
    login1 = Frame(master1)
    login_button1 = Button(login1, text="Cadastrar", command=cadastrar)
    login_button1.pack(fill='x', expand=True, pady=10)
    login1.pack(padx=30, pady=30, fill='x', expand=True)
    # Nome
    nome_entry = Label(login1, text="Nome :")
    nome_entry.pack(fill='x', expand=True)

    nome_entry = Entry(login1, bd=5)
    nome_entry.pack(fill='x', expand=True)
    nome_entry.focus()

    email_label1 = Label(login1, text="Endereço de Email :")
    email_label1.pack(fill='x', expand=True)

    email_entry1 = Entry(login1, bd=5)
    email_entry1.pack(fill='x', expand=True)
    email_entry1.focus()

    # Password
    password_label1 = Label(login1, text="Senha :")
    password_label1.pack(fill='x', expand=True)

    password_entry1 = Entry(login1, bd=5, show="*")
    password_entry1.pack(fill='x', expand=True)

    # Password Repeat
    password_label2 = Label(login1, text="Redefinir Senha:")
    password_label2.pack(fill='x', expand=True)

    password_entry2 = Entry(login1, bd=5, show="*")
    password_entry2.pack(fill='x', expand=True)


# Login
vr = Tk()
icon = PhotoImage(master=vr, file='icon.png')
vr.wm_iconphoto(True, icon)
vr.title('Login')
vr.config(bg='')
vr.geometry('490x500+400+100')  # largura x altura dist esq + dist top
vr.wm_resizable(width=False, height=False)

# Adicionando Imagens
layout = PhotoImage(file="")

# Layout
labelLayout = Label(vr, image=layout)
labelLayout.place(x=0, y=0)

# Conf de Botoes
bt1 = Button(vr,
             bd=5,
             text='Abrir',
             command=clicked_bt1,
             width=5,
             borderwidth=5,
             activeforeground='red',
             padx=5
             )
bt1.place(width=70,
          height=30,
          x=37,
          y=34
          )
bt2 = Button(vr,
             text='Cadastrar',
             bd=5,
             command=loginCadastro,
             width=5,
             borderwidth=5,
             activeforeground='red',
             padx=5
             )
bt2.place(width=70,
          height=30,
          x=385,
          y=34
          )


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
login_button = Button(login,
                      text="Logar",
                      bd=5,
                      command=clicked_login,
                      width=15,
                      borderwidth=5,
                      activeforeground='red', padx=5)
login_button.pack(fill='x',
                  expand=True,
                  pady=10)
login.pack(padx=30,
           pady=30,
           fill='x',
           expand=True)

email_label = Label(login,
                    text="Endereço de Email:")
email_label.pack(fill='x',
                 expand=True)

email_entry = Entry(login,
                    bd=5)
email_entry.pack(fill='x',
                 expand=True)
email_entry.focus()

# Password
password_label = Label(login,
                       text="Senha:")
password_label.pack(fill='x',
                    expand=True)

password_entry = Entry(login,
                       bd=5, show="*")
password_entry.pack(fill='x',
                    expand=True)


def window():
    global screen
    window = Tk()
    window.config(bg='#8ed49f')
    window.colormapwindows()
    window.attributes('-fullscreen', True)
    window.bind("<F11>")
    window.title('Menu')
    screen = Label(window, text='', font=("Times", 20), bd=5, relief='ridge')
    screen.grid(row=0, column=1)
    # window.wm_resizable(width=False, height=False)
    wi = 15
    Button(window, foreground='red', width=wi, borderwidth=10, activeforeground='red', padx=5)
    bt1 = Button(window,
                 foreground='blue',
                 text='Cadastrar Produto',
                 image='',
                 width=wi,
                 borderwidth=5,
                 activeforeground='red',
                 padx=5,
                 command=bot1
                 )
    bt2 = Button(window,
                 foreground='blue',
                 text='Apagar Produto',
                 image='',
                 width=wi,
                 borderwidth=5,
                 activeforeground='red',
                 padx=5,
                 command=bot2
                 )
    bt3 = Button(window,
                 foreground='blue',
                 text='Editar Produto',
                 image='',
                 width=wi,
                 borderwidth=5,
                 activeforeground='red',
                 padx=5,
                 command=bot3
                 )
    bt4 = Button(window,
                 foreground='blue',
                 text='Calcular',
                 image='',
                 width=wi,
                 borderwidth=5,
                 activeforeground='red',
                 padx=5,
                 command=bot4
                 )
    bt5 = Button(window,
                 foreground='blue',
                 text='Valores',
                 image='',
                 width=wi,
                 borderwidth=5,
                 activeforeground='red',
                 padx=5,
                 command=bot5
                 )
    bt6 = Button(window,
                 foreground='blue',
                 text='Ferramentas',
                 image='',
                 width=wi,
                 borderwidth=5,
                 activeforeground='red',
                 padx=5,
                 command=bot6
                 )
    bt7 = Button(window,
                 text='Sair',

                 image='',
                 width=wi,
                 borderwidth=5,
                 padx=5,
                 command=bot7,
                 background='red',
                 foreground='blue',

                 )
    bt1.grid(row=0, column=0)
    bt2.grid(row=1, column=0)
    bt3.grid(row=2, column=0)
    bt4.grid(row=3, column=0)
    bt5.grid(row=4, column=0)
    bt6.grid(row=5, column=0)
    bt7.grid(row=8, column=0)
    bvindo()
    window.mainloop()


def bot1():
    global cProdu_label, cProdu_entry, cProduv_entry, cProdu
    cProdu = Tk()
    cProdu.colormapwindows()
    cProdu.geometry('490x250+400+100')
    cProdu.title('Cadastrando Produto')
    screen['text'] = 'Cadastrando Produto... '

    # Nome do produto

    cProdu_label = Label(cProdu,
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

    cProduv_label = Label(cProdu,
                          text='Valor',
                          bd=5,
                          borderwidth=5,
                          font=50,
                          takefocus=True,
                          )
    cProduv_label.pack()
    cProduv_entry = Entry(cProdu, border=5)
    cProduv_entry.pack(expand=True, padx=10, pady=10, fill='x')

    # Botão
    cProdu_button = Button(cProdu,
                           text="Cadastrar",
                           foreground='blue',
                           image='',
                           width=15,
                           borderwidth=10,
                           activeforeground='red',
                           padx=5,
                           command=cprod
                           )
    cProdu_button.pack(expand=True, pady=5, padx=5)
    cProdu_button.focus()
    return window


def cprod():
    global produtos

    produtos = (f'Produto: {cProdu_entry.get()} Valor: R${cProduv_entry.get()},00'.replace('{}', ''))
    produtos = produtos.replace('{}', '')
    screen['text'] = 'Ultimo Cadastrado', produtos
    cProdu.destroy()

    with open('produtos.txt', 'w') as f:
        f.write(f'{produtos}\n')
        return '\n', f.write(f'{produtos}\n')


def bvindo():
    data_atual = date.today()
    data_em_texto = '0{} / 0{} / {}'.format(data_atual.day, data_atual.month, data_atual.year)
    print(data_em_texto)

    screen.grid(row=10, column=2, padx=5, pady=5)
    screen['text'] = 'Bem Vindo', name[0], data_em_texto[0:]


def bot2():
    return


def bot3():
    open('cadastro.txt')

    return


def bot4():
    screen['text'] = 'Calculando Produto...'

    return


def bot5():
    screen['text'] = 'Valores Produto...'

    return


def bot6():
    screen['text'] = 'Ferramentas...'

    return


def bot7():
    login.quit()


# window()


login.mainloop()
