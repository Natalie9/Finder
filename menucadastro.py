#MENU DE CADASTRO

#Variáveis definidas em cada função local para não dar erro. 

#DEFINIÇÕES
def cor():
	amarelo = 0
	verde = 0
	vermelho = 0
	azul = 0
	print("\n1. Amarelo")
	print("2. Verde")
	print("3. Vermelho")
	print("4. Azul")
	cor = input("\nEscolha uma cor: ")
	while (cor != '1') and (cor != '2') and (cor != '3') and (cor != '4'):
		cor = input("\nDígito inválido! Favor escolher novamente: ")
	if cor == ('1'):
		amarelo += 1
	if cor == ('2'):
		verde += 1		
	if cor == ('3'):
		vermelho += 1
	if cor == ('4'):
		azul += 1

def tamanho():
	pequeno = 0
	medio = 0
	grande = 0
	print("\n1. Pequeno")
	print("2. Médio")
	print("3. Grande")
	tamanho = input("\nEscolha um tamanho: ")
	while (tamanho != '1') and (tamanho !='2') and (tamanho != '3'):
		tamanho = input("\nDígito inválido! Favor escolher novamente: ")
	if tamanho == ('1'):
		pequeno += 1
	if tamanho == ('2'):
		medio += 1
	if tamanho == ('3'):
		grande += 1

def material_escolar():
	livro = 0
	print("\n1. Caderno")
	print("2. Mochila")
	print("3. Estojo")
	print("4. Garrafa")
	print("5. Livro")
	sub_categoria1 = input("\nEscolha um objeto: ")
	while (sub_categoria1 != '1') and (sub_categoria1 != '2') and (sub_categoria1 != '3') and (sub_categoria1 != '4') and (sub_categoria1 != '5'):
		sub_categoria1 = input("\nDígito inválido! Favor escolher novamente: ")
	if sub_categoria1 == ('1'):
		cor()
	if sub_categoria1 == ('2'):
		cor()
		tamanho()
	if sub_categoria1 == ('3'):
		cor()
		tamanho()
	if sub_categoria1 == ('4'):
		cor()
	if sub_categoria1 == ('5'): 
		livro +=1

def documentos():
	rg = 0
	cpf = 0
	cartao = 0
	carteirinha = 0
	print("\n1. RG")
	print("2. CPF")
	print("3. Cartão de crédito/débito")
	print("4. Carteirinha de ônibus/biblioteca")
	sub_categoria2 = input("\nEscolha uma categoria: ")
	while sub_categoria2 != ('1' ) and (sub_categoria2 != '2') and (sub_categoria2 != '3') and (sub_categoria2 != '4'):
		sub_categoria2 = input("\nDígito inválido! Favor escolher novamente: ")
	if sub_categoria2 == ('1'):
		rg += 1
	if sub_categoria2 == ('2'):
		cpf += 1
	if sub_categoria2 == ('3'):
		cartao += 1
	if sub_categoria2 == ('4'):
		carteirinha += 1

def itens_pessoais():
	agasalho = 0
	oculos = 0
	print("\n1. Agasalho/moletom")
	print("2. Óculos")
	sub_categoria3 = input("\nEscolha uma categoria: ")
	while (sub_categoria3 != '1') and (sub_categoria3 != '2'):
		sub_categoria3 = input("\nDígito inválido! Favor escolher novamente: ")
	if sub_categoria3 == ('1'):
		agasalho += 1 
	if sub_categoria3 == ('2'):
		oculos += 1

def cadastro_material():
	print("CATEGORIAS:\n")
	print("1. MATERIAL ESCOLAR")
	print("2. DOCUMENTOS")
	print("3. ITENS PESSOAIS")
	categoria = input("\nEscolha uma categoria: ")
	while (categoria != '1') and (categoria != '2') and (categoria != '3'):
		categoria = input("\nDígito inválido! Favor escolher novamente: ")
	if categoria == ('1'):
		material_escolar()
	if categoria == ('2'):
		documentos()
	if categoria == ('3'):
		itens_pessoais()

cadastro_material()