class Cuenta_Bancaria:
    def __init__(self, numero=None, nombre_propietario=None, saldo: float = 0):
        self._numero = numero
        self._nombre_propietario = nombre_propietario
        self._saldo = saldo

    def __str__(self):
        return f'Cuenta Bancaria:\nNúmero: {self._numero}\nPropietario: {self._nombre_propietario}\nSaldo: {self._saldo}'

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def nombre_propietario(self):
        return self._nombre_propietario

    @nombre_propietario.setter
    def nombre_propietario(self, nombre_propietario):
        self._nombre_propietario = nombre_propietario

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def credito(self, valor: float = 0):
        self._saldo = float(self._saldo) + float(valor)
        return self._saldo

    def debito(self, valor: float = 0):
        self._saldo = float(self._saldo) - float(valor)
        return self._saldo

    def mostrar_saldo(self):
        print(self._saldo)
