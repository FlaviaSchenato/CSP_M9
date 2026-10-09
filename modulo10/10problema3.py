n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = 0

for i in range(n1, n2 + 1, 1):
    if i % 2 != 0:
        soma = soma + i

print(soma)
