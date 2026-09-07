# # Grilla del aula

aula = [['L','L','L','L'],
        ['L','L','L','L'],
        ['L','L','L','L']]

for fila in aula:
    for asiento in fila:
        print(asiento, end=' ')
    print('')
    
while True: # while a_ocupar != -1
    print('')
    a_ocupar_fila = int(input('Ingrese la fila a ocupar, (-1 para detener el programa): '))
    a_ocupar_columna = int(input('Ingrese la columna a ocupar, (-1 para detener el programa): '))
    
    if a_ocupar_fila in range(0,3) and a_ocupar_columna in range(0,4):
        if aula[a_ocupar_fila][a_ocupar_columna] == 'L':
            aula[a_ocupar_fila][a_ocupar_columna] = 'O'
            print('Lugar ocupado correctamente.')
            continue
        else:
            print('Ese lugar ya estaba ocupado.')
            continue
    
    if a_ocupar_fila == -1 or a_ocupar_columna == -1:
        print('Saliendo...')
        break
    
    print('Fila o columna fuera de rango. Fila debe ser un numero entre 0 y 2. Columna debe ser un numero entre 0 y 3.')
    
contador = 0
for fila in aula:
    contador += fila.count('O')

print(f'Hay {contador} asientos ocupados.')

for fila in aula:
    for asiento in fila:
        print(asiento, end=' ')
    print('')




# Actividad Bingo 
import random

carton = random.sample(range(1, 51), 25)
sorteados = random.sample(range(1, 51), 50)
carton_bingo = []

# Armado del carton (5 filas de 5) - con FOR
for i in range(5):
    carton_bingo.append(carton[i * 5 : (i + 1) * 5])

contador_sorteos = 0
bingo = False
indice_sorteo = 0

# Recorrido de los numeros sorteados
while indice_sorteo < len(sorteados) and not bingo:
    num = sorteados[indice_sorteo]
    input("Presiona Enter para sortear el siguiente numero...")
    contador_sorteos += 1
    print(f"el numero sorteado es: {num}")

    encontrado = False

    # Busqueda del numero en el carton 
    i = 0
    for fila in carton_bingo:
        j = 0
        for num_carton in fila:
            if num_carton == num:
                carton_bingo[i][j] = 'X'
                encontrado = True
            j += 1
        i += 1

    if encontrado:
        print(f"Numero {num} marcado en el carton.")
    else:
        print(f"El numero {num} no esta en el carton.")

    # Mostrar carton actualizado
    print("--- CARTON ---")
    for fila in carton_bingo:
        for n in fila:
            print(str(n).rjust(3), end=" ")
        print("")
    print("--------------")

    # Revisar filas 
    for fila in carton_bingo:
        marcados_en_fila = 0
        for n in fila:
            if n == 'X':
                marcados_en_fila += 1
        if marcados_en_fila == 5:
            bingo = True

    # Revisar columnas 
    j = 0
    while j < 5:
        marcados_en_columna = 0
        i = 0
        while i < 5:
            if carton_bingo[i][j] == 'X':
                marcados_en_columna += 1
            i += 1
        if marcados_en_columna == 5:
            bingo = True
        j += 1

    # Revisar diagonal principal 
    marcados_diagonal_1 = 0
    i = 0
    while i < 5:
        if carton_bingo[i][i] == 'X':
            marcados_diagonal_1 += 1
        i += 1
    if marcados_diagonal_1 == 5:
        bingo = True

    # Revisar diagonal secundaria 
    marcados_diagonal_2 = 0
    i = 0
    while i < 5:
        if carton_bingo[i][4 - i] == 'X':
            marcados_diagonal_2 += 1
        i += 1
    if marcados_diagonal_2 == 5:
        bingo = True

    if bingo:
        print("¡BINGO!")
        print(f"Se sortearon {contador_sorteos} numeros en total.")

    indice_sorteo += 1