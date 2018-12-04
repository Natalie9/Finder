#MENU DE CADASTRO

#VARIÁVEIS
	#CORES
amarelo = 0
verde = 0
vermelho = 0
azul = 0
	#TAMANHO
pequeno = 0
medio = 0
grande = 0
	#OBJETOS
livro = 0
rg = 0
cpf = 0
carteirinha = 0
agasalho = 0
oculos = 0

#DEFINIÇÕES
def cor():
	print("\n1. Amarelo")
	print("2. Verde")
	print("3. Vermelho")
	print("4. Azul")
	cor = input("\nEscolha uma cor: ")
	while cor == ('1' or '2' or '3' or '4'):
		if cor == ('1'):
			amarelo += 1
			break
		elif cor == ('2'):
			verde += 1
			break
		elif cor == ('3'):
			vermelho += 1
			break
		else:
			azul += 1
			break
	else:
		sub_categoria1 = input("\nDígito inválido! Favor escolher novamente: ")

def tamanho():
		print("\n1. Pequeno")
		print("2. Médio")
		print("3. Grande")
		tamanho = input("\nEscolha um tamanho: ")
		while tamanho == ('1' or '2' or '3'):
			if tamanho == ('1'):
				pequeno += 1
				break
			elif tamanho == ('2'):
				medio += 1
				break
			else:
				grande += 1
				break
		else:
			sub_categoria1 = input("\nDígito inválido! Favor escolher novamente: ")

def material_escolar():
		print("\n1. Caderno")
		print("2. Mochila")
		print("3. Estojo")
		print("4. Garrafa")
		print("5. Livro")
		sub_categoria1 = input("\nEscolha um objeto: ")
		while sub_categoria1 == ('1' or '2' or '3' or '4' or '5'):
			if sub_categoria1 == ('1'):
				cor()
			elif sub_categoria1 == ('2'):
				cor()
				tamanho()
			elif sub_categoria1 == ('3'):
				cor()
				tamanho()
			elif sub_categoria1 == ('4'):
				cor()
			else: 
				livro +=1
				break
		else:
			sub_categoria1 = input("\nDígito inválido! Favor escolher novamente: ")

def documentos():
		print("\n1. RG")
		print("2. CPF")
		print("3. Cartão de crédito/débito")
		print("4. Carteirinha de ônibus/biblioteca")
		sub_categoria2 = input("\nEscolha uma categoria: ")
		while sub_categoria2 == ('1' or '2' or '3' or '4'):
			if sub_categoria2 == ('1'):
				rg += 1
				break
			elif sub_categoria2 == ('2'):
				cpf += 1
				break
			elif sub_categoria2 == ('3'):
				cartao += 1
				break
			else:
				carteirinha += 1
				break
		else:
			sub_categoria2 = input("\nDígito inválido! Favor escolher novamente: ")	

def itens_pessoais():
		print("\n1. Agasalho/moletom")
		print("2. Óculos")
		sub_categoria3 = input("\nEscolha uma categoria: ")
		while sub_categoria3 == ('1' or '2'):
			if sub_categoria3 == ('1'):
				agasalho += 1 
				break
			else:
				oculos += 1
				break
		else:
			sub_categoria3 = input("\nDígito inválido! Favor escolher novamente: ")

def cadastro_material():
	print("CATEGORIAS:\n")
	print("1. MATERIAL ESCOLAR")
	print("2. DOCUMENTOS")
	print("3. ITENS PESSOAIS")
	categoria = input("\nEscolha uma categoria: ")
	while categoria == ('1' or '2' or '3'):
		if categoria == ('1'):
			material_escolar()
		elif opcao == ('2'):
			documentos()
		else:
			itens_pessoais()
	else:
		opcao = input("\nDígito inválido! Favor escolher novamente: ")

cadastro_material()