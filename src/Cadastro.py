import Menu

def cadastrarObjeto():
    arq = open('objetos.txt', 'a')
    texto = Menu.objetos()
    arq.writelines(texto)
    arq.close()
    print('\n\t\tCadastro realizado com sucesso! \n')
    
   




