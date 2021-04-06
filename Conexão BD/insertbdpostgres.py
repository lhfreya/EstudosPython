import psycopg2


try:
    # Conecta no Banco de Dados
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


# Insere registros

cur.execute("INSERT INTO empresas (nome,cnpj,proprietario,atuacao,cidade,uf,fone,software) VALUES ('Agrofac',21334411000180,81712456,'AGRO','Goiânia','GO',6232327782,54487)")

cur.execute("INSERT INTO empresas (nome,cnpj,proprietario,atuacao,cidade,uf,fone,software) VALUES ('One Engenharia',21314420000180,234444656,'ENG.CIVIL','Goiânia','GO',6232327700,177890)")


# Salva registros
conector.commit()
print("Registros salvos com sucesso!")
conector.close()