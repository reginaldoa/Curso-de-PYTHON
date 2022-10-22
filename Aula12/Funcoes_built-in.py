#Python tem tipagem dinâmica.

num1 = input('digite um numero:')
num2 = input('digite outro numero:')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print("Não é possível converter os números para realizar contas.")

#isnumeric , isdigit (retornam o mesmo valor)
#isdecimal retorna true se todos os caracteres for decimais.


