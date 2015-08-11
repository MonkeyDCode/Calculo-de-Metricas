def val_gral(x):
    if (len(x) == 0):
        print "Se necesita un dato"
        return 0
    else:
        return 1
def val(x):
    if(x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7"):
        x = int(x)
    else:
        print "Da un valor numerico permitido"
    return x
def val_tel(x):
    cont = 0
    for i in range (0,len(x)):
        if(x[i] == "0" or x[i] == "1" or x[i] == "2" or x[i] == "3" or x[i] == "4" or x[i] == "5" or x[i] == "6" or x[i] == "7" or x[i] == "8" or x[i] == "9"):
            cont = cont + 1
    if (cont == len(x)):
        x = int(x)
        return x
    else:
        print "Solo numeros son validos"
        return "0"            
def val_nom(y):
    ban = 1
    for i in range (0,len(y)):
        if(y[i] == "0" or y[i] == "1" or y[i] == "2" or y[i] == "3" or y[i] == "4" or y[i] == "5" or y[i] == "6" or y[i]== "7" or y[i] == "8" or y[i] == "9"):        
            ban = 0
    if (ban == 0):
        return "0"
    else:
        return y
