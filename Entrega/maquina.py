def getValue(direccion):
	#GLOBALES
	if direccion >= 1000 and direccion < 2000:
		return dir_int_globales[direccion - 1000]['Valor']
	elif direccion >= 2000 and direccion < 3000:
		return dir_float_globales[direccion - 2000]['Valor']
	elif direccion >= 3000 and direccion < 4000:
		return dir_char_globales[direccion - 3000]['Valor']
	elif direccion >= 4000 and direccion < 5000:
		return dir_string_globales[direccion - 4000]['Valor']
	elif direccion >= 5000 and direccion < 6000:
		return dir_bool_globales[direccion - 5000]['Valor']
	#LOCALES
	elif direccion >= 6000 and direccion < 7000:
		return dir_int_locales[direccion - 6000]['Valor']
	elif direccion >= 7000 and direccion < 8000:
		return dir_float_locales[direccion - 7000]['Valor']
	elif direccion >= 8000 and direccion < 9000:
		return dir_char_locales[direccion - 8000]['Valor']
	elif direccion >= 9000 and direccion < 10000:
		return dir_string_locales[direccion - 9000]['Valor']
	elif direccion >= 10000 and direccion < 11000:
		return dir_bool_locales[direccion - 10000]['Valor']
	#FUNCIONES
	elif direccion >= 11000 and direccion < 12000:
		return dir_int_funciones[direccion - 11000]['Valor']
	elif direccion >= 12000 and direccion < 13000:
		return dir_float_funciones[direccion - 12000]['Valor']
	elif direccion >= 13000 and direccion < 14000:
		return dir_char_funciones[direccion - 13000]['Valor']
	elif direccion >= 14000 and direccion < 15000:
		return dir_string_funciones[direccion - 14000]['Valor']
	elif direccion >= 15000 and direccion < 16000:
		return dir_bool_funciones[direccion - 15000]['Valor']
	#TEMPORALES
	elif direccion >= 16000 and direccion < 17000:
		return dir_int_temporales[direccion - 16000]['Valor']
	elif direccion >= 17000 and direccion < 18000:
		return dir_float_temporales[direccion - 17000]['Valor']
	elif direccion >= 18000 and direccion < 19000:
		return dir_char_temporales[direccion - 18000]['Valor']
	elif direccion >= 19000 and direccion < 20000:
		return dir_string_temporales[direccion - 19000]['Valor']
	elif direccion >= 20000 and direccion < 21000:
		return dir_bool_temporales[direccion - 20000]['Valor']
	#CONSTANTES
	elif direccion >= 21000 and direccion < 22000:
		return dir_int_constantes[direccion - 21000]['Valor']
	elif direccion >= 22000 and direccion < 23000:
		return dir_float_constantes[direccion - 22000]['Valor']
	elif direccion >= 23000 and direccion < 24000:
		return dir_char_constantes[direccion - 23000]['Valor']
	elif direccion >= 24000 and direccion < 25000:
		return dir_string_constantes[direccion - 24000]['Valor']
	elif direccion >= 25000 and direccion < 26000:
		return dir_bool_constantes[direccion - 25000]['Valor']
	else:
		return -1

def setValue(direccion, valor):
	#GLOBALES
	if direccion >= 1000 and direccion < 2000:
		dir_int_globales[direccion - 1000]['Valor']=valor
	elif direccion >= 2000 and direccion < 3000:
		dir_float_globales[direccion - 2000]['Valor']=valor
	elif direccion >= 3000 and direccion < 4000:
		dir_char_globales[direccion - 3000]['Valor']=valor
	elif direccion >= 4000 and direccion < 5000:
		dir_string_globales[direccion - 4000]['Valor']=valor
	elif direccion >= 5000 and direccion < 6000:
		dir_bool_globales[direccion - 5000]['Valor']=valor
	#LOCALES
	elif direccion >= 6000 and direccion < 7000:
		dir_int_locales[direccion - 6000]['Valor']=valor
	elif direccion >= 7000 and direccion < 8000:
		dir_float_locales[direccion - 7000]['Valor']=valor
	elif direccion >= 8000 and direccion < 9000:
		dir_char_locales[direccion - 8000]['Valor']=valor
	elif direccion >= 9000 and direccion < 10000:
		dir_string_locales[direccion - 9000]['Valor']=valor
	elif direccion >= 10000 and direccion < 11000:
		dir_bool_locales[direccion - 10000]['Valor']=valor
	#FUNCIONES
	elif direccion >= 11000 and direccion < 12000:
		dir_int_funciones[direccion - 11000]['Valor']=valor
	elif direccion >= 12000 and direccion < 13000:
		dir_float_funciones[direccion - 12000]['Valor']=valor
	elif direccion >= 13000 and direccion < 14000:
		dir_char_funciones[direccion - 13000]['Valor']=valor
	elif direccion >= 14000 and direccion < 15000:
		dir_string_funciones[direccion - 14000]['Valor']=valor
	elif direccion >= 15000 and direccion < 16000:
		dir_bool_funciones[direccion - 15000]['Valor']=valor
	#TEMPORALES
	elif direccion >= 16000 and direccion < 17000:
		dir_int_temporales[direccion - 16000]['Valor']=valor
	elif direccion >= 17000 and direccion < 18000:
		dir_float_temporales[direccion - 17000]['Valor']=valor
	elif direccion >= 18000 and direccion < 19000:
		dir_char_temporales[direccion - 18000]['Valor']=valor
	elif direccion >= 19000 and direccion < 20000:
		dir_string_temporales[direccion - 19000]['Valor']=valor
	elif direccion >= 20000 and direccion < 21000:
		dir_bool_temporales[direccion - 20000]['Valor']=valor
	#CONSTANTES
	elif direccion >= 21000 and direccion < 22000:
		dir_int_constantes[direccion - 21000]['Valor']=valor
	elif direccion >= 22000 and direccion < 23000:
		dir_float_constantes[direccion - 22000]['Valor']=valor
	elif direccion >= 23000 and direccion < 24000:
		dir_char_constantes[direccion - 23000]['Valor']=valor
	elif direccion >= 24000 and direccion < 25000:
		dir_string_constantes[direccion - 24000]['Valor']=valor
	elif direccion >= 25000 and direccion < 26000:
		dir_bool_constantes[direccion - 25000]['Valor']=valor

def test():
	auxCont = contCuadruplos
	while cuadruplos[auxCont][0] != ENDPROGRAM:
		cuadruploActual = cuadruplos[auxCont]

		if cuadruploActual[0] == ASIG:
			operando1= cuadruploActual[1]
			operando1= getValue(operando1)
			resultado= cuadruploActual[3]
			setValue(resultado, operando1)

		if cuadruploActual[0] == SUMA:
			operando1= cuadruploActual[1]
			operando1= getValue(operando1)
			operando2= cuadruploActual[2]
			operando2= getValue(operando2)
			resultado= cuadruploActual[3]
			setValue(resultado, operando1+operando2)


