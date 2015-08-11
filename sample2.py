#mario Alberto Gutierrez Corral
#Lista de numeros positivos que son la suma de ese numero

#funciones
def Suma(n,i):
    if(i>n-i):
        return 99
    else:
        print n ," = ",(n-i)," + ", i
        return Suma(n,i+1)
#programa principal
x=int(raw_input("dame un numero"))
Suma(x,1)
