
""" importa o sistema de banco de dados """
import sqlite3
import random
import os 

""" primeira senha do sistema """
MASTER_PASSWORD = "1212"

""" Caso a senha esteja errada """
SENHA = input("Insira seu login:")
if SENHA != (MASTER_PASSWORD):
    print("SENHA INVALIDA!")
    exit() 
    
""" Cria e conecta um banco de dados no sistema DB """
CONN = sqlite3.connect('app1.db')

CURSOR = CONN.cursor()
""" Cria uma tabela no banco de dados se ela nao existir"""
CURSOR.execute('''
    create table if not exists users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    );
    ''')
""" funcao MENU com as opcoes do menu """
def menu():
    print("****************")
    print("a: inserir nova senha")
    print("b: Listar servicos salvos")
    print("c: Recuperar senha")
    print("d: Sair")
    print("****************")
""" Cria funcao para receber e passar o parametro service """
def receber_senha(service):
    pass
""" Funcao para pegar informacoes e passar como dados para o BD """
def inserir_password(service, username, password):
    CURSOR.execute("""
                   INSERT INTO users (service, username, password)
                   VALUES ("{service}", "{username}", "{password}")
                   """)
    CONN.commit()
""" Funcao para mostrar os servicos que contem as senhas salvas """
def mostrar_locais():
    CURSOR.execute("""
                   Select service FROM users;
                    """)
    for service in CURSOR.fetchall():
        print(service)      
""" estrutura de repeticao para acrescentar parametro de quebra """
while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in["a", "b", "c", "d"]:
        print("Opcao invalida")
        continue
    
    if op == "d":
         break
     
    if op == "a":
        service = input('qual o nome do servico?')
        username = input('qual o nome de usuario?') 
        password = input('qual a senha?')    
        inserir_password(service, username, password)
        
    if op == "b":
        mostrar_locais()
        
CONN.close()



