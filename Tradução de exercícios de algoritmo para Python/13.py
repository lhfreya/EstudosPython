def main():

    maria = float(input("Valor do deposito de Maria:"))
    jose = float(input("valor do deposito de José:"))

    #processamento

    calc = maria + jose
    aux = maria*100
    aux = calc/aux
    calc = calc-aux

    print("Maria tem:",aux,"%" "E José tem:",calc,"%")




main()