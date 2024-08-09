
# dicionario = {'vinho':540,'cerveja':320, 'coca':642, 'pepsi':100}

# transformar em lista de tuplas
# list = [(x, y) for x, y in dict.items()]
# ou
# list = zip(dict.keys(), dict.values())

# transformar em tupla
# tupla = list(dicionario.items())

# transformar em lista
# list = list(dicionario.items())

# para separar em 'lista' de chaves ou valores
# chaves = vendas_tecnologia.keys()
# valores = vendas_tecnologia.values()

# - Dicionário com valor padrão:
# dicionario = dict.fromkeys(lista_chaves, valor_padrao)

# - Dicionário a partir de listas de tuplas:
# dicionario = dict(lista_tuplas) #ou dict(zip(lista_tuplas))

# acessar chave e valor dentro de for
# for chave in vendas_tecnologia:
#      print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

# EXERCICIOS

# niveis_co2 = {
#     'AC': [325,405,429,486,402],
#     'AL': [492,495,310,407,388],
#     'AP': [507,503,368,338,400],
#     'AM': [429,456,352,377,363],
#     'BA': [321,508,372,490,412],
#     'CE': [424,328,425,516,480],
#     'ES': [449,506,461,337,336],
#     'GO': [425,460,385,485,460],
#     'MA': [361,310,344,425,490],
#     'MT': [358,402,425,386,379],
# }
# media = 425
# for item in niveis_co2: 
#     if sum(niveis_co2[item])/5 > media:  #trabalha-se acionando o dicionario e depois a variavel
#         print('O Estado de {} está em perigo'.format(item))


# EXERCICIO 2

# produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
# vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
# vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

# vendas = list(zip(vendas2019, vendas2020))
# vendas_produtos = dict(zip(produtos, vendas))
# print(vendas_produtos)