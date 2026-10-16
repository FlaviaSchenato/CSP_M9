def eh_primo(numero):
    primo = True

    if numero <= 1:
        primo = False

    for i in range(2, numero, 1):
        if numero % i == 0:
            primo = False

        return primo

numero = int(input("Digite um número: "))

resultado = eh_primo(numero)

print(resultado)