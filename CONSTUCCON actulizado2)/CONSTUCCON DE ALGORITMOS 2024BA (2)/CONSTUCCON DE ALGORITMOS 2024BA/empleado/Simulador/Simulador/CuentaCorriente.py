_author__ = "David Andres Cabrera Belalcazar"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.cabrerab@campusucc,edu.co"

class Corriente: 
    # Aquí inicia mi clase
    
    '''#------------------------------------------------------------
     # Atributos
    ---------------------------------------------------------------#'''

    __saldo = 0
    
    '''---------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------'''
    _method_= 'ConsignarValor'
    _params_='Monto'
    _returns_='Ninguno'
    _descriptions_='Este metodo permite consingar un monto a la cuenta'    
    
    def ConsignarValor(self, monto):
        #aqui inicia mi metodo
            self.__saldo= self.__saldo+monto
         # Aqui inicia mi metodo
         
    _method_= 'DarSaldo'
    _params_='Ninguno'
    _returns_='Saldo'
    _descriptions_='Este metodo retorna el saldo'    
    
    def DarSaldo(self):
        #aqui inicia mi metodo
           return self.__saldo
        
    _method_= 'CalcularSaldoTotal'
    _params_='Ninguno'
    _returns_='Saldo Total'
    _descriptions_='Este metodo suma el saldo de todas las cuentas'    
    
    def CalcularSaldoTotal(self):
        #aqui inicia mi metodo
        total = self.__CuentaCorriente.DarSaldo()+self.__CuentaAhorros.DarSaldo()
        return total
         
    _method_='RetirarValor'
    _params_='monto'
    _returns_='Ninguno'
    _descriptions_='Este metodo retira un monto a la cuenta'    
    def RetirarValor(self, monto):
        self.__saldo=self.__saldo-monto
        
    _method_='Ahorrar'  
    _params_='Ahorro'
    _returns_='Ninguno'
    _descriptions_='Este metodo ahorra un monto en la cuenta'
    def Ahorrar(self, Ahorro):
         self.__saldo=self.__saldo+Ahorro
         

