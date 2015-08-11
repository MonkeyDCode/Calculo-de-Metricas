#eliminar los espacios en blanco de una frase
def elimina(fra):
    frase2 = " "
    n = len(fra)
    for i in range(0,n):
        if(fra[i] == " "):
            i = i - 1
        else:
            frase2 = frase2 + fra[i]
    return frase2

