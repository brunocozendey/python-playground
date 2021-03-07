from ExtratorArgumentosUrl import ExtratorArgumentosUrl
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
print(ExtratorArgumentosUrl.url_eh_valida(url))


argumentosUrl = ExtratorArgumentosUrl(url) 
moeda_origem, moeda_destino = argumentosUrl.ExtraiArgumentos()
valor = argumentosUrl.extraiValor()

print(moeda_destino, moeda_origem, valor)

