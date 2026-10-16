def contar_vogais(texto):
    cont = 0

    for letra in texto:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            cont = cont + 1

    return cont

texto = input("Digite uma palavra: ")

resultado = contar_vogais(texto)

print(resultado)
