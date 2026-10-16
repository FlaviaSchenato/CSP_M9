def fatorial(numero):
    fat = 1

    for i in range(1, numero + 1, 1):
        fat = fat * i

    return fat

numero = int(input("Digite um número: "))

resultado = fatorial(numero)

print(resultado)
