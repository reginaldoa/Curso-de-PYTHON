num_1 = 1
num_2 = 100
divisao = num_1 / num_2

print(f'{divisao:.2f}')
print(f'{num_1:0>10.2f}')
print(f'{num_2:0>10}')

nome = "Reginaldo alves da silva"
nome_formatado = '{:@>25}'.format(nome)

print(nome_formatado)
print(nome.upper())