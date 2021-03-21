def main():
  #entrada de dados

    altura = float(input("Digite a altura do paciente: "))
    sexo = input("Digite o sexo do paciente, H(Masculino) ou F(Feminino): ")
    pesopaciente = float(input("Digite o seu peso: "))

    #processamento

    if sexo == "H" or sexo == "h":
        peso = (72.7 * altura) - 58
        print ("O peso ideal do paciente é: ",peso)
    elif sexo == "F" or sexo == "f":
        peso = (62.1 * altura) - 44.7
        print ("O peso ideal da paciente é: ",peso)
    else:

            print("Sexo inválido")



#saida de dados

    if pesopaciente < peso:
        print("Você está abaixo do peso ideal.")
    elif pesopaciente > peso:
        print("Você está acima do peso ideal.")
    else:
        print("Você está na média de peso.")

main()