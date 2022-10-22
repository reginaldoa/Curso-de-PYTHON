from datetime import date

data_atual = date.today()
nome= "Reginaldo Alves da Silva"
idade = 27
peso =96
altura = 1.76
ano_nascimento = data_atual.year - idade
imc = peso / altura ** 2

#Exercício resolvido com sucesso.
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg. \n'
      f'O IMC de {nome} é de {imc:.2f} \n{nome} nasceu em {ano_nascimento}.')

#Um ponto interessante, é que os ensinamentos em javascript, estão tornando o aprendizado em python mais agradável.