import elimina
import frecuencia
abc=['',""," ",":","-","%","&","(",")","*",",","/","[","]","{","}", "|","~","+","<","=","!",">"]
reservadas=["",'',"and","as","assert","break","class","complex","continue","def","del","elif","else","except","exec","finally","float","for","from","global","if","import","in","input","int","is","lambda","len","long","not","or","pass","print","raise","range","raw_input","return","try","type","while","dict","set","min","max","list","cmp"]

def unaLinea(archivo):   
    linea=archivo.readline()
    a=""
    while linea!="":
        while linea[0]=='#':
            linea=archivo.readline()
        a=a+linea
        linea=archivo.readline()
        a=a[:-1]
        a=a+" "
    return a

def eliminaentre(nombre):
    cadena2=""
    cadena3=[]
    cadena=unaLinea(nombre)
    longitud= len(cadena)
    bandera=2
    for i in range(0,longitud):
        if(cadena[i]!='"'):
            if (bandera%2==0):
                cadena2=cadena2+cadena[i]
        else:
            bandera=bandera+1
    for i in range (0,len(cadena2)):
        cadena3.append(cadena2[i])
        
    for j in range(0,len(cadena3)):
        for h in range(0,len(abc)):
            if (cadena3[j]==abc[h]):
                cadena3[j]=" "
    cadena2=""
    for i in range (0,len(cadena3)):
        cadena2=cadena2+cadena3[i]

    cantidad,palabras = frecuencia.calcula(cadena2)
    

    for a in range(0,len (palabras)):
        for b in range(0, len(reservadas)):
            if palabras[a]==reservadas[b]:

                
                cantidad[a]=0
                palabras[a]="++"
                
    palabras1=[]
    cantidad1=[]
    for a in range(0,len(cantidad)):
        if cantidad[a]!=0:
            palabras1.append(palabras[a])
            cantidad1.append(cantidad[a])
            

    cant=0
    for a in range(0,len(cantidad1)):
        cant=cant+cantidad1[a]
    tot=len(palabras1)

    return cant,tot



