from tkinter import filedialog, Tk
from Productos import Producto
import matplotlib.pyplot as plt
from PIL import Image
import webbrowser

datos=[]
fecha=[]
instrucciones=[]

#metodos para ordenar  el listado de productos
def ordenarProductos():
    global datos
    cambio=True    
    while cambio:
        cambio=False
        for i in range(len(datos)-1):
            if datos[i].getTotal() < datos[i+1].getTotal():
                aux=datos[i]
                datos[i]=datos[i+1]
                datos[i+1]=aux
                cambio= True

#metodo para obtener los valores de las instrucciones
def buscarInstrucciones(nombre):
    global instrucciones
    respuesta=""
    nombre=nombre.lower()
    for i in instrucciones:
        if i[0]==nombre:
            respuesta= i[1]
        else:
            pass
    
    if respuesta=="":
        return None
    else:
        return respuesta

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

def validacionFecha(arg):
    meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    fecha=[]
    bandera=False
    arg[0]=arg[0].strip()
    arg[1]=arg[1].strip()
    arg[0]=arg[0].lower()
    for m in meses:
        if m == arg[0]:
            bandera=True
        else:
            pass

    if bandera:
        fecha.append(arg[0])
    else:        
        print('ERROR: *** Ingrese un mes valido ***')
        print('       *** por favor ingrese un nuevo archivo ***')
    if bandera:
        try:
            año=int(arg[1])
        except:
            print('ERROR: *** el año tiene que ser un numero ***')
            print('       *** por favor ingrese un nuevo archivo ***')

        else:
            if año >0:
                fecha.append(año)
                return fecha
            else:
                print('ERROR: *** El año tiene que ser un numero entero positivo ***')
                print('       *** por favor ingrese un nuevo archivo ***')
    else:
        return fecha

#metodo para realizar la primera opcion "cargar un archivo .data"
def cargar_archivo():
    global fecha   #arreglo donde se almacenan los datos de la fecha que se utilizaran 
    global datos 
    fecha.clear()
    datos.clear()
    archivo= obtener_archivo('data')
    caracteres=[]
    palabra=""
    if archivo != None:
        if len(archivo)>0:
            a=archivo.split('=')
            arg=a[0].split(':')
            fecha=validacionFecha(arg)
         #   print(fecha)  # impresion de fecha a utilizar
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
                        print("ERROR: *** el precio tiene que ser un numero ***")
                        print('       *** por favor ingrese un nuevo archivo ***')
                    else:     
                        contador=contador+1
                else:
                    ca=pro.strip()
                    try:
                        cantidad=float(ca)
                    except:
                        print("ERROR: *** La cantidad tiene que ser un numero ***")
                        print('       *** por favor ingrese un nuevo archivo ***')
                    else:     
                        contador=contador+1
                        nombre= nombre.lower()
                    z=Producto(nombre,precio,cantidad)
                    z.calcularTotal()
                    datos.append(z)
                    contador=0
                    nombre=""
                    precio=0
                    cantidad=0
            print('*** Archivos Cargados ***')
       #     print('****** Resultado ******')                  
       #     for p in datos:
      #          p.impresion_datos()
        else: 
            print ('ERROR: *** archivo vacio ***')  # validacion para un archivo vacio
            print('        *** por favor ingrese un nuevo archivo ***')
    else:
        print('ERROR: *** No se ha seleccionado ningun archivo ***')
    
#metodo para realizar la segunda opcion "cargar instrucciones .lfp"
def cargar_instrucciones():
    global instrucciones
    instrucciones.clear()
    archivo= obtener_archivo('lfp')
    palabra=""
    if archivo != None:
        if len(archivo)>0:
            for char in archivo:
                if char =='<' or char =='>' or char =='¿' or char =='?':
                    pass
                else:
                    palabra+=char
            datos=palabra.split(',')
            for dat in datos:
                tmp=dat.split(':')
                tmp[0]=tmp[0].lower()
                a=""
                for ch in tmp[1].strip():
                    if ord(ch)==34:
                        pass
                    else:
                        a=a+ch
                tmp[1]=a.lower()
                instrucciones.append(tmp)
            
            print('*** Archivos Cargados ***')
        else: 
            print ('ERROR: *** archivo vacio ***')  # validacion para un archivo vacio
            print('        *** por favor ingrese un nuevo archivo ***')
    else:
        print('ERROR: *** No se ha seleccionado ningun archivo ***')

#metodo para generar las graficas
def analizar():
    global datos
    global fecha
    global instrucciones
    if len(datos)==0 or len(fecha)==0 or len(instrucciones)==0:
        if len(datos)==0:
            print('ERROR: *** No se ha cargado el archivo de productos ***')
        if len(fecha)==0:
            print('ERROR: *** Los datos de la fecha del archivo productos son erroneos***')
            print('       *** por favor ingrese un nuevo archivo ***')
        if len(instrucciones)==0:
            print('ERROR: *** No se ha cargado el archivo de instrucciones ***')
    else:
        nombre=buscarInstrucciones('Nombre')
        grafica=buscarInstrucciones('Grafica')
        titulo=buscarInstrucciones('Titulo')
        tituloX=buscarInstrucciones('TituloX')
        tituloY=buscarInstrucciones('TituloY')

        #print(nombre+ " " + grafica + " " + titulo+ " "+tituloX+" "+ tituloY)

        if nombre == None or grafica == None:
            print('ERROR: *** Falta el nombre o el tipo de graica ***')
            print('       *** por favor ingrese un nuevo archivo ***')
        else:
            ejeX=[]
            ejeY=[] 
            for d in datos:
                ejeX.append(d.getNombre())
                ejeY.append(d.getTotal())

            grafica=grafica.lower()
            grafica=grafica.strip()
            plt.rcdefaults()

            if titulo ==None or titulo =="":
                titulo=fecha[0]+ " - " + str(fecha[1])       
            if tituloX == None or tituloX == "":
                pass
            if tituloY ==None or tituloY == "":
                pass

            if grafica == 'barras':
                grB, adB = plt.subplots()
                adB.bar(ejeX, ejeY) # Datos de la grafica
                adB.set_xlabel(tituloX) #titulos
                adB.set_ylabel(tituloY)
                adB.grid(axis='y', color='lightgray', linestyle='dashed')
                adB.set_title(titulo)
                grB.savefig(nombre)
                try:
                    img= Image.open(nombre+'.png')
                except: 
                    print('ERROR: *** Hubo un problema al intentar abrir la imagen ***')
                else:
                    img.show()

            elif grafica =='líneas' or grafica =='lineas':
                grL, adL = plt.subplots()
                adL.plot(ejeX, ejeY)
                adL.set_xlabel(tituloX, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'black'})
                adL.set_ylabel(tituloY, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'black'})
                adL.grid(axis='y', color='darkgray', linestyle='dashed')
                adL.set_title(titulo)
                grL.savefig(nombre)
                try:
                    img= Image.open(nombre+'.png')
                except: 
                    print('ERROR: *** Hubo un problema al intentar abrir la imagen ***')
                else:
                    img.show()
                    

            elif grafica == 'pie' or grafica == 'pastel' or grafica == 'gráfico de pastel' or grafica == 'grafico de pastel':
                grP, adP = plt.subplots()
                adP.pie(ejeY, labels=ejeX, autopct='%1.1f%%',
                shadow=True, startangle=90)
                adP.axis('equal')
                adP.set_title(titulo)
                grP.savefig(nombre)
                try:
                    img= Image.open(nombre+'.png')
                except: 
                    print('ERROR: *** Hubo un problema al intentar abrir la imagen ***')
                else:
                    img.show()
                    
            else:
                print('ERROR: *** Grafica no Disponible Faltan Datos ***')
                print('       *** por favor ingrese un nuevo archivo ***')

#metodo para generar el reporte html
def generar_reporte ():
    global datos
    ordenarProductos()
    try:
        mensaje = '''<!DOCTYPE html>
<html lang="es">
<head>
    <title>Reporte</title>
    <meta http-equiv=Content-Type content=text/html; charset=UTF-8>
    <link href="style.css" rel="stylesheet" type="text/css">
    <script src="script.js"></script>
</head>
<body>
    <section>
        <h1>Reporte de Productos</h1>
        <br>
        <h3>Producto Mas Vendido:       '''+str(datos[0].getNombre()) +'''</h3>
        <h3>Producto Menos Vendido:     '''+str(datos[len(datos)-1].getNombre())+''' </h3>
        <br>
        <div class="tbl-header">
            <table cellpadding="0" cellspacing="0" border="0">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Precio</th>
                        <th>Cantidad</th>
                        <th>total</th>
                    </tr>
                </thead>
            </table>
        </div>
        <div class="tbl-content">
            <table cellpadding="0" cellspacing="0" border="0">
                <tbody>'''
        for d in datos:
            mensaje=mensaje+''' 
                    <tr>
                        <td>'''+str(d.getNombre())+'''</td>
                        <td>'''+str(d.getPrecio())+'''</td>
                        <td>'''+str(d.getCantidad())+'''</td>
                        <td>'''+str(d.getTotal())+'''</td>
                    </tr>'''
        mensaje=mensaje+'''        </tbody>
            </table>
        </div>
    </section>
    <div class="made-with-love">
        Abner Martín Noj Hernández - 201801027
</body>
</html>'''
        f = open('index.html','w', encoding="utf-8")
        f.write(mensaje)
        f.close()
    except:
        print('ERROR: *** Error al crear el reporte ***')
    else:
        print('*** Archivo Creado ***')
        webbrowser.open('index.html')
#metodo de la logica princial del programa
def menu ():
    seleccion= 0
    while (seleccion !=5):

        print ('\n**************************')
        print ('\n          Menu')
        print ('\n**************************')
        print('1. Cargar Data')
        print('2. Cargar Instrucciones')
        print('3. Analizar')
        print('4. Reportes')
        print('5. Salir')
        print ('**************************\n')

        try:
            seleccion = int(input('Seleccione una opcion: \n'))
            if seleccion == 1:
                cargar_archivo()
            elif seleccion ==2:
                cargar_instrucciones()
            elif seleccion == 3:
                analizar()
            elif seleccion == 4:
                generar_reporte()
            elif seleccion == 5:
                print ("*** Adios ***")
            else:
                print ('*** Opcion no disponible ***')
        except:
            print('*** Por favor seleccione una opcion valida ***')


#main
if __name__=='__main__':
    menu()
