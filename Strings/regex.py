import re

tel1 = "Meu numero é 1234-1234"
tel2 = "fala comigo 1234-1234 esse é o meu telefone"
tel3 = "1234-1234 é o meu celular"
tel4 = "lalalalalal lalall alalal"
padrao1 = "[123456789][123456789][123456789][123456789][-][123456789][123456789][123456789][123456789]"
padrao2 = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
padrao3 = "[0-9]{4}[-][0-9]{4}"
padrao4 = "[0-9]{4,5}[-]*[0-9]{4}"


retorno = re.search(padrao3, tel1)
print(retorno.group())