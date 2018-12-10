tipo = 0
tipo_mat = 0
proc_cor = 0
proc_tamanho = 0
class_doc = 0
item_pess = 0
proc_size = 0



def fun_size():
    global proc_size
    print("\nQual o tamanho da vestimenta? ")
    print("1. 12")
    print("2. 13")
    print("3. P")
    print("4. M")
    print("5. G")
    print("6. GG")
    proc_size = input("Digite o número da vestimenta: ")
    while (proc_size != '1') and (proc_size != '2') and (proc_size != '3') and (proc_size != '4') and (proc_size != '5') and (proc_size != '6'):
        proc_size = input("ERRO!! Digite um número de 1 à 6.\nTente Novamente: ")

def fun_cor():
    global proc_cor
    print("\nQual a cor do objeto? \n")
    print("1. Amarelo, ou semelhante")
    print("2. Verde, ou semelhante")
    print("3. Vermelho, ou semelhante")
    print("4. Azul, ou semelhante")
    proc_cor = input("\nO número que representa a cor do objeto é? ")
    while (proc_cor != '1') and (proc_cor != '2') and (proc_cor != '3') and (proc_cor != '4'):
        proc_cor = input("ERRO!! Digite um número de 1 à 4.\nTente Novamente: ")

def fun_tamanho():
    global proc_tamanho
    print("\nQual o tamanho do objeto?\n")
    print("1. Pequeno")
    print("2. Médio")
    print("3. Grande")
    proc_tamanho = input("\nO número que representa o tamanho do objeto é? ")
    while (proc_tamanho != '1') and (proc_tamanho != '2') and (proc_tamanho != '3'):
        proc_tamanho = input("ERRO!! Digite um número de 1 à 3.\nTente Novamente: ")

def proc_item_pessoal():
    global item_pess
    global proc_size
    global proc_cor
    print("\nO que é? \n")
    print("1. Agasalho/Moleton")
    print("2. Óculos")
    item_pess = input("\n Digite o número referente: ")
    while (item_pess != '1') and (item_pess != '2'):
        item_pess = input("ERRO!! Digite um número de 1 à 2.\nTente Novamente: ")
    if item_pess == ('1'):
        fun_cor()
        fun_size()
    if item_pess == ('2'):
        fun_cor()

def proc_doc():
    global class_doc
    print("\nQual a classe do documento? \n")
    print("1. RG")
    print("2. CPF")
    print("3. Cartão de Crédito/Débito")
    print("4. Carteirinha de Ônibus")
    print("5. Carteirinha da Biblioteca")
    class_doc = input("\nEscolha uma das opções: ")
    while (class_doc != '1') and (class_doc != '2') and (class_doc != '3') and (class_doc != '4') and (class_doc != '5'):
        class_doc = input("ERRO!! Digite um número de 1 à 5.\nTente Novamente: ")

def proc_materiais_esco():
    global tipo_mat
    global proc_cor
    global proc_tamanho
    print("Escolha qual tipo de material escolar\n")
    print("1. Caderno")
    print("2. Mochila")
    print("3. Estojo")
    print("4. Garrafa")
    print("5. Livro")
    tipo_mat = input("\nDigite o número de 1 à 5 que representa o tipo de material escolar ")
    while (tipo_mat != '1') and (tipo_mat != '2') and (tipo_mat != '3') and (tipo_mat != '4') and (tipo_mat != '5'):
        tipo_mat = input("ERRO!! Digite um número de 1 à 5.\nTente Novamente: ")
    if tipo_mat == ('1'):
        fun_cor()
    if tipo_mat == ('2'):
        fun_tamanho()
        fun_cor()
    if tipo_mat == ('3'):
        fun_tamanho()
        fun_cor()
    if tipo_mat == ('4'):
        fun_cor()

def tipos_objetos():
    global tipo
    print("Escolha o tipo de objeto:\n")
    print("1. Materiais Escolares")
    print("2. Documentos")
    print("3. Itens Pessoais")
    tipo = input("\nEscolha um tipo: ")
    while (tipo != '1') and (tipo != '2') and (tipo != '3'):
        tipo = input("\nERRO!! Escolha entre 1,2 e 3.\nTente Novamente: ")
    if tipo == ('1'):
        proc_materiais_esco()
    if tipo == ('2'):
        proc_doc()
    if tipo == ('3'):
        proc_item_pessoal()

def objetos():
    global tipo
    global tipo_mat
    global proc_cor
    global proc_tamanho
    global class_doc
    global item_pess
    global proc_size
    tipos_objetos()
    if tipo == ('1'):
        return tipo +"/"+ tipo_mat +"/"+ proc_cor +"/"+proc_tamanho+"\n"
    if tipo == ('2'):
        return tipo+"/"+class_doc+"\n"
    if tipo == ('3'):
        return tipo+"/"+item_pess+"/"+proc_size+"/"+proc_cor+"\n"
