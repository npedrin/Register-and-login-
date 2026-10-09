import os
contas={
    "sophialinda": "sophia2010*"
}

def limpar_tela():
    '''Função para limpar a tela independente do sistema operacional'''
    sistema=os.name
    if sistema =="nt":
        os.system("cls")
    else:
        os.system("clear")


def registrar_logar():
    '''Input para decidir se vai registrar ou logar. '''
    opcao=int(input("""Deseja registrar ou logar:
(1: Registrar) 
(2: Login)
"""))
    if opcao==1:
        limpar_tela()
        print('Registrar')
        criar_conta()
    elif opcao==2:
        limpar_tela()
        print('Login')
        login()
        
def login(): 
    '''Ver por que essa porra esta repetindo mesmo depois de logar'''
    tentativas=0
    while tentativas<3:
        username=input('Usuário: ')
        password=input('Senha: ')
        if contas.get(username)==password:
            print('Logado!')
            input('Pressione qualquer tecla para prosseguir.')
            return

        print('''Usuário ou senha invalidos.
Tente novamente!''')
    
    limpar_tela()
    print('Você excedeu o limite de tentativas. ')

def criar_conta():
    '''Sistema de criar conta com usuário, senha e confirmar senha.
    Se chegar ate 3 tentativas e o usuário não colocar o c_password igual
    a senha, sistema para e nao efetua o registrar.'''
    contador_s=1
    user=input('Informe o seu nome de usuário: ')
    while contador_s<=3:
        password=input('Informe a sua senha: ')
        c_password=input('Confirmar senha: ')
        if c_password == password: 
            limpar_tela()
            print('Conta criada com sucesso!')
            contas[user]=password
            input('Pressione qualquer tecla para continuar.')
            main()
            break
        elif c_password!=password:
            print('A senha deve ser igual. ')
            contador_s+=1
            if contador_s>3:
                print('Você usou suas 3 tentativas!')
def mostrar_contas():
    for chave, valor in contas.items():
        print(f'''Username: {chave} 
Senha: {valor}''')
   

def main():
    registrar_logar()

if __name__ == "__main__":
    main()