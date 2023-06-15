from cuenta import Cuenta_Bancaria

class Cuenta_corriente(Cuenta_Bancaria):
    def __init__(self, numero=None, nombrepropietario=None, saldo: float = 0, tiene_cheque: bool = False):
        self._tiene_cheque = tiene_cheque
        super(Cuenta_corriente, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

if __name__ == '__main__':
    Cuentas_corrientes = Cuenta_corriente('0956721823', 'Katherine', '250', True)

    Cuentas_corrientes.mostrar_saldo()
    Cuentas_corrientes.credito(1400)

    Cuentas_corrientes.mostrar_saldo()
    Cuentas_corrientes.debito(30)

    print(Cuentas_corrientes)
