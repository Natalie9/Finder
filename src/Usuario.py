import getpass
import Cadastro 
import Busca
id = 0; 

def teste():
    print(2+2)

def cadastrar():    
    global id
    print('Cadastro de novo usuário: ')
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    senha = getpass.getpass("Digite sua senha: ")
    senha2 = getpass.getpass('Digite sua senha novamente: ')
  

    while senha!= senha2:
        print ('Senhas não compatíveis, por favor, digite sua senha novamente')
        senha = getpass.getpass("Digite sua senha: ")
        senha2 = getpass.getpass('Digite sua senha novamente: ')

    ref_arquivo = open("cadastro.txt","r")
    
    for linha in ref_arquivo:
        id=id+1

        valores1 = linha.split("-")
        valores = valores1[1].split("/")
        
        if(email==valores[0]):
            print('\t\tEmail já cadastrado! Tente novamente')
            
            cadastrar()
    ref_arquivo.close()

    arq = open('cadastro.txt', 'a')
    texto = str(id)+"-"+email+"/"+senha+"/"+nome+"/"+telefone +"\n"
    arq.writelines(texto)
    arq.close()
    print('\n\t\tCadastro realizado com sucesso! \n')
    op = input("\t\tO que deseja fazer? \n\t 1 - Cadastrar objeto encontrado \n\t 2 - Procurar objeto \n")
    while op!='1' and op!='2': 
        print("Opção inválida!\n")
        op = input("\t\tO que deseja fazer? \n\t 1 - Cadastrar objeto encontrado \n\t 2 - Procurar objeto perdido \n")
    if op=='1':
        Cadastro.cadastrarObjeto(id)
    if op=='2':
        Busca.buscarObjeto(id)
    

def logar():
    aux=0
    global id

    aut_email= input('Email: ')
    aut_senha= getpass.getpass('\nSenha: ')

    ref_arquivo = open("cadastro.txt","r")
    for linha in ref_arquivo:
        valores1 = linha.split("-")
        valores = valores1[1].split("/")

        if((aut_email==valores[0]) and (aut_senha==valores[1])):
            aux=1
            print('\t\tAcesso liberado!!')
            
            op = input("\t\tO que deseja fazer? \n\t 1 - Cadastrar objeto encontrado \n\t 2 - Procurar objeto perdido \n")
            while op!='1' and op!='2': 
                print("Opção inválida!\n")
                op = input("\t\tO que deseja fazer? \n\t 1 - Cadastrar objeto encontrado \n\t 2 - Procurar objeto perdido \n")
            if op=='1':
                Cadastro.cadastrarObjeto(valores1[0])
            if op=='2':

                Busca.buscarObjeto(valores1[0])
        
    
    if(aux==0):
        print('Dados incorretos, favor, tentar novamente')
        ref_arquivo.close()
        logar()
    ref_arquivo.close()


print


print("\n\t\t\t##############################");
print("\n\t\t\t#                            #");
print("\n\t\t\t#           Finder           #");
print("\n\t\t\t#                            #");
print("\n\t\t\t#     ACHADOS E PERDIDOS     #");
print("\n\t\t\t#                            #");
print("\n\t\t\t#                            #");
print("\n\t\t\t##############################\n\n\n\n\n\n");

print("\t\tBem vindo ao Finder! Seu achados e perdidos virtual!\n \t\tO que deseja fazer?")
opcao = input('\t\t1 - Cadastrar novo usuário \n\t\t2 - Fazer login \n')
while (opcao != "1") and (opcao!="2"):
    opcao = input('Opção inválida! \n \n \t\t1 - Cadastrar novo usuário \n\t\t2 - Fazer login \n')
if(opcao=='1'):
    cadastrar()
if(opcao=='2'):
    logar()
