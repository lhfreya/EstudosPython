def main():

    #entrada de dados

    tdia = float (input("Digite a taxa cobrada por dia:"))
    tkm = float(input("Digite a taxa cobrada por km:"))
    dias = int(input("Digite a qtd de dias do aluguel:"))
    km = int(input("Digite a qtd de KM rodados:"))

    #processamento

    vdia = dias * tdia
    vkm  = km * tkm
    vt   = vdia + vkm
    desc = vt * 0.10
    vcdesc = vt - desc

    print("O valor cobrado por",dias,"dias de aluguel é:",vdia)
    print("O valor por KM é:",vkm)
    print("O valor total é:",vt)
    print("O desconto é de :", desc)
    print("O valor total com desconto é de :", vcdesc)

main()
