#Cria um dicionario para os usuários
usuarios = {}
#Este código é usado para cadastrar o usuário no sistema
def cadastrar_usuario():
    nome = input("Digite o nome de usuário para o cadastro: ")
    if nome in usuarios:
        print("Usuario já existente!")

    else:
        senha = input("Digite a senha: ")
        usuarios[nome] = senha
        print("Usuario cadastrado!")
#Este entra no login 
def fazer_login():
    nome = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    if nome in usuarios and usuarios[nome] == senha:
        print("Login feito com sucesso. {}!".format(nome))

    else:
        print("Usuario ou senha incorretos.")
#Apaga o usuário do sistema, muito eficaz para aqueles que saem da empresa
def apagar_usuario():
    nome = input("Digite o nome de usuário que irá apagar: ")
    if nome in usuarios:
        senha = input("Digite sua senha para concluir: ")
        if usuarios[nome] == senha:
            del usuarios[nome]
            print(f"Usuario '{nome}' apagado com sucesso.")
        
        else: 
            print("Senha incorreta. Não foi possível apagar o usuário.")
    else:
        print("Usuário não encontrado. Verifique o login novamente.")

#sistema de menu, para cada etapa do sistema acima
while True:
    print("Menu")
    print("1-Cadastrar Usuário")
    print("2-Fazer login")
    print("3-Apagar usuário")
    print("4-Sair")

    opção = input("Escolha uma opção: ")

    if opção == "1":
        cadastrar_usuario()

    elif opção == "2":
        fazer_login()

    elif opção == "3":
        apagar_usuario()

    elif opção == "4":
        print("Saindo.")
        break
    else:
        print("Opção inválida.")


     