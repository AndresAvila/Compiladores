# Yacc example

import ply.yacc as yacc
import MyLittleDuckl
import sys 
# Get the token map from the lexer.  This is required.
from MyLittleDuckl import tokens

def p_programa(p): #Done
    '''programa : PROGRAM ID SEMICOLON cicloVars cicloFuncion bloque'''
    p[0] = "OK"

def p_cicloVars(p): #Done
    '''cicloVars : vars cicloVars 
        |'''

def p_vars(p): #Done
    '''vars : VAR auxVar1 '''

def p_auxVar1(p): #Done
    '''auxVar1 : idVars COLON tipo SEMICOLON auxVar1 
        |'''

def p_idVars(p): #Ambig
    '''idVars : ID COMMA idVars 
        | ID'''

def p_tipo(p): #Done
    '''tipo : auxTipo1
        | CHAR '''

def p_auxTipo1(p): #Done
    '''auxTipo1 : auxTipo2 LBRACKET CTEINT RBRACKET'''

def p_auxTipo2(p): #Done
    '''auxTipo2 : INT
        | BOOL
        | STRING
        | FLOAT '''

def p_bloque(p): #Done
    '''bloque : LBRACE cicloBloque RBRACE'''

def p_cicloBloque(p): #Done
    '''cicloBloque : ESTATUTO cicloBloque 
        |'''

def p_estatuto(p): #Done
    '''estatuto : asignacion
        | condicion
        | escritura
        | lectura
        | llamada
        | ciclo'''

def p_asignacion(p): #Done
    '''asignacion : ID  auxAsignacion1 EQUALA expresion SEMICOLON'''

def p_auxAsignacion1(p): #Done
    '''auxAsignacion1 : LBRACKET exp RBRACKET 
        |'''

def p_escritura(p): #Done
    '''escritura : PRINT LPAREN auxEscritura1 RPAREN SEMICOLON'''

def p_auxEscritura1(p): #AMBIG
    '''auxEscritura1 : auxEscritura2 COMMA auxEscritura1
        | auxEscritura2 '''

def p_auxEscritura2(p): #Done
    '''auxEscritura2 : expresion
        | CTESTRING'''

#def p_expresion(p): #Done
#    '''expresion : exp auxExpresion exp
#        |'''

def p_auxExpresion(p): #Done
    '''auxExpresion : GTHAN
        | LTHAN
        | NOTEQUAL
        | GETHAN
        | LETHAN
        | EQUAL '''

def p_condicion(p): #Done
    '''condicion : IF LPAREN expresion RPAREN bloque auxCondicion SEMICOLON'''

def p_auxCondicion(p): #Done
    '''auxCondicion : ELSE bloque
        |'''

def p_exp(p): #Done
    '''exp : cicloExp'''

def p_cicloExp(p): #Ambig
    '''cicloExp : termino auxExp cicloExp
        | termino'''

def p_auxExp(p): #Done
    '''auxExp : PLUS
        | MINUS'''

def p_termino(p): #Done
    ''' termino : cicloTermino'''

def p_cicloTermino(p): #Ambig
    '''cicloTermino : factor auxTermino cicloTermino
        | factor '''

def p_auxTermino(p): #Done
    '''auxTermino : MULTI
        | DIVIDE'''

def p_factor(p): #Done
    ''' factor : LPAREN expresion RPAREN
        | auxFactor varcte'''

def p_auxFactor(p): #Done
    '''auxFactor : auxExp
        |'''

def p_varcte(p): #Done
    '''varcte : ID auxVarcte
        | CTEINT
        | CTREFLOAT
        | CTECHAR
        | CTEBOOL
        | CTESTRING'''

def p_auxVarcte(p): #Done
    '''auxVarcte : LPAREN exp RPAREN
        | LBRACKET exp LBRACKET 
        |'''

def p_funcion(p): #Done
    '''funcion : FUNCTION ID LPAREN auxFunction RPAREN bloque'''

def p_auxFunction(p): #Done
    '''auxFunction : parametros
        |'''

def p_parametros(p): # Done
    '''parametros : auxParametros '''

def p_auxParametros(p): #Ambig
    '''auxParametros : tipo ID COMMA auxParametros
        | tipo ID '''

def p_ciclo(p): #Done
    '''ciclo : WHILE LPAREN expresion RPAREN bloque SEMICOLON '''

def p_llamada(p): #Done
    '''llamada : ID LPAREN auxLlamada RPAREN'''

def p_auxLlamada(p): #Done
    '''aux_llamada : argumentos
        |'''

def p_argumentos(p): #Done
    ''' argumentos : auxArgumentos1
        |'''

def p_auxArgumentos1(p): #Ambig
    '''p_auxArgumentos1 : exp COMMA auxArgumentos1
        | exp'''

def p_lectura(p): #Done
    ''' lectura : READ LPAREN ID RPAREN SEMICOLON '''

# Error rule for syntax errors
def p_error(p):
    print("Error de tipo: ", p.value,"  linea: ", p.lineno)
    global err
    err = 0

# Build the parser
# Build the parser
parser = yacc.yacc(start='programa')

def archivo(file):
  fi = open(file, 'r')
  data = fi.read()
  fi.close()
  if parser.parse(data) == 'OK':
    print('Programa valido')
