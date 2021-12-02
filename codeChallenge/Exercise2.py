tablero=[
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

def validate(field):
    '''Esto es para validar si hay 20 posiciones ocupadas 
    '''
    total = 0
    for fila in field:
        total = total + sum(fila)
    if total != 20:
        return False
    '''Esto es para rellenar el tablero para solucionar los bordes
    '''
    tableroValidacion = [[0] *(12) for j in range(12)]

    for i in range(1,11):
        for j in range(1,11):
            tableroValidacion[i][j] = field[i-1][j-1]

    listaBarcos = []
    listaPosiciones = []
    '''Funciones auxiliares para buscar los barcos
    '''
    def buscarEste(x,y,tableroValidacion):
        tamañoBarco = 0
        while (tableroValidacion[x][y] == 1):
            tamañoBarco = tamañoBarco + 1
            tableroValidacion[x][y] = 2   #marcador para no contar de nuevo el mismo barco 
            y = y + 1
        return(tamañoBarco,x,y-1)  #y-1 xq la ultima posicion que busco tenia un 0, por ende devuelve la posicion anterior  

    def buscarSur(x,y,tableroValidacion):
        tamañoBarco = 0
        while (tableroValidacion[x][y] == 1):
            tamañoBarco = tamañoBarco + 1
            tableroValidacion[x][y] = 2    #marcador para no contar de nuevo el mismo barco
            x = x + 1
        return(tamañoBarco,x-1,y)   #x-1 xq la ultima posicion que busco tenia un 0, por ende devuelve la posicion anterior

    '''Recorrido del tablero para buscar los barcos y guardar los datos de tamaño y posicion
    '''
    for i in range(12):
        for j in range(12):
            if (tableroValidacion[i][j] == 1):
                m,k,l = buscarEste(i,j,tableroValidacion)   # busca para el este m=tamaño del barco
                if (m == 1):      
                    tableroValidacion[i][j] = 1
                    m,k,l = buscarSur(i,j,tableroValidacion)  #busca para el sur 
                listaBarcos.append(m)    #Guardamos en lista de barcos el tamaño del barco
                listaPosiciones.append([(i,j),(k,l)])    #guardamos la posicion
 
    '''Validacion de los 10 barcos y sus tamaños correctos
    '''
    listaBarcosOrden = listaBarcos.copy()   #coopia para no modificar el orden de la lista de barcos 
    listaBarcosOrden.sort()  #ordenamos para compararla con la lista validada
    listaValidada = [1,1,1,1,2,2,2,3,3,4]
    
    if listaValidada != listaBarcosOrden:
        return False

    '''Validacion de que haya espacio entre barcos
    '''
    p = listaPosiciones   #solo para ahorrar texto
   # for fila in tableroValidacion:     Se quita porque es una doble corroboracion
        
    for i in range(10):
        suma = 0
        for j in range(p[i][0][0]-1,p[i][1][0]+2):    #recorre las filas desde (x-1) hasta (x+1)
            for k in range(p[i][0][1]-1,p[i][1][1]+2):  #recorre las columnas desde (y-1) hasta (y+1)
                suma = suma + tableroValidacion[j][k]  
        #el conteo en todo el area deberia ser igual al tamaño del barco que esta en listaBarcos
        if (suma == listaBarcos[i] * 2):  #multiplica por 2 xq se agrego un 2 donde se encontraba un barco
            continue
        else:
            return False

    return True   #si todo es verdadero, sale como verdadero



print(validate(tablero))

