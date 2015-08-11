#Mario Alberto Gutierrez Corral
#suma de numeros de forma recusiva de 2 en 2

#definicion de funciones

def suma_rec(n):
    if(n<2):
        return 0
    else:
        return n+ suma_rec(n-2)




#programa principal

x = int(raw_input("Dame el numero hasta el que quieres que llegue la suma: "))
if(x%2 !=0):
    x=x-1
    
print "la suma  es",suma_rec(x)
