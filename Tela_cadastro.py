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

    def next(event):
        #########CONEXÃO COM O BANCO DE DADOS:
        conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cwtabtab123',
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

        def cadastrado(event):
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Cwtabtab123',
                database = 'bd_projeto'
            )
            ########################################
            cursor = conexao.cursor()
            idade = en_idade.get()
            esporte = en_esp.get()
            posicao = en_posicao.get()
            descricao = en_desc.get()
            if idade == '' or esporte == '' or descricao == '':
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
        i=0
        bt_cadastrar_cadast = Button(cadastro2, bd = 0, image = img_bt_cadastrar2, command= lambda: cadastrado(i))
        bt_cadastrar_cadast.place(width=112, height=41, x=330, y=493)

        cadastro2.bind('<Return>', cadastrado)
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
    i=0
    bt_cadastrar_cadast = Button(cadastro1, bd = 0, image = img_bt_next, command= lambda: next(i))
    bt_cadastrar_cadast.place(width=112, height=41, x=330, y=493)

    cadastro1.bind('<Return>', next)

    cadastro1.mainloop()


def perfil(i):
    #########CONEXÃO COM O BANCO DE DADOS:
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cwtabtab123',
            database = 'bd_projeto'
        )
    ########################################
    cursor = conexao.cursor()
    comando = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando)
    resultado = cursor.fetchall() #Ler banco de dados
    #login.destroy()
    time.sleep(0.3)
    perfil = Tk()
    perfil.title("Perfil")
    perfil.geometry("490x560+500+100")
    perfil.resizable(width=1, height=1)
    
    #Funções
    perfil.bind('<Button-1>', posiciona.inicio_place)
    perfil.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, perfil))
    perfil.bind('<Button-2>', lambda arg: posiciona.para_geometry(perfil))

    #Nova tela
    Tela_perfil = PhotoImage(file="Tela_perfil.png")
    img_bt_lupa = PhotoImage(file="bt_lupa.png")
    img_bt_feed = PhotoImage(file="bt_feed.png")
    lab_perfil = Label(perfil, image=Tela_perfil)
    lab_perfil.pack()

    #Criação de caixas de entrada
    en_nome = Label(perfil, text=f"{resultado[i][1]}")
    en_nome.place(width=132, height=25, x=194, y=190)

    en_idade = Label(perfil, text=f"{resultado[i][6]}")
    en_idade.place(width=135, height=25, x=195, y=224)

    en_cidade = Label(perfil, text=f"{resultado[i][4]}")
    en_cidade.place(width=134, height=24, x=204, y=259)

    en_fone = Label(perfil, text=f"{resultado[i][3]}")
    en_fone.place(width=136, height=25, x=185, y=295)

    en_esporte = Label(perfil, text=f"{resultado[i][7]}")
    en_esporte.place(width=132, height=25, x=208, y=330)

    en_posicao = Label(perfil, text=f"{resultado[i][8]}")
    en_posicao.place(width=134, height=24, x=208, y=364)

    en_desc = Label(perfil, text=f"{resultado[i][9]}", wraplength=186)
    en_desc.place(width=186, height=74, x=149, y=426)

    # Criando botoes
    bt_lupa = Button(perfil, bd = 0, image = img_bt_lupa, command= lambda: filtro(i))
    bt_lupa.place(width=63, height=63, x=19, y=8)

    bt_feed = Button(perfil, bd = 0, image = img_bt_feed, command= lambda: feed(i))
    bt_feed.place(width=56, height=38, x=409, y=7)

    perfil.mainloop()

def feed(i):
    #########CONEXÃO COM O BANCO DE DADOS:
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cwtabtab123',
            database = 'bd_projeto'
        )
    ########################################
    cursor = conexao.cursor()
    comando1 = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando1)
    resultado = cursor.fetchall() #Ler banco de dados
    #login.destroy()
    time.sleep(0.3)
    feed = Toplevel()
    feed.title("Feed")
    feed.geometry("490x560+500+100")
    feed.resizable(width=1, height=1)
    
    #Funções
    feed.bind('<Button-1>', posiciona.inicio_place)
    feed.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, feed))
    feed.bind('<Button-2>', lambda arg: posiciona.para_geometry(feed))

    def LerFeed(i):
        #########CONEXÃO COM O BANCO DE DADOS:
        print(i)
        conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Cwtabtab123',
                database = 'bd_projeto'
            )
        ########################################
        cursor = conexao.cursor()
        
        comando = f'SELECT * FROM cadastro1, cadastro2'
        cursor.execute(comando)
        resultado = cursor.fetchall() #Ler banco de dados
        #login.destroy()
        time.sleep(0.3)
        lerfeed = Toplevel()
        lerfeed.title("lerfeed")
        lerfeed.geometry("490x560+500+100")
        lerfeed.resizable(width=1, height=1)
        
        #Funções
        lerfeed.bind('<Button-1>', posiciona.inicio_place)
        lerfeed.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, lerfeed))
        lerfeed.bind('<Button-2>', lambda arg: posiciona.para_geometry(lerfeed))

        def destruir():
                lerfeed.destroy()
                feed.destroy()
                
        #Nova tela
        tela_ler_feed = PhotoImage(file="feed.png")
        d = PhotoImage(file="bt_perfil.png")
        lab_tela_ler_feed = Label(lerfeed, image=tela_ler_feed)
        lab_tela_ler_feed.pack()

        #Criando caixas
        comando2 = f'SELECT * FROM publicacao'
        cursor.execute(comando2)
        resultado2 = cursor.fetchall()

        en_nome = Label(lerfeed, text=f"{resultado[i][1]}")
        en_nome.place(width=171, height=27, x=7, y=117)
        print(resultado[i][0])
        acumulo = 0
        for j in range(len(resultado2)):
            if resultado2[j][1] == resultado[i][0]:
                acumulo +=1
                if(acumulo == 1):
                    en_publi_no_feed1 = Label(lerfeed, text=f"{resultado2[j][2]}", wraplength=449)
                    en_publi_no_feed1.place(width=449, height=51, x=19, y=153)
                    continue
                elif(acumulo == 2):
                    en_publi_no_feed2 = Label(lerfeed, text=f"{resultado2[j][2]}", wraplength=449)
                    en_publi_no_feed2.place(width=449, height=51, x=19, y=254)
                    continue
                elif(acumulo == 3):
                    en_publi_no_feed2 = Label(lerfeed, text=f"{resultado2[j][2]}", wraplength=449)
                    en_publi_no_feed2.place(width=449, height=51, x=19, y=353)
                    continue
                elif(acumulo == 4):
                    en_publi_no_feed2 = Label(lerfeed, text=f"{resultado2[j][2]}", wraplength=449)
                    en_publi_no_feed2.place(width=449, height=51, x=19, y=450)
                    continue
        acumulo = 0

        en_nome2 = Label(lerfeed, text=f"{resultado[i][1]}")
        en_nome2.place(width=171, height=27, x=11, y=213)

        en_nome3 = Label(lerfeed, text=f"{resultado[i][1]}")
        en_nome3.place(width=171, height=27, x=10, y=316)

        en_nome4 = Label(lerfeed, text=f"{resultado[i][1]}")
        en_nome4.place(width=171, height=27, x=9, y=414)
        # Criando botoes
        i=0
        bt_perfil = Button(lerfeed, bd = 0, image = d, command= destruir)
        bt_perfil.place(width=63, height=63, x=19, y=8)

        lerfeed.mainloop()
    #fim
    #Nova tela
    Tela_escolha_feed = PhotoImage(file="Telaescolhafeed.png")
    b = PhotoImage(file="PublicarFeed.png")
    c = PhotoImage(file="LerFeed.png")
    d = PhotoImage(file="bt_perfil.png")
    lab_Tela_escolha_feed= Label(feed, image=Tela_escolha_feed)
    lab_Tela_escolha_feed.pack()

    # Criando botoes
    bt_perfil = Button(feed, bd = 0, image = d, command=feed.destroy)
    bt_perfil.place(width=63, height=63, x=19, y=8)

    criar_feed = Button(feed, bd = 0, image = c, command= lambda: LerFeed(i))
    criar_feed.place(width=172, height=112, x=156, y=167)

    publi_feed = Button(feed, bd = 0, image = b,  command= lambda: Publicarfeed(i))
    publi_feed.place(width=172, height=112, x=154, y=309)

    feed.mainloop()

def Publicarfeed(i):
    print(i)
    time.sleep(0.3)
    publi = Toplevel()
    publi.title("PublicarFeed")
    publi.geometry("490x560+500+100")
    publi.resizable(width=1, height=1)
    
    #Funções
    publi.bind('<Button-1>', posiciona.inicio_place)
    publi.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, publi))
    publi.bind('<Button-2>', lambda arg: posiciona.para_geometry(publi))

    def publicar(i):
        #########CONEXÃO COM O BANCO DE DADOS:
        conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Cwtabtab123',
                database = 'bd_projeto'
            )
        ########################################
        cursor = conexao.cursor()
        publicacao = en_coment.get()
        comando = f'SELECT * FROM cadastro1, cadastro2'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        if publicacao == '':
            label = Label(publi, text="Digite alguma coisa")
            label.place(width=151, height=17, x=166, y=503)
        else:
            comando = f'INSERT INTO publicacao (id_cadastro1, publi) VALUES ("{resultado[i][0]}","{publicacao}")'
            cursor.execute(comando)
            conexao.commit() #edita o 
            publi.destroy()
        cursor.close()
        conexao.close()
    #Nova tela
    fundo = PhotoImage(file="publicafeed.png")
    pub = PhotoImage(file="publicar.png")
    volt = PhotoImage(file="voltar.png")
    perf = PhotoImage(file="bt_perfil.png")
    lab_tela1 = Label(publi, image=fundo)
    lab_tela1.pack()

    #criação de caixa de entrada
    en_coment = Entry(publi, bd=2, font = ("calibri", 15), justify=LEFT)
    en_coment.place(width=219, height=223, x=132, y=164)

    # Criando botoes
    bt_perfil = Button(publi, bd = 0, image = perf, command=publi.destroy)
    bt_perfil.place(width=63, height=63, x=19, y=8)

    criar_feed = Button(publi, bd = 0, image = volt, command= publi.destroy)
    criar_feed.place(width=55, height=33, x=409, y=9)

    publi_feed = Button(publi, bd = 0, image = pub, command= lambda: publicar(i))
    publi_feed.place(width=93, height=34, x=198, y=424)

    publi.mainloop()


def filtro(i):
    #########CONEXÃO COM O BANCO DE DADOS:
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cwtabtab123',
            database = 'bd_projeto'
        )
    ########################################
    cursor = conexao.cursor()
    comando1 = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando1)
    resultado = cursor.fetchall() #Ler banco de dados
    #login.destroy()
    time.sleep(0.3)
    filtrar = Toplevel()
    filtrar.title("Filtrar")
    filtrar.geometry("490x560+500+100")
    filtrar.resizable(width=1, height=1)
    
    #Funções
    filtrar.bind('<Button-1>', posiciona.inicio_place)
    filtrar.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, filtrar))
    filtrar.bind('<Button-2>', lambda arg: posiciona.para_geometry(filtrar))

    def func_filt(event):
        label = Label(filtrar, text=f'Você selecionou: {selected_filt.get()}')
        label.place(width=132, height=17, x=175, y=457)
        i=0
        bt_seta = Button(filtrar, bd = 0, image = img_bt_seta, command= lambda: pesquisa(i))
        bt_seta.place(width=63, height=63, x=214, y=389)
    def pesquisa(i):
        #########CONEXÃO COM O BANCO DE DADOS:
        '''if selected_filt.get() == 'Nome':
            label = Label(filtrar, text='Selecione outro filtro')
            label.place(width=132, height=17, x=175, y=457)
            print("Entrou aqui")
            print(selected_filt.get())
        else:'''
        print(selected_filt.get())
        conexao = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'Cwtabtab123',
                    database = 'bd_projeto'
                )
            ########################################
            #login.destroy()
        time.sleep(0.3)
        pesquisar = Toplevel()
        pesquisar.title("Pesquisa")
        pesquisar.geometry("490x560+500+100")
        pesquisar.resizable(width=1, height=1)
            
            #Funções
        pesquisar.bind('<Button-1>', posiciona.inicio_place)
        pesquisar.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, pesquisar))
        pesquisar.bind('<Button-2>', lambda arg: posiciona.para_geometry(pesquisar))

        def destruir():
            pesquisar.destroy()
            filtrar.destroy()
            '''def func_filt(event):
                label = Label(pesquisar, text=f'Você selecionou: {selected_filt.get()}')
                label.place(width=132, height=17, x=175, y=457)
                bt_seta = Button(pesquisar, bd = 0, image = img_bt_seta)
                bt_seta.place(width=63, height=63, x=214, y=389)'''
        def nome(eventual):
            entrada = en_pesquisa.get()
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'Cwtabtab123',
                    database = 'bd_projeto'
                )
            ########################################
            cursor = conexao.cursor()
            comando = f"SELECT * FROM cadastro1, cadastro2 WHERE nome = '{entrada}'"
            cursor.execute(comando)
            resultado = cursor.fetchall() #Ler banco de dados
            for i in range(len(resultado)):
                if resultado[i][0] == resultado[i][5]:
                    pesquisado(i)
        def cidade(eventual):
            entrada = en_pesquisa.get()
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'Cwtabtab123',
                    database = 'bd_projeto'
                )
            ########################################
            cursor = conexao.cursor()
            comando = f"SELECT * FROM cadastro1, cadastro2 WHERE cidade = '{entrada}'"
            cursor.execute(comando)
            resultado = cursor.fetchall() #Ler banco de dados
            for i in range(len(resultado)):
                if resultado[i][0] == resultado[i][5]:
                    pesquisado(i)

        def idade(eventual):
            entrada = en_pesquisa.get()
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'Cwtabtab123',
                    database = 'bd_projeto'
                )
            ########################################
            cursor = conexao.cursor()
            comando = f"SELECT * FROM cadastro1, cadastro2 WHERE idade = '{entrada}'"
            cursor.execute(comando)
            resultado = cursor.fetchall() #Ler banco de dados
            for i in range(len(resultado)):
                if resultado[i][0] == resultado[i][5]:
                    pesquisado(i)
        def esporte(eventual):
            entrada = en_pesquisa.get()
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'Cwtabtab123',
                    database = 'bd_projeto'
                )
            ########################################
            cursor = conexao.cursor()
            comando = f"SELECT * FROM cadastro1, cadastro2 WHERE esporte = '{entrada}'"
            cursor.execute(comando)
            resultado = cursor.fetchall() #Ler banco de dados
            for i in range(len(resultado)):
                if resultado[i][0] == resultado[i][5]:
                        pesquisado(i)
        def pesquisado(i):
            entrada = en_pesquisa.get()
            #########CONEXÃO COM O BANCO DE DADOS:
            conexao = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'Cwtabtab123',
                    database = 'bd_projeto'
                )
            ########################################
            cursor = conexao.cursor()
            comando = f"SELECT * FROM cadastro1, cadastro2 WHERE {selected_filt.get()} = '{entrada}'"
            cursor.execute(comando)
            resultado = cursor.fetchall() #Ler banco de dados
            filtrar.destroy()
            pesquisar.destroy()
            time.sleep(0.3)
            tk_pesquisado = Toplevel()
            tk_pesquisado.title("pesquisado")
            tk_pesquisado.geometry("490x560+500+100")
            tk_pesquisado.resizable(width=1, height=1)
            
            #Funções
            tk_pesquisado.bind('<Button-1>', posiciona.inicio_place)
            tk_pesquisado.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, tk_pesquisado))
            tk_pesquisado.bind('<Button-2>', lambda arg: posiciona.para_geometry(tk_pesquisado))

            #Nova tela
            Tela_pesquisado = PhotoImage(file="Tela_pesquisado.png")
            img_bt_perfil = PhotoImage(file="bt_perfil.png")
            img_bt_feed = PhotoImage(file="bt_feed.png")
            img_bt_seta = PhotoImage(file="bt_seta.png")
            lab_tk_pesquisado = Label(tk_pesquisado, image=Tela_pesquisado)
            lab_tk_pesquisado.pack()

            #Criação de caixas de entrada
            en_nome = Label(tk_pesquisado, text=f"{resultado[i][1]}")
            en_nome.place(width=132, height=25, x=194, y=190)

            en_idade = Label(tk_pesquisado, text=f"{resultado[i][6]}")
            en_idade.place(width=135, height=25, x=195, y=224)

            en_cidade = Label(tk_pesquisado, text=f"{resultado[i][4]}")
            en_cidade.place(width=134, height=24, x=204, y=259)

            en_fone = Label(tk_pesquisado, text=f"{resultado[i][3]}")
            en_fone.place(width=136, height=25, x=185, y=295)

            en_esporte = Label(tk_pesquisado, text=f"{resultado[i][7]}")
            en_esporte.place(width=132, height=25, x=208, y=330)

            en_posicao = Label(tk_pesquisado, text=f"{resultado[i][8]}")
            en_posicao.place(width=134, height=24, x=208, y=364)

            en_desc = Label(tk_pesquisado, text=f"{resultado[i][9]}", wraplength=186)
            en_desc.place(width=186, height=74, x=149, y=426)

            # Criando botoes
            i=0
            bt_perfil = Button(tk_pesquisado, bd = 0, image = img_bt_perfil, command= tk_pesquisado.destroy)
            bt_perfil.place(width=63, height=63, x=19, y=8)

            bt_feed = Button(tk_pesquisado, bd = 0, image = img_bt_feed, command= lambda: feed(i))
            bt_feed.place(width=56, height=38, x=409, y=7)

            bt_seta = Button(tk_pesquisado, bd = 0, image = img_bt_seta, command= tk_pesquisado.destroy)
            bt_seta.place(width=63, height=63, x=410, y=483)

            tk_pesquisado.mainloop()
            #Nova tela
        Tela_pesquisar = PhotoImage(file="Tela_pesquisar.png")
        img_bt_perfil = PhotoImage(file="bt_perfil.png")
        img_bt_feed = PhotoImage(file="bt_feed.png")
        img_bt_lupa = PhotoImage(file="bt_lupa.png")
        lab_tela_pesquisar = Label(pesquisar, image=Tela_pesquisar)
        lab_tela_pesquisar.pack()

            #Criação de caixas de entrada
            
        en_pesquisa = Entry(pesquisar, bd=2, font = ("calibri", 15), justify=LEFT)
        en_pesquisa.place(width=230, height=51, x=130, y=278)

            # Criando botoes
        bt_perfil = Button(pesquisar, bd = 0, image = img_bt_perfil, command= destruir)
        bt_perfil.place(width=63, height=63, x=19, y=8)

        bt_lupa = Button(pesquisar, bd = 0, image = img_bt_lupa)
        bt_lupa.place(width=63, height=63, x=214, y=389)

        bt_feed = Button(pesquisar, bd = 0, image = img_bt_feed, command= lambda: feed(i))
        bt_feed.place(width=56, height=38, x=409, y=7)

        if selected_filt.get() == 'Nome':
            label = Label(pesquisar, text=f'{selected_filt.get()}:')
            label.place(width=135, height=15, x=176, y=243)
            bt_lupa = Button(pesquisar, bd = 0, image = img_bt_lupa, command= nome)
            bt_lupa.place(width=63, height=63, x=214, y=389)
            pesquisar.bind('<Return>', nome)
        elif selected_filt.get() == 'Cidade':
            label = Label(pesquisar, text=f'{selected_filt.get()}:')
            label.place(width=135, height=15, x=176, y=243)
            bt_lupa = Button(pesquisar, bd = 0, image = img_bt_lupa, command= cidade)
            bt_lupa.place(width=63, height=63, x=214, y=389)
            pesquisar.bind('<Return>', cidade)
        elif selected_filt.get() == 'Idade':
            label = Label(pesquisar, text=f'{selected_filt.get()}:')
            label.place(width=135, height=15, x=176, y=243)
            bt_lupa = Button(pesquisar, bd = 0, image = img_bt_lupa, command= idade)
            bt_lupa.place(width=63, height=63, x=214, y=389)
            pesquisar.bind('<Return>', idade)
        elif selected_filt.get() == 'Esporte':
            label = Label(pesquisar, text=f'{selected_filt.get()}:')
            label.place(width=135, height=15, x=176, y=243)
            bt_lupa = Button(pesquisar, bd = 0, image = img_bt_lupa, command= esporte)
            bt_lupa.place(width=63, height=63, x=214, y=389)
            pesquisar.bind('<Return>', esporte)

        pesquisar.mainloop()
    #Nova tela
    Tela_filtrar = PhotoImage(file="Tela_filtrar.png")
    img_bt_perfil = PhotoImage(file="bt_perfil.png")
    img_bt_feed = PhotoImage(file="bt_feed.png")
    img_bt_seta = PhotoImage(file="bt_seta.png")
    lab_perfil = Label(filtrar, image=Tela_filtrar)
    lab_perfil.pack()

    #Criação de caixas de entrada
    selected_filt = StringVar()
    filt_list = ['Nome', 'Cidade', 'Idade', 'Esporte']

    filt_box = ttk.Combobox(
            filtrar,
            textvariable = selected_filt,
            width=20
            #postcommand=dropdown_opened
        )
    filt_box['values'] = [filt_list[m] for m in range(0,4)]
    filt_box['state'] = 'readonly'
    filt_box.place(width=220, height=45, x=143, y=306)

    filt_box.bind('<<ComboboxSelected>>', func_filt)
    '''
    en_nome = Label(filtrar, text=f"{resultado[i][1]}")
    en_nome.place(width=132, height=25, x=194, y=190)
    '''
    # Criando botoes
    bt_perfil = Button(filtrar, bd = 0, image = img_bt_perfil, command= filtrar.destroy)
    bt_perfil.place(width=63, height=63, x=19, y=8)

    bt_seta = Button(filtrar, bd = 0, image = img_bt_seta)
    bt_seta.place(width=63, height=63, x=214, y=389)

    bt_feed = Button(filtrar, bd = 0, image = img_bt_feed, command= lambda: feed(i))
    bt_feed.place(width=56, height=38, x=409, y=7)

    filtrar.mainloop()

def escolhas(i):
    #########CONEXÃO COM O BANCO DE DADOS:
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cwtabtab123',
            database = 'bd_projeto'
        )
    ########################################
    cursor = conexao.cursor()
    comando1 = f'SELECT * FROM cadastro1, cadastro2'
    cursor.execute(comando1)
    resultado = cursor.fetchall() #Ler banco de dados
    login.destroy()
    time.sleep(0.3)
    escolha = Tk()
    escolha.title("Escolhas")
    escolha.geometry("490x560+500+100")
    escolha.resizable(width=1, height=1)
    
    #Funções
    escolha.bind('<Button-1>', posiciona.inicio_place)
    escolha.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, escolha))
    escolha.bind('<Button-2>', lambda arg: posiciona.para_geometry(escolha))

    '''def opcao(escolha):
        #########CONEXÃO COM O BANCO DE DADOS:
        conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'pregador17',
                database = 'bd_projeto'
        )
            ########################################
        cursor = conexao.cursor()
        if escolha == 'basquete':
            comando = f'INSERT INTO escolhas (idade, esporte, posicao, descricao) VALUES ("{idade}", "{esporte}","{posicao}","{descricao}")'
            cursor.execute(comando)
            conexao.commit() #edita o'''
    #Imagens
    Tela_escolha = PhotoImage(file="Tela_escolha.png")
    img_bt_seta = PhotoImage(file="bt_seta.png")
    img_basquete = PhotoImage(file="bt_basquete.png")
    img_futebol = PhotoImage(file="bt_futebol.png")
    img_treinador = PhotoImage(file="bt_treinador.png")
    img_patrocinio = PhotoImage(file="bt_patrocinio.png")
    img_paratletas = PhotoImage(file="bt_paratletas.png")
    img_natacao = PhotoImage(file="bt_natacao.png")
    lab_escolha = Label(escolha, image=Tela_escolha)
    lab_escolha.pack()

    #Criação de caixas de entrada
    bt_seta = Button(escolha, bd = 0, image = img_bt_seta, command = escolha.destroy)
    bt_seta.place(width=63, height=63, x=408, y=20)
    bt_basquete = Button(escolha, bd = 0, image = img_basquete)#, command = lambda: opcao[j] == 'basquete')
    bt_basquete.place(width=119, height=38, x=131, y=253)
    bt_futebol = Button(escolha, bd = 0, image = img_futebol)#, command = lambda: opcao[j] == 'basquete')
    bt_futebol.place(width=119, height=38, x=249, y=300)
    bt_treinador = Button(escolha, bd = 0, image = img_treinador)#, command = lambda: opcao[j] == 'basquete')
    bt_treinador.place(width=119, height=38, x=127, y=344)
    bt_patrocinio = Button(escolha, bd = 0, image = img_patrocinio)#, command = lambda: opcao[j] == 'basquete')
    bt_patrocinio.place(width=119, height=38, x=250, y=389)
    bt_paratletas = Button(escolha, bd = 0, image = img_paratletas)#, command = lambda: opcao[j] == 'basquete')
    bt_paratletas.place(width=119, height=38, x=129, y=436)
    bt_natacao = Button(escolha, bd = 0, image = img_natacao)#, command = lambda: opcao[j] == 'basquete')
    bt_natacao.place(width=119, height=38, x=249, y=482)
    escolha.mainloop()

def entrar(i):
    conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cwtabtab123',
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
i=0
bt_entrar = Button(login, bd = 0, image = img_bt_entrar, command = lambda: entrar(i))
bt_entrar.place(width=146, height=71, x=185, y=417)

bt_cadastrar1 = Button(login, bd = 0, image = img_bt_cadastrar1, command = tela_cadastro1)
bt_cadastrar1.place(width=148, height=41, x=183, y=499)


login.bind('<Return>', entrar)

login.mainloop()