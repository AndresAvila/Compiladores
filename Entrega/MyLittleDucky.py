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
ERR = -1


def p_programa(p): #Done
    '''programa : PROGRAM ID addProcedureDir SEMICOLON paso19 cicloVars cicloFuncion MAIN paso20 bloque'''
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
    while (len(varList) > 0):
        varDirectory[varList.pop()] = {'Tipo' : p[-1], 'Scope' : 'Global'}
    #print("TERMINA addTypeGlobal")
    print(varDirectory)


def p_idVars(p): #Done
    '''idVars : ID addVariableDir ambIdVars '''

def p_addVariableDir(p):
    '''addVariableDir : '''
    #print("pasa por addVariableDir")
    if (p[-1] in varDirectory):
        print("Ya existe la variable")
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
    '''auxVar1Main : idVarsMain COLON tipo addTypeGlobalMain SEMICOLON'''

def p_addTypeGlobalMain(p):
    '''addTypeGlobalMain : '''
    #print("pasa por addTypeGlobalMain")
    while (len(varListMain) > 0):
        #print("entra loop addTypeGlobalMain")
        varDirectoryMain[varListMain.pop()] = {'Tipo' : p[-1], 'Scope' : 'Main'}
    #print("TERMINA addTypeGlobalMain")
    print(varDirectoryMain)


def p_idVarsMain(p): #Done
    '''idVarsMain : ID addVariableDirMain ambIdVarsMain '''

def p_addVariableDirMain(p):
    '''addVariableDirMain : '''
    #print("pasa por addVariableDirMain")
    if (p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
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
    '''auxVar1Funcion : idVarsFuncion COLON tipo addTypeGlobalFuncion SEMICOLON'''

def p_addTypeGlobalFuncion(p):
    '''addTypeGlobalFuncion : '''
    #print("pasa por addTypeGlobalFuncion")
    while (len(varListFuncion) > 0):
        #print("entra loop addTypeGlobalFuncion")
        varDirectoryFunc[varListFuncion.pop()] = {'Tipo' : p[-1], 'Scope' : 'Funcion'}
    #print("TERMINA addTypeGlobalFuncion")
    #print(varDirectoryFunc)


def p_idVarsFuncion(p): #Done
    '''idVarsFuncion : ID addVariableDirFuncion ambIdVarsFuncion '''

def p_addVariableDirFuncion(p):
    '''addVariableDirFuncion : '''
    global contVarLocFunc
    #print("pasa por addVariableDirFuncion")
    if (p[-1] in varDirectoryFunc or p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
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
        | CTEINT paso1 cteInt
        | CTEFLOAT paso1 cteFloat
        | CTECHAR paso1 cteChar
        | CTEBOOL paso1 cteBool
        | CTESTRING paso1 cteString
        | llamada '''

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
    varDirectoryFunc.clear()
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
        #print("entra loop addTypeGlobalFuncion")
        varDirectoryFunc[varListFuncion.pop()] = {'Tipo' : p[-2], 'Scope' : 'Funcion'}
        varListFuncion.append(p[-1])
        decNumParametro += 1
        parametrosA[varListFuncion.pop()] = {'Valor' : 0, 'Tipo' : p[-2], 'NumParametro' : decNumParametro}
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

#Cuadruplos

def p_paso1(p):
    '''paso1 : '''
    #print(p[-1])
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

def p_paso4(p):
    '''paso4 : '''
    global pOperadores
    global pTipos
    #print("Entra paso4")
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == SUMA or pOperadores[-1]== RESTA :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and (cubo[tipoDer][tipoIzq][op] == INT or cubo[tipoDer][tipoIzq][op] == FLOAT) :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
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
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and (cubo[tipoDer][tipoIzq][op] == INT or cubo[tipoDer][tipoIzq][op] == FLOAT) :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
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
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and cubo[tipoDer][tipoIzq][op] == BOOL :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
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
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cubo[tipoDer][tipoIzq][op] != ERR and cubo[tipoDer][tipoIzq][op] == BOOL :
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
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
        #print("hola")
        if pOperadores[-1] == ASIG:
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            print(opdoIzq)
            print(opdoDer)
            print(tipoIzq)
            print(tipoDer)
            if opdoIzq in varDirectory.keys() or opdoIzq in varDirectoryMain.keys() or opdoIzq in varDirectoryFunc.keys() or opdoIzq in procDirectory.keys():
                if cubo[tipoDer][tipoIzq][op] != ERR:
                    tipoRes = cubo[tipoDer][tipoIzq][op]
                    #print(tipoRes)
                    cuadruplos[contCuadruplos] = [op, opdoDer, "", opdoIzq ]
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
    print((procDirectory[funcActual]['Tipo']))
    if tipoRes == translate(procDirectory[funcActual]['Tipo']) :
        cuadruplos[contCuadruplos] = [RETURN, "", "", res]
        procDirectory[funcActual]['Retorno'] = res
        contCuadruplos += 1
        print(cuadruplos)
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
        cuadruplos[contCuadruplos] = [ERA, funcActual, "", ""]
        contCuadruplos += 1
        numArgumento = 1
    else:
        print("No existe la funcion")
        exit()

def p_paso25(p):
    '''paso25 : '''
    global cuadruplos
    global contCuadruplos
    global numArgumento
    global funcActual
    res = pOperandos.pop()
    tipo = pTipos.pop()
    try :
        numPar = procDirectory[funcActual]['Parametros'][res]['NumParametro']
        if numPar == numArgumento :
            tipoParam = translate(procDirectory[funcActual]['Parametros'][res]['Tipo'])
            if tipo == tipoParam :
                cuadruplos[contCuadruplos] = [PARAM, res, "", numArgumento]
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
    cuadruplos[contCuadruplos] = [GOSUB, funcActual, "", ""]
    contCuadruplos += 1 


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

archivo("test")
