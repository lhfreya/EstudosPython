def main():

    cont: int = 0
    contm: int = 0
    contf: int = 0
    somam: int = 0
    somaf: int = 0
    idade = 0

    while idade != -1:


      idade = int(input("Digite a sua idade ou -1 para sair:"))

      if idade != -1:
         nome = str(input("Digite seu nome:"))
         sexo = int(input("Digite 1 para o sexo Masculino ou 2 para Feminino:"))

         if sexo == 1:

           somam = (somam) + idade
           contm = contm + 1

         elif sexo == 2:

           somaf = (somaf) + idade
           contf = contf +1

      else:
       break

    mediam = (somam)/contm
    mediaf = (somaf)/contf

    print("A média masculina é:", mediam)
    print(" A média feminina é:", mediaf)
    print(" A quantidade de homens é:",contm)
    print(" A quantidade de mulheres é:", contf)

main()