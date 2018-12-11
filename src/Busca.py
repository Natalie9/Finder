import Menu
cont=0 

def buscarDadosUsuario(id):
        ref_arquivo = open('cadastro.txt',"r")
        for linha in ref_arquivo:
            valores1 = linha.split("-")
            valores = valores1[1].split("/")
            if(valores1[0]==id):                
                print("Nome: " +valores[2]+ " Email:" + valores[0] + " Telefone: " +valores[3])
def buscarObjeto(id):
    global cont 
    objetoBuscado= Menu.objetos(id)
    

    ref_arquivo = open('objetos.txt',"r")
    for linha in ref_arquivo:
        valores = objetoBuscado.split("-")
        valores1 = linha.split("-")
        if((valores1[1]==valores[1])):
            usu=valores1[0]
            cont +=1
            buscarDadosUsuario(usu)
            

    print("\t\tExistem " + str(cont) + " objetos que cosrrespondem ao buscado!")
    ref_arquivo.close()
 
    