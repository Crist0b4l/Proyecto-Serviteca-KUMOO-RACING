

vehiculos = []

while True:
    # Menú
    print("Menú Principal")
    print("1. Ingresar Camioneta")
    print("2. Registro Mantenimiento")
    print("3. Consultar Camioneta")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1-4): "))
    # 1. Ingresar camioneta
    if opcion == 1:
    #Patente
        while True:
            print("Ingrese la patente (AA1000 o BBBB10) o presione '0' para volver al menú: ")
            patente = input().upper()
            if patente == '0':
                break
            
            if len(patente) == 6:
                if (patente[0].isalpha() and patente[1].isalpha() and patente[2].isdigit() and patente[3].isdigit() and patente[4].isdigit() and patente[5].isdigit()):
                    break
                elif (patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isalpha() and patente[4].isdigit() and patente[5].isdigit()):
                    break
            print("Patente inválida. Intente nuevamente")
                
    #Año fabricacion   
        if patente != '0':
            while True:
                print("Ingrese el año de fabricación (1975-2024) o presione '0' para volver al menú:  ")
                anio_fabricacion = int(input())
                if anio_fabricacion == 0:
                    break
            
                if 1975 <= anio_fabricacion <= 2024:
                    break
                print("Año no válido, por favor ingrese un año dentro del rango permitido")
                
    #Tipo vehiculo
            if anio_fabricacion != 0:
                while True:
                    print("Ingrese el tipo de vehículo, '2' para 4x2 - tracción simple o '4' para 4x4 - tracción doble o presione '0' para volver al menú: ")
                    tipo_vehiculo = int(input())
                    if tipo_vehiculo == 0:
                        break
                    
                    if tipo_vehiculo == 2 or tipo_vehiculo == 4:
                        break
                    print("Por favor ingrese un valor válido")
                    
    #Marca
                if tipo_vehiculo != 0:
                    while True:
                        print("Ingrese la marca del vehículo o presione '0' para volver al menú: ")
                        marca_vehiculo = input().title()
                        if marca_vehiculo == '0':
                            break
                        
                        if marca_vehiculo:
                            break
                        print("Por favor ingrese un valor")
                        
    #Modelo
                    if marca_vehiculo != '0':
                        while True:
                            print("Ingrese el modelo del vehículo o presione '0' para volver al menú: ")
                            modelo_vehiculo = input().title()
                            if modelo_vehiculo == '0':
                                break
                            
                            if modelo_vehiculo:
                                break
                            print("Por favor ingrese un valor")
                            
    #Agregar
                        if marca_vehiculo != '0':
                            vehiculos.append([patente, anio_fabricacion, tipo_vehiculo, marca_vehiculo, modelo_vehiculo, []])
                            print("Ingreso exitoso!")
    
    # 2. Registro mantenimiento
    elif opcion == 2:
        while True:
            print("Ingresa la patente de la camioneta para registrar el mantenimiento o presione '0' para volver al menú:  ")
            patente_mantenimiento = input().upper()
            if patente_mantenimiento == '0':
                break
            
            camioneta = None
            for cam in vehiculos:
                if cam[0] == patente_mantenimiento:
                    camioneta = cam
                    break
            
            if camioneta:
                print("Ingrese la fecha del mantenimiento o presione '0' para volver al menú:  ")
                fecha = input()
                if fecha == '0':
                    break
                print("Ingrese observaciones del mantenimiento o presione '0' para volver al menú:  ")
                observaciones = input()
                if observaciones == '0':
                    break
                
                if fecha and observaciones:
                    camioneta[5].append(f"Fecha: {fecha} - Observaciones: {observaciones}")
                    print("Mantenimiento registrado")
                    break
                
            else:
                print("Camioneta no encontrada, intente con otra patente.")
                
    # 3. Consultar camioneta
    elif opcion == 3:
        while True:
            print("Ingresa la patente de la camioneta para consultar sus datos o presione '0' para volver al menú: ")
            patente_consulta = input().upper()
            if patente_consulta == '0':
                break
            
            camioneta = None
            for cam in vehiculos:
                if cam[0] == patente_consulta:
                    camioneta = cam
                    break
            
            if camioneta:
                print(f"Patente: {camioneta[0]}")
                print(f"Año fabricación: {camioneta[1]}")
                print(f"Tipo de vehículo: {camioneta[2]}")
                print(f"Marca: {camioneta[3]}")
                print(f"Modelo: {camioneta[4]}")
                print(f"Registro Mantenimiento: {camioneta[5]}")
                break

            else:
                print("Camioneta no encontrada, intente con otra patente.")
                
    # 4. Salir
    elif opcion == 4:
        print("Gracias por atenderse con nosotros")
        break
                
    # Opción no valida (< 1 or > 4)
    else:
        print("Esa no es una opción válida, por favor seleccione una opción entre 1 y 4")

    
