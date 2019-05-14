import re
import sys
 
simbolos = {"*": "tk_mult", "(": "tk_par_izq", ")": "tk_par_der", "&&": "tk_y",
            "||": "tk_o", "+": "tk_mas", "-": "tk_menos", "/": "tk_div", "%": "tk_mod",
            ",": "tk_coma", ".": "tk_punto", ":": "tk_dosp", ";":"tk_pyc",
			"'": "tk_comilla_sen", '"': "tk_comilla_dob"
            }
 
lista = []

class Control:
    estado = 0
    fila = 1
    columna = 1
    token = ""
    lexema = ""
 
def estadoUno(token):
    resultado = ""
    if re.match(r'funcion_principal[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'funcion_principal[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'funcion_principal', token):
        resultado = salida("no", len(re.findall(r'funcion_principal', token)[0]), token)
    elif re.match(r'fin_principal[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_principal[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_principal', token):
        resultado = salida("no", len(re.findall(r'fin_principal', token)[0]), token)
    elif re.match(r'funcion[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'funcion[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'funcion', token):
        resultado = salida("no", len(re.findall(r'funcion', token)[0]), token)
    elif re.match(r'fin_seleccionar[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_seleccionar[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_seleccionar', token):
        resultado = salida("no", len(re.findall(r'fin_seleccionar', token)[0]), token)
    elif re.match(r'fin_estructura[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_estructura[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_estructura', token):
        resultado = salida("no", len(re.findall(r'fin_estructura', token)[0]), token)
    elif re.match(r'fin_mientras[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_mientras[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_mientras', token):
        resultado = salida("no", len(re.findall(r'fin_mientras', token)[0]), token)
    elif re.match(r'fin_funcion[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_funcion[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_funcion', token):
        resultado = salida("no", len(re.findall(r'fin_funcion', token)[0]), token)
    elif re.match(r'fin_para[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_para[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_para', token):
        resultado = salida("no", len(re.findall(r'fin_para', token)[0]), token)
    elif re.match(r'fin_si[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'fin_si[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'fin_si', token):
        resultado = salida("no", len(re.findall(r'fin_si', token)[0]), token)
    elif re.match(r'falso[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'falso[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'falso', token):
        resultado = salida("no", len(re.findall(r'falso', token)[0]), token)
    elif re.match(r'f[\s$]', token):
        resultado = salida("id", len(re.findall(r'f', token)[0]), token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
 
def estadoDos(token):
    #print(token)
    resultado = ""
    if re.match(r'imprimir[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'imprimir[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'imprimir', token):
        resultado = salida("no", len(re.findall(r'imprimir', token)[0]), token)
    elif re.match(r'i[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'i[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'i[\s$]', token):
        resultado = salida("id", len(re.findall(r'i', token)[0]), token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
 
def estadoTres(token):
    resultado = ""
    if re.match(r'entero[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'entero[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'entero', token):
        resultado = salida("no", len(re.findall(r'entero', token)[0]), token)
    elif re.match(r'entonces[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'entonces[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'entonces', token):
        resultado = salida("no", len(re.findall(r'entonces', token)[0]), token)
    elif re.match(r'entre[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'entre[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'entre', token):
        resultado = salida("no", len(re.findall(r'entre', token)[0]), token)
    elif re.match(r'estructura[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'estructura[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'estructura', token):
        resultado = salida("no", len(re.findall(r'estructura', token)[0]), token)
    elif re.match(r'e[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
 
def estadoCuatro(token):
    resultado = ""
    if re.match(r'real[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'real[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'real', token):
        resultado = salida("no", len(re.findall(r'real', token)[0]), token)
    elif re.match(r'romper[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'romper[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'romper', token):
        resultado = salida("no", len(re.findall(r'romper', token)[0]), token)
    elif re.match(r'retornar[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'retornar[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'retornar', token):
        resultado = salida("no", len(re.findall(r'retornar', token)[0]), token)
    elif re.match(r'r[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
 
def estadoCinco(token):
    resultado = ""
    if re.match(r'booleano[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'booleano[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'booleano', token):
        resultado = salida("no", len(re.findall(r'booleano', token)[0]), token)
    elif re.match(r'b[\s$]', token):
        resultado = salida("id", len(re.findall('b', token)[0]), token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
 
def estadoSeis(token):
    resultado = ""
    if re.findall(r'\".+.+\"', token) or re.findall(r'\"\"', token) or re.findall(r'\" +\"', token):
        resultado = salida("tk_cadena",len(re.findall(r'\".*?\"', token)[0]),token)
    elif re.findall(r'\'.\'', token):
        resultado = salida("tk_caracter",len(re.findall(r'[\'].[\']', token)[0]),token)
    else:
        error()
        resultado = "error"
    return resultado
 
 
def estadoSiete(token):
    resultado = ""
    if re.match(r'[a-zA-Z0-9_]*', token):
        resultado = salida("id", len(re.findall(r'[a-zA-Z0-9_]*', token)[0]), token)
    else:
        error()
        resultado = "error"
    return resultado
 
 
def estadoOcho(token):
    resultado = ""
    if re.match(r'[-+]?\d*\.\d+', token):
        resultado = estadoNueve(token)
    elif re.match(r'[-+]?\d+', token):
        resultado = salida("tk_entero", len(re.findall(r'[-+]?\d+', token)[0]), token)
    else:
        error()
        resultado = "error"
    return resultado
 
 
def estadoNueve(token):
    resultado = ""
    if re.match(r'[-+]?\d*\d+', token):
        resultado = salida("tk_real", len(re.findall(r'[-+]?\d*\.\d+', token)[0]), token)
    elif re.match(r'[\.a-zA-Z]', token):
        resultado = estadoQuince(token)
    else:
        error()
        resultado = "error"
    return resultado
 
 
def estadoDiez(token):
    resultado = ""
    if re.match(r'\=\=', token):
        resultado = estadoCatorce(token)
    elif re.match(r'\=', token):
        resultado = salida("tk_asig", len(re.findall(r'\=', token)[0]), token)
    else:
        error()
        resultado = "error"
    return  resultado
 
 
def estadoOnce(token):
    resultado = ""
    if re.match(r'\!\=', token):
        resultado = estadoCatorce(token)
    elif re.match(r'\!', token):
        resultado = salida("tk_neg", len(re.findall(r'\!', token)[0]), token)
    else:
        error()
        resultado = "error"
    return resultado
 
 
def estadoDoce(token):
    resultado = ""
    if re.match(r'\<\=', token):
        resultado = estadoCatorce(token)
    elif re.match(r'\<', token):
        resultado = salida("tk_menor", len(re.findall(r'\<', token)[0]), token)
    else:
        error()
        resultado = "error"
    return resultado
 
 
def estadoTrece(token):
    resultado = ""
    if re.match(r'\>\=', token):
        resultado = estadoCatorce(token)
    elif re.match(r'\>', token):
        resultado = salida("tk_mayor", len(re.findall(r'\>', token)[0]), token)
    else:
        error()
        resultado = "error"
    return  resultado
 
 
def estadoCatorce(token):
    resultado = ""
    if re.match(r'\=\=', token):
        resultado = salida("tk_igual", len(re.findall(r'\=\=', token)[0]), token)
    elif re.match(r'\!\=', token):
        resultado = salida("tk_dif", len(re.findall(r'\!\=', token)[0]), token)
    elif re.match(r'\<\=', token):
        resultado = salida("tk_menor_igual", len(re.findall(r'\<\=', token)[0]), token)
    elif re.match(r'\>\=', token):
        resultado = salida("tk_mayor_igual", len(re.findall(r'\>\=', token)[0]), token)
    else:
        error()
        resultado = "error"
    return  resultado
 
def estadoQuince(token):
    return salida(simbolos[token[0]], 1, token)
 
def estadoDiezySeis(token):
    c = simbolos[token[:2]]
    resultado = salida(c,2,token)
    return resultado
 
def estadoDiezySiete(token):
    resultado = ""
    if re.match(r'verdadero[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'verdadero[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'verdadero', token):
        resultado = salida("no", len(re.findall(r'verdadero', token)[0]), token)
    elif re.match(r'v[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
 
def estadoDiezyOcho(token):
    resultado = ""
    if re.match(r'leer[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'leer[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'leer', token):
        resultado = salida("no", len(re.findall(r'leer', token)[0]), token)
    elif re.match(r'l[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoDiezyNueve(token):
    resultado = ""
    if re.match(r'caracter[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'caracter[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'caracter', token):
        resultado = salida("no", len(re.findall(r'caracter', token)[0]), token)
    elif re.match(r'caso[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'caso[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'caso', token):
        resultado = salida("no", len(re.findall(r'caso', token)[0]), token)
    elif re.match(r'cadena[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'cadena[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'cadena', token):
        resultado = salida("no", len(re.findall(r'cadena', token)[0]), token)
    elif re.match(r'c[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoVeinte(token):
    resultado = ""
    if re.match(r'defecto[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'defecto[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'defecto', token):
        resultado = salida("no", len(re.findall(r'defecto', token)[0]), token)
    elif re.match(r'd[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoVeintiuno(token):
    resultado = ""
    if re.match(r'si_no[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'si_no[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'si_no', token):
        resultado = salida("no", len(re.findall(r'si_no', token)[0]), token)
    elif re.match(r'si[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'si[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'si', token):
        resultado = salida("no", len(re.findall(r'si', token)[0]), token)
    elif re.match(r'seleccionar[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'seleccionar[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'seleccionar', token):
        resultado = salida("no", len(re.findall(r'seleccionar', token)[0]), token)
    elif re.match(r's[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoVeintidos(token):
    resultado = ""
    if re.match(r'mientras[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'mientras[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'mientras', token):
        resultado = salida("no", len(re.findall(r'mientras', token)[0]), token)
    elif re.match(r'm[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoVeintitres(token):
    resultado = ""
    if re.match(r'hacer[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'hacer[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'hacer', token):
        resultado = salida("no", len(re.findall(r'hacer', token)[0]), token)
    elif re.match(r'h[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoVeinticuatro(token):
    resultado = ""
    if re.match(r'para[a-zA-Z0-9_]+', token):
        resultado = salida("id", len(re.findall(r'para[a-zA-Z0-9_]+', token)[0]), token)
    elif re.match(r'para', token):
        resultado = salida("no", len(re.findall(r'para', token)[0]), token)
    elif re.match(r'p[\s$]', token):
        resultado = salida("id", 1, token)
    else:
        resultado = estadoSiete(token)
    return resultado
 
def estadoTab(token):
    if re.match(r'\t+', token):
        length = len(re.findall(r'\t+', token)[0])
        Control.token = token[length:]
        Control.columna += (length * len(token))
    return "__espacio"
 
 
def estadoEspacio(token):
    if re.match(r'\s+', token):
        length = len(re.findall(r'\s+', token)[0])
        Control.token = token[length:]
        Control.columna += length
    return "__espacio"
 
 
def estadoComentario(token):
    if re.match(r'//.*$', token):
        length = len(re.findall(r'//.*$', token)[0])
        Control.token = token[length:]
        Control.columna += length
    elif re.match(re.compile(r'/\*', re.DOTALL), token):
        if re.match(r'//*(.*?)/*/', token):
            length = len(re.findall(r'//*(.*?)/*/', token)[0]) + 2
            Control.token = token[length:]
            Control.columna += length
        elif re.match(r'/\*.*$', token):
            while True:
                inputs = lista.pop(0)
                Control.token = inputs
                Control.fila += 1
                Control.columna = 1
                token = Control.token
                if re.match(r'(.*?)/*/',token):
                    length = len(re.findall(r'(.*?)/*/',token)[0]) + 1
                    Control.token = token[length:]
                    Control.columna += length
                    break
    return "__comentario"
 
 
def salida(identificador, length, token):
    if (re.match("tk_cadena", identificador)):
        extracted = token[:length]
        Control.token = token[length:]
    else:
        extracted = token[:length]
        Control.token = token[length:]
 
    imprimir(identificador, extracted, length)
    if identificador == "no":
        identificador = extracted

    return identificador
 
def imprimir(id, lexema, length):
    if id == "no":
        pass
        # print("<" + str(lexema) + "," + str(Control.fila) + "," + str(Control.columna) + ">")
    elif id == "tk_entero" or id == "tk_real" or id == "tk_cadena" or id == "tk_caracter":
        # print("<" + str(id) + "," + str(lexema) + "," + str(Control.fila) + "," + str(Control.columna) + ">")
        pass
    elif re.match("tk",id):
        # print("<" + str(id) + "," + str(Control.fila) + "," + str(Control.columna) + ">")
        pass
    else:
        # print("<" + str(id) + "," + str(lexema) + "," + str(Control.fila) + "," + str(Control.columna) + ">")
        pass
    if(id == "tk_cadena"):
        Control.columna += length
    else:
        Control.columna += length
    Control.lexema = lexema
 
def simbolo(identificador, length, token):
    token = token[length:]
    print("<" + identificador + "," + str(Control.fila) + "," + str(Control.columna) + ">")
    Control.columna += length
    Control.lexema = identificador
 
def delta(estado, token):
    c = token[:1]
    resultado = ""
    if len(token) == 0:
        return "no#"
    elif estado == 0:
        if c == "f":
            resultado = estadoUno(token)
        elif c == "i":
            resultado = estadoDos(token)
        elif c == "e":
            resultado = estadoTres(token)
        elif c == "r":
            resultado = estadoCuatro(token)
        elif c == "b":
            resultado = estadoCinco(token)
        elif c == "v":
            resultado = estadoDiezySiete(token)
        elif c == "l":
            resultado = estadoDiezyOcho(token)
        elif c == "c":
            resultado = estadoDiezyNueve(token)
        elif c == "d":
            resultado = estadoVeinte(token)
        elif c == "s":
            resultado = estadoVeintiuno(token)
        elif c == "m":
            resultado = estadoVeintidos(token)
        elif c == "h":
            resultado = estadoVeintitres(token)
        elif c == "p":
            resultado = estadoVeinticuatro(token)
        elif token[:2] == "||":
            resultado = estadoDiezySeis(token)
        elif re.match(r'\s', token):
            resultado = estadoEspacio(token)
        elif re.match(r'\t', token):
            resultado = estadoEspacio(token)
        elif re.match(r'\"', token):
            resultado = estadoSeis(token)
        elif re.match(r'\'', token):
            resultado = estadoSeis(token)
        elif re.match(r'[a-zA-Z]', token):
            resultado = estadoSiete(token)
        elif re.match(r'\d', token):
            resultado = estadoOcho(token)
        elif re.match(r'\.', token):
            resultado = estadoNueve(token)
        elif re.match(r'\=', token):
            resultado = estadoDiez(token)
        elif re.match(r'\!', token):
            resultado = estadoOnce(token)
        elif re.match(r'\<', token):
            resultado = estadoDoce(token)
        elif re.match(r'\>', token):
            resultado = estadoTrece(token)
        elif re.match(r'//.*$', token):
            resultado = estadoComentario(token)
        elif re.match(r'/\*', token):
            resultado = estadoComentario(token)
        elif token[0] in simbolos:
            resultado = estadoQuince(token)
        elif token[:2] in simbolos:
            resultado = estadoDiezySeis(token)
        else:
            error()
            resultado = "error"
        # print("resultado: ",resultado)
    return resultado
 
def error():
    print(">>> Error lexico (linea: " + str(Control.fila) + ", posicion: " + str(Control.columna) + ")")
    sys.exit(0)

def readAllLines():
    # print("ENTRE")
    while True:
        try:
            inputs = input()
        except EOFError:
            break
        lista.append(inputs)
    if len(lista) > 0:
        Control.token = lista.pop(0)
    # print(lista)
    # exit()

def getNextToken(estado, token):
    #Empty lines
    while len(Control.token) == 0 and len(lista) > 0:
        Control.token = lista.pop(0)
        Control.columna = 1
        Control.fila += 1
    resultado = delta(Control.estado,Control.token)
    #Stuff we don't care about
    while resultado == "__espacio" or resultado == "__comentario" or resultado == "no#":
        if(resultado == "no#"):
            #line is over, read another one, if possible
            if len(lista) > 0:
                Control.columna = 1
                Control.fila += 1
                Control.token = lista.pop(0)
                resultado = delta(Control.estado,Control.token)
            else:
                resultado = "EOF"
        elif resultado == "__espacio" or resultado == "__comentario":
            resultado = delta(Control.estado,Control.token)
    if(resultado == "error"):
        sys.exit()
    return resultado

# readAllLines()

# while True:
#     result = getNextToken(Control.estado, Control.token)
#     print(result)
#     if result == "EOF" or result == "error":
#         break
#     else:
#         pass