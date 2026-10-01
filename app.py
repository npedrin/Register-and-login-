import os
restaurantes=[]


def boas_vindas():
    print("IFOOD 2.0?")
#Opções disponiveis
def escolher_opcao():
    print("""
    1. Cadastrar Restaurante
    2. Listar Restaurantes.
    3. Ativar Restaurante")
    4. Sair
    """)

#Cadastrar novo restaurante
def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes. ")
    nome_do_restaurante=input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("Digite uma tecla para voltar ao menu principal.")
    main()

#Listar restaurantes
def listar_restaurantes():
    os.system("cls")
    print("Lista de restaurantes. ")
    for restaurante in restaurantes:
        print(f" - {restaurante}")
    input("Digite uma tecla para voltar ao menu principal.")
    main()

#Escolher opções
def opcoes():
    try:
        op_escolhida=int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {op_escolhida}")
        if op_escolhida==1:
            cadastrar_novo_restaurante()
        elif op_escolhida==2:
            listar_restaurantes()
        elif op_escolhida==3:
            print("Ativar Restaurante")
        elif op_escolhida==4:
            finalizar_app()
        else:
            print("Opção Inválida!")
    except:
        print("Opção Inválida!")
        input("Digite qualquer tecla.")
        main()

#opção 4 (Finalizando app)
def finalizar_app():
    os.system('cls')
    print("Encerrando programa")



def main():
    os.system("cls")
    boas_vindas()
    escolher_opcao()
    opcoes()

if __name__ == "__main__":
    main()
