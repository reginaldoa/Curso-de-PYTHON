# A idéria do for, é ser utilizado para coisas finitas.
#Função range(start = 0 , stop, step = 1)

texto = 'PYTHON'

for letra in texto:
    print(letra)

for n in range(7,10, 2):
    print(n)

print("##############")

for n in range(100):
    if n % 8 == 0:
        print(n)

textoo="python"
nova_string = ""

#continue - pula para o próximo laço
# break - termina o laço


for l in textoo:
    if l == "p":
        nova_string = nova_string + l.upper()
    elif l == "y":
        nova_string += l.upper()
        break
    else:
        nova_string += l


print(nova_string)

