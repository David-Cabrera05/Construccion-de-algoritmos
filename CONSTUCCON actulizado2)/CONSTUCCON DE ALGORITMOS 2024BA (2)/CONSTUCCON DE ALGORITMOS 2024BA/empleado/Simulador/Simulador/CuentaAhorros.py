__author__ = "David Andres Cabrera Belalcazar"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.cabrerab@campusucc,edu.co"

class Ahorrros: 
    # Aquí inicia mi clase
    
    '''#------------------------------------------------------------
     # Atributos
    ---------------------------------------------------------------#'''

    __saldo = 0
    interes = 0

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
    
    _method_= ' retirarValor '
    _params_=' monto '
    _returns_=' Valor a retirar '
    _descriptions_=' Metodo que retorna el valor a retirar '

    def retirarValor(self, monto):
         # Aqui va mi codigo
        self.saldo = self.saldo - monto

    _method_= ' darIntereses '
    _params_=' ninguno '
    _returns_=' Dar intereses '
    _descriptions_=' Metodo que retorna el interes '

    def darIntereses(self):
         # Aqui va mi codigo
        return self.interes_mensual
    
    __method__ = 'ActualizarSaldoPorPasoMes'
    __parmeter__ = 'nignuno' 
    __returns__ = 'Saldo actualizado'
    __description__ = " Metodo que actualiza el saldo de la cuenta de ahorros por paso de mes "
         
    def ActualizarSaldoPorPasoMes(self):
        self.interesppm = self.saldo + (self.saldo * self.interes_mensual)
