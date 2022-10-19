print("Bem vindo ao jogo da forca")
print("Dica: um time de futebol.")

chances = 3
palavra_secreta = 'PALMEIRAS'
letras_digitadas = []

while True:
    letra = input("Digite uma letra:")
    letra = letra.upper()
    if len(letra) > 1 or letra.isnumeric():
        print("Digite apenas uma letra para continuar no jogo. Não será aceito números.")
    if chances < 2:
        print("Você perdeu todas as chances, o jogo terminou.")
        break
    if letra not in palavra_secreta:
        chances -= 1
        print(f'Você errou, atualmente tem {chances} chances')
        continue
    if letra in palavra_secreta:
        print(f"Que legal, você acertou a letra {letra}")
        letras_digitadas.append(letra)
        #print(letras_digitadas)

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)



    if secreto_temporario == palavra_secreta:
        print(f"Parabéns, você venceu, a palavra é: {palavra_secreta}")
        break




