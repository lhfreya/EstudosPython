def main():

    cont: int = 0
    contm: int = 0
    contf: int = 0
    soma = 0
    idade = 0

    while idade != 200:


        idade = int(input("Digite a sua idade ou 200 para sair:"))


        if idade != 200:
         sexo = int(input("Digite 1 para o sexo Maculino ou 2 para Feminino:"))
         soma = (soma)+idade
         cont = cont + 1

         if sexo == 1:
          contm = contm + 1

         elif sexo == 2:
            contf = contf + 1

        else:
            break


    media = (soma)/cont
    percentm = (contm)*100/cont
    percentf = (contf)*100/cont

    print("A porcentagem de Homens é:",percentm,"%")
    print("A porcentagem de Mulheres é:",percentf,"%")
    print("A media das idades é:", media, "anos")



main()
