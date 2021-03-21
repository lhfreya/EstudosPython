def main():

    slrio = float(input("Digite o salário do vendedor:"))
    vd = float(input("Digite o valor da venda do mês:"))

    if vd<10000:

        bonus = slrio*0.15
        print("O bônus é no valor de:",bonus,"R$")

    elif vd>=10000 and vd<=50000:

        bonus = slrio*0.20
        print("O bônus é no valor de:",bonus,"R$")

    elif vd>50000:

        bonus = slrio*0.30
        print("O bônus é no valor de:", bonus, "R$")


main()