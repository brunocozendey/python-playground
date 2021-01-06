class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto .. {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    
    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel_a_sacar)

    def saca(self,valor):
        if ():
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite'.format(valor))
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco(self):
        return "001"

    @staticmethod
    def codigos_bancos(self):
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
conta = Conta(123, 'Bruno', 100.0,1000.0)
conta2 = Conta(124, 'Gabi', 200.0,1500.0)

conta.extrato()    
conta2.extrato()
conta.transfere(10,conta2)
conta.extrato()    
conta2.extrato()
print(conta.limite)
conta.limite = 1200.0 
print(conta.limite)
