def main():

    bim1 = float(input("Digite a 1º nota:"))
    bim2 = float(input("Digite a 2º nota:"))
    bim3 = float(input("Digite a 3º nota:"))
    bim4 = float(input("Digite a 4º nota:"))

    media = (bim1+bim2+bim3+bim4)/4

    if media>=7:
        print("Aluno aprovado!")
    elif media<7:
        print("Aluno reprovado!")

main()