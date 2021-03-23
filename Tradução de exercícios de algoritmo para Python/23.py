def main():

    cont: int = 0
    maior: int = 0
    menor: int = 120
    soma: int = 0


    while cont<5:
        idade = int(input("Digite uma idade:"))
        soma = (soma) + idade
        cont = cont + 1


        if idade > maior and idade < menor:

            maior = idade
            menor = idade

        elif idade > maior:

            maior = idade

        elif idade < menor:

             menor = idade




    media = soma / cont




    print("A maior idade é:",maior,"anos")
    print("A menor idade é:",menor,"anos")
    print("A media das idades é:",media,"anos")







main()