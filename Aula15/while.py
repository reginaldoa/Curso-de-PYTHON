#while True:#loop infinito
  # nome = input("qual o seu nome?")
  # print(f'olá {nome}')

x = 0

#while x < 10:
 #   if x == 3:
  #      x = x + 1
   #     break

    #print(x)
    #x = x + 1
#print('acabou')

x = 0 # coluna

#while x < 10:
#    y = 0  # linha

#    while y < 5:
#        print(f'({x}),({y})')
#        y += 1

#    x += 1 # é igual a x = x +1
#print('acabou')

while True:
    print()
    num_1 = input('digite um numero:')
    num_2 = input('digite outro numero:')
    operador = input('Digite um operador:')
    sair = input('Deseja sair? [s]im ou [n]ão:')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('operação inválida')






