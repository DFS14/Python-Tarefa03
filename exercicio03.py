#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Percentual de desconto



valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual de desconto: "))


valor_final = valor - (valor * (desconto / 100))
print("O valor final após o desconto é", valor_final)
