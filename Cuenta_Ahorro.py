from cuenta import Cuenta_Bancaria

class CuentaAhorro(Cuenta_Bancaria):
    def __init__(self, interes: float = 0, numero_cuenta=None, nombre_propietario=None, saldo: float = 0):
        self._interes = interes
        super(CuentaAhorro, self).__init__(numero=numero_cuenta, nombre_propietario=nombre_propietario, saldo=saldo)

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nuevo_interes):
        self._interes = nuevo_interes

    def pagar_interes(self):
        self._saldo = self._saldo + ((float(self._saldo) * int(self._interes)) / 100)
        return self._saldo

if __name__ == '__main__':
    cuenta_ahorro = CuentaAhorro(6, '0956721823', 'Katherine', '320')

    cuenta_ahorro.mostrar_saldo()
    cuenta_ahorro.credito(1400)

    cuenta_ahorro.mostrar_saldo()
    cuenta_ahorro.debito(30)

    print(cuenta_ahorro)