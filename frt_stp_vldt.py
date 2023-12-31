import json # útil para lidar com a base de usuário (arquivo .json)
import os
from time import sleep
import cryptocode

# retorna o id e o password lidos via terminal
def get_id_password():
    id = input("Digite o seu ID: ").strip()
    password = cryptocode.encrypt(input("Digite sua senha: ").strip(), "py")

    return id, password

# se o id e o password estão cadastrados: retorna o nome do usuário. Caso contrário, retorna None
def id_password_test(user_list, id, password):
    for i in range(len(user_list)):
        if id == user_list[i]['id']:
            if cryptocode.decrypt(password, "py") == cryptocode.decrypt(user_list[i]['password'], "py"):
                return True
    return False

def id_password_validation(max_attempts=1, data_base=None):

    if data_base == None:
        print("Banco de dados não encontrado")
        exit(1)

    user_list = data_base['users']

    tentativas = 0
    while True:
        tentativas += 1

        # limpa o terminal, só para melhorar a estética
        os.system('cls' if os.name == 'nt' else 'clear')
    
        id, password = get_id_password()

        if id_password_test(user_list, id, password):
            return id
        else:
            print("Nome de usuário e/ou senha incorretos")

        # se tentou por cinco vezes, retorna False
        if tentativas == max_attempts:
            return None
        
        sleep(1.8)