def calcular_area(largura, altura=0):

    if altura == 0:
        altura = largura
    
    area = largura * altura

    return area

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

resultado = calcular_area(largura, altura)

print(resultado)
