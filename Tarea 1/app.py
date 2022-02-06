from tkinter import filedialog, Tk

cont_caracteres=0
cont_digitos=0
cont_simbolos=0

#funcion para validar simbolos
def validacion_simbolos (valor):
    respuesta= False
    if valor>=33 and valor <=47:
        respuesta = True
        return respuesta
    elif valor>=58 and valor <=64:
        respuesta = True
        return respuesta
    elif valor>=91 and valor <=96:
        respuesta = True
        return respuesta
    elif valor>=123 and valor <=126:
        respuesta = True
        return respuesta
    elif valor>=168 and valor <=170:
        respuesta = True
        return respuesta
    elif valor>=174 and valor <=180:
        respuesta = True
        return respuesta
    elif valor>=184 and valor <=197:
        respuesta = True
        return respuesta
    elif valor>=200 and valor <=207:
        respuesta = True
        return respuesta
    elif valor>=213 and valor <=223:
        respuesta = True
        return respuesta
    elif valor>=238 and valor <=242:
        respuesta = True
        return respuesta
    elif valor>=244 and valor <=254:
        respuesta = True
        return respuesta
    else:
        return respuesta

#funcion para validar digitos
def validacion_digitos(valor):
    respuesta = False
    if valor>=48 and valor <=57:
        respuesta = True
        return respuesta
    elif valor>=171 and valor <=172:
        respuesta = True
        return respuesta
    elif valor == 243:
        respuesta = True
        return respuesta
    else:
        return respuesta

#funcion para obtener un arhivo
def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title= "Seleccione un archivo",
        initialdir="./",
        filetypes= {
            ("archivos txt", "*.txt")
        }
    )
    if archivo is None:
        return None
    else:
        texto = archivo.read()
        archivo.close()
        return texto

#metodo para contar los caracteres, digitos y simbolos 
def conteo (texto):
    global cont_caracteres
    global cont_digitos
    global cont_simbolos
    
    for valor in texto:
        if ord(valor)>32:
            if validacion_simbolos(ord(valor)):
                cont_caracteres+=1
                cont_simbolos+=1
            elif validacion_digitos(ord(valor)):
                cont_caracteres+=1
                cont_digitos+=1
            else:
                cont_caracteres+=1
        else:
            pass
        
    
    print("-------------------------------")
    print ("Caracteres: " + str (cont_caracteres))
    print ("Digitos: " + str (cont_digitos))
    print ("Simbolos: " + str(cont_simbolos))
    print("-------------------------------")


if __name__=='__main__':
    txt= abrir()
    if txt is None:
        print('\n*** No se seleccionó un archivo de entrada ***\n')
    else:
        conteo(txt)
        
