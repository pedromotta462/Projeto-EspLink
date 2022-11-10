import mysql.connector
import pandas as pd

#apps = pd.read_csv('googleplaystore.csv')
#coments = pd.read_csv('googleplaystore_user_reviews.csv')
#print(coments['Translated_Review'])
#coments.dropna(inplace=True)
#Eliminar os comentários com Aspas "" pois estavam dando problema no banco de dados
a = 0

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pregador17',
    database = 'bd_projeto'
)

cursor = conexao.cursor()
##CRIAR DATABASE
#comando = "CREATE DATABASE projeto_BD"
#cursor.execute(f"{comando}")

#CRUD
##CREATE

#for i in range (len(coments.index)):
'''nome = "Alysson"
senha = "123"
telefone = 81255613
cidade = "Recife"
comando = f'INSERT INTO cadastro1 (nome, senha, telefone, cidade) VALUES ("{nome}", "{senha}", "{telefone}", "{cidade}")'
cursor.execute(comando)
conexao.commit() #edita o BD'''

##READ

comando = f'SELECT * FROM cadastro1,cadastro2'
cursor.execute(comando)
resultado = cursor.fetchall() #Ler banco de dados
#if resultado[i][0] == resultado[i][5] and 'Mary' == resultado[i][1] and senha == resultado[i][2]:
print(resultado[50])

##UPDATE

#id = 10
#nome = "Teste papi 2"
#comando = f'UPDATE fabricantes SET nome = "{nome}" WHERE id = {id}'
#cursor.execute(comando)
#conexao.commit() #edita o 

##DELETE
'''id = 10
comando = f'DELETE FROM cadastro1'
comando2 = f'DELETE FROM cadastro2'
cursor.execute(comando)
cursor.execute(comando2)
conexao.commit() #edita o BD'''

cursor.close()
conexao.close()