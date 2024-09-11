__author__ = "David Andres Cabrera Belalcazar"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.cabrerab@campusucc,edu.co"
'''----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------'''
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class CuentaBancaria:

    # Aquí inicia mi clase
    """#---------------------------------------------------------------------------
    # Atributos
    ------------------------------------------------------------------------------#"""
    __cedula=''
    __nombre=''
    __saldo = 0
    __interes = 0    
    __cuentaCorriente = CuentaCorriente()
    __cuentaAhorros = CuentaAhorros()
    __cdt = CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    _method_='Ahorrar'
    _params_='monto'
    _returns_='Ninguno'
    _descriptions_='Este metodo permite añadir un monto en la cuenta de ahorros'
    def Ahorrar(self, monto):
    # Verificar si hay suficientes fondos en la cuenta corriente
        self.__cuentaCorriente.RetirarValor(monto)
        self.__cuentaAhorros.ConsignarValor(monto)

    _method_='retirarAhorro'
    _params_='monto'
    _returns_='Ninguno'
    _descriptions_='Este metodo permite retirar un monto en la cuenta de ahorros'
    def retirarAhorro(self, monto):
    # Verificar si hay suficientes fondos en la cuenta de ahorros
        self.__cuentaAhorros.RetirarValor(monto)

    _method_='darSaldoCorriente'
    _params_='ninguno'
    _returns_='el saldo de la cuenta corriente'
    _descriptions_='Este metodo permite retornar al saldo de la cuenta corriente'
    def darSaldoCorriente(self):
         return self.__cuentaCorriente.DarSaldo()
    
    _method_='retirarTodo'
    _params_='ninguno'
    _returns_='Cantidad retirada'
    _descriptions_='Este metodo permite retirar todo de la cuenta de ahorros y corriente'
    def retirarTodo(self):
        total = self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldo())
        self.__cuentaCorriente.RetirarValor(self.__cuentaCorriente.DarSaldo())
        return 'Usted acaba de retirar'+total
    _method_='duplicarAhorro'
    _params_='ninguno'
    _returns_='Ninguno'
    _descriptions_='Este metodo permite duplicar el dinero de la cuenta de ahorros'
    def duplicarAhorro(self):
        self.__cuentaAhorros.ConsignarValor(self.__saldoCuentaAhorros.DarSaldo())
        