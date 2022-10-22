#Aula falando sobre formatações de string, abaixo alguns exemplos

nome = "Reginaldo"
peso = 96.00
altura = 1.76
imc = peso/( altura ** 2 )


#normal
print("o meu nome é", nome,'e meu imc é de', imc)

#formatado1
print('o meu nome é {}, e meu imc é de {:.2f}'.format(nome,imc))

#formatado1 com parametros nomeados
print('o meu nome é {n}, e meu imc é de {i:.2f}'.format(n=nome,i=imc))

#F-strings
print(f"O meu nome é {nome} e meu IMC é de {imc:.2f}")

