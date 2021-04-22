import psycopg2


def select():

   # Conecta no Banco de Dados

   conector = psycopg2.connect(
      database='fitmuscle',
      user='postgres',
      password='pgadmin123',
      host='localhost',
      port='5432')



  # Cria a Query
   cur = conector.cursor()

   cur.execute("SELECT*FROM clientes")
   dado = cur.fetchall()

# Mostra resultados do SELECT #
   print(dado)

   for dado in dado:
      print("nome =", dado[0])
      print("cpf =", dado[1])
      print("data =", dado[2])





   conector.close()

select()