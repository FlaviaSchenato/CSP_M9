def calcular_juros_simples(capital, taxa, tempo=1):
    juros = (capital * taxa * tempo) / 100

    return juros

capital = float(input("Digite o capital: "))
taxa = float(input("Digite a taxa (ex: 2.1): "))
tempo = int(input("Digite o tempo em meses: "))

resultado = calcular_juros_simples(capital, taxa, tempo)

print(resultado)