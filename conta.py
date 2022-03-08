class Conta:
    # CONSTRUTOR
    def __init__(self, numero, titular, limite, saldo):
        print("Construindo o objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo
        self.__codigo_banco = "001"
        print("Objeto - {}".format(self.__titular))

    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __validar_saldo_disponivel(self, valor_a_sacar):
        valor_disponivel_conta = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_conta

    def sacar(self, valor):
        if self.__validar_saldo_disponivel(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transferir(self, valor, conta_origem, conta_destino):
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
