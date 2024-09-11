__author__ = "David Andres Cabrera Belalcazar"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.cabrerab@campusucc,edu.co"

"""---------------------------------------------------
    # Importaciones
    ------------------------------------------------------"""
from Empleado.Fecha import Fecha


class Empleado: 
    # Aquí inicia mi clase
    
    '''#------------------------------------------------------------
     # Atributos
    ---------------------------------------------------------------#'''
    
    nombre = ''
    apellido = '' 
    salario = 0
    
    '''#----------------------------------------------------------------
    # 1 Masculino y 2 femenino
    -------------------------------------------------------------------#'''
    
    sexo = 0
    
    """#---------------------------------------------------
    # Asociaciomes
    ------------------------------------------------------#"""
    
    fechaNacimiento = Fecha ()
    fechaIngreso = Fecha ()
   
    """#---------------------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------------------------#"""

    # Estas son buenas practicas, no se hace en comentarios sino directamente
    _method_= 'CambiarSalario'
    _params_='nuevoSalario'
    _returns_='Nada'
    _descriptions_='Este metodo permite cambiar el salario del empelado por uno nuevo'
    def CambiarSalario(self, nuevoSalario): 
        # Aquí inicia mi metodo
        self.salario = nuevoSalario
        
    _method_= 'DarSalario'
    _params_='Ninguno'
    _returns_='Salario empleado'
    _descriptions_='Devuleve el salario del empelado'    
    
    def DarSalario(self):
        #  # Aqui va mi codigo (el sistema asume que el salario es 0, por eso se imprementa el "nuevoSalario" para cambiarlo)
        return self.salario 
        # Al ir con parametros se le da una asignacion que en este caso es el propio parametro
            
    _method_= 'AumentoSalarial'
    _params_='aumento'
    _returns_='Ninguno'
    _descriptions_='Permite aumentar el salario en un valor ingresado por el usuario'    
    
    def AumentoSalarial(self, aumento):
        #aqui inicia mi metodo
        self.salario = self.salario+aumento

    _method_= 'CalcularSalarioAnual'
    _params_='Ninguno'
    _returns_='Salario anual'
    _descriptions_='Permite calcular el salario anual del empleado'    
    def CalcularSalarioAnual(self):
        #aqui inicia mi metodo
        return self.salario*12
    
    _method_= 'CalcularImpuestoSalarioAnual'
    _params_='Ninguno'
    _returns_='Impuesto del salario anual'
    _descriptions_='Permite calcular el impuesto a el salario anual del empleado'   
    def CalcularImpuestoSalarioAnual(self):
        #aqui inicia mi metodo
        salarioAnual = self.CalcularSalarioAnual()
        return salarioAnual*0.19
        
    _method_= 'CalcularImpuestoSalario'
    _params_='Ninguno'
    _returns_='Impuesto del salario'
    _descriptions_='Permite calcular el impuesto a el salario del empleado'
    def CalcularImpuestoSalario(self):
        #aqui inicia mi metodo
        SalarioMensual = self.CalcularImpuestoSalario()
        return SalarioMensual*0.19
    #forma2
    #return self.DarSalario ()*0.19
        
    _method_= 'DarFechaIngreso'
    _params_='Ninguno'
    _returns_='Fecha de ingreso'
    _descriptions_='Muestra la fecha de ingreso del empleado'
    def DarFechaIngreso(self):
        #aqui inicia mi metodo
        return self.fechaIngreso.DarFecha()
    
    _method_= 'DarFechaNacimiento'
    _params_='Ninguno'
    _returns_='Fecha de nacimiento'
    _descriptions_='Muestra la fecha de nacimiento del emlpeado'
    def DarFechaNacimiento(self):
        #aqui inicia mi metodo
        return 'Tu fecha de naciemiento es'+ self.fechaNacimiento.DarFecha()
    