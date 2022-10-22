#Variaveis no python são um pouco mais simples de ser feitas
#Não posso iniciar uma variavel com números

nome= "Reginaldo Alves da Silva"
idade = 36
altura= 1.76
e_maior = idade > 18
peso = 96.00

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade:', e_maior)
print("Peso:", peso)

#Exercício proposto, calcular o IMC#

print(f"{nome} tem {idade} anos, e seu IMC é de {peso/(altura**2):,.2f}")

