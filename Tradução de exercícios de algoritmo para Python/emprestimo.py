def emprestimo():

    emp = float(input('Valor do crédito:'))
    slrio = float(input('Valor do seu salário:'))
    prest = int(input('Escolha a quantidade de prestações entre:6,12 ou 24:'))

    trintaporcento = (slrio / 100) * 30
    juros = (emp / 100) * 50

    vprest = (emp / prest) + (juros / prest)

    if prest == 6 or 12 or 24:
        if vprest > trintaporcento:
            print('Desculpe, infelizmente o valor das prestações ultrapassam sua margem.')

        else:
            print('Parabéns seu crédito foi aprovado!')
            print('O valor de suas parcelas é de:R$',vprest,'em',prest,'vezes')

    else:

        print('Desculpe, não trabalhamos com esse formato de parcelas!')


emprestimo()



