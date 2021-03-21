def cot():
    # Entrada de dados
    dolar = float(input("Digite o valor em dolar:"))
    cotacao = float(input("Digite a cotação do dolar:"))
    cotacao1 = float(input("Digite a cotação do Euro:"))

    # Processamento
    real = dolar * cotacao
    euro = real / cotacao1
    # Saida de dados
    print("O valor em real é de:", real, "R$")
    print("O valor em Euro é de:", euro, "E$")


cot()