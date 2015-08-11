def Llenado():
    x=[]
    for i in range (0,27):
        x.append(0)
    return x

def Cuenta (pal):
    x=Llenado()
    for i in range (0,26):
        for j in range (0,len(pal)):
            if((abc[i]==pal[j].lower())):
                x[i]=x[i]+1
    return x

def Imprimir (x):
    for i in range (0,26):
        if (x[i]!=0):
            print (abc[i], "=",x[i])

def llenado(pal):
    y=""
    x=[]
    for i in range (0,len(pal)):
        if ((pal[i]==" ")or(i==len(pal)-1)):
            if(i==len(pal)-1):
                y=y+pal[i]
            x.append(y)
            y=""
        else:
            y=y+pal[i]
    return x

def Llenado2(x):
    y=[]
    y.append(x[0])
    flag=True
    for i in range (1,len(x)):
        for j in range (0,len(y)):
            if (y[j]==x[i]):
                flag=False
        if(flag):
            y.append(x[i])
        flag=True
    return y
        
def Frecuencia(pal):
    x=llenado(pal)
    y=Llenado2(x)
    z=[]
    cont=0
    for i in range (0,len(y)):
        for j in range (0,len(x)):
            if (y[i]==x[j]):
                cont+=1
        z.append(cont)
        cont=0
    return z,y

def calcula(pal):
    can,pals=Frecuencia(pal)
    return can,pals
