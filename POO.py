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
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia
        self.limite = limite
#definiendo metodos
    def retira(self, valor):
        self.saldo -= valor
    def deposita(self, valor):
        self.saldo += valor

    def extracto(self):
        print(f'El saldo de la cuenta de {self.titular} es: {self.saldo}')

cuenta1 = Cuenta(123,'Alvaro', 55.0, '001', 1000.0)
cuenta2 = Cuenta(321,'Jose', 100.0, '001', 1000.0)
