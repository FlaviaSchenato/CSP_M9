def fibonacci(n):
    lista = []

    a = 0
    b = 1

    for i in range(0, n, 1):
        lista.append(a)

        proximo = a + b
        a = b
        b = proximo

    return lista

n = int(input("Digite um numero: "))

resultado = fibonacci(n)

print(resultado)