from tkinter import *
from tkinter import ttk
from numpy import imag
import numpy as np
import posiciona
import time
import mysql.connector

login = Tk()
login.title("Tela de login")
login.geometry("490x560+500+100")
login.iconbitmap(default="ico.ico")
login.resizable(width=1, height=1)

#Variaveis globais 
esconda_senha = StringVar()
a = False

#Funções
login.bind('<Button-1>', posiciona.inicio_place)
login.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, login))
login.bind('<Button-2>', lambda arg: posiciona.para_geometry(login))

def tela_cadastro1():
    #login.destroy()
    time.sleep(0.3)

    cadastro1 = Toplevel()
    cadastro1.title("Cadastramento1")
    cadastro1.geometry("490x560+500+100")
    cadastro1.resizable(width=1, height=1)
    #Funções
    cadastro1.bind('<Button-1>', posiciona.inicio_place)
    cadastro1.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, cadastro1))
    cadastro1.bind('<Button-2>', lambda arg: posiciona.para_geometry(cadastro1))

    def next():
        #########CONEXÃO COM O BANCO DE DADOS:
        conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1801',
            database = 'bd_projeto'
        )
        ########################################
        cursor = conexao.cursor()
        user_cadast = en_user_cadast.get()
        senha_cadast = en_senha_cadast1.get()
        confirm_senha_cadast = en_senha_cadast2.get()
        tel_cadast = en_tel_cadast.get()
        cidade_cadast = en_cidade_cadast.get()
        if user_cadast == '' or senha_cadast == '' or tel_cadast == '' or cidade_cadast == '':
            label = Label(cadastro1, text="Campo não preenchido")
            label.place(width=151, height=17, x=166, y=503)
        else:
            if senha_cadast != confirm_senha_cadast:
                label = Label(cadastro1, text="Senhas diferentes")
                label.place(width=151, height=17, x=166, y=503)
            else:
                comando = f'INSERT INTO cadastro1 (nome, senha, telefone, cidade) VALUES ("{user_cadast}", "{senha_cadast}", {tel_cadast}, "{cidade_cadast}")'
                cursor.execute(comando)
                conexao.commit() #edita o
                print(user_cadast, senha_cadast, tel_cadast, cidade_cadast) 
                tela_cadastro2()
        cursor.close()
        conexao.close()
    def tela_cadastro2():
        #time.sleep(0.3)
        cadastro2 = Toplevel()
        cadastro2.title("Cadastramento2")
        cadastro2.geometry("490x560+500+100")
        cadastro2.resizable(width=1, height=1)

        #Funções
        cadastro2.bind('<Button-1>', posiciona.inicio_place)
        cadastro2.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, cadastro2))
        cadastro2.bind('<Button-2>', lambda arg: posiciona.para_geometry(cadastro2))
        #def destruir():
        #    cadastro1.destroy()
        #    cadastro2.destroy()

        def cadastrado():
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1801',
                database = 'bd_projeto'
            )
            ########################################
            cursor = conexao.cursor()
            idade = en_idade.get()
            esporte = en_esp.get()
            posicao = en_posicao.get()
            descricao = en_desc.get()
            if idade == '' or esporte == '' or posicao == '' or descricao == '':
                label = Label(cadastro2, text="Campo não preenchido")
                label.place(width=151, height=17, x=166, y=503)
            else:
                comando = f'INSERT INTO cadastro2 (idade, esporte, posicao, descricao) VALUES ("{idade}", "{esporte}","{posicao}","{descricao}")'
                cursor.execute(comando)
                conexao.commit() #edita o 
                cadastro1.destroy()
                cadastro2.destroy()
            cursor.close()
            conexao.close()


        #Nova tela
        Tela_cadastro2 = PhotoImage(file="Tela_cadastro2.png")
        img_bt_cadastrar2 = PhotoImage(file="bt_cadastrar2.png")
        lab_cadastro2 = Label(cadastro2, image=Tela_cadastro2)
        lab_cadastro2.pack()

        #Criação de caixas de entrada

        en_idade = Entry(cadastro2, bd=2, font = ("calibri", 15), justify=LEFT)
        en_idade.place(width=227, height=52, x=158, y=86)

        #esporte
        en_esp = Entry(cadastro2, bd=2, font = ("calibri", 15), justify=LEFT)
        en_esp.place(width=226, height=51, x=157, y=169)

        #posição
        en_posicao = Entry(cadastro2, bd=2, font = ("calibri", 15), justify=LEFT)
        en_posicao.place(width=226, height=51, x=157, y=255)

        #Descrição
        en_desc = Entry(cadastro2, bd=2, font = ("calibri", 15), justify=LEFT)
        en_desc.place(width=229, height=98, x=157, y=346)
        # Criando botoes
        bt_cadastrar_cadast = Button(cadastro2, bd = 0, image = img_bt_cadastrar2, command= cadastrado)
        bt_cadastrar_cadast.place(width=112, height=41, x=330, y=493)

        cadastro2.mainloop()

    #Nova tela
    Tela_cadastro1 = PhotoImage(file="Tela_cadastro.png")
    img_bt_next = PhotoImage(file="bt_next.png")
    lab_cadastro1 = Label(cadastro1, image=Tela_cadastro1)
    lab_cadastro1.pack()

    #Criação de caixas de entrada
    #User
    en_user_cadast = Entry(cadastro1, bd=2, font = ("calibri", 15), justify=LEFT)
    en_user_cadast.place(width=227, height=52, x=157, y=86)

    #senha
    en_senha_cadast1 = Entry(cadastro1, bd=2, show = "*", font = ("calibri", 15), justify=LEFT)
    en_senha_cadast1.place(width=227, height=52, x=157, y=170)

    #confirmar senha
    en_senha_cadast2 = Entry(cadastro1, bd=2, show = "*", font = ("calibri", 15), justify=LEFT)
    en_senha_cadast2.place(width=227, height=52, x=157, y=255)

    #telefone
    en_tel_cadast = Entry(cadastro1, bd=2, font = ("calibri", 15), justify=LEFT)
    en_tel_cadast.place(width=227, height=52, x=157, y=342)

    #Cidade
    en_cidade_cadast = Entry(cadastro1, bd=2, font = ("calibri", 15), justify=LEFT)
    en_cidade_cadast.place(width=227, height=52, x=157, y=422)

    # Criando botoes
    bt_cadastrar_cadast = Button(cadastro1, bd = 0, image = img_bt_next, command= next)
    bt_cadastrar_cadast.place(width=112, height=41, x=330, y=493)

    cadastro1.mainloop()

#Tela 1
def perfil(i):
    #########CONEXÃO COM O BANCO DE DADOS:
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1801',
            database = 'bd_projeto'
        )
    ########################################
    cursor = conexao.cursor()
    comando1 = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando1)
    resultado = cursor.fetchall() #Ler banco de dados
    #login.destroy()
    time.sleep(0.3)
    tela1 = Tk()
    tela1.title("Tela 1")
    tela1.geometry("490x560+500+100")
    tela1.resizable(width=1, height=1)
    
    #Funções
    tela1.bind('<Button-1>', posiciona.inicio_place)
    tela1.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, tela1))
    tela1.bind('<Button-2>', lambda arg: posiciona.para_geometry(tela1))

    #Nova tela
    Tela_tela1 = PhotoImage(file="Tela_perfil.png")
    img_bt_lupa = PhotoImage(file="bt_lupa.png")
    img_bt_feed = PhotoImage(file="bt_feed.png")
    lab_tela1 = Label(tela1, image=Tela_tela1)
    lab_tela1.pack()

    #Criação de caixas de entrada
    en_nome = Label(tela1, text=f"{resultado[i][1]}")
    en_nome.place(width=132, height=25, x=194, y=190)

    en_idade = Label(tela1, text=f"{resultado[i][6]}")
    en_idade.place(width=135, height=25, x=195, y=224)

    en_cidade = Label(tela1, text=f"{resultado[i][4]}")
    en_cidade.place(width=134, height=24, x=204, y=259)

    en_fone = Label(tela1, text=f"{resultado[i][3]}")
    en_fone.place(width=136, height=25, x=185, y=295)

    en_esporte = Label(tela1, text=f"{resultado[i][7]}")
    en_esporte.place(width=132, height=25, x=208, y=330)

    en_posicao = Label(tela1, text=f"{resultado[i][8]}")
    en_posicao.place(width=134, height=24, x=208, y=364)

    en_desc = Label(tela1, text=f"{resultado[i][9]}", wraplength=186)
    en_desc.place(width=186, height=74, x=149, y=426)

    # Criando botoes
    bt_lupa = Button(tela1, bd = 0, image = img_bt_lupa)
    bt_lupa.place(width=63, height=63, x=19, y=8)

    bt_feed = Button(tela1, bd = 0, image = img_bt_feed)
    bt_feed.place(width=56, height=38, x=409, y=7)

    tela1.mainloop()

def escolhas(i):
    #########CONEXÃO COM O BANCO DE DADOS:
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1801',
            database = 'bd_projeto'
        )
    ########################################
    cursor = conexao.cursor()
    comando1 = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando1)
    resultado = cursor.fetchall() #Ler banco de dados
    login.destroy()
    time.sleep(0.3)
    tela2 = Tk()
    tela2.title("Escolhas")
    tela2.geometry("490x560+500+100")
    tela2.resizable(width=1, height=1)
    
    #Funções
    tela2.bind('<Button-1>', posiciona.inicio_place)
    tela2.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, tela2))
    tela2.bind('<Button-2>', lambda arg: posiciona.para_geometry(tela2))

    '''def opcao(escolha):
        #########CONEXÃO COM O BANCO DE DADOS:
        conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1801',
                database = 'bd_projeto'
        )
            ########################################
        cursor = conexao.cursor()
        if escolha == 'basquete':
            comando = f'INSERT INTO escolhas (idade, esporte, posicao, descricao) VALUES ("{idade}", "{esporte}","{posicao}","{descricao}")'
            cursor.execute(comando)
            conexao.commit() #edita o '''
    #Imagens
    Tela_tela2 = PhotoImage(file="Tela_escolha.png")
    img_bt_seta = PhotoImage(file="bt_seta.png")
    img_basquete = PhotoImage(file="bt_basquete.png")
    lab_tela2 = Label(tela2, image=Tela_tela2)
    lab_tela2.pack()

    #Criação de caixas de entrada

    # Criando botoes
    escolhas = []
    j=0
    bt_seta = Button(tela2, bd = 0, image = img_bt_seta, command = tela2.destroy)
    bt_seta.place(width=63, height=63, x=408, y=20)
    bt_basquete = Button(tela2, bd = 0, image = img_basquete)# command = lambda: escolhas[j] == 'basquete')
    bt_basquete.place(width=119, height=38, x=131, y=253)

    tela2.mainloop()

def entrar():
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1801',
            database = 'bd_projeto'
        )
    cursor = conexao.cursor()
    comando = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando)
    resultado = cursor.fetchall() #Ler banco de dados
    #print(resultado[0][1])
    user = en_user.get()
    senha = en_senha.get()
    for i in range(len(resultado)):
        if resultado[i][0] == resultado[i][5] and user == resultado[i][1] and senha == resultado[i][2]:
            escolhas(i)
            perfil(i)
        else:
            label = Label(login, text="Login ou senha errada")
            label.place(width=206, height=17, x=155, y=392)
    print(user, senha)
    cursor.close()
    conexao.close()


# Importar imagens
Tela_login = PhotoImage(file="Tela_login.png")
img_bt_entrar = PhotoImage(file="bt_entrar.png")
img_bt_cadastrar1 = PhotoImage(file="bt_cadastrar1.png")


# Criação de labels
lab_login = Label(login, image=Tela_login)
lab_login.image = Tela_login
lab_login.pack()

#Criação de caixas de entrada
en_user = Entry(login, bd=2, font = ("calibri", 15), justify=LEFT)
en_user.place(width=228, height=48, x=144, y=253)

en_senha = Entry(login, bd=2,textvariable=esconda_senha, show = "*", font = ("calibri", 15), justify=LEFT)
en_senha.place(width=227, height=47, x=144, y=335)


# Criando botoes
bt_entrar = Button(login, bd = 0, image = img_bt_entrar, command = entrar)
bt_entrar.place(width=146, height=71, x=185, y=417)

bt_cadastrar1 = Button(login, bd = 0, image = img_bt_cadastrar1, command = tela_cadastro1)
bt_cadastrar1.place(width=148, height=41, x=183, y=499)

login.mainloop()