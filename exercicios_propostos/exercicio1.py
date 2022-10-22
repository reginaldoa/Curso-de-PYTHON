"""
1- Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número
inteiro

"""
"""
 2- Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
"""
"""
 3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras  ou menos, escreva, "seu nome é curto" 
Se tiver entre 5 e 6 letras, escrava "seu nome é normal"; maior que 6 , escreva "seu nome é muito grande"
"""

# Esses exercícios foram realizados antes de verificar a aula de resolução dos mesmos, portanto, podem haver diferenças.

#Exercício 1

num = input("Digite um número:")

try:
    num = int(num)
    print(f" Você digitou o número: {num}")

    if num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número é impar")

except:
    print("Será necessário digitar um número inteiro.")



#Exercício2
horas = input("Quais horas são agora?")

try:
    horas = int(horas)

    if horas >= 0 and horas < 12:
        print("Bom dia!")
    elif horas >= 12 and horas < 18:
        print("Boa tarde")
    elif horas >= 18 and horas <= 23:
        print("Boa noite")
    else:
        print("Esse horário não é valido, tente novamente.")

except:
    print("Será necessário digitar um número inteiro")




#Exercício 3
nome = input("Digite o seu nome:")

if len(nome) == 0:
    print("O seu nome não existe?")
elif len(nome) <= 4:
    print("O seu nome é curto.")
elif len(nome) > 4 and len(nome) <= 6:
    print("O seu nome é normal")
else:
    print("O seu nome é muito grande.")

print(len(nome))