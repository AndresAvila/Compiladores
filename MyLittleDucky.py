# Yacc example

import ply.yacc as yacc
import MyLittleDuckl
#import sys 
# Get the token map from the lexer.  This is required.
from MyLittleDuckl import tokens

def p_programa(p):
    '''PROGRAMA ::= 'program' 'id' ';' VARS* (FUNCIÓN)* BLOQUE'''

def p_vars(p):
    '''VARS ::= 'var' ( 'id' ( ',' 'id' )* ':' TIPO ';' )+'''

def p_tipo(p):
    '''TIPO ::= (('int'|'bool'|'string'| 'float') ('[' 'cte int' ']')+) | char'''

def p_bloque(p):
    '''BLOQUE ::= '{' ESTATUTO* '}' '''

def p_estatuto(p):
    '''ESTATUTO ::= ASIGNACIÓN | CONDICIÓN | ESCRITURA | LECTURA | LLAMADA | CICLO'''

def p_asignacion(p):
    '''ASIGNACIÓN ::= 'id' ('[' EXP ']')? '=' EXPRESIÓN ';' '''

def p_escritura(p):
    '''ESCRITURA ::= 'print' '(' (EXPRESIÓN | 'cte string')(',' (EXPRESIÓN | 'cte string'))* ')' ';' '''

def p_expresion(p):
    '''EXPRESIÓN ::= EXP (('>' | '<' | '<>' | '>=' | '<=' | '==')EXP)?'''

def p_condicion(p):
    '''CONDICIÓN ::= 'if' '(' EXPRESIÓN ')' BLOQUE ('else' BLOQUE)? ';' '''

def p_exp(p):
    '''EXP ::= TÉRMINO (( '+' | '-' )TÉRMINO)* '''

def p_termino(p):
    ''' TÉRMINO ::= FACTOR (( '*' | '/' )FACTOR)* '''

def p_factor(p):
    ''' FACTOR ::= '(' EXPRESIÓN ')' | ( '+' | '-' )? VAR_CTE '''

def p_varcte(p):
    '''VAR_CTE ::= 'id' (('(' EXP ')')|('[' EXP ']'))? | 'cte int' | 'cte float' | 'cte char' | 'cte bool' | 'cte string' '''

def p_funcion(p):
    ''' FUNCIÓN ::= 'function' 'id' '(' PARAMETROS? ')' BLOQUE '''

def p_parametros(p):
    ''' PARAMETROS ::= TIPO 'id' (',' TIPO 'id')* '''

def p_ciclo(p):
    ''' CICLO ::= 'while' '(' EXPRESIÓN ')' BLOQUE ';' '''

def p_llamada(p):
    ''' LLAMADA ::= 'id' '(' ARGUMENTOS? ')' '''

def p_argumentos(p):
    ''' ARGUMENTOS ::= (EXP (',' EXP)*)? '''

def p_lectura(p):
    ''' LECTURA ::= 'read' '(' 'id' ')' ';' '''

def p_empty(p):
  '''empty : '''

# Error rule for syntax errors
def p_error(p):
    print("Error de tipo: ", p.value,"  linea: ", p.lineno)
    global err
    err = 0

# Build the parser
yacc.yacc()

err = 1

while True:
  try:
    nombre = input("Nombre del archivo? (Teclee 'S' para salir) ")
    if nombre == 'S':
      break
    fil = open(nombre, "r")
    s = fil.readlines()
    e = ""
    for line in s:
      e += line
    yacc.parse(e)

    if err:
      print("No hay ningun error, buen programa (Y)!")

  except EOFError:
    print("Error! No se pudo abrir el archivo!")
    break;
