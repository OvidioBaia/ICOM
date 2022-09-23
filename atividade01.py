import numpy as np
###### 1-questão #####

# total_estoque = int(input("Total de mercadoria em estoque: "))
# total_valor_mercadoria = 0.0
# media_valor_mercadoria = 0.0
# for i in range(total_estoque):
#     valor_mercadoria = int(input("Valor da mercadoria: "))
#     total_valor_mercadoria+=valor_mercadoria

# media_valor_mercadoria = total_valor_mercadoria / total_estoque
# print("Valor total em estoque é: %3.2f" % (total_valor_mercadoria) )
# print("Media de valor da mercadoria: %3.2f" % (media_valor_mercadoria))

####### 2-questão ######

# dias_do_ano = 6
# temperaturas = []
# maior_temperatura = 0.0
# menor_temperatura = 0.0
# media_temperatura = 0.0
# dias_temperatura_menor_media = 0
# for i in range(dias_do_ano):
#     media_temperatura = float(input("Media de temperatura do dia  %1d:  " %(i+1)))
#     temperaturas.append(media_temperatura)

# maior_temperatura = max(temperaturas)
# menor_temperatura = min(temperaturas)
# media_temperatura = np.mean(temperaturas)
# for i in temperaturas:
#     if i < media_temperatura:
#         dias_temperatura_menor_media+=1

# print("Menor temperatura: %2.2f" % (menor_temperatura))
# print("Maior temperatura: %2.2f" % (maior_temperatura))
# print("Media temperatura: %2.2f" % (media_temperatura))
# print("Dia com temperaturas menor quue a media: %2d" % (dias_temperatura_menor_media))

##### 3-questão ###############

# quantidade_nomes = 5
# nomes = []

# for i in range(quantidade_nomes):
#     nome = input("Digite o nome de uma pessoa: ")
#     nomes.append(nome)

# nome_pesquisa = input("Digite o nome que deseja pesquisar: ")

# if nome_pesquisa in nomes:
#     print("ACHEI")
# else:
#     print("NÂO ACHEI")

##### 4-questão #####

# codigo = input("Digite o codigo do empregado: ")
# ano_de_nascimento = int(input("Digite o ano de nascimento: "))
# ano_ingresso_empresa = int(input("Digite o ano de engresso na empresa: "))

# idade = 2022 - ano_de_nascimento
# tempo_de_trabalho = 2022 - ano_ingresso_empresa
# isValid_idade = idade >= 65
# isValid_tempo_trabalho = tempo_de_trabalho >= 30 
# isValid_tempo_trabalho_e_idade = (idade >= 60) and (tempo_de_trabalho >= 25)

# def showInformation(mensagem):
#     print("Idade: %2d" % (idade))
#     print("Tempo de trabalho: %2d" % (tempo_de_trabalho))
#     print(mensagem)

# if (isValid_idade) or (isValid_tempo_trabalho) or (isValid_tempo_trabalho_e_idade):
#    showInformation("REQUERER APOSENTADORIA")
# else:
#     showInformation("NÃO REQUERER APOSENTADORIA")
    