import requests
import json


def requisicao(titulo):

  try:

   req = requests.get('http://www.omdbapi.com/?t='+ titulo)
   dicionario = json.loads(req.text)
   return dicionario

  except:

    print('Erro ao estabelecer conexão! Tente novamente mais tarde ou contate o suporte')
    return None



def informações_filme(filme):


    print('Titulo:',filme["Title"])
    print('Ano:',filme["Yer"])
    print('Diretore:',filme["Director"])
    print('Atores:',filme["Actors"])
    print('Nota:',filme["imdbRating"])


sair = False
while not sair:

 op = input("Digite o nome de um filme ou SAIR para fechar:")

 if op == ('SAIR'):

    sair = True
    print('Até mais!')

 else:

     filme = requisicao(op)
     if filme["Response"] == 'False':
         print('Filme não encontrado')
     else:

        informações_filme(filme)





