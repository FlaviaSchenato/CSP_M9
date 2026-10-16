def par_ou_impar(numero):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    return resultado

numero = int(input("Digite um número: "))

resultado = par_ou_impar(numero)

print(resultado)