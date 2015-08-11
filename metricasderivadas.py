#metricas derivadas
import math
def metricasderivadas(n1,N1,n2,N2):
    
    longitudP=N1+N2
    vocabularioP=n1+n2
    volumenP=longitudP * ((math.log10(vocabularioP))/math.log10(2))
    dificultadP=(n1/2.0)*(N2/n2)
    if dificultadP==0:
        nivelP=0
    else:
        nivelP=1.0/dificultadP
    esfuerzo=dificultadP*volumenP
    tiempo=esfuerzo/18.0
    numero= ((esfuerzo**(2.0/3.0))/3000.0)
    return longitudP,vocabularioP,volumenP,dificultadP,nivelP,esfuerzo,tiempo,numero
