def decode(string, rails):
    size = len(string) 
    grilla = [['..'] *(size) for j in range(rails)]  #se crea la grilla a partir del largo de la cadena
    
    i = 0
    d = -1             
    for j in range(size):
        grilla[i][j] = 'X'
        if i==0 or i==(rails-1):
            d = d *(-1)
        i = i + d
                
    c = 0

    for i in range(rails):
        for j in range(size):
            if (grilla[i][j] == 'X'):
                grilla[i][j] = string[c]
                c = c + 1

    for j in range(size):
        for i in range(rails):
            if grilla[i][j] != '..':                
                string = string + grilla[i][j]

    return string

def encode(string, rails):
    size = len(string) 
    grilla = [['..'] *(size) for j in range(rails)]
   
    i = 0
    d = -1
    for j in range(size):
        grilla[i][j] = 'X'
        if i==0 or i==(rails-1):
            d = d *(-1)
        i = i + d

    f = 0

    for j in range(size):
        for i in range(rails):
            if (grilla[i][j] == 'X'):
                grilla[i][j] = string[f]
                f = f + 1
    
    for i in range(rails):
        for j in range(size):
            if grilla[i][j] != '..':                
                string = string + grilla[i][j]
    
    return string

