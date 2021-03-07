from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formatar_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março","abril",
            "maio", "junho", "julho","agosto",
            "setembro", "outubro", "novembro","dezembro"
        ]
        return meses_do_ano[self.momento_cadastro.month-1]

    def dia_cadastro(self):
        dias_da_semana = [
            "segunda", "terça", "quarta",
             "quinta", "sexta","sábado","domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def formatar_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
        
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
