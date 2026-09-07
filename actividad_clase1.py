#Actividad 1

saldo_inicial = 50000
saldo_actual = saldo_inicial


while True:
    print("\n===== CAJERO AUTOMATICO =====")
    print("1. Consultar saldo.")
    print("2. Ingresar dinero.")
    print("3. Retirar dinero.")
    print("4. Salir.")
    opcion = input("eliga una opcion: ")
    match opcion:
        case "1":
            print(f"tu saldo actual es: {saldo_actual} ")
        case "2":
            ingreso = input("ingrese la cantidad de dinero deseada: ")
            while not ingreso.isdigit():
                ingreso = input("ingrese la cantidad de dinero deseada: ")
            ingreso = int(ingreso)
            saldo_actual = saldo_actual + ingreso
            print(f"su dinero fue ingresado exitosamente. su saldo actual es de {saldo_actual}")                            
        case "3":
            retiro = int(input("ingrese la cantidad de dinero que desea retirar: "))
            while not retiro.isdigit():
                retiro = int(input("ingrese la cantidad de dinero que desea retirar: "))
            retiro = int(retiro)
            saldo_actual = saldo_actual - retiro
            print(f"su retiro a sido exitoso. su saldo actual es de {saldo_actual}")                
        case "4":
            print("hasta luego")
            break 


# Actividad 2 

total_actual = 0 

hamburguesa  = 4500

bebidas = 1500

papas_fritas = 2000

while True:
    opcion = input("""\n
    ===== MENU PRINCIPAL =====
    1. Agregar hamburguesa ($4500)
    2. Agregar bebidas ($1500)
    3. Agregar papas fritas ($2000)
    4. Pagar el pedido (cerrar ticket)
    5. Cancelar pedidos y salir
    Elija una opcion: """)
    match opcion:
        case "1":
            total_actual = total_actual + hamburguesa
            print(f"Hamburguesa fue agreada. Total actual ${total_actual} ") 
        case "2":
            total_actual = total_actual + bebidas
            print(f"Bebidas fue agregadas. Total actual ${total_actual} ")
        case "3":
            total_actual = total_actual + papas_fritas
            print(f"Papas fritas fue agregadas. Total actual ${total_actual}")
        case "4":
            print(f"El total a pagar seria: ${total_actual}")
            efectivo_ingresado = int(input("Efectivo total con el que pago el cliente: "))
            while not efectivo_ingresado >= total_actual:
                efectivo_ingresado += int(input("el efectivo no es suficiente, ingrese mas dinero: "))
            vuelto = efectivo_ingresado - total_actual
            print(f"su vuelto es de {vuelto}")
            total_actual = 0
        case "5":
            print("Pedidos cancelados")
            break
            
                     
#Actividad 3

while True:
    print("\n=== CONTROL DE TEMPERATURA ===")
    temperatura_str = input("ingrese la temperatura del horno: ")
    if temperatura_str == "fin" or temperatura_str == "FIN":
        break
    texto_correcto = temperatura_str.replace(".", "", 1)
    if (temperatura_str == "" or 
        temperatura_str == "." or 
        temperatura_str.count(".") > 1 or 
        not texto_correcto.isdigit()):
        print("Error vuelva a intentarlo de nuevo")
        continue
    temperatura_str = float(temperatura_str)
    print("temperatura ingresada correctamente")
    if temperatura_str < 100.0 or temperatura_str > 500.0:
        print("¡ADVERTENCIA! Temperatura fuera de rango")
            

            
             
            
                
            
            
           

    
    



                        

        

    
    





   



    
    