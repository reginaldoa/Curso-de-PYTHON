#operadores lógicos
#and, or, not
#in e not in

#and = todas as comparações devem ser verdadeiras
# or = uma das comparações devem ser verdadeiras para retornar verdadeiro

a = 2
b = 2
c = 3

d = ""
e = 0

nome = "Reginaldo Alves"

if 'a' not in nome:
    print('Existe a letra "A" no seu nome')
else:
    print('Não existe')

print(a == b and b < c)
print(not a == a or b > c)

if not d:
    print('Preencha o valor de D')



#Programa simulando um login
usuario = input('Nome de usuário:')
senha = input('Senha do usuário:')

usuario_bd = "reginaldo"
senha_bd = 123456


if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print("Usuário ou senha inválida.")