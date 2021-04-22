import psycopg2



# Conecta no Banco de Dados
conector = psycopg2.connect(
    database='fitmuscle',
    user='postgres',
    password='pgadmin123',
    host='localhost',
    port='5432')



# Cria a Query
cur = conector.cursor()

# Insere registros

cur.execute("INSERT INTO clientes (nome,cpf,data,peso,modalidade) VALUES ('Paula','001.001.000-99','13/05/2021','57','musculação');")



# Salva registros

conector.commit()
print("Registros salvos com sucesso!")
conector.close()