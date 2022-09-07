from window import *
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def clicked_bt1():
    print('Open... ')

conect = []
conect1 = []

def loginCadastro():


    def cadastrar():
        global conect, conect1
        logine = ({email_entry1.get()})
        loginp = ({password_entry1.get()})
        conect.append(logine)
        conect1.append(loginp)
        print(list(conect), list(conect1))
        if logine in list(conect) and loginp in list(conect1):
            showinfo(title='Informação', message='Cadastrado com sucesso!')
            master1.destroy()
        else:
            showerror(title='Informação', message='Cadastrado Não Realizado!')
            master1.destroy()
            return loginCadastro()

    master1 = Tk()
    master1.iconbitmap()
    master1.title('Cadastro')
    master1.geometry('290x250+400+100')  # largura x altura dist esq + dist top
    master1.wm_resizable(width=False, height=False)

    login1 = Frame(master1)
    login_button1 = Button(login1, text="Cadastrar", command=cadastrar)
    login_button1.pack(fill='x', expand=True, pady=10)
    login1.pack(padx=30, pady=30, fill='x', expand=True)
    # Email
    email_label1 = Label(login1, text="Endereço de Email:")
    email_label1.pack(fill='x', expand=True)

    email_entry1 = Entry(login1, bd=5)
    email_entry1.pack(fill='x', expand=True)
    email_entry1.focus()

    # Password
    password_label1 = Label(login1, text="Senha:")
    password_label1.pack(fill='x', expand=True)

    password_entry1 = Entry(login1, bd=5, show="*")
    password_entry1.pack(fill='x', expand=True)


# Atribuindo TK = Master
vr = Tk()
vr.iconmask('')
vr.title('Login')
vr.geometry('490x500+400+100')  # largura x altura dist esq + dist top
vr.wm_resizable(width=False, height=False)

# Adicionando Imagens
layout = PhotoImage(file="")

# Layout
labelLayout = Label(vr, image=layout)
labelLayout.place(x=0, y=0)

# Conf de Botoes
bt1 = Button(vr, text='Abrir', font='Arial 10', command=clicked_bt1)
bt1.place(width=70, height=30, x=37, y=34)
bt2 = Button(vr, text='Cadastrar', font='Arial 10', command=loginCadastro)
bt2.place(width=70, height=30, x=385, y=34)

email = StringVar()
password = StringVar()

def clicked_login():


    logine = ({email_entry.get()})
    loginp = ({password_entry.get()})
    print(logine, loginp)
    if logine == conect[0] and loginp == conect1[0]:
        showinfo(title='Informação', message='Logado com sucesso!')
        vr.destroy()
        return window()
    else:
        showerror(title='Erro', message='Login informado errado! ')

# Email
login = Frame(vr)
login_button = Button(login, text="Logar", command=clicked_login)
login_button.pack(fill='x', expand=True, pady=10)
login.pack(padx=30, pady=30, fill='x', expand=True)

email_label = Label(login, text="Endereço de Email:")
email_label.pack(fill='x', expand=True)

email_entry = Entry(login, bd=5)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# Password
password_label = Label(login, text="Senha:")
password_label.pack(fill='x', expand=True)

password_entry = Entry(login, bd=5, show="*")
password_entry.pack(fill='x', expand=True)


login.mainloop()
