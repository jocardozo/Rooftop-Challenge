def makeFigure(size):
    
    figure = [[0] *(size) for j in range(size)]  #creamos la matriz de 0 en el tamaño pedido
    
    x = 0 
    y = 0
    figure[0][0] =1  

'''Funciones auxiliares para el recorrido de la serpiente
''' 
 
   def moverEste(figure,x,y,pasos):
        for i in range(pasos):
            y = y + 1 
            x = x 
            figure[x][y] =1 
        return(x,y)

    def moverSur(figure,x,y,pasos):
        for i in range(pasos):
            x = x + 1 
            y = y
            figure[x][y] =1
        return(x,y)

    def moverOeste(figure,x,y,pasos):
        for i in range(pasos): 
            y = y - 1 
            x = x
            figure[x][y] =1
        return(x,y)

    def moverNorte(figure,x,y,pasos):
        for i in range(pasos):
            y = y
            x = x - 1
            figure[x][y] =1 
        return(x,y)

    x,y = moverEste(figure,x,y,size-1)     #Esta por fuera del patron, asi que 'definimos' como movimiento por defecto
    
    d = "s"

'''Recorrido de la serpiente
'''
    for i in range(1,size,1):
        if (d == "s"):
            x,y = moverSur(figure,x,y,size-i)
            d = "o"
            continue
        if (d == "o"):    
            x,y = moverOeste(figure,x,y,size-i+1)
            d = "n"
            continue
        if (d == "n"):
            x,y = moverNorte(figure,x,y,size-i)
            d = "e"
            continue   
        if (d == "e"):    
            x,y = moverEste(figure,x,y,size-i+1)
            d = "s"
            continue
    
    return(figure)