texto = input("Digite uma palavra: ")

cont = 0

for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "0" or letra == "u":
        cont = cont + 1

print(cont)