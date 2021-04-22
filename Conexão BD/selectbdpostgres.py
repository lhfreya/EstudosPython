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
      print("Cliente =", dado[0],"CPF =", dado[1],"Inscrição =", dado[2],"Peso =", dado[3], "Modalidade =", dado[4])






   conector.close()

select()