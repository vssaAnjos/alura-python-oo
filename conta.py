class Conta:
    # CONSTRUTOR
    def __init__(self, numero, titular, limite, saldo):
        print("Construindo o objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.limite = limite
        self.saldo = saldo

        print("Objeto - {}".format(self.titular))

    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

