import psycopg2

def select():



 try:

    # Conecta no Banco de Dados#
  conector = psycopg2.connect(
        database='Enterprise',
        user='postgres',
        password='pgadmin1234',
        host='127.0.0.1',
        port='5090')


 except Exception as erro:

    print('Não foi possivel conectar com servidor', erro)




  # Cria a Query
 cur = conector.cursor()
 cur.execute("SELECT nome, cpf, cargo FROM proprietarios")
 dado = cur.fetchall()

 # Mostra resultados do SELECT #
 print(dado)
 for dado in dado:
  print("nome =", dado[0])
  print("cpf =", dado[1])
  print("cargo =", dado[2])

 conector.close()

select()