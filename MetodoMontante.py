cantidadVariables = 0
matriz = []
matrizIdentidad = []
matrizConIdentidad = []
guardarVariables = []
respuestas = []
finalizar = 0

def crearMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad):
    cantidadVariables = 0
    print("Ingrese la cantidad de variables")
    cantidadVariables = int(input())
    # Guardo la cantidad de variables en una lista
    guardarVariables.append(cantidadVariables)
    # Matriz Original 
    for i in range(cantidadVariables):
        matriz.append([])
        # El +1 es para el vector de terminos independientes
        for j in range(cantidadVariables+1):
            matriz[i].append(0)

    # Matriz identidad 
    for i in range(cantidadVariables):
        matrizIdentidad.append([])
        for j in range(cantidadVariables):
            if j == i:
                matrizIdentidad[i].append(1)
            else:
                matrizIdentidad[i].append(0)

    filas = columnas = 0
    # llenamos con los datos la matriz
    for columnas in range(0,cantidadVariables):
        for filas in range(0,cantidadVariables+1):
            print(str(columnas)+str(filas), end=" ")
            matriz[columnas][filas] = float(input())

    k=0
    # Matriz original expandida con la matriz identidad
    for i in range(cantidadVariables):
        matrizConIdentidad.append([])
        for o in range(cantidadVariables*2):
            # la primera mitad de las columnas son la matriz original
            if o < cantidadVariables:
                matrizConIdentidad[i].append(float(matriz[i][k]))
            else:# la segunda mitad es la matriz identidad
                matrizConIdentidad[i].append(float(matrizIdentidad[i][k]))

            if k >= cantidadVariables-1:
                k = 0
            else:
                k += 1
def resolverMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad):
    # obtenemos la cantidad de variables 
    cantidadVariables = guardarVariables[0]
    listaResultados=[]
    pivoteActual = 0
    pivoteAnterior = 0
    i=0
    numeroFila = -1
    centrar = 0
    #print("------------------------------------")
    for i in range(cantidadVariables):
        centrar = 12*cantidadVariables*2
        print('{:{align}{width}}'.format(
            "       COLUMNA #"+str(i+1), align='^', width=centrar))
        numeroFila = -1
        listaTemporal = []
        # si el pivote no es 0 entoces el valor de numero fila cambia a 0 que significa que no hay que hacer pivoteo parcial
        if(matrizConIdentidad[i][i] == 0):
            #se imprime la matriz
            for q in range(cantidadVariables):
                for n in range(cantidadVariables*2):
                    print(matrizConIdentidad[q][n], end=" ")
                print(" ")
            p = i
            # Bucamos un renglon que no sea cero
            for p in range(i,cantidadVariables):
                if matrizConIdentidad[p][i] != 0:
                    numeroFila = p
                    p = cantidadVariables

            # solo intercambiamos los renglones si existe uno sin un cero
            print(str(numeroFila))
            if numeroFila != -1:
                #copiamos los valores del renglon encontrado
                for j in range(cantidadVariables*2):
                    listaTemporal.append(matrizConIdentidad[numeroFila][j])
                #la lista temporal la copiamos en la fila 0 y la fila 0 la compiamos en la fila p
                for l in range(cantidadVariables*2):
                    matrizConIdentidad[numeroFila][l] = matrizConIdentidad[i][l]
                    matrizConIdentidad[i][l] = listaTemporal[l]
        else:
            numeroFila=0
        #-------------------------------------------------------
        #se imprime la matriz
        for q in range(cantidadVariables):
            for n in range(cantidadVariables*2):

                print('{:>12.6f}'.format(matrizConIdentidad[q][n]), end=" ")
                # se imprime una divison para distinguir el otro lado de la matriz 
                if n==cantidadVariables-1:
                    print("|", end=" ")
            print(" ")
 
        #-----------------------------------------------------------------
        if numeroFila != -1:
            # Obtenemos pivotes
            if i == 0:
                pivoteActual = matrizConIdentidad[i][i]
                pivoteAnterior = 1
            else:
                pivoteActual = matrizConIdentidad[i][i]
                pivoteAnterior = matrizConIdentidad[i-1][i-1]
            print(" ")
            print('{:{align}{width}}'.format("       Pivote actual = "+str(pivoteActual)+"  "+"Pivote anterior = "+str(pivoteAnterior), align='^', width=centrar, prec=6))
            print(" ")
            #print("Pivote actual = "+str(pivoteActual))
            #print("Pivote anterior = "+str(pivoteAnterior))


            for l in range(cantidadVariables):
                if l != i:
                    # Filas a modificar 
                    for p in range(cantidadVariables*2-(i+1)):
                        # i es la fila actual
                        # l es la fila a modificar
                        # p es la columna actual
                        resultadotem=0
                        # "Formula para ir resolviendo cada fila"
                        listaResultados.append(((pivoteActual*matrizConIdentidad[l][p+1+i])-(matrizConIdentidad[l][i]*matrizConIdentidad[i][p+1+i]))/pivoteAnterior)
                        resultadotem=((pivoteActual*matrizConIdentidad[l][p+1+i])-(matrizConIdentidad[l][i]*matrizConIdentidad[i][p+1+i]))/pivoteAnterior
                        #print("("+str(pivoteActual)+"("+str(matrizConIdentidad[l][p+1+i])+")"+"-"+str(matrizConIdentidad[l][i])+"("+str(matrizConIdentidad[i][p+1+i])+"))"+"/"+str(pivoteAnterior)+" = "+str(resultadotem))
                        print('{:{align}{width}}'.format("("+str(pivoteActual)+"("+str(matrizConIdentidad[l][p+1+i])+")"+"-"+str(matrizConIdentidad[l][i])+"("+str(matrizConIdentidad[i][p+1+i])+"))"+"/"+str(pivoteAnterior)+" = "+str(resultadotem), align='<', width=centrar,prec=2))
                        
                        
                    # Ingresamos eso datos a las fila correspondiente
                    y=0
                    for w in range(cantidadVariables*2):       
                        if w > i:
                            matrizConIdentidad[l][w] = listaResultados[y]
                            y+=1
                        else:
                            matrizConIdentidad[l][w] = 0
                    
                    #print(listaResultados)
                    print(" ")
                    print("Fila modificada"+str(listaResultados))
                    print(" ")
                    #print('{:{align}{width}}'.format(str(listaResultados), align='>', width=centrar))

                    listaResultados = []

            # sobreescribe el ultimo pivote
            if i>0:
                matrizConIdentidad[i-1][i-1] = pivoteActual
            print(" ")

    print(" ")
    if numeroFila != -1:
        print('{:{align}{width}}'.format("    Matriz solucionada", align='^', width=centrar))
        #se imprime la matriz
        for q in range(cantidadVariables):
            for n in range(cantidadVariables*2):
                if q == n :
                    matrizConIdentidad[q][n]=pivoteActual
                print('{:>12.6f}'.format(matrizConIdentidad[q][n]), end=" ")
                # se imprime una divison para distinguir el otro lado de la matriz
                if n == cantidadVariables-1:
                    print("|", end=" ")
            print(" ")
        print(" ")
        print("Calculando soluciones")
        print(" ")
        for u in range(cantidadVariables):
            res = 0
            print("x"+str(u+1)+" =",end=" ")
            for a in range(cantidadVariables):   
                res += matriz[a][cantidadVariables]*(matrizConIdentidad[u][cantidadVariables+a]/pivoteActual)
                print(str(matriz[a][cantidadVariables])+"*("+str(matrizConIdentidad[u][cantidadVariables+a])+"/"+str(pivoteActual)+")",end=" ")
                if a<cantidadVariables-1:
                    print("+",end=" ")
            print("= "+str(res))
            respuestas.append(res)
            #print(" ")
        print(" ")
        print("Soluciones="+str(respuestas))
        print(" ")
    else:
        print("NO TIENE SOLUCION o LA SOLUCION ES DEPENDIENTE")
    
    print(" ")
    print(" ")
    print("PRESIONE ENTER PARA FINALIZAR")
    ll = str(input())

crearMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad)
resolverMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad)
