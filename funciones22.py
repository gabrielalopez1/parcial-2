#  en este archivo voy a hacer las funciones que voy a necesitar para hacer uso del import 
def validar(dato):
    while True:
        # uso um try/except para que el codifo no se corte cuando ingresen caracteres diferentes a numeros
        try:
            entrada = int(input(dato))
            return entrada 
        except:
            print("ingrese solo numeros")

def numero_paciente(EPS, contador):
    # le sumo 1 al contador por cada paciente que se va ingresando
    if EPS == 1:
        return f"EPS-Sisben-{contador}"
    if EPS == 2:
        return f"EPS-Sura-{contador}"
    if EPS == 3:
        return f"EPS-Coomeva-{contador}"
    if EPS == 4:
        return f"EPS-Medimas-{contador}"
    if EPS == 5:
        return f"EPS-Salud Total-{contador}"
    
def validarF(dato):
    while True:
        try:
            entrada = float(input(dato))
            return dato
        except:
            print("ingrese numeros decimales")