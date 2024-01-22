#Programacion orientada a objetos con python

#numero de cuenta, saldo, agencia, limite



def cuenta (numero,titular,saldo,limite):
    cuenta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }
    return cuenta

cuenta(321, 'Jose', 100.0, 1000.0)

cuenta_1 = cuenta(321, 'Jose', 100.0, 1000.0)
cuenta_1['numero']


#retirar dinero cuenta
def retira(cuenta,valor):
    cuenta['saldo'] -= valor

def deposita(cuenta,valor):
    cuenta['saldo'] += valor

def extracto(cuenta):
    print(f"El saldo de la cuenta de {cuenta['titular']} es: {cuenta['saldo']}")

retira(cuenta_1,40)
extracto(cuenta_1)

deposita(cuenta_1, 100)
extracto(cuenta_1)


#creando clases para generar objetos
class Cuenta:
    def __init__(self, numero, titular, saldo, agencia, limite):
        print('Creando cuenta bancaria...')
        self.__numero = numero #atributo privado con __
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__limite = limite

#definiendo metodos
    def __puede_retirar(self, valor_a_retirar):
        valor_disponible = self.__saldo + self.__limite
        return valor_a_retirar <= valor_disponible
    def retira(self, valor):
        if (self.__puede_retirar(valor)):
          self.__saldo -= valor
        else:
          print(f'El valor {valor} excedio el limite permitido')
    
    def deposita(self, valor):
        self.__saldo += valor

    def extracto(self):
        print(f'El saldo de la cuenta de {self.__titular} es: {self.__saldo}')

    def transfiere(self, valor,destino):
        self.retira(valor) #encapsulando
        destino.deposita(valor)
    #Getters
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @staticmethod
    def codigo_banco():
        return '1001'
    #Setter
    def set_limite(self, limite):
        self.__limite = limite
        return self.__limite
    

cuenta1 = Cuenta(123,'Alvaro', 55.0, '001', 1000.0)
cuenta2 = Cuenta(321,'Jose', 100.0, '001', 1000.0)


#Creando una nueva clase Cliente

class Cliente:
    def __init__(self, nombre, limite):
        print("Creando nuevo cliente...")
        self.__nombre = nombre
        self.__limite = limite
    @property
    def nombre(self):
       return self.__nombre.title()
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre= nombre
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite


