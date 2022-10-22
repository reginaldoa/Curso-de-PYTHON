usuario=input('Digite o seu usuário:')

qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("É necessário digitar pelo menos  6 caracteres")
else:
    print("Você foi cadastrado no sistema")



string1 = input("digite alguma coisa:")
string2 = input("digite mais alguma coisa:")


#Em python, tudo é um objeto.
#com a função len, podemos "fazer conta" de strings
print(f'A quantidade total de caracteres digitada foi {len(string1) + len(string2)}')