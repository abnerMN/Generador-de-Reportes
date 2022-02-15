from tkinter import filedialog, Tk
from Productos import Producto
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
        datos=""
        info = open(archivo,'r+',encoding='utf-8')
        for linea in info.readlines():
            datos+=linea.strip()
        info.close()
        return datos
    else:
        return None


#metodo para realizar la primera opcion "cargar un archivo .data"
def cargar_archivo ():
    archivo= obtener_archivo('data')
    fecha=[]  #arreglo donde se almacenan los datos de la fecha que se utilizaran 
    datos=[]
    caracteres=[]
    palabra=""
    if archivo != None:
        if len(archivo)>0:
            a=archivo.split('=')
            fecha=a[0].split(':')
            for ch in a[1]:
                if ch=='(' or ch==')' or ch=='[' or ch==']'or ord(ch)==8221 or ord(ch)==8220 or ord(ch)==34:
                    pass
                elif ch ==',' or ch ==';':
                    caracteres.append(palabra)
                    palabra=""
                else:
                    palabra+=ch
            
            contador=0
            nombre=""
            precio=0
            cantidad=0
            for pro in caracteres:
                if contador==0:
                    nombre=pro.strip()
                    contador=contador+1
                elif contador ==1:
                    pr=pro.strip()
                    try:
                        precio=float(pr)
                    except:
                        print("el precio tiene que ser un numero")
                    else:     
                        contador=contador+1
                else:
                    ca=pro.strip()
                    try:
                        cantidad=float(ca)
                    except:
                        print("La cantidad tiene que ser un numero")
                    else:     
                        contador=contador+1
                    z=Producto(nombre,precio,cantidad)
                    z.calcularTotal()
                    datos.append(z)
                    contador=0
                    nombre=""
                    precio=0
                    cantidad=0
            print(caracteres)
            print('borrador')
            
            for p in datos:
                p.impresion_datos()



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
