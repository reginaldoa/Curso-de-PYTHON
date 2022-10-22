num1 = 10
num2 = 20

while num1 <= num2:
    break
    print(num1)
    num1 += 1
    if num1 == num2:
        print(num1)
        print("acabou aqui o teste")
        break



nome = "reginaldo alves da silva"
nova_variavel = ''

for letra in nome:
    if letra == "r":
        letra = letra.upper()
    nova_variavel += letra
    print(nova_variavel)