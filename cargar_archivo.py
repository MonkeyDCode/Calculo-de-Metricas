#cargar archivo
import os
def cls():
    os.system(['clear','cls'][os.name == 'nt'])


def cargar():
    bandera=False
    while(bandera!=True):    
        nombre=raw_input("dame el nombre del archivo, y su extencion: ")
        
        if os.path.isfile(nombre):
            print"ARCHIVO CARGADO CON EXITO"
            bandera=True
            return nombre
        
        else:
            print"ARCHIVO INEXITENTE"

def historial():
    if os.path.isfile('historial.txt'):
        return True
    else:
        return False


