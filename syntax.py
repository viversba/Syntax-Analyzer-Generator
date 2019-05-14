token = ""

orden = ["tk_mas","tk_menos","tk_mult","tk_div","tk_mod","tk_asig","tk_menor","tk_mayor","tk_menor_igual","tk_mayor_igual","tk_igual","tk_y","tk_o","tk_div","tk_neg","tk_dosp","tk_pyc","tk_coma","tk_punto","tk_par_izq","tk_par_der","id","tk_entero","tk_real","tk_caracter","tk_cadena","funcion_principal","fin_principal","leer","imprimir","booleano","caracter","entero","real","cadena","si","entonces","fin_si","si_no","mientras","hacer","fin_mientras","para","fin_para","seleccionar","entre","caso","romper","defecto","fin_seleccionar","estructura","fin_esctructura","funcion","fin_funcion","retornar","falso","verdadero","EOF"]

def S():
	global token
	if token == "funcion" or token == "estructura" or token == "funcion_principal" :
		FE()
		FUNC_PRINC()
		FE()
	else:
		syntaxErr( 'funcion', 'estructura', 'funcion_principal' )

def FUNC_PRINC():
	global token
	if token == "funcion_principal" :
		match( "funcion_principal" )
		BODY_FUNCION()
		match( "fin_principal" )
	else:
		syntaxErr( 'funcion_principal' )

def FE():
	global token
	if token == "funcion" :
		DF()
		FE()
	elif token == "estructura" :
		DE()
		FE()
	elif token == "funcion_principal" or token == "EOF" :
		pass
	else:
		syntaxErr( 'funcion', 'estructura', 'funcion_principal', 'EOF' )

def DF():
	global token
	if token == "funcion" :
		match( "funcion" )
		NOMBRE()
		match( "id" )
		match( "tk_par_izq" )
		ARG()
		match( "tk_par_der" )
		match( "hacer" )
		BODY_FUNCION()
		match( "retornar" )
		RET()
		match( "fin_funcion" )
	else:
		syntaxErr( 'funcion' )

def NOMBRE():
	global token
	if token == "booleano" or token == "real" or token == "caracter" or token == "cadena" or token == "entero" :
		TIPO()
	elif token == "id" :
		match( "id" )
	else:
		syntaxErr( 'booleano', 'real', 'caracter', 'cadena', 'entero', 'id' )

def TIPO():
	global token
	if token == "booleano" :
		match( "booleano" )
	elif token == "real" :
		match( "real" )
	elif token == "caracter" :
		match( "caracter" )
	elif token == "cadena" :
		match( "cadena" )
	elif token == "entero" :
		match( "entero" )
	else:
		syntaxErr( 'booleano', 'real', 'caracter', 'cadena', 'entero' )

def ARG():
	global token
	if token == "booleano" or token == "real" or token == "caracter" or token == "cadena" or token == "entero" or token == "id" :
		NOMBRE()
		match( "id" )
		SIG_ARG()
	elif token == "tk_par_der" :
		pass
	else:
		syntaxErr( 'booleano', 'real', 'caracter', 'cadena', 'entero', 'id', 'tk_par_der' )

def SIG_ARG():
	global token
	if token == "tk_coma" :
		match( "tk_coma" )
		NOMBRE()
		match( "id" )
		SIG_ARG()
	elif token == "tk_par_der" :
		pass
	else:
		syntaxErr( 'tk_coma', 'tk_par_der' )

def BODY_FUNCION():
	global token
	if token == "leer" or token == "imprimir" :
		COMANDO()
		BODY_FUNCION()
	elif token == "entero" or token == "real" or token == "cadena" or token == "caracter" or token == "booleano" :
		DECLARACION_VARIABLE()
		BODY_FUNCION()
	elif token == "id" :
		match( "id" )
		ASIGNACION_LLAMADO_INSTANCIACION()
		BODY_FUNCION()
	elif token == "si" :
		CONDICIONAL()
		BODY_FUNCION()
	elif token == "para" or token == "mientras" or token == "hacer" :
		CICLO()
		BODY_FUNCION()
	elif token == "seleccionar" :
		SELECCION()
		BODY_FUNCION()
	elif token == "fin_principal" or token == "retornar" or token == "si_no" or token == "fin_si" or token == "fin_para" or token == "fin_mientras" or token == "romper" or token == "fin_seleccionar" :
		pass
	else:
		syntaxErr( 'leer', 'imprimir', 'entero', 'real', 'cadena', 'caracter', 'booleano', 'id', 'si', 'para', 'mientras', 'hacer', 'seleccionar', 'fin_principal', 'retornar', 'si_no', 'fin_si', 'fin_para', 'fin_mientras', 'romper', 'fin_seleccionar' )

def COMANDO():
	global token
	if token == "leer" :
		match( "leer" )
		match( "tk_par_izq" )
		VARIABLE()
		match( "tk_par_der" )
		match( "tk_pyc" )
	elif token == "imprimir" :
		match( "imprimir" )
		match( "tk_par_izq" )
		CONCAT()
		match( "tk_par_der" )
		match( "tk_pyc" )
	else:
		syntaxErr( 'leer', 'imprimir' )

def CONCAT():
	global token
	if token == "id" :
		VARIABLE_LLAMADO_OPERACIONES()
		SIG_CONCAT()
	elif token == "tk_real" or token == "tk_entero" :
		OPERACION_NUMERICA()
		SIG_CONCAT()
	elif token == "verdadero" or token == "falso" or token == "tk_neg" :
		OPERACION_BOOLEANA()
		SIG_CONCAT()
	elif token == "tk_cadena" or token == "tk_caracter" :
		STRING()
		SIG_CONCAT()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		OPERACION_MIXTA()
		SIG_OPERACION_MIXTA_TRANSICION()
		match( "tk_par_der" )
	else:
		syntaxErr( 'id', 'tk_real', 'tk_entero', 'verdadero', 'falso', 'tk_neg', 'tk_cadena', 'tk_caracter', 'tk_par_izq' )

def SIG_CONCAT():
	global token
	if token == "tk_par_der" :
		pass
	elif token == "tk_coma" :
		match( "tk_coma" )
		CONCAT()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma' )

def STRING():
	global token
	if token == "tk_cadena" :
		match( "tk_cadena" )
	elif token == "tk_caracter" :
		match( "tk_caracter" )
	else:
		syntaxErr( 'tk_cadena', 'tk_caracter' )

def OPERACION_BOOLEANA():
	global token
	if token == "verdadero" :
		match( "verdadero" )
		SIG_OPERACION_BOOLEANA()
	elif token == "falso" :
		match( "falso" )
		SIG_OPERACION_BOOLEANA()
	elif token == "tk_neg" :
		match( "tk_neg" )
		OPERACION_BOOLEANA_MIXTA()
	else:
		syntaxErr( 'verdadero', 'falso', 'tk_neg' )

def SIG_OPERACION_BOOLEANA():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_igual" :
		match( "tk_igual" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_dif" :
		match( "tk_dif" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_mayor" :
		match( "tk_mayor" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_menor" :
		match( "tk_menor" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_mayor_igual" :
		match( "tk_mayor_igual" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_menor_igual" :
		match( "tk_menor_igual" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual' )

def OPERACION_BOOLEANA_SIMPLE_MIXTA():
	global token
	if token == "verdadero" :
		match( "verdadero" )
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "falso" :
		match( "falso" )
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "id" :
		match( "id" )
		AGREG_ID_BOOL()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_real" or token == "tk_entero" :
		TRANSICION_NUMERICA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_neg" :
		match( "tk_neg" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
		match( "tk_par_der" )
		SIG_OP_BOOL_SIMPLE_MIXTA()
	else:
		syntaxErr( 'verdadero', 'falso', 'id', 'tk_real', 'tk_entero', 'tk_neg', 'tk_par_izq' )

def TRANSICION_NUMERICA():
	global token
	if token == "tk_real" :
		match( "tk_real" )
		SIG_OPERACION_MIXTA_TRANSICION()
	elif token == "tk_entero" :
		match( "tk_entero" )
		SIG_OPERACION_MIXTA_TRANSICION()
	else:
		syntaxErr( 'tk_real', 'tk_entero' )

def SIG_OPERACION_MIXTA_TRANSICION():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" or token == "tk_y" or token == "tk_o" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" or token == "tk_igual" or token == "tk_dif" :
		pass
	elif token == "tk_mas" :
		match( "tk_mas" )
		OPERACION_MIXTA()
	elif token == "tk_menos" :
		match( "tk_menos" )
		OPERACION_MIXTA()
	elif token == "tk_div" :
		match( "tk_div" )
		OPERACION_MIXTA()
	elif token == "tk_mult" :
		match( "tk_mult" )
		OPERACION_MIXTA()
	elif token == "tk_mod" :
		match( "tk_mod" )
		OPERACION_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_y', 'tk_o', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_igual', 'tk_dif', 'tk_mas', 'tk_menos', 'tk_div', 'tk_mult', 'tk_mod' )

def SIG_OP_BOOL_SIMPLE_MIXTA():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_y', 'tk_o' )

def OPERACION_BOOLEANA_MIXTA():
	global token
	if token == "verdadero" :
		match( "verdadero" )
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "falso" :
		match( "falso" )
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "id" :
		match( "id" )
		AGREG_ID_BOOL()
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_real" or token == "tk_entero" :
		TRANSICION_NUMERICA()
		SIG_OP_BOOL_NUM_SIM_MIXTA()
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_neg" :
		match( "tk_neg" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		OPERACION_BOOLEANA_MIXTA()
		match( "tk_par_der" )
		SIG_OPERACION_BOOLEANA()
	else:
		syntaxErr( 'verdadero', 'falso', 'id', 'tk_real', 'tk_entero', 'tk_neg', 'tk_par_izq' )

def SIG_OP_BOOL_NUM_SIM_MIXTA():
	global token
	if token == "tk_mayor" :
		match( "tk_mayor" )
		TRANSICION_NUMERICA()
	elif token == "tk_menor" :
		match( "tk_menor" )
		TRANSICION_NUMERICA()
	elif token == "tk_mayor_igual" :
		match( "tk_mayor_igual" )
		TRANSICION_NUMERICA()
	elif token == "tk_menor_igual" :
		match( "tk_menor_igual" )
		TRANSICION_NUMERICA()
	else:
		syntaxErr( 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual' )

def OP_BOOL_MIX_ANIDADA():
	global token
	if token == "verdadero" :
		match( "verdadero" )
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "falso" :
		match( "falso" )
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "id" :
		match( "id" )
		AGREG_ID_BOOL()
		SIG_OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_neg" :
		match( "tk_neg" )
		OP_BOOL_MIX_ANIDADA()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		OP_BOOL_MIX_ANIDADA()
		match( "tk_par_der" )
		SIG_OP_BOOL_MIX_ANIDADA()
	else:
		syntaxErr( 'verdadero', 'falso', 'id', 'tk_neg', 'tk_par_izq' )

def SIG_OPERACION_BOOLEANA_MIXTA():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_igual" :
		match( "tk_igual" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_dif" :
		match( "tk_dif" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_mayor" :
		match( "tk_mayor" )
		TRANSICION_NUMERICA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_menor" :
		match( "tk_menor" )
		TRANSICION_NUMERICA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_mayor_igual" :
		match( "tk_mayor_igual" )
		TRANSICION_NUMERICA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	elif token == "tk_menor_igual" :
		match( "tk_menor_igual" )
		TRANSICION_NUMERICA()
		SIG_OP_BOOL_SIMPLE_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual' )

def SIG_OP_BOOL_MIX_ANIDADA():
	global token
	if token == "tk_par_der" :
		pass
	elif token == "tk_y" :
		match( "tk_y" )
		OP_BOOL_MIX_ANIDADA()
	elif token == "tk_o" :
		match( "tk_o" )
		OP_BOOL_MIX_ANIDADA()
	elif token == "tk_igual" :
		match( "tk_igual" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_dif" :
		match( "tk_dif" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif' )

def AGREG_ID_BOOL():
	global token
	if token == "tk_y" or token == "tk_o" or token == "tk_igual" or token == "tk_dif" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" or token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		CONCAT()
		match( "tk_par_der" )
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR_BOOL()
	else:
		syntaxErr( 'tk_y', 'tk_o', 'tk_igual', 'tk_dif', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_par_izq', 'tk_punto' )

def AGREG_ID_SIG_ATR_BOOL():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" or token == "tk_y" or token == "tk_o" or token == "tk_igual" or token == "tk_dif" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" :
		pass
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR_BOOL()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_punto' )

def OPERACION_NUMERICA():
	global token
	if token == "tk_real" :
		match( "tk_real" )
		SIG_OPERACION()
	elif token == "tk_entero" :
		match( "tk_entero" )
		SIG_OPERACION()
	else:
		syntaxErr( 'tk_real', 'tk_entero' )

def SIG_OPERACION():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_mas" :
		match( "tk_mas" )
		OPERACION_MIXTA()
	elif token == "tk_menos" :
		match( "tk_menos" )
		OPERACION_MIXTA()
	elif token == "tk_mult" :
		match( "tk_mult" )
		OPERACION_MIXTA()
	elif token == "tk_div" :
		match( "tk_div" )
		OPERACION_MIXTA()
	elif token == "tk_mod" :
		match( "tk_mod" )
		OPERACION_MIXTA()
	elif token == "tk_mayor" :
		match( "tk_mayor" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA_TRANSICION()
	elif token == "tk_menor" :
		match( "tk_menor" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA_TRANSICION()
	elif token == "tk_mayor_igual" :
		match( "tk_mayor_igual" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA_TRANSICION()
	elif token == "tk_menor_igual" :
		match( "tk_menor_igual" )
		OPERACION_MIXTA()
		SIG_OP_BOOL_SIMPLE_MIXTA_TRANSICION()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_mas', 'tk_menos', 'tk_mult', 'tk_div', 'tk_mod', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual' )

def SIG_OP_BOOL_SIMPLE_MIXTA_TRANSICION():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_y', 'tk_o' )

def VARIABLE_LLAMADO_OPERACIONES():
	global token
	if token == "id" :
		match( "id" )
		AGREG_ID()
		OPERACION_CON_VARIABLES()
	else:
		syntaxErr( 'id' )

def AGREG_ID():
	global token
	if token == "tk_mas" or token == "tk_menos" or token == "tk_div" or token == "tk_mult" or token == "tk_mod" or token == "tk_y" or token == "tk_o" or token == "tk_igual" or token == "tk_dif" or token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" :
		pass
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		CONCAT()
		match( "tk_par_der" )
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR()
	else:
		syntaxErr( 'tk_mas', 'tk_menos', 'tk_div', 'tk_mult', 'tk_mod', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif', 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_par_izq', 'tk_punto' )

def AGREG_ID_SIG_ATR():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" or token == "tk_mas" or token == "tk_menos" or token == "tk_div" or token == "tk_mult" or token == "tk_mod" or token == "tk_y" or token == "tk_o" or token == "tk_igual" or token == "tk_dif" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" :
		pass
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_mas', 'tk_menos', 'tk_div', 'tk_mult', 'tk_mod', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_punto' )

def OPERACION_CON_VARIABLES():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_mas" :
		match( "tk_mas" )
		OPERACION_MIXTA()
	elif token == "tk_menos" :
		match( "tk_menos" )
		OPERACION_MIXTA()
	elif token == "tk_div" :
		match( "tk_div" )
		OPERACION_MIXTA()
	elif token == "tk_mult" :
		match( "tk_mult" )
		OPERACION_MIXTA()
	elif token == "tk_mod" :
		match( "tk_mod" )
		OPERACION_MIXTA()
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA()
	elif token == "tk_igual" :
		match( "tk_igual" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	elif token == "tk_dif" :
		match( "tk_dif" )
		OPERACION_BOOLEANA_SIMPLE_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_mas', 'tk_menos', 'tk_div', 'tk_mult', 'tk_mod', 'tk_y', 'tk_o', 'tk_igual', 'tk_dif' )

def OPERACION_MIXTA():
	global token
	if token == "tk_par_izq" :
		match( "tk_par_izq" )
		OPERACION_MIXTA_ANIDADA()
		match( "tk_par_der" )
		SIG_OPERACION_MIXTA_ANIDADA()
	elif token == "tk_entero" :
		match( "tk_entero" )
		SIG_OPERACION_MIXTA()
	elif token == "tk_real" :
		match( "tk_real" )
		SIG_OPERACION_MIXTA()
	elif token == "id" :
		match( "id" )
		AGREG_ID()
		SIG_OPERACION_MIXTA()
	else:
		syntaxErr( 'tk_par_izq', 'tk_entero', 'tk_real', 'id' )

def OPERACION_MIXTA_ANIDADA():
	global token
	if token == "tk_par_izq" :
		match( "tk_par_izq" )
		OPERACION_MIXTA_ANIDADA()
		match( "tk_par_der" )
		SIG_OPERACION_MIXTA_ANIDADA()
	elif token == "tk_entero" :
		match( "tk_entero" )
		SIG_OPERACION_MIXTA_ANIDADA()
	elif token == "tk_real" :
		match( "tk_real" )
		SIG_OPERACION_MIXTA_ANIDADA()
	elif token == "id" :
		match( "id" )
		AGREG_ID()
		SIG_OPERACION_MIXTA_ANIDADA()
	else:
		syntaxErr( 'tk_par_izq', 'tk_entero', 'tk_real', 'id' )

def SIG_OPERACION_MIXTA_ANIDADA():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" or token == "tk_mas" or token == "tk_menos" or token == "tk_div" or token == "tk_mult" or token == "tk_mod" or token == "tk_y" or token == "tk_o" or token == "tk_igual" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" or token == "tk_dif" :
		pass
	elif token == "tk_mas" :
		match( "tk_mas" )
		OPERACION_MIXTA_ANIDADA()
	elif token == "tk_menos" :
		match( "tk_menos" )
		OPERACION_MIXTA_ANIDADA()
	elif token == "tk_div" :
		match( "tk_div" )
		OPERACION_MIXTA_ANIDADA()
	elif token == "tk_mult" :
		match( "tk_mult" )
		OPERACION_MIXTA_ANIDADA()
	elif token == "tk_mod" :
		match( "tk_mod" )
		OPERACION_MIXTA_ANIDADA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_mas', 'tk_menos', 'tk_div', 'tk_mult', 'tk_mod', 'tk_y', 'tk_o', 'tk_igual', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_dif' )
	#WARNING: This non terminal has repeated no terminal across it's many rules

def SIG_OPERACION_MIXTA():
	global token
	if token == "tk_par_der" or token == "tk_coma" or token == "tk_pyc" or token == "tk_mas" or token == "tk_menos" or token == "tk_div" or token == "tk_mult" or token == "tk_mod" or token == "tk_y" or token == "tk_o" or token == "tk_igual" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" or token == "tk_dif" :
		pass
	elif token == "tk_mas" :
		match( "tk_mas" )
		OPERACION_MIXTA()
	elif token == "tk_menos" :
		match( "tk_menos" )
		OPERACION_MIXTA()
	elif token == "tk_div" :
		match( "tk_div" )
		OPERACION_MIXTA()
	elif token == "tk_mult" :
		match( "tk_mult" )
		OPERACION_MIXTA()
	elif token == "tk_mod" :
		match( "tk_mod" )
		OPERACION_MIXTA()
	else:
		syntaxErr( 'tk_par_der', 'tk_coma', 'tk_pyc', 'tk_mas', 'tk_menos', 'tk_div', 'tk_mult', 'tk_mod', 'tk_y', 'tk_o', 'tk_igual', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_dif' )
	#WARNING: This non terminal has repeated no terminal across it's many rules

def VARIABLE():
	global token
	if token == "id" :
		match( "id" )
		SIG_VAR()
	else:
		syntaxErr( 'id' )

def SIG_VAR():
	global token
	if token == "tk_par_der" :
		pass
	elif token == "tk_punto" :
		match( "tk_punto" )
		VARIABLE()
	else:
		syntaxErr( 'tk_par_der', 'tk_punto' )

def DECLARACION_VARIABLE():
	global token
	if token == "entero" :
		match( "entero" )
		match( "id" )
		ASIGNACION_INICIAL()
		SIGUIENTE_DECLARACION()
		match( "tk_pyc" )
	elif token == "real" :
		match( "real" )
		match( "id" )
		ASIGNACION_INICIAL()
		SIGUIENTE_DECLARACION()
		match( "tk_pyc" )
	elif token == "cadena" :
		match( "cadena" )
		match( "id" )
		ASIGNACION_INICIAL()
		SIGUIENTE_DECLARACION()
		match( "tk_pyc" )
	elif token == "caracter" :
		match( "caracter" )
		match( "id" )
		ASIGNACION_INICIAL()
		SIGUIENTE_DECLARACION()
		match( "tk_pyc" )
	elif token == "booleano" :
		match( "booleano" )
		match( "id" )
		ASIGNACION_INICIAL()
		SIGUIENTE_DECLARACION()
		match( "tk_pyc" )
	else:
		syntaxErr( 'entero', 'real', 'cadena', 'caracter', 'booleano' )

def SIGUIENTE_DECLARACION():
	global token
	if token == "tk_pyc" :
		pass
	elif token == "tk_coma" :
		match( "tk_coma" )
		match( "id" )
		ASIGNACION_INICIAL()
		SIGUIENTE_DECLARACION()
	else:
		syntaxErr( 'tk_pyc', 'tk_coma' )

def ASIGNACION_INICIAL():
	global token
	if token == "tk_coma" or token == "tk_pyc" :
		pass
	elif token == "tk_asig" :
		match( "tk_asig" )
		ASIGNACION()
	else:
		syntaxErr( 'tk_coma', 'tk_pyc', 'tk_asig' )

def ASIGNACION():
	global token
	if token == "id" :
		VARIABLE_LLAMADO_OPERACIONES()
	elif token == "tk_real" or token == "tk_entero" :
		OPERACION_NUMERICA()
	elif token == "verdadero" or token == "falso" or token == "tk_neg" :
		OPERACION_BOOLEANA()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		ASIGNACION()
		match( "tk_par_der" )
	elif token == "tk_cadena" or token == "tk_caracter" :
		STRING()
	else:
		syntaxErr( 'id', 'tk_real', 'tk_entero', 'verdadero', 'falso', 'tk_neg', 'tk_par_izq', 'tk_cadena', 'tk_caracter' )

def ASIGNACION_LLAMADO_INSTANCIACION():
	global token
	if token == "tk_par_izq" :
		match( "tk_par_izq" )
		CONCAT()
		match( "tk_par_der" )
		match( "tk_pyc" )
	elif token == "tk_asig" :
		match( "tk_asig" )
		ASIGNACION()
		match( "tk_pyc" )
	elif token == "id" :
		match( "id" )
		match( "tk_pyc" )
	elif token == "tk_punto" :
		match( "tk_punto" )
		AGREG_ID_BODY()
		match( "tk_asig" )
		ASIGNACION()
		match( "tk_pyc" )
	else:
		syntaxErr( 'tk_par_izq', 'tk_asig', 'id', 'tk_punto' )

def AGREG_ID_BODY():
	global token
	if token == "id" :
		match( "id" )
		AGREG_ID_SIG_ATR_BODY()
	else:
		syntaxErr( 'id' )

def AGREG_ID_SIG_ATR_BODY():
	global token
	if token == "id" or token == "tk_asig" :
		pass
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR_BODY()
	else:
		syntaxErr( 'id', 'tk_asig', 'tk_punto' )

def CONDICIONAL():
	global token
	if token == "si" :
		match( "si" )
		match( "tk_par_izq" )
		OPERACION_MIXTA()
		match( "tk_par_der" )
		match( "entonces" )
		BODY_FUNCION()
		SINO()
		match( "fin_si" )
	else:
		syntaxErr( 'si' )

def OPERACION_BOOLEANA_MIXTA_CONDICIONAL():
	global token
	if token == "verdadero" :
		match( "verdadero" )
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "falso" :
		match( "falso" )
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "id" :
		match( "id" )
		AGREG_ID_BOOL_CONDICIONAL()
		BOOLEANA_O_NUMERICA()
	elif token == "tk_neg" :
		match( "tk_neg" )
		OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
		match( "tk_par_der" )
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	else:
		syntaxErr( 'verdadero', 'falso', 'id', 'tk_neg', 'tk_par_izq' )

def BOOLEANA_O_NUMERICA():
	global token
	if token == "tk_mas" :
		match( "tk_mas" )
		OPERACION_MIXTA()
		OPERACION_BOOLEANA_NUMERICA_CONDICIONAL()
	elif token == "tk_menos" :
		match( "tk_menos" )
		OPERACION_MIXTA()
		OPERACION_BOOLEANA_NUMERICA_CONDICIONAL()
	elif token == "tk_mult" :
		match( "tk_mult" )
		OPERACION_MIXTA()
		OPERACION_BOOLEANA_NUMERICA_CONDICIONAL()
	elif token == "tk_div" :
		match( "tk_div" )
		OPERACION_MIXTA()
		OPERACION_BOOLEANA_NUMERICA_CONDICIONAL()
	elif token == "tk_mod" :
		match( "tk_mod" )
		OPERACION_MIXTA()
		OPERACION_BOOLEANA_NUMERICA_CONDICIONAL()
	elif token == "tk_igual" :
		match( "tk_igual" )
		OPERACION_MIXTA()
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_mayor" :
		match( "tk_mayor" )
		OPERACION_MIXTA()
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_menor" :
		match( "tk_menor" )
		OPERACION_MIXTA()
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_mayor_igual" :
		match( "tk_mayor_igual" )
		OPERACION_MIXTA()
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_menor_igual" :
		match( "tk_menor_igual" )
		OPERACION_MIXTA()
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	else:
		syntaxErr( 'tk_mas', 'tk_menos', 'tk_mult', 'tk_div', 'tk_mod', 'tk_igual', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_y', 'tk_o' )

def DECISION_OPERACION():
	global token
	if token == "tk_real" or token == "tk_entero" :
		OPERACION_NUMERICA()
	elif token == "verdadero" or token == "falso" or token == "tk_neg" :
		OPERACION_BOOLEANA()
	else:
		syntaxErr( 'tk_real', 'tk_entero', 'verdadero', 'falso', 'tk_neg' )

def OPERACION_BOOLEANA_NUMERICA_CONDICIONAL():
	global token
	if token == "tk_igual" :
		match( "tk_igual" )
		OPERACION_MIXTA()
	elif token == "tk_mayor" :
		match( "tk_mayor" )
		OPERACION_MIXTA()
	elif token == "tk_menor" :
		match( "tk_menor" )
		OPERACION_MIXTA()
	elif token == "tk_mayor_igual" :
		match( "tk_mayor_igual" )
		OPERACION_MIXTA()
	elif token == "tk_menor_igual" :
		match( "tk_menor_igual" )
		OPERACION_MIXTA()
	elif token == "tk_dif" :
		match( "tk_dif" )
		OPERACION_MIXTA()
	else:
		syntaxErr( 'tk_igual', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_dif' )

def OP_BOOL_MIX_ANIDADA_CONDICIONAL():
	global token
	if token == "verdadero" :
		match( "verdadero" )
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "falso" :
		match( "falso" )
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "id" :
		match( "id" )
		AGREG_ID_BOOL_CONDICIONAL()
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_neg" :
		match( "tk_neg" )
		OP_BOOL_MIX_ANIDADA_CONDICIONAL()
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		OP_BOOL_MIX_ANIDADA()
		match( "tk_par_der" )
		SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	else:
		syntaxErr( 'verdadero', 'falso', 'id', 'tk_neg', 'tk_par_izq' )

def SIG_OPERACION_BOOLEANA_MIXTA_CONDICIONAL():
	global token
	if token == "tk_par_der" :
		pass
	elif token == "tk_y" :
		match( "tk_y" )
		OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	elif token == "tk_o" :
		match( "tk_o" )
		OPERACION_BOOLEANA_MIXTA_CONDICIONAL()
	else:
		syntaxErr( 'tk_par_der', 'tk_y', 'tk_o' )

def AGREG_ID_BOOL_CONDICIONAL():
	global token
	if token == "tk_mas" or token == "tk_menos" or token == "tk_mult" or token == "tk_div" or token == "tk_mod" or token == "tk_igual" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" or token == "tk_y" or token == "tk_o" :
		pass
	elif token == "tk_par_izq" :
		match( "tk_par_izq" )
		CONCAT()
		match( "tk_par_der" )
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR_BOOL_CONDICIONAL()
	else:
		syntaxErr( 'tk_mas', 'tk_menos', 'tk_mult', 'tk_div', 'tk_mod', 'tk_igual', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_y', 'tk_o', 'tk_par_izq', 'tk_punto' )

def AGREG_ID_SIG_ATR_BOOL_CONDICIONAL():
	global token
	if token == "tk_par_der" or token == "tk_mas" or token == "tk_menos" or token == "tk_mult" or token == "tk_div" or token == "tk_mod" or token == "tk_igual" or token == "tk_mayor" or token == "tk_menor" or token == "tk_mayor_igual" or token == "tk_menor_igual" or token == "tk_y" or token == "tk_o" :
		pass
	elif token == "tk_punto" :
		match( "tk_punto" )
		match( "id" )
		AGREG_ID_SIG_ATR_BOOL_CONDICIONAL()
	else:
		syntaxErr( 'tk_par_der', 'tk_mas', 'tk_menos', 'tk_mult', 'tk_div', 'tk_mod', 'tk_igual', 'tk_mayor', 'tk_menor', 'tk_mayor_igual', 'tk_menor_igual', 'tk_y', 'tk_o', 'tk_punto' )

def SINO():
	global token
	if token == "si_no" :
		match( "si_no" )
		BODY_FUNCION()
	elif token == "fin_si" :
		pass
	else:
		syntaxErr( 'si_no', 'fin_si' )

def CICLO():
	global token
	if token == "para" :
		match( "para" )
		match( "tk_par_izq" )
		TIPO_PARA()
		match( "id" )
		match( "tk_asig" )
		ASIGNACION()
		match( "tk_pyc" )
		OPERACION_MIXTA()
		match( "tk_pyc" )
		PASOS_PARA()
		match( "tk_par_der" )
		match( "hacer" )
		BODY_FUNCION()
		match( "fin_para" )
	elif token == "mientras" :
		match( "mientras" )
		match( "tk_par_izq" )
		OPERACION_MIXTA()
		match( "tk_par_der" )
		match( "hacer" )
		BODY_FUNCION()
		match( "fin_mientras" )
	elif token == "hacer" :
		match( "hacer" )
		BODY_FUNCION_CICLO()
		match( "mientras" )
		match( "tk_par_izq" )
		OPERACION_MIXTA()
		match( "tk_par_der" )
	else:
		syntaxErr( 'para', 'mientras', 'hacer' )

def BODY_FUNCION_CICLO():
	global token
	if token == "leer" or token == "imprimir" :
		COMANDO()
		BODY_FUNCION_CICLO()
	elif token == "entero" or token == "real" or token == "cadena" or token == "caracter" or token == "booleano" :
		DECLARACION_VARIABLE()
		BODY_FUNCION_CICLO()
	elif token == "id" :
		match( "id" )
		ASIGNACION_LLAMADO_INSTANCIACION()
		BODY_FUNCION_CICLO()
	elif token == "si" :
		CONDICIONAL()
		BODY_FUNCION_CICLO()
	elif token == "para" or token == "hacer" :
		CICLOS_ANIDADOS()
		BODY_FUNCION_CICLO()
	elif token == "seleccionar" :
		SELECCION()
		BODY_FUNCION_CICLO()
	elif token == "mientras" :
		pass
	else:
		syntaxErr( 'leer', 'imprimir', 'entero', 'real', 'cadena', 'caracter', 'booleano', 'id', 'si', 'para', 'hacer', 'seleccionar', 'mientras' )

def CICLOS_ANIDADOS():
	global token
	if token == "para" :
		match( "para" )
		match( "tk_par_izq" )
		TIPO_PARA()
		match( "id" )
		match( "tk_asig" )
		ASIGNACION()
		match( "tk_pyc" )
		OPERACION_BOOLEANA_MIXTA()
		match( "tk_pyc" )
		PASOS_PARA()
		match( "tk_par_der" )
		match( "hacer" )
		BODY_FUNCION()
		match( "fin_para" )
	elif token == "hacer" :
		match( "hacer" )
		BODY_FUNCION_CICLO()
		match( "mientras" )
		match( "tk_par_izq" )
		OPERACION_BOOLEANA_MIXTA()
		match( "tk_par_der" )
	else:
		syntaxErr( 'para', 'hacer' )

def PASOS_PARA():
	global token
	if token == "tk_real" :
		match( "tk_real" )
	elif token == "tk_entero" :
		match( "tk_entero" )
	elif token == "id" :
		match( "id" )
	else:
		syntaxErr( 'tk_real', 'tk_entero', 'id' )

def TIPO_PARA():
	global token
	if token == "id" :
		pass
	elif token == "booleano" or token == "real" or token == "caracter" or token == "cadena" or token == "entero" :
		TIPO()
	else:
		syntaxErr( 'id', 'booleano', 'real', 'caracter', 'cadena', 'entero' )

def SELECCION():
	global token
	if token == "seleccionar" :
		match( "seleccionar" )
		match( "tk_par_izq" )
		match( "id" )
		AGREG_ID_SIG_ATR_BOOL_CONDICIONAL()
		match( "tk_par_der" )
		CASOS()
		match( "fin_seleccionar" )
	else:
		syntaxErr( 'seleccionar' )

def CASOS():
	global token
	if token == "defecto" :
		SOLO_DEFECTO()
	elif token == "caso" :
		ESPECIFICOS()
	else:
		syntaxErr( 'defecto', 'caso' )

def SOLO_DEFECTO():
	global token
	if token == "defecto" :
		match( "defecto" )
		match( "tk_dosp" )
		BODY_FUNCION()
		ROMPER()
	else:
		syntaxErr( 'defecto' )

def ROMPER():
	global token
	if token == "romper" :
		match( "romper" )
		match( "tk_pyc" )
	elif token == "fin_seleccionar" :
		pass
	else:
		syntaxErr( 'romper', 'fin_seleccionar' )

def ESPECIFICOS():
	global token
	if token == "caso" :
		match( "caso" )
		TIPO_CASO()
		match( "tk_dosp" )
		BODY_FUNCION()
		ROMPER()
	else:
		syntaxErr( 'caso' )

def TIPO_CASO():
	global token
	if token == "tk_entero" :
		match( "tk_entero" )
	elif token == "tk_real" :
		match( "tk_real" )
	elif token == "tk_cadena" :
		match( "tk_cadena" )
	elif token == "tk_caracter" :
		match( "tk_caracter" )
	elif token == "verdadero" :
		match( "verdadero" )
	elif token == "falso" :
		match( "falso" )
	else:
		syntaxErr( 'tk_entero', 'tk_real', 'tk_cadena', 'tk_caracter', 'verdadero', 'falso' )

def RET():
	global token
	if token == "tk_par_izq" or token == "tk_entero" or token == "tk_real" or token == "id" :
		OPERACION_MIXTA()
		match( "tk_pyc" )
	else:
		syntaxErr( 'tk_par_izq', 'tk_entero', 'tk_real', 'id' )

def DE():
	global token
	if token == "estructura" :
		match( "estructura" )
		match( "id" )
		BODY_ESTRUCTURA()
		match( "fin_estructura" )
	else:
		syntaxErr( 'estructura' )

def BODY_ESTRUCTURA():
	global token
	if token == "booleano" or token == "real" or token == "caracter" or token == "cadena" or token == "entero" :
		TIPO()
		match( "id" )
		SIG_DECLARACION_ESTRUCTURA()
		match( "tk_pyc" )
		SIG_BODY_ESTRUCTURA()
	elif token == "id" :
		match( "id" )
		AGREG_ID_SIG_ATR_BODY()
		match( "id" )
		SIG_DECLARACION_ESTRUCTURA()
		match( "tk_pyc" )
		SIG_BODY_ESTRUCTURA()
	else:
		syntaxErr( 'booleano', 'real', 'caracter', 'cadena', 'entero', 'id' )

def SIG_BODY_ESTRUCTURA():
	global token
	if token == "fin_estructura" :
		pass
	elif token == "booleano" or token == "real" or token == "caracter" or token == "cadena" or token == "entero" :
		TIPO()
		match( "id" )
		SIG_DECLARACION_ESTRUCTURA()
		match( "tk_pyc" )
		SIG_BODY_ESTRUCTURA()
	elif token == "id" :
		match( "id" )
		AGREG_ID_SIG_ATR_BODY()
		match( "id" )
		SIG_DECLARACION_ESTRUCTURA()
		match( "tk_pyc" )
		SIG_BODY_ESTRUCTURA()
	else:
		syntaxErr( 'fin_estructura', 'booleano', 'real', 'caracter', 'cadena', 'entero', 'id' )

def SIG_DECLARACION_ESTRUCTURA():
	global token
	if token == "tk_coma" :
		match( "tk_coma" )
		match( "id" )
		SIG_DECLARACION_ESTRUCTURA()
	elif token == "tk_pyc" :
		pass
	else:
		syntaxErr( 'tk_coma', 'tk_pyc' )

def match( expectedToken ):
	global token
	if token == expectedToken:
		token = getNextToken(Control.estado, Control.token)
	else:
		syntaxErr( expectedToken )

def syntaxErr(*args):
	global token
	global orden
	preds = []
	arguments = str(args)
	args = list(args)
	if arguments[1:-2] == "'funcion_principal'":
		print('Error sintactico: falta funcion_principal')
		exit()
	print('<' + str(Control.fila) + ',' + str(Control.columna) + '> Error sintactico: se encontro: "' + str(token) +'"; se esperaba:',end="")
	for i in range(len(orden)):
		if orden[i] in arguments:
			preds.append(orden[i])
	if len(preds) == 1:
		print(' "' + preds[0] + '".',end="")
	else:
		for i in range(len(preds)-1):
			print(' "' + preds[i] + '",',end="")
		print(' "' + preds[len(preds)-1] + '"',end="")
		print(".")

	exit()

def main():
	global token
	readAllLines()
	token = getNextToken(Control.estado, Control.token)
	S()
	if token != 'EOF':
		syntaxErr('EOF')
	print('El analisis sintactico ha finalizado exitosamente.')

main()

#WARNING: This grammar is not LL1 and will not be usable for a syntax analyzer. The cause is either because it has left recursion (which is easy to check) or beacuse it has common elements on differente predictions set for a given non terminal.
#However, the code is still generated...