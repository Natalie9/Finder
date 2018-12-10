import getpass
import Cadastro 
import Busca


def teste():
    print(2+2)

def cadastrar():    
    print('Cadastro de novo usuário: ')
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    senha = getpass.getpass("Digite sua senha: ")
    senha2 = getpass.getpass('Digite sua senha novamente: ')
    pontuacao = 0

    while senha!= senha2:
        print ('Senhas não compatíveis, por favor, digite sua senha novamente')
        senha = getpass.getpass("Digite sua senha: ")
        senha2 = getpass.getpass('Digite sua senha novamente: ')

   
    arq = open('cadastro.txt', 'a')
    texto = email+"/"+senha+"/"+nome+"/"+telefone + "/" + str(pontuacao)+"\n"
    arq.writelines(texto)
    arq.close()
    print('\n\t\tCadastro realizado com sucesso! \n')

def logar():
    aut_email= input('Email: ')
    aut_senha= getpass.getpass('\nSenha: ')

    ref_arquivo = open("cadastro.txt","r")
    for linha in ref_arquivo:
        valores = linha.split("/")

    if((aut_email==valores[0]) and (aut_senha==valores[1])):
        print('\t\tAcesso liberado!!')
        ref_arquivo.close()
        op = input("O que deseja fazer? \n 1 - Cadastrar objeto encontrado \n 2 - Procurar objeto perdido \n")
        while op!='1' and op!='2': 
            print("Opção inválida!\n")
            op = input("O que deseja fazer? \n 1 - Cadastrar objeto encontrado \n 2 - Procurar objeto perdido \n")
        if op=='1':
            Cadastro.cadastrarObjeto()
        if op=='2':
            Busca.buscarObjeto()
    else:
        print('Dados incorretos, favor, tentar novamente')
        ref_arquivo.close()
        logar()
    
opcao = input('1 - Cadastrar novo usuário \n2 - Fazer login \n')
while (opcao != "1") and (opcao!="2"):
    opcao = input('Opção inválida! \n \n 1 - Cadastrar novo usuário \n2 - Fazer login \n')
if(opcao=='1'):
    cadastrar()
if(opcao=='2'):
    logar()
