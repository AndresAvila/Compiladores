# Yacc example

import ply.yacc as yacc
import MyLittleDuckl
import sys 
import cubo


# Get the token map from the lexer.  This is required.
from MyLittleDuckl import tokens
from collections import deque


tokens = MyLittleDuckl.tokens   
varDirectory = {}
varDirectoryMain = {}
varDirectoryFunc = {}
procDirectory = {}
varList = []
varListMain = []
varListFuncion = []
dirProcedure = {}
dirConstantes = {}
dirTemporales = {}

funcActual = ""

cuadruplos = {}
pOperadores = []
pOperandos = []
pTipos = []
contTemporales = 0
contCuadruplos = 40001
contParametros = 0
contVarLocFunc = 0
pSaltos = []

parametrosA = {}
decNumParametro = 0
numArgumento = 0
#pSaltos = deque([])

cubo = cubo.cubo
print(cubo[1][1][1])

#Lista Direcciones
##GLOBALES
dir_int_globales=[]
inicia_int_globales=1000
cont_int_globales=0

dir_float_globales=[]
inicia_float_globales=2000
cont_float_globales=0

dir_char_globales=[]
inicia_char_globales=3000
cont_char_globales=0

dir_string_globales=[]
inicia_string_globales=4000
cont_string_globales=0

dir_bool_globales=[]
inicia_bool_globales=5000
cont_bool_globales=0

##LOCALES
dir_int_locales=[]
inicia_int_locales=6000
cont_int_locales=0

dir_float_locales=[]
inicia_float_locales=7000
cont_float_locales=0

dir_char_locales=[]
inicia_char_locales=8000
cont_char_locales=0

dir_string_locales=[]
inicia_string_locales=9000
cont_string_locales=0

dir_bool_locales=[]
inicia_bool_locales=10000
cont_bool_locales=0

##FUNCIONES
dir_int_funciones=[]
inicia_int_funciones=11000
cont_int_funciones=0

dir_float_funciones=[]
inicia_float_funciones=12000
cont_float_funciones=0

dir_char_funciones=[]
inicia_char_funciones=13000
cont_char_funciones=0

dir_string_funciones=[]
inicia_string_funciones=14000
cont_string_funciones=0

dir_bool_funciones=[]
inicia_bool_funciones=15000
cont_bool_funciones=0

##TEMPORALES
dir_int_temporales=[]
inicia_int_temporales=16000
cont_int_temporales=0

dir_float_temporales=[]
inicia_float_temporales=17000
cont_float_temporales=0

dir_char_temporales=[]
inicia_char_temporales=18000
cont_char_temporales=0

dir_string_temporales=[]
inicia_string_temporales=19000
cont_string_temporales=0

dir_bool_temporales=[]
inicia_bool_temporales=20000
cont_bool_temporales=0

##CONSTANTES
dir_int_constantes=[]
inicia_int_constantes=21000
cont_int_constantes=0

dir_float_constantes=[]
inicia_float_constantes=22000
cont_float_constantes=0

dir_char_constantes=[]
inicia_char_constantes=23000
cont_char_constantes=0

dir_string_constantes=[]
inicia_string_constantes=24000
cont_string_constantes=0

dir_bool_constantes=[]
inicia_bool_constantes=25000
cont_bool_constantes=0

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5

#Tipo
INT = 1
FLOAT = 4
CHAR = 5
BOOL = 2
STRING = 3

#Operaciones
SUMA = 1
RESTA = 2
MULT = 3
DIV = 4
ASIG = 13
OR = 6
AND = 5
MAYOR = 8
MENOR = 7
MAYORIG = 10
MENORIG = 9
IGUAL = 11
DIF = 12
GOTO = 14
GOTOF = 15
GOTOV = 16
PRINT = 17
ERA = 18
GOSUB = 19
RET = 20
RETURN = 21
PARAM = 22
ENDPROC = 23
ENDPROGRAM = 24
ERR = -1

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

def maquina():
    auxCont = 40001
    while cuadruplos[auxCont][0] != ENDPROGRAM:
        cuadruploActual = cuadruplos[auxCont]
        print("here ", auxCont)
        print("cuadruplo: ", cuadruploActual)

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

        if cuadruploActual[0] == RESTA:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]
            setValue(resultado, operando1-operando2)

        if cuadruploActual[0] == MULT:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]
            setValue(resultado, operando1*operando2)

        if cuadruploActual[0] == DIV:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]
            setValue(resultado, operando1/operando2)

        if cuadruploActual[0] == OR:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1=="true" or operando2=="true"):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == AND:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1=="true" and operando2=="true"):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == MAYOR:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1>operando2):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == MENOR:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1<operando2):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == MAYORIG:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1>=operando2):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == MENORIG:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1<=operando2):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == IGUAL:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]

            if (operando1==operando2):
                setValue(resultado, "true")
            else:
                setValue(resultado, "false")

        if cuadruploActual[0] == DIF:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            operando2= cuadruploActual[2]
            operando2= getValue(operando2)
            resultado= cuadruploActual[3]
            print(operando1)
            print(operando2)
            if (operando1==operando2):
                setValue(resultado, "false")
            else:
                setValue(resultado, "true")

        if cuadruploActual[0] == GOTO:
            resultado = cuadruploActual[3]

            auxCont = resultado-1

        if cuadruploActual[0] == GOTOF:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            resultado= cuadruploActual[3]

            if operando1 == "false":
                auxCont = resultado-1

        if cuadruploActual[0] == GOTOV:
            operando1= cuadruploActual[1]
            operando1= getValue(operando1)
            resultado= cuadruploActual[3]

            if operando1 == "true":
                auxCont = resultado-1


        auxCont += 1

def p_programa(p): #Done
    '''programa : PROGRAM ID addProcedureDir SEMICOLON paso19 cicloVars cicloFuncion MAIN paso20 bloque pasoFinal'''
    p[0] = "OK"

def p_addProcedureDir(p):
    '''addProcedureDir : '''
    #print("Pasa por addProcedureDir")
    dirProcedure[p[-1]] = {'Variables' : varDirectory.copy(), 'Tipo' : p[-2]} 
    varDirectory.clear()
    #print("TERMINA addProcedureDir")
    print(dirProcedure)

def p_cicloVars(p): #Done
    '''cicloVars : vars cicloVars 
        |'''

def p_vars(p): #Done
    '''vars : createVariableDir VAR auxVar1 '''

def p_createVariableDir(p):
    '''createVariableDir : '''
    varDirectory = {}
    #print("Pasa por createVariableDir")

def p_auxVar1(p): #Done
    '''auxVar1 : idVars COLON tipo addTypeGlobal SEMICOLON'''

def p_addTypeGlobal(p):
    '''addTypeGlobal : '''
    #print("pasa por addTypeGlobal")
    global cont_int_globales
    global cont_float_globales
    global cont_bool_globales
    global cont_char_globales
    global cont_string_globales
    while (len(varList) > 0):
        variable = varList.pop()
        if(translate(p[-1]) == 1):
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_int_globales + cont_int_globales}
            dir_int_globales.append({'Valor' : 0, 'Direccion' : inicia_int_globales + cont_int_globales, 'Arreglo' : ''})
            cont_int_globales += 1
        elif(translate(p[-1]) == 2):
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_bool_globales + cont_bool_globales}
            dir_bool_globales.append({'Valor' : '', 'Direccion' : inicia_bool_globales + cont_bool_globales, 'Arreglo' : ''})
            cont_bool_globales += 1
        elif(translate(p[-1]) == 3):
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_string_globales + cont_string_globales}
            dir_string_globales.append({'Valor' : '', 'Direccion' : inicia_string_globales + cont_string_globales, 'Arreglo' : ''})
            cont_string_globales += 1
        elif(translate(p[-1]) == 4):
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_float_globales + cont_float_globales}
            dir_float_globales.append({'Valor' : 0.0, 'Direccion' : inicia_float_globales + cont_float_globales, 'Arreglo' : ''})
            cont_float_globales += 1
        elif(translate(p[-1]) == 5):
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_char_globales + cont_char_globales}
            dir_char_globales.append({'Valor' : '', 'Direccion' : inicia_char_globales + cont_char_globales, 'Arreglo' : ''})
            cont_char_globales += 1
    #print("TERMINA addTypeGlobal")
    print(varDirectory)


def p_idVars(p): #Done
    '''idVars : ID addVariableDir ambIdVars '''

def p_addVariableDir(p):
    '''addVariableDir : '''
    #print("pasa por addVariableDir")
    if (p[-1] in varDirectory):
        print("Ya existe la variable")
        exit()
    else:

        varList.append(p[-1])
        #print("Se agrego ")
        

def p_ambIdVars(p): #Done
    '''ambIdVars : COMMA idVars
        |'''

def p_tipo(p): #Done
    '''tipo : INT ambAuxTipo1
        | BOOL ambAuxTipo1
        | STRING ambAuxTipo1
        | FLOAT ambAuxTipo1
        | CHAR ambAuxTipo1'''
    p[0] = p[1]


def p_ambAuxTipo1(p):
    '''ambAuxTipo1 : LBRACKET CTEINT RBRACKET
        | ''' 

def p_cicloVarsMain(p): #Done
    '''cicloVarsMain : varsMain cicloVarsMain 
        | '''

def p_varsMain(p): #Done
    '''varsMain : createVariableDirMain VAR auxVar1Main'''

def p_createVariableDirMain(p):
    '''createVariableDirMain : '''
    varDirectoryMain = {}
    #print("Pasa por createVariableDirMain")

def p_auxVar1Main(p): #Done
    '''auxVar1Main : idVarsMain COLON tipo addTypeMain SEMICOLON'''

def p_addTypeMain(p):
    '''addTypeMain : '''
    #print("pasa por addTypeMain")
    global cont_int_locales
    global cont_float_locales
    global cont_bool_locales
    global cont_char_locales
    global cont_string_locales
    while (len(varListMain) > 0):
        variable = varListMain.pop()
        if(translate(p[-1]) == 1):
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_int_locales + cont_int_locales}
            dir_int_locales.append({'Valor' : 0, 'Direccion' : inicia_int_locales + cont_int_locales, 'Arreglo' : ''})
            cont_int_locales += 1
        elif(translate(p[-1]) == 2):
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_bool_locales + cont_bool_locales}
            dir_bool_locales.append({'Valor' : '', 'Direccion' : inicia_bool_locales + cont_bool_locales, 'Arreglo' : ''})
            cont_bool_locales += 1
        elif(translate(p[-1]) == 3):
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_string_locales + cont_string_locales}
            dir_string_locales.append({'Valor' : '', 'Direccion' : inicia_string_locales + cont_string_locales, 'Arreglo' : ''})
            cont_string_locales += 1
        elif(translate(p[-1]) == 4):
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_float_locales + cont_float_locales}
            dir_float_locales.append({'Valor' : 0.0, 'Direccion' : inicia_float_locales + cont_float_locales, 'Arreglo' : ''})
            cont_float_locales += 1
        elif(translate(p[-1]) == 5):
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_char_locales + cont_char_locales}
            dir_char_locales.append({'Valor' : '', 'Direccion' : inicia_char_locales + cont_char_locales, 'Arreglo' : ''})
            cont_char_locales += 1
    #print("TERMINA addTypfunciones
    print(varDirectoryMain)


def p_idVarsMain(p): #Done
    '''idVarsMain : ID addVariableDirMain ambIdVarsMain '''

def p_addVariableDirMain(p):
    '''addVariableDirMain : '''
    #print("pasa por addVariableDirMain")
    if (p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
        exit()
    else:
        varListMain.append(p[-1])
        #print("Se agrego ")
        

def p_ambIdVarsMain(p): #Done
    '''ambIdVarsMain : COMMA idVarsMain
        | '''

def p_bloque(p): #Done
    '''bloque : LBRACE cicloVarsMain cicloBloque RBRACE'''

def p_cicloBloque(p): #Done
    '''cicloBloque : estatuto cicloBloque 
        | '''

def p_bloqueFuncion(p): #Done
    '''bloqueFuncion : LBRACE cicloVarsFuncion paso21 cicloBloqueFuncion RETURN expresion SEMICOLON RBRACE'''

def p_cicloBloqueFuncion(p): #Done
    '''cicloBloqueFuncion : estatuto cicloBloqueFuncion 
        | '''

def p_cicloVarsFuncion(p): #Done
    '''cicloVarsFuncion : varsFuncion cicloVarsFuncion 
        | '''

def p_varsFuncion(p): #Done
    '''varsFuncion : createVariableDirFuncion VAR auxVar1Funcion'''

def p_createVariableDirFuncion(p):
    '''createVariableDirFuncion : '''
    varDirectoryFunc = {}
    #print("Pasa por createVariableDirFuncion")

def p_auxVar1Funcion(p): #Done
    '''auxVar1Funcion : idVarsFuncion COLON tipo addTypeFuncion SEMICOLON'''

def p_addTypeFuncion(p):
    '''addTypeFuncion : '''
    #print("pasa por addTypeFuncion")
    global cont_int_funciones
    global cont_float_funciones
    global cont_bool_funciones
    global cont_char_funciones
    global cont_string_funciones
    while (len(varListFuncion) > 0):
        variable = varListFuncion.pop()
        if(translate(p[-1]) == 1):
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_int_funciones + cont_int_funciones}
            dir_int_funciones.append({'Valor' : 0, 'Direccion' : inicia_int_funciones + cont_int_funciones, 'Arreglo' : ''})
            cont_int_funciones += 1
        elif(translate(p[-1]) == 2):
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_bool_funciones + cont_bool_funciones}
            dir_bool_funciones.append({'Valor' : '', 'Direccion' : inicia_bool_funciones + cont_bool_funciones, 'Arreglo' : ''})
            cont_bool_funciones += 1
        elif(translate(p[-1]) == 3):
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_string_funciones + cont_string_funciones}
            dir_string_funciones.append({'Valor' : '', 'Direccion' : inicia_string_funciones + cont_string_funciones, 'Arreglo' : ''})
            cont_string_funciones += 1
        elif(translate(p[-1]) == 4):
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_float_funciones + cont_float_funciones}
            dir_float_funciones.append({'Valor' : 0.0, 'Direccion' : inicia_float_funciones + cont_float_funciones, 'Arreglo' : ''})
            cont_float_funciones += 1
        elif(translate(p[-1]) == 5):
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_char_funciones + cont_char_funciones}
            dir_char_funciones.append({'Valor' : '', 'Direccion' : inicia_char_funciones + cont_char_funciones, 'Arreglo' : ''})
            cont_char_funciones += 1
    #print("TERMINA addTypeFuncion")
    #print(varDirectoryFunc)


def p_idVarsFuncion(p): #Done
    '''idVarsFuncion : ID addVariableDirFuncion ambIdVarsFuncion '''

def p_addVariableDirFuncion(p):
    '''addVariableDirFuncion : '''
    global contVarLocFunc
    #print("pasa por addVariableDirFuncion")
    if (p[-1] in varDirectoryFunc or p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
        exit()
    else:
        print("Se agrego ")
        varListFuncion.append(p[-1])
        contVarLocFunc += 1
        
        

def p_ambIdVarsFuncion(p): #Done
    '''ambIdVarsFuncion : COMMA idVarsFuncion
        | '''

def p_estatuto(p): #Done
    '''estatuto : asignacion
        | condicion
        | escritura
        | ciclo '''

    #print("entra a estatuto")

def p_asignacion(p): #Done
    '''asignacion : ID paso1 addType auxAsignacion1 EQUALA asig exp paso11 SEMICOLON'''
    #print("entra a asignacion")

def p_auxAsignacion1(p): #Done
    '''auxAsignacion1 : LBRACKET exp RBRACKET 
        | '''

def p_escritura(p): #Done
    '''escritura : PRINT LPAREN auxEscritura1 RPAREN SEMICOLON'''
    #print("entra a escritura")

def p_auxEscritura1(p): #Done
    '''auxEscritura1 : auxEscritura2 paso18 ambAuxEscritura1'''

def p_ambAuxEscritura1(p): #Done
    '''ambAuxEscritura1 : COMMA auxEscritura1
        | '''

def p_auxEscritura2(p): #Done
    '''auxEscritura2 : exp 
        | CTESTRING paso1 '''

def p_cicloExpresion(p):
    '''cicloExpresion : expresion paso10  '''


def p_auxCicloExpresion(p):
    '''auxCicloExpresion : AND paso8_and cicloExpresion paso9 auxCicloExpresion
        | OR paso8_or cicloExpresion paso9 auxCicloExpresion
        | '''

def p_expresion(p): #Done
    '''expresion : exp auxExpresion '''


def p_auxExpresion(p): #Done
    '''auxExpresion : GTHAN mayor exp
        | LTHAN menor exp
        | NOTEQUAL diferente exp
        | GETHAN mayorIg exp
        | LETHAN menorIg exp
        | EQUAL igual exp
        | '''

def p_expAndOr(p): 
    '''expAndOr : cicloExpresion auxCicloExpresion '''

def p_condicion(p): #Done
    '''condicion : IF LPAREN expAndOr paso12 RPAREN bloque auxCondicion paso14'''
    #print("entra a condicion")

def p_auxCondicion(p): #Done
    '''auxCondicion : ELSE paso13 bloque
        | '''

def p_exp(p): #Done
    '''exp : cicloExp'''

def p_cicloExp(p): #Done
    '''cicloExp : termino paso4 ambExp'''

def p_ambExp(p): #Done
    '''ambExp : auxExp cicloExp
        | '''

def p_auxExp(p): #Done
    '''auxExp : PLUS paso3_suma
        | MINUS paso3_resta'''

def p_termino(p): #Done
    ''' termino : cicloTermino'''

def p_cicloTermino(p): #Done
    '''cicloTermino : factor paso5 ambCicloTermino'''

def p_ambCicloTermino(p): #Done
    '''ambCicloTermino : auxTermino cicloTermino
        | '''

def p_auxTermino(p): #Done
    '''auxTermino : MULTI paso2_mult
        | DIVIDE paso2_div'''

def p_factor(p): #Done
    ''' factor : LPAREN paso6 exp RPAREN paso7
        | auxFactor varcte '''

def p_auxFactor(p): #Done
    '''auxFactor : auxExp
        | '''

def p_varcte(p): #Done
    '''varcte : ID paso1 addType auxVarcte
        | CTEINT paso1 cteInt assignDirectionCteInt
        | CTEFLOAT paso1 cteFloat assignDirectionCteFloat
        | CTECHAR paso1 cteChar assignDirectionCteChar
        | CTEBOOL paso1 cteBool assignDirectionCteBool
        | CTESTRING paso1 cteString assignDirectionCteString
        | llamada '''

def p_assignDirectionCteInt(p):
    '''assignDirectionCteInt :'''
    global cont_int_constantes
    global inicia_int_constantes
    if p[-3] not in dirConstantes.keys():
        dir_int_constantes.append({'Valor' : int(p[-3]), 'Direccion' : inicia_int_constantes + cont_int_constantes, 'Arreglo' : ''})
        dirConstantes[p[-3]] = {'Direccion' : inicia_int_constantes + cont_int_constantes, 'Tipo' : 1}
        cont_int_constantes += 1
        print("esto es: ", dir_int_constantes)


def p_assignDirectionCteFloat(p):
    '''assignDirectionCteFloat :'''
    global cont_float_constantes
    if p[-3] not in dirConstantes.keys():
        dir_float_constantes.append({'Valor' : float(p[-3]), 'Direccion' : inicia_float_constantes + cont_float_constantes, 'Arreglo' : ''})
        dirConstantes[p[-3]] = {'Direccion' : inicia_float_constantes + cont_float_constantes, 'Tipo' : 4}
        cont_float_constantes += 1

def p_assignDirectionCteChar(p):
    '''assignDirectionCteChar :'''
    global cont_char_constantes
    if p[-3] not in dirConstantes.keys():
        dir_char_constantes.append({'Valor' : p[-3], 'Direccion' : inicia_char_constantes + cont_char_constantes, 'Arreglo' : ''})
        dirConstantes[p[-3]] = {'Direccion' : inicia_char_constantes + cont_char_constantes, 'Tipo' : 5}
        cont_char_constantes += 1

def p_assignDirectionCteBool(p):
    '''assignDirectionCteBool :'''
    global cont_bool_constantes
    if p[-3] not in dirConstantes.keys():
        print("HEY")
        dir_bool_constantes.append({'Valor' : p[-3][1:], 'Direccion' : inicia_bool_constantes + cont_bool_constantes, 'Arreglo' : ''})
        dirConstantes[p[-3]] = {'Direccion' : inicia_bool_constantes + cont_bool_constantes, 'Tipo' : 2}
        cont_bool_constantes += 1

def p_assignDirectionCteString(p):
    '''assignDirectionCteString :'''
    global cont_string_constantes
    if p[-3] not in dirConstantes.keys():
        dir_string_constantes.append({'Valor' : p[-3], 'Direccion' : inicia_string_constantes + cont_string_constantes, 'Arreglo' : ''})
        dirConstantes[p[-3]] = {'Direccion' : inicia_string_constantes + cont_string_constantes, 'Tipo' : 3}
        cont_string_constantes += 1

def translate(x):
    if x == "int":
        return 1
    elif x == "bool":
        return 2
    elif x == "string":
        return 3
    elif x == "float":
        return 4
    elif x == "char":
        return 5
    else:
        return -1

def p_addType(p):
    '''addType : '''
    if p[-2] in varDirectory.keys():
        print(translate(varDirectory[p[-2]]['Tipo']))
        pTipos.append(translate(varDirectory[p[-2]]['Tipo']))
    elif p[-2] in varDirectoryMain.keys():
        print(translate(varDirectoryMain[p[-2]]['Tipo']))
        pTipos.append(translate(varDirectoryMain[p[-2]]['Tipo']))
    elif p[-2] in varDirectoryFunc.keys():
        print(translate(varDirectoryFunc[p[-2]]['Tipo']))
        pTipos.append(translate(varDirectoryFunc[p[-2]]['Tipo']))
    else:
        return -1


def p_auxVarcte(p): #Done
    '''auxVarcte : LPAREN exp RPAREN
        | LBRACKET exp LBRACKET 
        | '''

def p_cicloFuncion(p): #Done
    '''cicloFuncion : funcion cicloFuncion 
        | '''

def p_funcion(p): #Done
    '''funcion : FUNCTION tipo ID initDicFunc LPAREN auxFunction RPAREN bloqueFuncion addProcDirectoryFunc paso22 paso23'''

def p_addProcDirectoryFunc(p):
    '''addProcDirectoryFunc : '''
    global contParametros
    global contVarLocFunc
    procDirectory[funcActual]['Variables'] = varDirectoryFunc.copy()
    procDirectory[funcActual]['Tipo'] = p[-7]
    procDirectory[funcActual]['# Parametros'] = contParametros
    procDirectory[funcActual]['Locales'] = contVarLocFunc

    #procDirectory[p[-6]] = {'Variables' : varDirectoryFunc.copy(), 'Tipo' : p[-6], 'Parametros' : contParametros, 'Locales' : contVarLocFunc, 'Inicio' : contCuadruplos }
    #varDirectoryFunc.clear()
    contParametros = 0
    contVarLocFunc = 0
    #print("pasa por addProcDirectoryFunc")
    print(procDirectory)

def p_initDicFunc(p):
    '''initDicFunc : '''
    global funcActual
    funcActual = p[-1]
    procDirectory[p[-1]] = {'Variables' : "", 'Tipo' : "", '# Parametros' : 0, 'Locales' : 0, 'Inicio' : 0, 'Retorno' : 0, 'Parametros' : 0 }

def p_auxFunction(p): #Done
    '''auxFunction : parametros
        | '''

def p_parametros(p): # Done
    '''parametros : auxParametros '''

def p_auxParametros(p): #Done
    '''auxParametros : tipo ID addParameters ambAuxParametros'''

def p_addParameters(p):
    '''addParameters : '''
    global contParametros
    global funcActual
    global decNumParametro
    if (p[-1] in varDirectoryFunc or p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
    else:
        #print("Se agrego ")
        contParametros += 1
        varListFuncion.append(p[-1])
    while (len(varListFuncion) > 0):
        #print("entra loop addTypeFuncion")
        varDirectoryFunc[varListFuncion.pop()] = {'Tipo' : p[-2], 'Scope' : 'Funcion', 'Direccion': getBaseFuncDirection(translate(p[-2])) + getFuncCounter(translate(p[-2]))}
        varListFuncion.append(p[-1])
        decNumParametro += 1
        parametrosA[varListFuncion.pop()] = {'Valor' : 0, 'Tipo' : p[-2], 'NumParametro' : decNumParametro, 'Direccion': getBaseFuncDirection(translate(p[-2])) + getFuncCounter(translate(p[-2]))}
        changeFuncCounter(translate(p[-2]))
        procDirectory[funcActual]['Parametros'] = parametrosA.copy()
        

def p_ambAuxParamentros(p): #Done
    '''ambAuxParametros : COMMA auxParametros
        | '''

def p_ciclo(p): #Done
    '''ciclo : WHILE paso15 LPAREN expAndOr RPAREN paso16 bloque paso17'''
    #print("entra a ciclo")

def p_llamada(p): #Done
    '''llamada : CALL COLON ID paso24 cteLlamada LPAREN auxLlamada RPAREN paso26'''
    print("entra a llamada")

def p_auxLlamada(p): #Done
    '''auxLlamada : argumentos
        | '''

def p_argumentos(p): #Done
    ''' argumentos : auxArgumentos1
        | '''

def p_auxArgumentos1(p): #Done
    '''auxArgumentos1 : exp paso25 ambAuxArgumentos1'''

def p_ambAuxArgumentos1(p): #Done
    '''ambAuxArgumentos1 : COMMA auxArgumentos1
        | '''

def p_lectura(p): #Done
    ''' lectura : READ LPAREN ID RPAREN SEMICOLON '''
    #print("entra a lectura")

def encuentraOperando(x):
    if x in varDirectory:
        return varDirectory[x].get('Direccion')
    if x in varDirectoryMain:
        return varDirectoryMain[x].get('Direccion')
    if x in varDirectoryFunc:
        return varDirectoryFunc[x].get('Direccion')

#Cuadruplos
def p_paso1(p):
    '''paso1 : '''
    #print(p[-1])
    print(encuentraOperando(p[-1]))
    pOperandos.append(p[-1])

def p_paso2_mult(p):
    '''paso2_mult : '''
    pOperadores.append(MULT)

def p_paso2_div(p):
    '''paso2_div : '''
    pOperadores.append(DIV)

def p_paso3_suma(p):
    '''paso3_suma : '''
    pOperadores.append(SUMA)

def p_paso3_resta(p):
    '''paso3_resta : '''
    pOperadores.append(RESTA)

def translateToDirection(variable):
    #print("BEFORE IF:", variable)
    #print("vardirfunc", varDirectoryFunc)
    if variable in varDirectoryMain.keys():
        return varDirectoryMain[variable].get('Direccion')
    elif variable in varDirectory.keys():
        return varDirectory[variable].get('Direccion')
    elif variable in varDirectoryFunc.keys():
        #print("ELIF 3", varDirectoryFunc)
        return varDirectoryFunc[variable].get('Direccion')
    elif variable in dirConstantes.keys():
        return dirConstantes[variable].get('Direccion')
    elif variable in parametrosA.keys():
        #print("ELIF 5", parametrosA)
        return parametrosA[variable].get('Direccion')
    elif variable in dirConstantes.keys():
        return dirConstantes[variable].get('Direccion')
    else:
        return variable

def getBaseFuncDirection(type):
    if type == 1:
        return 11000
    elif type == 4:
        return 12000
    elif type == 5:
        return 13000
    elif type == 3:
        return 14000
    elif type == 2:
        return 15000
    else:
        return -1

def getFuncCounter(type):
    global cont_int_funciones
    global cont_bool_funciones
    global cont_string_funciones
    global cont_float_funciones
    global cont_char_funciones
    if type == 1:
        return cont_int_funciones
    elif type == 4:
        return cont_float_funciones
    elif type == 5:
        return cont_char_funciones
    elif type == 3:
        return cont_string_funciones
    elif type == 2:
        return cont_bool_funciones
    else:
        return -1

def changeFuncCounter(type):
    global cont_int_funciones
    global cont_bool_funciones
    global cont_string_funciones
    global cont_float_funciones
    global cont_char_funciones
    if type == 1:
        dir_int_funciones.append({'Valor' : 0, 'Direccion' : inicia_int_funciones + cont_int_funciones, 'Arreglo' : ''})
        cont_int_funciones += 1
    elif type == 4:
        dir_float_funciones.append({'Valor' : 0.0, 'Direccion' : inicia_float_funciones + cont_float_funciones, 'Arreglo' : ''})
        cont_float_funciones += 1
    elif type == 5:
        dir_char_funciones.append({'Valor' : '', 'Direccion' : inicia_char_funciones + cont_char_funciones, 'Arreglo' : ''})
        cont_char_funciones += 1
    elif type == 3:
        dir_string_funciones.append({'Valor' : '', 'Direccion' : inicia_string_funciones + cont_string_funciones, 'Arreglo' : ''})
        cont_string_funciones += 1
    elif type == 2:
        dir_bool_funciones.append({'Valor' : '', 'Direccion' : inicia_bool_funciones + cont_bool_funciones, 'Arreglo' : ''})
        cont_bool_funciones += 1
    else:
        pass

def getBaseTemporalDirection(type):
    if type == 1:
        return 16000
    elif type == 4:
        return 17000
    elif type == 5:
        return 18000
    elif type == 3:
        return 19000
    elif type == 2:
        return 20000
    else:
        return -1

def getTemporalCounter(type):
    global cont_int_temporales
    global cont_bool_temporales
    global cont_string_temporales
    global cont_float_temporales
    global cont_char_temporales
    if type == 1:
        return cont_int_temporales
    elif type == 4:
        return cont_float_temporales
    elif type == 5:
        return cont_char_temporales
    elif type == 3:
        return cont_string_temporales
    elif type == 2:
        return cont_bool_temporales
    else:
        return -1

def changeTemporalCounter(type):
    global cont_int_temporales
    global cont_bool_temporales
    global cont_string_temporales
    global cont_float_temporales
    global cont_char_temporales
    if type == 1:
        dir_int_temporales.append({'Valor' : 0, 'Direccion' : inicia_int_temporales + cont_int_temporales, 'Arreglo' : ''})
        cont_int_temporales += 1
    elif type == 4:
        dir_float_temporales.append({'Valor' : 0.0, 'Direccion' : inicia_float_temporales + cont_float_temporales, 'Arreglo' : ''})
        cont_float_temporales += 1
    elif type == 5:
        dir_char_temporales.append({'Valor' : '', 'Direccion' : inicia_char_temporales + cont_char_temporales, 'Arreglo' : ''})
        cont_char_temporales += 1
    elif type == 3:
        dir_string_temporales.append({'Valor' : '', 'Direccion' : inicia_string_temporales + cont_string_temporales, 'Arreglo' : ''})
        cont_string_temporales += 1
    elif type == 2:
        dir_bool_temporales.append({'Valor' : '', 'Direccion' : inicia_bool_temporales + cont_bool_temporales, 'Arreglo' : ''})
        cont_bool_temporales += 1
    else:
        pass

def p_paso4(p):
    '''paso4 : '''
    global pOperadores
    global pTipos
    #print("Entra paso4")
    global contTemporales
    global contCuadruplos
    print(funcActual)
    if pOperadores :
        if pOperadores[-1] == SUMA or pOperadores[-1]== RESTA :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            opdoDerDir = translateToDirection(opdoDer)
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            opdoIzqDir = translateToDirection(opdoIzq)
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and (cubo[tipoDer][tipoIzq][op] == INT or cubo[tipoDer][tipoIzq][op] == FLOAT) :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzqDir, opdoDerDir, getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes)]
                pOperandos.append(getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes))
                pTipos.append(tipoRes)
                changeTemporalCounter(tipoRes)
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error arimetico 4 - tipos no validos")
                exit()
    #print("Sale paso 4") 


def p_paso5(p):
    '''paso5 : '''
    global pTipos
    global pOperadores
    #print("Entra paso 5")
    #print(pTipos)
    #print(pOperandos)
    
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == MULT or pOperadores[-1]== DIV :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            opdoDerDir = translateToDirection(opdoDer)
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            opdoIzqDir = translateToDirection(opdoIzq)
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and (cubo[tipoDer][tipoIzq][op] == INT or cubo[tipoDer][tipoIzq][op] == FLOAT) :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoIzqDir, opdoDerDir, getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes)]
                pOperandos.append(getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes))
                pTipos.append(tipoRes)
                changeTemporalCounter(tipoRes)
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error arimetico 5 - tipos no validos")
                exit()
    #print("Sale paso 5")               

def p_paso6(p):
    '''paso6 : '''
    pOperadores.append("(")

def p_paso7(p):
    '''paso7 : '''
    if pOperadores[-1] == "(" :
        pOperadores.pop()
    else:
        print("Falta parentesis izquierdo")
        exit()

def p_paso8_and(p):
    '''paso8_and : '''
    pOperadores.append(AND)

def p_paso8_or(p):
    '''paso8_or : '''
    pOperadores.append(OR)

def p_paso9(p):
    '''paso9 : '''
    global pTipos
    global pOperadores
    #print("Entra paso 9")
    #print(pTipos)
    #print(pOperandos)
    
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == AND or pOperadores[-1]== OR :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            opdoDerDir = translateToDirection(opdoDer)
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            opdoIzqDir = translateToDirection(opdoIzq)
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and cubo[tipoDer][tipoIzq][op] == BOOL :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoIzqDir, opdoDerDir, getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes)]
                pOperandos.append(getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes))
                pTipos.append(tipoRes)
                changeTemporalCounter(tipoRes)
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error arimetico 9 - tipos no validos")
                exit()
    #print("Sale paso 9") 

def p_paso10(p):
    '''paso10 : '''
    global pTipos
    global pOperadores
    #print("Entra paso 10")
    #print(pTipos)
    #print(pOperadores)
    
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == MAYOR or pOperadores[-1]== MENOR or pOperadores[-1]== IGUAL or pOperadores[-1]== DIF or pOperadores[-1]== MAYORIG or pOperadores[-1]== MENORIG:
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            opdoDerDir = translateToDirection(opdoDer)
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            opdoIzqDir = translateToDirection(opdoIzq)
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and cubo[tipoDer][tipoIzq][op] == BOOL :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoIzqDir, opdoDerDir, getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes)]
                pOperandos.append(getBaseTemporalDirection(tipoRes) + getTemporalCounter(tipoRes))
                pTipos.append(tipoRes)
                changeTemporalCounter(tipoRes)
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error arimetico 10 - tipos no validos")
                exit()
    #print("Sale paso 10")  

def p_paso11(p):
    '''paso11 : '''
    global pTipos
    global pOperadores
    #print("Entra paso 11")
    #print(pTipos)
    #print(pOperadores)
    
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == ASIG:
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            opdoDerDir = translateToDirection(opdoDer)
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            opdoIzqDir = translateToDirection(opdoIzq)
            tipoIzq = pTipos.pop()
            print(opdoIzq)
            print(opdoDer)
            print(tipoIzq)
            print(tipoDer)
            if opdoIzq in varDirectory.keys() or opdoIzq in varDirectoryMain.keys() or opdoIzq in varDirectoryFunc.keys() or opdoIzq in procDirectory.keys():
                if cubo[tipoDer][tipoIzq][op] != ERR:
                    tipoRes = cubo[tipoDer][tipoIzq][op]
                    #print(tipoRes)
                    cuadruplos[contCuadruplos] = [op, opdoDerDir, "", opdoIzqDir ]
                    pOperandos.append(contTemporales)
                    pTipos.append(tipoRes)
                    contTemporales+=1
                    contCuadruplos+=1
                    print(cuadruplos)
                else:
                    print("Error arimetico 11 - tipos no validos")
                    exit()
            else: 
                print("La variable no existe ", opdoIzq)
                exit()
    #print("Sale paso 11")

def p_paso12(p):
    '''paso12 : '''
    global pTipos
    global pOperandos
    global pSaltos
    global contCuadruplos
    aux = pTipos.pop()
    #print("valor de aux: ", aux)
    if aux == BOOL :
        resultado = pOperandos.pop()
        cuadruplos[contCuadruplos] = [GOTOF, resultado, "", ""]
        #print(cuadruplos[contCuadruplos][3])
        pSaltos.append(contCuadruplos)
        contCuadruplos += 1
        #print(pSaltos, "VALOR DE PSALTOS")
        #print(contCuadruplos, "VALOR DE CONTCUADRUPLOS")
    else: 
        print("Condicion del if no es bool")
        exit()

def p_paso13(p):
    '''paso13 : '''
    global contCuadruplos
    global pSaltos
    global cuadruplos
    cuadruplos[contCuadruplos] = [GOTO, "", "", ""]
    contCuadruplos += 1
    cuadruplos[pSaltos.pop()][3] = contCuadruplos
    pSaltos.append(contCuadruplos - 1)
    #print("cuadruplos paso 13", cuadruplos)
    #print(pSaltos)

def p_paso14(p):
    '''paso14 : '''
    global cuadruplos
    global contCuadruplos
    global pSaltos
    cuadruplos[pSaltos.pop()][3] = contCuadruplos
    print(cuadruplos)

def p_paso15(p):
    '''paso15 : '''
    global pSaltos
    global contCuadruplos
    pSaltos.append(contCuadruplos)

def p_paso16(p):
    '''paso16 : '''
    global pTipos
    global pOperandos
    global pSaltos
    global contCuadruplos
    aux = pTipos.pop()
    #print("valor de aux: ", aux)
    if aux == BOOL :
        resultado = pOperandos.pop()
        cuadruplos[contCuadruplos] = [GOTOF, resultado, "", ""]
        #print(cuadruplos[contCuadruplos][3])
        pSaltos.append(contCuadruplos)
        contCuadruplos += 1
        #print(pSaltos, "VALOR DE PSALTOS")
        #print(contCuadruplos, "VALOR DE CONTCUADRUPLOS")
    else: 
        print("Condicion del while no es bool")
        exit()

def p_paso17(p):
    '''paso17 : '''
    global cuadruplos
    global pSaltos
    global contCuadruplos
    cuadruplos[pSaltos.pop()][3] = contCuadruplos + 1
    cuadruplos[contCuadruplos] = [GOTO, "", "", pSaltos.pop()]
    contCuadruplos += 1
    #print("cuadruplos while: " , cuadruplos)

def p_paso18(p):
    '''paso18 : '''
    global cuadruplos
    global contCuadruplos
    global pOperandos
    print("entra print")
    cuadruplos[contCuadruplos] = [PRINT, "", "", pOperandos.pop()]
    print(cuadruplos)
    print("sale print")
    contCuadruplos += 1
    #print("cuadruplos print: " , cuadruplos)

def p_paso19(p):
    '''paso19 : '''
    global cuadruplos
    global contCuadruplos
    global pSaltos
    cuadruplos[contCuadruplos] = [GOTO, "", "", ""]
    pSaltos.append(contCuadruplos)
    contCuadruplos += 1

def p_paso20(p):
    '''paso20 : '''
    global cuadruplos
    global contCuadruplos
    global pSaltos
    cuadruplos[pSaltos.pop()][3] = contCuadruplos

def p_paso21(p):
    '''paso21 : '''
    global pSaltos
    global cuadruplos
    global contCuadruplos
    global funcActual
    global procDirectory
    #print('-------------------')
    procDirectory[funcActual]['Inicio'] = contCuadruplos
    #print('-------------------')
    #procDirectory[funcActual]['Inicio'] = contCuadruplos

def p_paso22(p):
    '''paso22 : '''
    global cuadruplos
    global contCuadruplos
    global pSaltos
    global decNumParametro
    procDirectory[funcActual]['Variables'].clear()
    cuadruplos[contCuadruplos] = [RET, "", "", ""]
    contCuadruplos += 1
    print(cuadruplos)
    parametrosA.clear()
    decNumParametro = 0
    

def p_paso23(p):
    '''paso23 : '''
    global pOperandos
    global contCuadruplos
    global funcActual
    global pTipos
    res = pOperandos.pop()
    tipoRes = pTipos.pop()
    #print(tipoRes)
    print("Q U E  P A S A")
    print((procDirectory[funcActual]))
    if tipoRes == translate(procDirectory[funcActual]['Tipo']) :
        print("VOY A ENTRAR")
        cuadruplos[contCuadruplos] = [RETURN, "", "", translateToDirection(res)]
        procDirectory[funcActual]['Retorno'] = translateToDirection(res)
        contCuadruplos += 1
        print(cuadruplos)
        print("PROC DIRECTORY", procDirectory[funcActual])
    else :
        print("Tipo de retorno invalido")
        exit()

def p_paso24(p):
    '''paso24 : '''
    global funcActual
    global numArgumento
    global cuadruplos
    global contCuadruplos
    print("entra a paso24")
    funcActual = p[-1]
    if p[-1] in procDirectory :
        print("La funcion existe en procDirectory")
        cuadruplos[contCuadruplos] = [ERA, procDirectory[funcActual]['# Parametros'] + procDirectory[funcActual]['Locales'], "", ""]
        contCuadruplos += 1
        numArgumento = 1
    else:
        print("No existe la funcion")
        exit()

def translateParameterToDirection(variable):
    if variable in procDirectory[funcActual]['Parametros'].keys():
        return procDirectory[funcActual]['Parametros'][variable]['Direccion']
    else:
        return -1

def p_paso25(p):
    '''paso25 : '''
    global cuadruplos
    global contCuadruplos
    global numArgumento
    global funcActual
    res = pOperandos.pop()
    tipo = pTipos.pop()
    numArgumento = 1
    try :
        print("res:", res)
        print("osoyogi:", procDirectory[funcActual]['Parametros'])
        numPar = procDirectory[funcActual]['Parametros'][res]['NumParametro']
        print("############################")
        if numPar == numArgumento :
            tipoParam = translate(procDirectory[funcActual]['Parametros'][res]['Tipo'])
            if tipo == tipoParam :
                cuadruplos[contCuadruplos] = [PARAM, translateParameterToDirection(res), "", numArgumento]
                numArgumento += 1
                contCuadruplos += 1
            else :
                print("Tipo invalido, no se puede")
                exit()
        else :
            print("Argumentos invalidos")
            exit()
    except :
        print("Error try")
        exit()
        
def p_paso26(p):
    '''paso26 : '''
    global cuadruplos
    global contCuadruplos
    global funcActual
    cuadruplos[contCuadruplos] = [GOSUB, procDirectory[funcActual]['Inicio'], "", ""]
    contCuadruplos += 1 

def p_pasoFinal(p):
    '''pasoFinal : '''
    global cuadruplos
    global contCuadruplos
    cuadruplos[contCuadruplos]=[ENDPROGRAM, '','','']
    contCuadruplos +=1

def p_cteInt(p):
    '''cteInt : '''
    pTipos.append(INT)

def p_cteFloat(p):
    '''cteFloat : '''
    pTipos.append(FLOAT)


def p_cteChar(p):
    '''cteChar : '''
    pTipos.append(CHAR)


def p_cteBool(p):
    '''cteBool : '''
    pTipos.append(BOOL)
    print(pTipos)

def p_cteString(p):
    '''cteString : '''
    pTipos.append(STRING)

def p_cteLlamada(p):
    '''cteLlamada : '''
    global pOperandos
    global pTipos
    print("entra ctellamada")
    print("heyeyeyeyeyeyeyye", procDirectory[p[-2]]['Retorno'])
    pTipos.append(translate(procDirectory[p[-2]]['Tipo']))
    pOperandos.append(procDirectory[p[-2]]['Retorno'])
    print(pTipos, "pTipos")
    print(pOperandos, "pOperandos")
    print("sale ctellamada")

def p_mayor(p):
    '''mayor : '''
    pOperadores.append(MAYOR)

def p_menor(p):
    '''menor : '''
    pOperadores.append(MENOR)

def p_mayorIg(p):
    '''mayorIg : '''
    pOperadores.append(MAYORIG)

def p_menorIg(p):
    '''menorIg : '''
    pOperadores.append(MENORIG)

def p_igual(p):
    '''igual : '''
    pOperadores.append(IGUAL)

def p_diferente(p):
    '''diferente : '''
    pOperadores.append(DIF)

def p_asig(p):
    '''asig : '''
    pOperadores.append(ASIG)

# Error rule for syntax errors
def p_error(p):
    print("Error de tipo: " + str(p.value) + "  linea: " + str(p.lineno))
    global err
    err = 0

# Build the parser
# Build the parser
parser = yacc.yacc(start='programa')

def archivo(file):
  fi = open(file, 'r')
  data = fi.read()
  #print (data)
  fi.close()
  if parser.parse(data) == 'OK':
    print('Programa valido')
    print(cuadruplos)
    maquina()
    print(dir_int_locales)
    print(dir_bool_locales)
    print(dir_bool_temporales)

archivo("test")
