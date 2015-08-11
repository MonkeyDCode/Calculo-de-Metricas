#menu principal
import validacion
import os
import cargar_archivo
import metricanN
import metrican2
import metricasderivadas
import guardaHistorial

def cls():
    os.system(['clear','cls'][os.name == 'nt'])
banderaDeMetrica=0
banderaDeArchivo=0
banderaDeMetricaD=0
opc = 0
nombre=""
while (opc <> 6):
    cls()
    print"1.-cargar archivo"
    print"2.-metricas basicas"
    print"3.-metricas derivadas"
    print"4.-guardar en el historial"
    print"5.-mostrar historial"
    print"6.-salir\n"
    while (opc < 1 or opc > 6):
        
        opc = raw_input("Cual es tu opcion?(1-6): ")
        opc = validacion.val(opc)
    if(opc == 1):
        banderaDeArchivo=1
        cls()
        opc=0
        nombre=cargar_archivo.cargar()
        
        raw_input("\n\npresiona enter para continuar")
    elif(opc == 2):
        cls()
        if(banderaDeArchivo==1):
            archivo=open(nombre,'r')
            N2,n2 = metrican2.eliminaentre(archivo)
            archivo.close
            archivo1=open(nombre,'r')
            n1,N1 = metricanN.unodos(archivo1)
            archivo1.close
            
            print "n1= ",n1,"      N1= ",N1,"      n2= ",n2,"      N2= ",N2
            raw_input("\n\npresiona enter para continuar")
            banderaDeMetrica=1
        else:
            print"NECESITAS CARGAR ANTES EL ARCHIVO"
            raw_input("\n\npresiona enter para continuar")
        opc=0
    elif(opc == 3):
        cls()
        if(banderaDeArchivo==1 and banderaDeMetrica==1):
            longitudP,vocabularioP,volumenP,dificultadP,nivelP,esfuerzo,tiempo,numero = metricasderivadas.metricasderivadas(n1,N1,n2,N2)
            print "longitud del programa:  ",longitudP
            print"vocabulario del programa",vocabularioP
            print"volumen del programa",volumenP
            print"dificultad del programa",dificultadP
            print"nivel del programa",nivelP
            print"esfuerzo de implementacion",esfuerzo
            print"tiempo de implementacion",tiempo
            print"numero de bugs liberados",numero
            banderaDeMetricaD=1
        elif(banderaDeArchivo==0):
            print"NECESITAS CARGAR ANTES EL ARCHIVO"
        elif(banderaDeMetrica==0):
            print "necesitas calcular metricas basicas antes"
        raw_input("\n\npresiona enter para continuar")
        opc=0
    elif(opc == 4):
        cls()
        if(banderaDeArchivo==0):
            print"NECESITAS CARGAR ANTES EL ARCHIVO"
        if(banderaDeMetrica==0):
            print"NECESITAS ANTES CALCULAR METRICAS BASICAS"
        if(banderaDeMetricaD==0):
            print"NECESITAS ANTES CALCULAR METRICAS DERIVADAS"
        if(banderaDeArchivo==1 and banderaDeMetrica==1 and banderaDeMetricaD==1):
            guardaHistorial.guarda(nombre,n1,N1,n2,N2,longitudP,vocabularioP,volumenP,dificultadP,nivelP,esfuerzo,tiempo,numero)
        raw_input("\n\npresiona enter para continuar")
        opc=0
    elif(opc == 5):
        cls()
        banderaHistorial=cargar_archivo.historial()
        if(banderaHistorial==True):
            archi=open('historial.txt','r')
            linea=archi.readline()
            while linea!="":
                print linea
                linea=archi.readline()
            archi.close()
                
        else:
            print"el archivo aun no se crea, guarde alguna metrica antes de mostrar el historial"
        raw_input("\n\npresiona enter para continuar")
        opc=0
    elif(opc == 6):
        print"Gracias por usar el programa"
