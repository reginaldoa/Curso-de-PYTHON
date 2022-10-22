#Operadores relacionais
# == > >= < <= !=

num_1 = 2 #int
num_2 = 2 #int

expressao = (num_1 != num_2)
print(expressao)

nome = input('Qual o seu nome?')
idade = int(input("Qual a sua idade?"))


#Limite para pegar empréstimo
idade_menor = 20 #jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f" {nome}, Você pode pegar empréstimos")
else:
    print(f"{nome}, você não pode pegar o empréstimo")
