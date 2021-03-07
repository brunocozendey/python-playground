import requests

from AcessoCep import AcessoCep

cep = "22290040"

objeto_cep = AcessoCep(cep)

bairro, cidade, uf = objeto_cep.acessa_api()

print(bairro,cidade,uf)