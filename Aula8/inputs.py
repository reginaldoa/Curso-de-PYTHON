# inputs = entrada de dados
#Tudo o que for digitado no input, é considerado string, mesmo que seja um número.


nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? " )

ano_nascimento= 2022 - int(idade)

print()
print(f"O usuário digitou: {nome}, o mesmo tem {idade} anos ")
print()
print(f"{nome}  nasceu em {ano_nascimento}")


#Outro exemplo

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro numero: '))

print(numero_1 + numero_2)