class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError('Url inválida')

    @staticmethod
    def url_eh_valida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def ExtraiArgumentos(self):

        busca_moeda_origem = "moedaorigem"
        busca_moeda_destino = "moedadestino"

        inidice_inicial_moeda_origem = self.encontraIndiceInicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")

        moeda_origem = self.url[inidice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.trocaMoedaOrigem()
            inidice_inicial_moeda_origem = self.encontraIndiceInicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")
            moeda_origem = self.url[inidice_inicial_moeda_origem:indice_final_moeda_origem]


        indice_final_moeda_destino = self.url.find("&valor")
        inidice_inicial_moeda_destino = self.encontraIndiceInicial(busca_moeda_destino)
        moeda_destino = self.url[inidice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def encontraIndiceInicial(self,moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada) + 1
    
    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extraiValor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontraIndiceInicial(busca_valor)
        valor = self.url[indice_inicial_valor-1:]
        return valor
