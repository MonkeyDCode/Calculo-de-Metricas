#Mario Alberto Gutierrez Corral
#invertir una cadena

#definicion de funciones

def CadC(C):
    n=len(C)
    if (n == 1):
        return C
    else:
        return C[-1]+CadC(C[:-1])
    
#P.P
C = raw_input("Cual es el texto: ")
print CadC (C)
