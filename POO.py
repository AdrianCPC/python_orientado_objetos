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