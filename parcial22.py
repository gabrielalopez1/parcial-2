# forma de importar las funciones
from funciones22 import * 
from datetime import datetime as dt
contador = 0
pacientes = {}

while True:
    print("ingrese la opcion que desee")
    # hago un menu para empezar a dirigir al usuario segun lo que necesite hacer
    menu = input("1. Ingresar paciente\n2. Informe de afiliacion EPS\n3. Borrar paciente\n4. Salir\n")
    if menu == "1":
        print("Por favor ingrese los siguientes datos:")
        nom = input("Nombre del paciente: ")
        id = validar("Número de documento: ")       
        d = validar("Ingrese día de nacimiento:")
        m = validar("Ingrese mes de nacimiento:")
        a = validar("Ingrese año de nacimiento:")
        try:
            fecha = dt(a,m,d)

        except ValueError:
            print("Ingrese los iontervalos de la fecha correcta")
        edad = validar("Edad: ")
        # como los rangos de la cantidad normal de la hormona son diferentes para hombres y mujeres, pregunto el genero del paciente
        # si es mujer le pregunto si es manopausica o no porque los valores varian
        # y pido el valor de la hormona para dar un diagnostico
        # creo la variable diagnostico por fuera para que al momento de añadir el paciente al diccionario, no me 
        # de el error de que la varieble no está definida 
        diagnosticof = []
        genero = input("F. femenino\nM. masculino\n")
        if genero == "F":
            print("¿pasa por la menopausia?")
            menopausia = validar("1. Sí\n2. No\n3. soy menor de 18 años\n")
            if menopausia == 1:
                hormonaM = validar("ingrese el valor de la hormona UI/L: ")
                # establezco el rango de los valores para dar el disnostico
                if 14<=hormonaM>=52:
                    diagnostico ="valor de la hormona Luteinizante normal"
                    # le doy appen para añadir a la lista de diagnostico final creada anteriormente
                    # estuve intentando mas formas de hacerle pero espero que con esta funcione 
                    diagnosticof.append(diagnostico)
                elif hormonaM>52 or hormonaM<14:
                    dianostico = "valor de la hormona Luteinizante fuera del rango normal"
                    diagnosticof.append(diagnostico)
            elif menopausia == 2:
                hormonaM = validar("ingrese el valor de la hormona UI/L: ")
                if 5<=hormonaM>=15:
                    diagnostico = "valor de la hormona Luteinizante dentro del rango normal"
                    diagnosticof.append(diagnostico)
                elif hormonaM>15 or hormonaM<5:
                    dianostico = "valor de la hormona Luteinizante fuera del rango normal"
                    diagnosticof.append(diagnostico)
            elif menopausia == 3:
                hormonaM = validar("ingrese el valor de la hormona UI/L: ")
                if 0<=hormonaM>=5:
                    diagnostico = "valor de la hormona Luteinizante dentro del rango normal"
                    diagnosticof.append(diagnostico)
                elif hormonaM>5 or hormonaM:
                    dianostico = "valor de la hormona Luteinizante fuera del rango normal"
                    diagnosticof.append(diagnostico)
            else:
                print("ingrese la opcion correcta")
        elif genero == "M":
            # uso una variable diferente para el valor de la hormona para el hombre aunque no era necesario ya que la variable
            # está sometida en diferentes condicionales
            edadH =input("1. hombre mayor de 18 años\n2. hombre menor de 18 años\n")
            if edadH == 1:
                hormonaH = validarF("ingrese el valor de la hormona UI/L: ")
                if 1.8<=hormonaH<=8.6:
                    diagnostico = "valor de la hormona Luteinizante dentro del rango normal"
                    diagnosticof.append(diagnostico)
                elif hormonaH<1.8 or hormonaH>8.6:
                    dianostico = "valor de la hormona Luteinizante fuera del rango normal"
                    diagnosticof.append(diagnostico)
            if edadH == 2:
                hormonaH = validarF("ingrese el valor de la hormona UI/L: ")
                if 1<=hormonaH<=1.8:
                    diagnostico = "valor de la hormona Luteinizante dentro del rango normal"
                    diagnosticof.append(diagnostico)
                elif hormonaH<1 or hormonaH>1.8:
                    dianostico = "valor de la hormona Luteinizante fuera del rango normal"
                    diagnosticof.append(diagnostico)
        else:
            print("opcion no disponible")

        print("EPS a la que está afiliado: ")
        EPS = validar("1. Sisben\n2. SURA\n3. Coomeva\n4. Medimas\n5. Salud Total\n")
        contador += 1
        # pongo un condicional porque otra vez di un menu y le digo que si 
        if EPS == 1:
            numpaciente_automatico = numero_paciente(EPS, contador)
            pacientes[id] = [nom,numpaciente_automatico,fecha,edad,genero,diagnosticof]
        elif EPS == 2:
            numpaciente_automatico = numero_paciente(EPS, contador)
            pacientes[id] = [nom,numpaciente_automatico,fecha,edad,genero,diagnosticof]
        elif EPS == 3:
            numpaciente_automatico = numero_paciente(EPS, contador)
            pacientes[id] = [nom,numpaciente_automatico,fecha,edad,genero,diagnosticof]       
        elif EPS == 4:
            numpaciente_automatico = numero_paciente(EPS, contador)
            pacientes[id] = [nom,numpaciente_automatico,fecha,edad,genero,diagnosticof]
        elif EPS == 5:
           numpaciente_automatico = numero_paciente(EPS, contador)
           pacientes[id] = [nom,numpaciente_automatico,fecha,edad,genero,diagnosticof]        
        else:
            print("esa opcion no está disponible")   

# no alcanzo a ver bien mi error al momento de poner el diagnostico :(((
# el codigo me imprime el diagnostico ya en el diccionario de pacientes pero para ciertos valores y el contador si funciona
        print(pacientes)
        continue     
        

    elif menu == 2:
        print("seleccione la opcion que desee")
        submenuinforme= validar("1. ver cantidad de pacientes menores de 10 años\n2. ver cantidad de pacientes mayores de 60 años\n")
        if submenuinforme == 1:
            print(list(filter(lambda edad: edad<10, pacientes.values())))
        elif submenuinforme == 2:
            print(list(filter(lambda edad: edad>60, pacientes.values())))
# no quiere funcionar esta opcion 
    elif menu == 3:
        doc = validar("ingrese el numero de identificacion del paciente que desea borrar: ")
        borrar = pacientes.pop(doc)
        continue
# esta tampoco 
    elif menu== 4:
        print("cerrando programa...")
        break

