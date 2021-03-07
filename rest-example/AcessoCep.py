import requests

class AcessoCep:

    def __init__(self,cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.formatar_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formatar_cep(self):
        return "{}-{}".format(self.cep[:4], self.cep[5:])

    def acessa_api(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()

        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )



