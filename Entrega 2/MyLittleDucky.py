# Yacc example

import ply.yacc as yacc
import MyLittleDuckl
import sys 
# Get the token map from the lexer.  This is required.
from MyLittleDuckl import tokens

tokens = MyLittleDuckl.tokens   
varDirectory = {}
varDirectoryMain = {}
varDirectoryFunc = {}
procDirectory = {}
varList = []
varListMain = []
dirProcedure = {}


def p_programa(p): #Done
    '''programa : PROGRAM ID addProcedureDir SEMICOLON cicloVars cicloFuncion MAIN bloque'''
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
    '''auxVar1 : idVars COLON tipo addTypeGlobal SEMICOLON auxVar1 
        | '''

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
        print("Se agrego ")
        

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

def p_bloque(p): #Done
    '''bloque : LBRACE cicloVarsMain cicloBloque RBRACE'''

def p_cicloVarsMain(p): #Done
    '''cicloVarsMain : varsMain cicloVarsMain 
        |'''

def p_varsMain(p): #Done
    '''varsMain : createVariableDirMain VAR auxVar1Main'''

def p_createVariableDirMain(p):
    '''createVariableDirMain : '''
    varDirectoryMain = {}
    print("Pasa por createVariableDirMain")

def p_auxVar1Main(p): #Done
    '''auxVar1Main : idVarsMain COLON tipo addTypeGlobalMain SEMICOLON auxVar1Main 
        | '''

def p_addTypeGlobalMain(p):
    '''addTypeGlobalMain : '''
    print("pasa por addTypeGlobalMain")
    while (len(varListMain) > 0):
        print("entra loop addTypeGlobalMain")
        varDirectoryMain[varListMain.pop()] = {'Tipo' : p[-1], 'Scope' : 'Main'}
    print("TERMINA addTypeGlobalMain")
    print(varDirectoryMain)


def p_idVarsMain(p): #Done
    '''idVarsMain : ID addVariableDirMain ambIdVarsMain '''

def p_addVariableDirMain(p):
    '''addVariableDirMain : '''
    print("pasa por addVariableDirMain")
    if (p[-1] in varDirectoryMain):
        print("Ya existe la variable")
    else:
        varListMain.append(p[-1])
        print("Se agrego ")
        

def p_ambIdVarsMain(p): #Done
    '''ambIdVarsMain : COMMA idVarsMain
        |'''

def p_cicloBloque(p): #Done
    '''cicloBloque : estatuto cicloBloque 
        |'''

def p_estatuto(p): #Done
    '''estatuto : asignacion
        | condicion
        | escritura
        | lectura
        | llamada
        | ciclo'''

def p_asignacion(p): #Done
    '''asignacion : ID  auxAsignacion1 EQUALA exp SEMICOLON'''

def p_auxAsignacion1(p): #Done
    '''auxAsignacion1 : LBRACKET exp RBRACKET 
        |'''

def p_escritura(p): #Done
    '''escritura : PRINT LPAREN auxEscritura1 RPAREN SEMICOLON'''

def p_auxEscritura1(p): #Done
    '''auxEscritura1 : auxEscritura2 ambAuxEscritura1'''

def p_ambAuxEscritura1(p): #Done
    '''ambAuxEscritura1 : COMMA auxEscritura1
        |'''

def p_auxEscritura2(p): #Done
    '''auxEscritura2 : exp
        | CTESTRING'''

def p_expresion(p): #Done
    '''expresion : exp auxExpresion exp
        |'''

def p_auxExpresion(p): #Done
    '''auxExpresion : GTHAN
        | LTHAN
        | NOTEQUAL
        | GETHAN
        | LETHAN
        | EQUAL '''

def p_condicion(p): #Done
    '''condicion : IF LPAREN expresion RPAREN bloque auxCondicion'''

def p_auxCondicion(p): #Done
    '''auxCondicion : ELSE bloque
        |'''

def p_exp(p): #Done
    '''exp : cicloExp'''

def p_cicloExp(p): #Done
    '''cicloExp : termino ambExp'''

def p_ambExp(p): #Done
    '''ambExp : auxExp cicloExp
        |'''

def p_auxExp(p): #Done
    '''auxExp : PLUS
        | MINUS'''

def p_termino(p): #Done
    ''' termino : cicloTermino'''

def p_cicloTermino(p): #Done
    '''cicloTermino : factor ambCicloTermino'''

def p_ambCicloTermino(p): #Done
    '''ambCicloTermino : auxTermino cicloTermino
        | '''

def p_auxTermino(p): #Done
    '''auxTermino : MULTI
        | DIVIDE'''

def p_factor(p): #Done
    ''' factor : LPAREN exp RPAREN
        | auxFactor varcte'''

def p_auxFactor(p): #Done
    '''auxFactor : auxExp
        |'''

def p_varcte(p): #Done
    '''varcte : ID auxVarcte
        | CTEINT
        | CTEFLOAT
        | CTECHAR
        | CTEBOOL
        | CTESTRING'''

def p_auxVarcte(p): #Done
    '''auxVarcte : LPAREN exp RPAREN
        | LBRACKET exp LBRACKET 
        |'''

def p_cicloFuncion(p): #Done
    '''cicloFuncion : funcion cicloFuncion 
        |'''

def p_funcion(p): #Done
    '''funcion : FUNCTION tipo ID addProcDirectoryFunc LPAREN auxFunction RPAREN bloque'''

def p_addProcDirectoryFunc(p):
    '''addProcDirectoryFunc : '''
    procDirectory[p[-1]] ={'Variables' : varDirectoryFunc.copy(), 'Tipo' : p[-2]}
    varDirectoryFunc.clear()
    #print("pasa por addProcDirectoryFunc")
    print(procDirectory)

def p_auxFunction(p): #Done
    '''auxFunction : parametros
        |'''

def p_parametros(p): # Done
    '''parametros : auxParametros '''

def p_auxParametros(p): #Done
    '''auxParametros : tipo ID ambAuxParametros'''

def p_ambAuxParamentros(p): #Done
    '''ambAuxParametros : COMMA auxParametros
        |'''

def p_ciclo(p): #Done
    '''ciclo : WHILE LPAREN expresion RPAREN bloque '''

def p_llamada(p): #Done
    '''llamada : ID LPAREN auxLlamada RPAREN SEMICOLON'''

def p_auxLlamada(p): #Done
    '''auxLlamada : argumentos
        |'''

def p_argumentos(p): #Done
    ''' argumentos : auxArgumentos1
        |'''

def p_auxArgumentos1(p): #Done
    '''auxArgumentos1 : exp ambAuxArgumentos1'''

def p_ambAuxArgumentos1(p): #Done
    '''ambAuxArgumentos1 : COMMA auxArgumentos1
        |'''

def p_lectura(p): #Done
    ''' lectura : READ LPAREN ID RPAREN SEMICOLON '''

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
