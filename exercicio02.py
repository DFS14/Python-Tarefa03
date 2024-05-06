#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Informa o IMC de pessoa

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
print("Seu IMC é", imc)