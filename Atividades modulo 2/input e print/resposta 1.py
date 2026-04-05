#Lê o valor do comprimento do terreno (inteiro)
comprimento = int(input('Digite o coprimento do terreno: '))
#Lê o valor da largura do terreno (inteiro)
largura = int(input('Digite a largura do terreno: '))
#Lê o preço por metro quadrado (ponto flutuante)
preço_m2 = float(input('Digite o preço do metro quadrado: '))
#Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura
#Calcula o preço total do terreno
preço_total = preço_m2 * area_m2
#Exibe o resultado formatado conforme o exemplo
print(f'O terreno possui {area_m2}m2 e custa R${preço_total:,.2f}')


