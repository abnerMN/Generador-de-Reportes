from tkinter import filedialog, Tk
from productos import Producto


#funcion para obtener los archivos por una ventana emergente
#tiene como parametro la extension del archivo
def obtener_archivo(tipo):
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title= "Seleccione un archivo",
        initialdir="./",
        filetypes= {
            ("archivos "+tipo, "*."+tipo)
        }
    )
    if archivo:
        info = open(archivo,'r+',encoding='utf-8')
        txt=info.read()
        info.close()
        return txt
    else:
        return None

def validacion_simbolos(valor):
    bandera=False
    if valor==':' or valor=='=':
        bandera=True
    elif valor == '(' or valor==')':
        bandera=True
    elif valor =='[' or valor ==']':
        bandera=True
    elif valor ==',' or valor ==';':
        bandera=True
    elif valor =='"':
        bandera=True
    return bandera



#metodo para realizar la primera opcion "cargar un archivo .data"
def cargar_archivo ():
    archivo= obtener_archivo('data')
    caracteres=[]
    datos = []
    palabra=""
    if archivo != None:
        if len(archivo)>0:
            for valor in archivo:
                if ord(valor)>32:
                    if validacion_simbolos(valor):
                        caracteres.append(palabra)
                        caracteres.append(valor)  
                        palabra=""
                    else:
                        palabra+=valor
                else:
                    pass

            for a in caracteres:
                if a== "":
                    pass
                else:
                    datos.append(a)
            
            print(datos)
            
        else: 
            print ('archivo vacio')  # validacion para un archivo vacio
    else:
        print('No se ha seleccionado ningun archivo')
    

#metodo para realizar la segunda opcion "cargar instrucciones .lfp"
def cargar_instrucciones ():
    archivo= obtener_archivo('lfp')
    if archivo != None:
        datos= archivo.parse()
        print (datos)
    else:
        print('No se ha seleccionado ningun archivo')

def analizar():
    pass

def generar_reporte ():
    pass

#metodo de la logica princial del programa
def menu ():
    seleccion= 0
    while (seleccion !=6):

        print ('\n**************************')
        print('1. Cargar Data')
        print('2. Cargar Instrucciones')
        print('3. Analizar')
        print('5. Reportes')
        print('6. Salir')
        print ('**************************\n')

        try:
            seleccion = int(input('Seleccione una opcion: \n'))
            if seleccion == 1:
                cargar_archivo()
            elif seleccion ==2:
                cargar_instrucciones()
            elif seleccion == 3:
                print('opcion ' +str(seleccion))
            elif seleccion == 4:
                print('opcion ' +str(seleccion))
            elif seleccion == 5:
                print('opcion ' +str(seleccion))
            elif seleccion == 6:
                print ("*** Adios ***")
            else:
                print ('*** Opcion no disponible ***')
        except:
            print('*** Por favor seleccione una opcion valida ***')


#main
if __name__=='__main__':
    #menu()
    cargar_archivo()
