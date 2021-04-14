
def main():

    slo = float(input("Digite o salário:"))
    sexo = int(input("Digite 1 para sexo masculino ou 2 para feminino:"))

    if sexo==1:
        slf = slo*1.08
        print("O salário do funcionario é:",slf,"R$")
    elif sexo==2:
        slf = slo*1.10
        print("O salário da funcionária é:",slf,"R$")



main()