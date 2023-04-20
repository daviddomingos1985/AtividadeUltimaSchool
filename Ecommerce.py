"""Trecho de código responsável pelo cadastro de um novo produto"""
def cadastrar_produto(estoque):
  #Obtém as informações do produto atual (Leitura)
  codigo = int(input("Digite o codigo do produto: "))
  categoria = input("Digite a categoria do produto: ")
  nome = input("Digite o nome do produto: ")
  descricao = input("Digite uma descrição para o produto: ")
  preco = float(input("Digite o preco do produto: "))

  #Adiciona um produto no estoque (Cadastro)
  produto = {"codigo": codigo, "produto": nome, "info": descricao, "preco": preco}
  if categoria not in estoque:
    estoque[categoria] = []
    estoque[categoria].append(produto)
  else:
    estoque[categoria].append(produto)
  
  #Retorna o estoque atualizado
  return estoque

#Mostrando informações do estoque
def mostrar_produto(produto):
  print("------------------------------------------")
  print("--------- Informações do produto ---------")
  print("------------------------------------------")
  print(f"Código: {produto['codigo']}")
  print(f"Produto: {produto['produto']}")
  print(f"Descrição: {produto['info']}")
  print(f"Preço: {produto['preco']}")
  print("")

#Apresenta TODOS os produtos cadastrados
def mostra_produtos(estoque):
  for categoria in estoque:
    for produto in estoque[categoria]:
      mostrar_produto(produto)

#Apresenta os produtos cadastrados com preço inferior ao limite estabelecido
def mostra_produtos_preco(estoque, preco):
  for categoria in estoque:
    for produto in estoque[categoria]:
      if produto["preco"] <= preco:
        mostrar_produto(produto)

#Dados brutos para não precisar digitar
estoque = {"Eletronicos": [{
                              'codigo': 2578,
                              'produto': "Televisão Smart 70'",
                              'info': 'Televisão smart de 70 polegadas, para você assistir a filmes e séries com o maior que a tecnologia pode oferecer. Aproveite!',
                              'preco': 4799.99},
                           {
                              'codigo': 2749,
                              'produto': 'Iphone 14 Pro Max 256GB',
                              'info': 'Iphone 14 Pro Max 256GB de armazenamento interno, acompanha carregador, capinha e película de vidro 3D. Entrega Grátis.',
                              'preco': 9499.99},
                           {
                              'codigo': 1478,
                              'produto': 'Smartphone Samsung Galaxy S23 Ultra',
                              'info': 'Smartphone Galaxy S23 Ultra 512GB de armazenamento interno, 16GB de memória RAM. Câmera de 200MP e Zoom de 10X.',
                              'preco': 6799.99},
                           {
                              'codigo': 3658,
                              'produto': 'Notebook Dell Inspiron',
                              'info': 'Notebook Dell Inspiron: 32GB de RAM, 1TB SSD, 4GB Placa de Vídeo Dedicada, Processador Intel Core i9.',
                              'preco': 12499.99}],
           "Livros":      [{
                              'codigo': 6987,
                              'produto': 'Livro O Senhor dos Anéis (Volume único)',
                              'info': 'Livro da obra literária O senhor dos anéis, de J.R.R.Tolkien. Aproveite esta oferta exclusiva!',
                              'preco': 129.0},
                           ]
          }

while True:
  print("-----------------------------------------------\n")
  print("Seja bem-vindo à DAVID Store, sua loja virtual!\n")
  print("-----------------------------------------------\n"
        "O que você deseja fazer:\n"
        "1) Cadastrar produto\n"
        "2) Mostrar produtos\n"
        "3) Filtrar produtos por preço\n"
        "0) Sair do programa\n"
        "-----------------------------------------------\n")
 
  opcao = int(input("Digite a opção desejada: "))
  
  #Cadastrar um produto
  if opcao == 1:
    estoque = cadastrar_produto(estoque)
  
  #Mostrar produtos
  elif opcao == 2:
    mostra_produtos(estoque)
  
  #Mostrar produtos dado um limite de preço
  elif opcao == 3:
    preco_desejado = float(input("Digite o limite máximo de preço a ser buscado: "))
    mostra_produtos_preco(estoque, preco_desejado)
  
  #Finalizar programa
  elif opcao == 0:
    print("Volte sempre! Agradecemos a preferência!\n")
    break
  
  #Verifica se a opção passada é inválida
  else:
    print("Opcao inválida!")