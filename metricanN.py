import elimina
abc=[":","!=","-","%","&","(","*","**",",","/","//","[","{", "|","~","+","<","<<","<=","<>","=","==",">",">=",">>","and","as","assert","break","class","complex","continue","def","del","elif","else","except","exec","finally","float","for","from","global","if","import","in","input","int","is","lambda","len","long","not","or","pass","print","raise","range","raw_input","return","try","type","while","dict","set","min","max","list","cmp"]
cant=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def unaLinea(archivo):
    
    linea=archivo.readline()
    a=""
    while linea!="":
        a=a+linea
        linea=archivo.readline()
        a=a[:-1]
    a=elimina.elimina(a)
    return a


def unodos(nombre):
    n1=0
    N1=0
    cadena=unaLinea(nombre)
    for i in range(0,len(abc)):
        cant[i]=cadena.count(abc[i])
    for j in range(0,len(abc)):
        if cant[j]!=0:
            n1=n1+1
            N1=N1+cant[j]
    return n1,N1
    

