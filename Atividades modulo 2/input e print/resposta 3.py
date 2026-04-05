nome1 = input("Digite o nome do produto: ")
preço1 = float(input("Digite o preço unitario do produto 1: "))
qtd1 = int(input("Digite a quantidade do produto 1: "))
total1 = preço1 * qtd1 
nome2 = input("Digite o nome do produto: ")
preço2 = float(input("Digite o preço unitario do produto 2: "))
qtd2 = int(input("Digite a quantidade do produto 2: "))
total2 = preço2 * qtd2
nome3 = input("Digite o nome do produto: ")
preço3 = float(input("Digite o preço unitario do produto: "))
qtd3 = int(input("Digite a quantidade do produto: "))
total3 = preço3 * qtd3
preço_total = total1 + total2 + total3
print (f"total: R${preço_total:,.2f}")


