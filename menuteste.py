#MENU INICIAL
def menu_inicial():
	print("*** BEM VINDO ***")
	print("\n1. Cadastro de Material")
	print("\n2. Busca de Material")
	opcao = input("\n Escolha uma opção: ")
	while (opcao != '1') and (opcao != '2'):
		opcao = input('\nDígito inválido! Favor escolher novamente: ')
	if opcao == ('1'):
		cadastro_material()
	if opcao == ('2'):
		busca_material()

#MENU DE CADASTRO

#Variáveis definidas em cada função local para não dar erro. 

#DEFINIÇÕES
def cor_caderno():
	caderno_amarelo = 0
	caderno_verde = 0
	caderno_vermelho = 0
	caderno_azul = 0
	print("\n1. Amarelo")
	print("2. Verde")
	print("3. Vermelho")
	print("4. Azul")
	cor = input("\nEscolha uma cor: ")
	while (cor != '1') and (cor != '2') and (cor != '3') and (cor != '4'):
		cor = input("\nDígito inválido! Favor escolher novamente: ")
	if cor == ('1'):
		caderno_amarelo += 1
	if cor == ('2'):
		caderno_verde += 1		
	if cor == ('3'):
		caderno_vermelho += 1
	if cor == ('4'):
		caderno_azul += 1

def cor_mochila():
	mochila_amarela = 0
	mochila_verde = 0
	mochila_vermelha = 0
	mochila_azul = 0
	print("\n1. Amarelo")
	print("2. Verde")
	print("3. Vermelho")
	print("4. Azul")
	cor = input("\nEscolha uma cor: ")
	while (cor != '1') and (cor != '2') and (cor != '3') and (cor != '4'):
		cor = input("\nDígito inválido! Favor escolher novamente: ")
	if cor == ('1'):
		mochila_amarela += 1
	if cor == ('2'):
		mochila_verde += 1		
	if cor == ('3'):
		mochila_vermelha += 1
	if cor == ('4'):
		mochila_azul += 1

def tamanho_estojo():
	estojo_pequeno = 0
	estojo_medio = 0
	estojo_grande = 0
	print("\n1. Pequeno")
	print("2. Médio")
	print("3. Grande")
	tamanho = input("\nEscolha um tamanho: ")
	while (tamanho != '1') and (tamanho !='2') and (tamanho != '3'):
		tamanho = input("\nDígito inválido! Favor escolher novamente: ")
	if tamanho == ('1'):
		estojo_pequeno += 1
	if tamanho == ('2'):
		estojo_medio += 1
	if tamanho == ('3'):
		estojo_grande += 1

def material_escolar():
	caderno = 0
	mochila = 0
	estojo = 0
	garrafa = 0
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
		caderno += 1
		cor_caderno()
	if sub_categoria1 == ('2'):
		mochila += 1
		cor_mochila()
	if sub_categoria1 == ('3'):
		estojo += 1
		tamanho_estojo()
	if sub_categoria1 == ('4'):
		garrafa += 1
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
	print("\nCATEGORIAS:\n")
	print("1. MATERIAL ESCOLAR")
	print("2. DOCUMENTOS")
	print("3. ITENS PESSOAIS")
	print("4. INÍCIO")
	categoria = input("\nEscolha uma categoria: ")
	while (categoria != '1') and (categoria != '2') and (categoria != '3') and (categoria != '4'):
		categoria = input("\nDígito inválido! Favor escolher novamente: ")
	if categoria == ('1'):
		material_escolar()
	if categoria == ('2'):
		documentos()
	if categoria == ('3'):
		itens_pessoais()
	if categoria == ('4'):
		menu_inicial()

#MENU DE BUSCA DE MATERIAL
def null_objeto():
	print("\nDesculpe, não há nenhum objeto cadastrado nessa categoria.")
	print("1. Voltar ao menu inicial")
	print("2. Sair")
	opcao = input("\nEscolha uma opção: ")
	while (opcao != '1') and (opcao != '2'):
		opcao = input("\nDígito inválido! Favor escolher novamente: ")
	if opcao == '1':
		menu_inicial()
	if opcao == '2':
		pass #sair do programa

def caderno_busca():
	if caderno == 0:
		null_objeto()
	else:
		print("\n1. Amarelo")
		print("2. Verde")
		print("3. Vermelho")
		print("4. Azul")
		cor = input("\nEscolha uma cor: ")
		while (cor != '1') and (cor != '2') and (cor != '3') and (cor != '4'):
			cor = input("\nDígito inválido! Favor escolher novamente: ")
		if cor == ('1'):
			if caderno_amarelo == 0:
				null_objeto()
			else:
				print("Há %s caderno(s) amarelo(s) cadastrados." %caderno_amarelo)
		if cor == ('2'):
			if caderno_verde == 0:
				null_objeto()
			else:
				print("Há %s caderno(s) verde(s) cadastrados." %caderno_verde)	
		if cor == ('3'):
			if caderno_vermelho == 0:
				null_objeto()
			else:
				print("Há %s caderno(s) vermelho(s) cadastrados." %caderno_vermelho)
		if cor == ('4'):
			if caderno_azul == 0:
				null_objeto()
			else:
				print("Há %s caderno(s) azul(s) cadastrados." %caderno_azul)

def mochila_busca():
	if mochila == 0:
		null_objeto()
	else: 
		#COR
		print("\n1. Amarelo")
		print("2. Verde")
		print("3. Vermelho")
		print("4. Azul")
		cor = input("\nEscolha uma cor: ")
		while (cor != '1') and (cor != '2') and (cor != '3') and (cor != '4'):
			cor = input("\nDígito inválido! Favor escolher novamente: ")
		if cor == ('1'):
			if mochila_amarela == 0:
				null_objeto()
			else:
				print("Há %s mochila(s) amarela(s) cadastradas." %mochila_amarela)
		if cor == ('2'):
			if mochila_verde == 0:
				null_objeto()
			else:
				print("Há %s mochila(s) verde(s) cadastradas." %mochila_verde)		
		if cor == ('3'):
			if mochila_vermelha == 0:
				null_objeto()
			else:
				print("Há %s mochila(s) vermelha(s) cadastradas." %mochila_vermelha)
		if cor == ('4'):
			if mochila_azul == 0:
				null_objeto()
			else:
				print("Há %s mochila(s) azul(s) cadastradas." %mochila_azul)

def estojo_busca():
	if estojo == 0:
		null_objeto()
	else:
		print("\n1. Pequeno")
		print("2. Médio")
		print("3. Grande")
		tamanho = input("\nEscolha um tamanho: ")
		while (tamanho != '1') and (tamanho !='2') and (tamanho != '3'):
			tamanho = input("\nDígito inválido! Favor escolher novamente: ")
		if tamanho == ('1'):
			if estojo_pequeno == 0:
				null_objeto()
			else:
				print("Há %s estojo(s) pequeno(s) cadastrados." %estojo_pequeno)
		if tamanho == ('2'):
			if estojo_medio == 0:
				null_objeto()
			else:
				print("Há %s estojo(s) medio(s) cadastrados." %estojo_medio)
		if tamanho == ('3'):
			if estojo_grande == 0:
					null_objeto()
			else:
				print("Há %s estojo(s) grande(s) cadastrados." %estojo_grande)

def material_escolar_busca():
	print("\n1. Caderno")
	print("2. Mochila")
	print("3. Estojo")
	print("4. Garrafa")
	print("5. Livro")
	sub_categoria1 = input("\nEscolha um objeto: ")
	while (sub_categoria1 != '1') and (sub_categoria1 != '2') and (sub_categoria1 != '3') and (sub_categoria1 != '4') and (sub_categoria1 != '5'):
		sub_categoria1 = input("\nDígito inválido! Favor escolher novamente: ")
	if sub_categoria1 == ('1'):
		caderno_busca()
	if sub_categoria1 == ('2'):
		mochila_busca()
	if sub_categoria1 == ('3'):
		estojo_busca()
	if sub_categoria1 == ('4'):
		garrafa
	if sub_categoria1 == ('5'): 
		livro

def documentos_busca():
	print("\n1. RG")
	print("2. CPF")
	print("3. Cartão de crédito/débito")
	print("4. Carteirinha de ônibus/biblioteca")
	sub_categoria2 = input("\nEscolha uma categoria: ")
	while sub_categoria2 != ('1' ) and (sub_categoria2 != '2') and (sub_categoria2 != '3') and (sub_categoria2 != '4'):
		sub_categoria2 = input("\nDígito inválido! Favor escolher novamente: ")
	if sub_categoria2 == ('1'):
		rg
	if sub_categoria2 == ('2'):
		cpf
	if sub_categoria2 == ('3'):
		cartao
	if sub_categoria2 == ('4'):
		carteirinha

def itens_pessoais_busca():
	print("\n1. Agasalho/moletom")
	print("2. Óculos")
	sub_categoria3 = input("\nEscolha uma categoria: ")
	while (sub_categoria3 != '1') and (sub_categoria3 != '2'):
		sub_categoria3 = input("\nDígito inválido! Favor escolher novamente: ")
	if sub_categoria3 == ('1'):
		agasalho
	if sub_categoria3 == ('2'):
		oculos

def busca_material():
	print("\nCATEGORIAS:\n")
	print("1. MATERIAL ESCOLAR")
	print("2. DOCUMENTOS")
	print("3. ITENS PESSOAIS")
	print("4. INÍCIO")
	categoria = input("\nEscolha uma categoria: ")
	while (categoria != '1') and (categoria != '2') and (categoria != '3') and (categoria != '4'):
		categoria = input("\nDígito inválido! Favor escolher novamente: ")
	if categoria == ('1'):
		material_escolar_busca()
	if categoria == ('2'):
		documentos_busca()
	if categoria == ('3'):
		itens_pessoais_busca()
	if categoria == ('4'):
		menu_inicial()
		
menu_inicial()