__author__ = "David Andres Cabrera Belalcazar"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.cabrerab@campusucc,edu.co"

class Fecha:
    # Aquí inicia mi clase
    """#---------------------------------------------------------------------------
    # Atributos
    ------------------------------------------------------------------------------#"""
    
    dia = 0
    mes = 0
    anio = 0
    
    """#---------------------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------------------------#"""
    _method_= 'DarFecha'
    _params_='nuevaFecha'
    _returns_='Nada'
    _descriptions_='Este metodo permite cambiar la fecha' 
    def DarFecha(self, nuevaFecha):
        # Aquí inicia mi algoritmo
        self.DarFecha = nuevaFecha
        
    _method_= 'CambiarFecha'
    _params_='nuevaFecha'
    _returns_='Nada'
    _descriptions_='Este metodo permite cambiar la fecha'
    
    def CambiarFecha(self, nuevaFecha): 
        # Aquí inicia mi metodo
        
        self.CambiarFecha = nuevaFecha
    
    _method_= 'DarDia'
    _params_='Ninguno'
    _returns_='Dia'
    _descriptions_='retorna al dia de la clase'
     
    def DarDia (self):
        # Aquí inicia mi metodo
        return self.dia
    
    _method_= 'DarMes'
    _params_='Ninguno'
    _returns_='Mes'
    _descriptions_='Devuelve el mes de la clase'
    def DarMes (self):
        # Aquí inicia mi metodo
        return self.mes
    
    _method_= 'DarAnio'
    _params_='Ninguno'
    _returns_='Mes'
    _descriptions_='Devuelve el año de la clase'
    
    def DarAnio (self):
        return self.anio
     
    _method_= 'DarFecha'
    _params_='Ninguno'
    _returns_='Fecha de la clase'
    _descriptions_='Da la fecha de la clase' 
    def DarFecha(self): 
        # Aquí inicia mi algoritmo
        return self.dia+'/'+self.mes+'/'+self.anio