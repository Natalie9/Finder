import Menu
cont =0 
def buscarObjeto():
    global cont 
    objetoBuscado= Menu.objetos()
    

    ref_arquivo = open('objetos.txt',"r")
    for linha in ref_arquivo:
        valores = linha
        if((objetoBuscado==linha)):
            cont +=1
    print("\t\tExistem " + str(cont) + " objetos que cosrrespondem ao buscado!")
    ref_arquivo.close()
 
    