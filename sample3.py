#Mario Alberto Gutierrez Corral
#suma de numeros de forma recusiva de 1 en 1

#definicion de funciones

def suma_rec(n):
    if(n==0):
        return 0
    else:
        return n+ suma_rec(n-1)




#programa principal

x = int(raw_input("Dame el numero hasta el que quieres que llegue la suma: "))
print "la suma  es",suma_rec(x)
