variavel_lista = ['Reginaldo','neide', 'renato']

for valor in variavel_lista:
    if valor.lower().startswith('n'):
        continue
        print(valor)
        print('achou')

else:
    print("nao existe uma palavra que começa com n")


#o BREAK, para imediatamente
# o CONTINUE, ao encontrar o valor desejado, pula o mesmo