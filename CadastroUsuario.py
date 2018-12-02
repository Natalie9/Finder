

def teste():
    print('Isso foi um teste')

def cadastrar():    
    print('Cadastro de novo usuário: ')
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    senha2 = input('Digite sua senha novamente: ')

    while senha!= senha2:
        print ('Senhas não compatíveis, por favor, digite sua senha novamente')
        senha = input('Digite sua senha: ')
        senha2 = input('Digite sua senha novamente: ')

   
    arq = open('cadastro.txt', 'w')
    texto = email+"/"+senha+"/"+nome+"/"+telefone
    arq.write(texto)
    arq.close()

    
    ref_arquivo = open("cadastro.txt","r")
    for linha in ref_arquivo:
        valores = linha.split("/")
        print('\n\t\tCadastro realizado com sucesso! \n', '\n Email: ', valores[0], ' - Senha: ', valores[1], '\n Nome: ', valores[2], 'Telefone: ', valores[3] )

    ref_arquivo.close()

def logar():
    aut_email= input('Email: ')
    aut_senha= input('\nSenha: ')

    ref_arquivo = open("cadastro.txt","r")
    for linha in ref_arquivo:
        valores = linha.split("/")
    if((aut_email==valores[0]) and (aut_senha==valores[1])):
        print('\t\tAcesso liberado!!')
        ref_arquivo.close()
    else:
        print('Dados incorretos, favor, tentar novamente')
        ref_arquivo.close()
        logar()
    

opcao = input('1 - Cadastrar novo usuário \n2 - Fazer login \n')
if(opcao=='1'):
    cadastrar()
if(opcao=='2'):
    logar()