import Menu

def cadastrarObjeto(id):
    arq = open('objetos.txt', 'a')
    texto = Menu.objetos(id)
    arq.writelines(str(texto))
    arq.close()
    print('\n\t\tCadastro realizado com sucesso! \n')
    
   




