import requests
import json

def consumomarvel(dicionario):

    
    try:
    
        req = requests.get('https://gateway.marvel.com/v1/public/characters?limit=100&ts=1609890812920&apikey={SUAPUBLICKEY}&hash={SUAHASH}')
        dicionario = json.loads(req.text)
        
        return dicionario['data']['results']
        
        
        

    except:

        print('Erro ao estabelecer conexão!')
        


def personagemwiki (Character, nome_personagem):
    
    for personagem in Character :
        if (personagem["name"] == nome_personagem):
            print('nome:'+personagem['name'])
            print('Descrição:'+personagem['description'])
            break


sair = False
while not sair:

    pesquisa = input("Digite o nome de um personagem ou sair para fechar:")

    if pesquisa == ('sair'):
        sair = True
        print('Até mais!') 

    else:
        Character = consumomarvel(pesquisa)
        if Character == 'null':
           print('Personagem não encontrado')
        
        else:
            personagemwiki(Character, pesquisa)
            