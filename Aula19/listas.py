""""
Listas em Python
Fatiamento
Append, insert, pop, del, clear, extend, +
min, max
range
"""

texto = 'valor'

# INDICE  0   1   2   3   4    Positivos
lista = ['A','B','C','D', 'E']
#   -    -5  -4  -3  -2   -1  #Negativos

lista[1] = "Reginaldo"
print(lista[2:5:2])   #começo, fim, quantas casas irá pular para cada índice



l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 #Para juntar as listas (ou algum valor), também posso usar a função extend
print(l3)

l1.append('A') #Insere um valor no final da lista
l2.insert(0, 'casa') # 0 = significa onde quero que 'casa' seja incluido

l2.pop()

print(l1)
print(l2)

teste = [1,2,3,4,5,6,7,8,9]
print(min(teste))
print(max(teste))


del(teste[3:8]) #começou a excluir após o 3, excluiu até o 8 nesse caso
print(teste)

#range
lista_range = list(range(0,100,8))
print(lista_range)

testando = [1,2,3,4,5,6,7,8,9]
soma = 0
for valor in testando:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')
print(soma)


listas_for = ['string', True, 20.0, 10]
for elem in listas_for:
    print(f"O tipo de elemento é {type(elem)} e seu valor é {elem}")


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances == 0:
        print("Você perdeu!!!")
        break
    letra = input("Digite uma letra:")
    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f"Que legal, você acertou a letra '{letra}' ")
    else:
        print(f"Poxa, a letra '{letra}' não existe na palavra secreta")
        digitadas.pop() #excluindo a letra errada
    #print(digitadas)

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
        else:secreto_temporario += '*'
    print(secreto_temporario)

    if secreto_temporario == secreto:
        print(f"Que legal, você ganhou!!! A palavra era {secreto_temporario}")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")
    if letra not in secreto:
        chances -= 1

    print(f'Você  tem {chances} chances ')



