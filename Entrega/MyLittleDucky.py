# Yacc example

import ply.yacc as yacc
import MyLittleDuckl
import sys 
import cubo


# Get the token map from the lexer.  This is required.
from MyLittleDuckl import tokens
from collections import deque
from Queue import PriorityQueue


#from memoria import Memoria

contprueba = 0

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
dirCompleto = {}

nombrePrograma = ""
funcActual = ""
nombreArreglo = ""
tipoArreglo = ""
boolArreglo = False
tamArr = 0

retornos = PriorityQueue()
cuadruplos = {}
pOperadores = []
pOperandos = []
pTipos = []
contTemporales = 0
contCuadruplos = 40001
contParametros = 0
contVarLocFunc = 0
contRetorno = 0
pSaltos = []

cantIntGlobales = 0
cantBoolGlobales = 0
cantFloatGlobales = 0
cantCharGlobales = 0
cantStringGlobales = 0

cantIntLocales = 0
cantBoolLocales = 0
cantFloatLocales = 0
cantCharLocales = 0
cantStringLocales = 0

cantIntFunciones = 0
cantBoolFunciones = 0
cantFloatFunciones = 0
cantCharFunciones = 0
cantStringFunciones = 0

parametrosA = {}
decNumParametro = 0
numArgumento = 0
#pSaltos = deque([])

cubo = cubo.cubo

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

dir_arreglos_temporales=[]
inicia_arreglos_temporales=26000
cont_arreglos_temporales=0


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
VER = 25
ERR = -1



class Memoria:

    def __init__(self, name, memoria, temporales):
        self.name  = name
        self.ints  = memoria['Int'] * [None]
        self.bools = memoria['Bool'] * [None]
        self.strings = memoria['String'] * [None]
        self.floats = memoria['Float'] * [None]
        self.chars = memoria['Char'] * [None]
        
        
        self.temp_int = temporales['Int'] * [None]
        self.temp_bool = temporales['Bool'] * [None]
        self.temp_string = temporales['String'] * [None]
        self.temp_float = temporales['Float'] * [None]   
        self.temp_char = temporales['Char'] * [None]      
        self.temp_arr = temporales['Arr'] * [None]

        self.valor_Retorno = None
      


   

    def offsetDireccion(self, direccion):
        # funcion que calcula el offset y tipo de una direccion recibida
        addressScope = self.scopeDireccion(direccion)[1]
        offset = direccion - addressScope
        if offset >= 0 and offset < 1000:
            return ['INT', 0]
        elif offset >= 1000 and offset < 2000:
            return ['FLOAT', 1000]
        elif offset >= 2000 and offset < 3000:
             return ['CHAR', 2000]
        elif offset >= 3000 and offset < 4000:
            return ['STRING', 3000]
        elif offset >= 4000 and offset < 5000:
            return ['BOOL', 4000]
        elif offset >= 5000:
            return ['INT', 5000]
        else:

            return "Error"

    def scopeDireccion(self, direccion):
        # funcion que regresa el scope y la direccion base de una direccion recibida
        #print(direccion, "direccion")
        if direccion >= 1000 and direccion < 6000:
            return ['Global', 1000]

        elif direccion >= 6000 and direccion < 11000:
            return ['Local', 6000]

        elif direccion >= 11000 and direccion < 16000:
            return ['Funcion', 11000]

        elif direccion >= 16000 and direccion < 21000:
            return ['Temporales', 16000]

        elif direccion >= 21000 and direccion < 26000:
            return ['Constantes', 21000]
        elif direccion >= 26000:
            return ['TemporalesArr', 26000]
        else:
            return ['Error', 9999999]


    def memoriaActual(self, scope, tipo):
        # funcion que regresa la memoria requerida en base al scope
        if scope == 'Global' or scope == 'Funcion' or scope == 'Local' or scope == 'Constantes':
            if tipo == 'INT':
                return self.ints
            elif tipo == 'BOOL':
                return self.bools
            elif tipo == 'STRING':
                return self.strings
            elif tipo == 'FLOAT':
                return self.floats
            elif tipo == 'CHAR':
                return self.chars
            
            
        elif scope == 'Temporales':
            if tipo == 'INT':
                return self.temp_int
            elif tipo == 'BOOL':
                return self.temp_bool
            elif tipo == 'STRING':
                return self.temp_strings
            elif tipo == 'FLOAT':
                return self.temp_float
            elif tipo == 'CHAR':
                return self.temp_char

        elif scope == 'TemporalesArr':
            return self.temp_arr






    def getValorDeDireccion(self, direccion, constantes):

        # funcion que regresa el valor almacenado en memoria al recibir una direccion
        scope = self.scopeDireccion(direccion)[0]
        #print("scope a", scope)
        tipo = self.offsetDireccion(direccion)[0]
        
        #print("tipo ", tipo)
        if scope != 'Constantes': # si no es una constante, busca en la misma memoria
            dirBase = self.scopeDireccion(direccion)[1]

            offset = self.offsetDireccion(direccion)[1]
            #print("dirBase ", dirBase)
            #print("offset ", offset)
            real = direccion - dirBase - offset
            #print(real, "real")
            mem = self.memoriaActual(scope, tipo)
            #print("mem......", mem)
            if real >= len(mem):
                print("Error: posicion de arreglo no existente.")
                exit()
            #print("memreal.....", mem[real])
            return mem[real]
        else: # busca la constante en base a la direccion
            keys = constantes.keys()
            cantidad = len(keys)
            i = 0
            while i < cantidad:
                if constantes[keys[i]]['Direccion'] == direccion:
                    if tipo == 'INT':
                        return int(keys[i])
                    elif tipo == 'FLOAT':
                        return float(keys[i])
                    else:
                        #print(keys[i], "return keysi")
                        return keys[i]
                i += 1


    def setValorDeDireccion(self, direccion, valor):
        #print(direccion, " direccion")
        #print(valor, " valor")
        scope = self.scopeDireccion(direccion)[0]
        #print(scope, " scope")
        tipo = self.offsetDireccion(direccion)[0]
        #print(tipo, " tipo")
        dirBase = self.scopeDireccion(direccion)[1]
        #print(dirBase, " dirBase")
        offset = self.offsetDireccion(direccion)[1]
        #print(offset, " offset")
        real = direccion - dirBase - offset
        #print(real, " real")
        mem = self.memoriaActual(scope, tipo)
        #print(mem, " mem")
        boolCons = True
        if real >= len(mem):
            if direccion >= 21000 and direccion < 26000:
                mem.pop()
                mem.append(valor)
                #print(mem, "mem aqui")
                boolCons = False
            else:
                print("Error: direccion no existente.")
                exit()
        if boolCons:
            mem[real] = valor


def maquina():
    auxCont = 40001
    pilaMemorias = []
    saltos = []
    MemoriaGlobal = Memoria("Global", dirCompleto[dirCompleto.keys()[0]]['Directorio Globales']['TamanoMemoria'], dirCompleto[dirCompleto.keys()[0]]['Directorio Temporales']['TamanoMemoria'])
    MemoriaActual = Memoria("Main", dirCompleto[dirCompleto.keys()[0]]['Directorio Locales']['TamanoMemoria'], dirCompleto[dirCompleto.keys()[0]]['Directorio Temporales']['TamanoMemoria'])
    MemoriaNueva = ""
    constantes = dirConstantes

    while cuadruplos[auxCont][0] != ENDPROGRAM:
        cuadruploActual = cuadruplos[auxCont]
        
        #print("here ", auxCont)
        #print("cuadruplo: ", cuadruploActual)

        if cuadruploActual[0] == ASIG:
            operando1= cuadruploActual[1]
            resultado= cuadruploActual[3]
            #print(MemoriaActual.valor_Retorno)
            if MemoriaActual.valor_Retorno != None:
                #print("VALOR DE RETORNO: ", MemoriaActual.valor_Retorno)
                operando1 = MemoriaActual.valor_Retorno
                MemoriaActual.valor_Retorno = None


                if operando1 >= 1000 and operando1 < 6000:
                    if operando1 >= 1000 and not isinstance(operando1, str):
                        operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                    MemoriaGlobal.setValorDeDireccion(resultado, operando1)
                    respuesta = MemoriaGlobal.getValorDeDireccion(resultado, constantes)
                else:
                    if operando1 >= 1000 and not isinstance(operando1, str):
                        operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                    MemoriaActual.setValorDeDireccion(resultado, operando1)
                    respuesta = MemoriaActual.getValorDeDireccion(resultado, constantes)
                MemoriaActual.valor_Temporal = respuesta


            else:
                if operando1 >= 1000 and operando1 < 6000:
                    operando1= MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                    if resultado >= 26000 and not isinstance(operando1, str):
                        resultado = MemoriaGlobal.getValorDeDireccion(resultado, constantes)
                    if operando1 >= 26000 and not isinstance(operando1, str):
                        operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                else:
                    operando1= MemoriaActual.getValorDeDireccion(operando1, constantes)
                    if resultado >= 26000:
                        resultado = MemoriaActual.getValorDeDireccion(resultado, constantes)
                    if operando1 >= 26000 and not isinstance(operando1, str):
                        operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                        #print("aqui es mayor", operando1)
            
                #print("operando1....", operando1)
                if operando1 >= 1000 and operando1 < 6000:
                    if operando1 >= 1000 and not isinstance(operando1, str):
                        operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                    MemoriaGlobal.setValorDeDireccion(resultado, operando1)
                    respuesta = MemoriaGlobal.getValorDeDireccion(resultado, constantes)
                else:
                    if operando1 >= 1000 and not isinstance(operando1, str):
                        operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                    MemoriaActual.setValorDeDireccion(resultado, operando1)
                    respuesta = MemoriaActual.getValorDeDireccion(resultado, constantes)
            
            #print("resultado de la asignacion ",resultado , " = ", respuesta)

        if cuadruploActual[0] == SUMA:
            cuadruploAnterior = cuadruplos[auxCont-1]
            operando1= cuadruploActual[1]
            #print(operando1, "op1")
            if operando1 >= 1000 and operando1 < 6000:
                if operando1 >= 26000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if cuadruploAnterior[0] != VER:
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                if operando1 >= 26000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if cuadruploAnterior[0] != VER: 
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
            #print(operando1, "op1")   

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 26000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 26000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            #print(operando1, " operando1 ", operando2, " operando2" )    
            respuesta = operando1 + operando2
            resultado = cuadruploActual[3]
            if resultado >= 1000 and resultado < 6000:
                if respuesta >= 1000:
                    respuesta = MemoriaGlobal.getValorDeDireccion(respuesta, constantes)
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
                resupesta = MemoriaGlobal.getValorDeDireccion(resultado)
            else:            
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

            #print("resultado de la suma",respuesta)

        if cuadruploActual[0] == RESTA:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
            #print("op1", operando1)
            #print("op2", operando2)
            resultado= cuadruploActual[3]
            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, operando1-operando2)
            else:
                MemoriaActual.setValorDeDireccion(resultado, operando1-operando2)

        if cuadruploActual[0] == MULT:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, operando1*operando2)
            else:
                MemoriaActual.setValorDeDireccion(resultado, operando1*operando2)

        if cuadruploActual[0] == DIV:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, operando1/operando2)
            else:
                MemoriaActual.setValorDeDireccion(resultado, operando1/operando2)

        if cuadruploActual[0] == OR:
            operando1= cuadruploActual[1]

            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
            #print("OPERANDO 1 OR: ", operando1)
            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1=="_true" or operando2=="_true":
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)
            #print("RESULTADO DEL OR",respuesta)

        if cuadruploActual[0] == AND:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1=="_true" and operando2=="_true":
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == MAYOR:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1>operando2:
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == MENOR:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1<operando2:
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == MAYORIG:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1>=operando2:
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == MENORIG:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000:
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1<=operando2:
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == IGUAL:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1==operando2:
                respuesta="_true"
            else:
                respuesta="_false"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == DIF:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)

            operando2= cuadruploActual[2]
            if operando2 >= 1000 and operando2 < 6000:
                operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):  
                    operando2 = MemoriaGlobal.getValorDeDireccion(operando2, constantes)
            else:
                operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)
                if operando2 >= 1000 and not isinstance(operando2, str):
                    operando2 = MemoriaActual.getValorDeDireccion(operando2, constantes)

            resultado= cuadruploActual[3]
            respuesta= "error"
            if operando1==operando2:
                respuesta="_false"
            else:
                respuesta="_true"

            if resultado >= 1000 and resultado < 6000:
                MemoriaGlobal.setValorDeDireccion(resultado, respuesta)
            else:
                MemoriaActual.setValorDeDireccion(resultado, respuesta)

        if cuadruploActual[0] == GOTO:
            resultado = cuadruploActual[3]

            auxCont = resultado-1



        if cuadruploActual[0] == GOTOF:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
            resultado= cuadruploActual[3]

            if operando1 == "_false":
                auxCont = resultado-1

            #print("VAMOS A........", auxCont+1)

        if cuadruploActual[0] == GOTOV:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
            resultado= cuadruploActual[3]

            if operando1 == "_true":
                auxCont = resultado-1

        if cuadruploActual[0] == VER:
            operando1= cuadruploActual[1]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000:
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
            operando2 = cuadruploActual[3]
            if operando1 > operando2 or operando1 < 0:
                print("fuera de rango")
                exit() 

        if cuadruploActual[0] == PRINT:
            operando1= cuadruploActual[3]
            if operando1 >= 1000 and operando1 < 6000:
                operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):  
                    operando1 = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
                if operando1 >= 1000 and not isinstance(operando1, str):
                    operando1 = MemoriaActual.getValorDeDireccion(operando1, constantes)
            if isinstance(operando1, str):
                print(operando1[1:-1])
            else:
                print(operando1)


        if cuadruploActual[0] == ERA:
            nombreFuncion = cuadruploActual[1]
            memoria = dirCompleto[dirCompleto.keys()[0]]['Directorio Funciones'][nombreFuncion]['TamanoMemoria']
            temporales = dirCompleto[dirCompleto.keys()[0]]['Directorio Temporales']['TamanoMemoria']
            #print(memoria)
            MemoriaNueva = Memoria(nombreFuncion, memoria, temporales)


        if cuadruploActual[0] == GOSUB:
            saltos.append(auxCont)
            salto = cuadruploActual[1]
            auxCont = salto - 1
            pilaMemorias.append(MemoriaActual)
            MemoriaActual = MemoriaNueva
        
        if cuadruploActual[0] == RETURN:
            valor = cuadruploActual[3]
            if valor >= 1000 and valor < 6000:
                retorno = MemoriaGlobal.getValorDeDireccion(valor, constantes)
            else:
                retorno = MemoriaActual.getValorDeDireccion(valor, constantes)
            MemoriaActual.valor_Retorno = retorno
            MemoriaActual.valor_Temporal = retorno
            cuadruploRET = 0
            for key in cuadruplos:
                if cuadruplos[key][0] == RET and key > auxCont:
                    cuadruploRET = key
                    #print("here if", cuadruploRET)
                    break
            auxCont = cuadruploRET - 1
                    

        if cuadruploActual[0] == RET:
            aux = MemoriaActual.valor_Retorno
            MemoriaActual = pilaMemorias.pop()
            MemoriaActual.valor_Retorno = aux
            auxCont = saltos.pop()

        if cuadruploActual[0] == PARAM:
            operando1 = cuadruploActual[1]
            resultado = cuadruploActual[3]
            #if resultado >= 26000:  
                #resultado = MemoriaActual.getValorDeDireccion(resultado, constantes)
            #print("parametro ", resultado)
            if operando1 >= 1000 and operando1 < 6000:
                valor = MemoriaGlobal.getValorDeDireccion(operando1, constantes)
            else:
                valor = MemoriaActual.getValorDeDireccion(operando1, constantes)
            #print(valor, " valor")
            #print(operando1, " ope1")
            MemoriaNueva.setValorDeDireccion(resultado, valor)

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
    #print(dirProcedure)
    global nombreArreglo
    nombreArreglo = p[-1]

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
    global tamArr
    global boolArreglo
    global cantIntGlobales 
    global cantBoolGlobales 
    global cantFloatGlobales 
    global cantCharGlobales 
    global cantStringGlobales 

    tamArreglo = int(tamArr)
    sumaArr = 0
    if not boolArreglo :
        tamArreglo = 0
    else :
        sumaArr = tamArreglo - 1
    while (len(varList) > 0):
        variable = varList.pop()
        if(translate(p[-1]) == 1):
            cantIntGlobales += 1 + sumaArr
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_int_globales + cont_int_globales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_int_globales + tamArreglo
                while (cont_int_globales < tamWhile) :
                    dir_int_globales.append({'Valor' : 0, 'Direccion' : inicia_int_globales + cont_int_globales, 'Arreglo' : ''})
                    cont_int_globales += 1
            else :
                dir_int_globales.append({'Valor' : 0, 'Direccion' : inicia_int_globales + cont_int_globales, 'Arreglo' : ''})
                cont_int_globales += 1
        elif(translate(p[-1]) == 2):
            cantBoolGlobales += 1 + sumaArr
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_bool_globales + cont_bool_globales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_bool_globales + tamArreglo
                while (cont_bool_globales < tamWhile) :
                    dir_bool_globales.append({'Valor' : '', 'Direccion' : inicia_bool_globales + cont_bool_globales, 'Arreglo' : ''})
                    cont_bool_globales += 1
            else :
                dir_bool_globales.append({'Valor' : '', 'Direccion' : inicia_bool_globales + cont_bool_globales, 'Arreglo' : ''})
                cont_bool_globales += 1
        elif(translate(p[-1]) == 3):
            cantStringGlobales += 1 + sumaArr
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_string_globales + cont_string_globales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_string_globales + tamArreglo
                while (cont_string_globales < tamWhile) :
                    dir_string_globales.append({'Valor' : '', 'Direccion' : inicia_string_globales + cont_string_globales, 'Arreglo' : ''})
                    cont_string_globales += 1
            else :
                dir_string_globales.append({'Valor' : '', 'Direccion' : inicia_string_globales + cont_string_globales, 'Arreglo' : ''})
                cont_string_globales += 1
        elif(translate(p[-1]) == 4):
            cantFloatGlobales  += 1 + sumaArr
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_float_globales + cont_float_globales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_float_globales + tamArreglo
                while (cont_float_globales < tamWhile) :
                    dir_float_globales.append({'Valor' : 0.0, 'Direccion' : inicia_float_globales + cont_float_globales, 'Arreglo' : ''})
                    cont_float_globales += 1
            else :
                dir_float_globales.append({'Valor' : 0.0, 'Direccion' : inicia_float_globales + cont_float_globales, 'Arreglo' : ''})
                cont_float_globales += 1
        elif(translate(p[-1]) == 5):
            cantCharGlobales += 1 + sumaArr
            varDirectory[variable] = {'Tipo' : p[-1], 'Scope' : 'Global', 'Direccion': inicia_char_globales + cont_char_globales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_char_globales + tamArreglo
                while (cont_char_globales < tamWhile) :
                    dir_char_globales.append({'Valor' : '', 'Direccion' : inicia_char_globales + cont_char_globales, 'Arreglo' : ''})
                    cont_char_globales += 1
            else :
                dir_char_globales.append({'Valor' : '', 'Direccion' : inicia_char_globales + cont_char_globales, 'Arreglo' : ''})
                cont_char_globales += 1
    #print("TERMINA addTypeGlobal")
    #print(varDirectory)
    

def p_idVars(p): #Done
    '''idVars : ID addVariableDir ambIdVars'''

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
    '''ambAuxTipo1 : LBRACKET CTEINT RBRACKET esArr assignDirectionCteInt
        | noEsArr''' 

def p_esArr(p):
    '''esArr : '''
    global boolArreglo
    global tamArr
    boolArreglo = True
    tamArr = p[-2]

def p_noEsArr(p):
    '''noEsArr : '''
    global boolArreglo
    boolArreglo = False

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
    global tamArr
    global boolArreglo
    global cantIntLocales 
    global cantBoolLocales 
    global cantFloatLocales 
    global cantCharLocales 
    global cantStringLocales
    tamArreglo = int(tamArr)
    sumaArr = 0
    if not boolArreglo :
        tamArreglo = 0
    else :
        sumaArr = tamArreglo - 1
    while (len(varListMain) > 0):
        variable = varListMain.pop()
        if(translate(p[-1]) == 1):
            cantIntLocales += 1 + sumaArr
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_int_locales + cont_int_locales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_int_locales + tamArreglo
                while (cont_int_locales < tamWhile) :
                    dir_int_locales.append({'Valor' : 0, 'Direccion' : inicia_int_locales + cont_int_locales, 'Arreglo' : ''})
                    cont_int_locales += 1
            else :
                dir_int_locales.append({'Valor' : 0, 'Direccion' : inicia_int_locales + cont_int_locales, 'Arreglo' : ''})
                cont_int_locales += 1   
        elif(translate(p[-1]) == 2):
            cantBoolLocales += 1 + sumaArr
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_bool_locales + cont_bool_locales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_bool_locales + tamArreglo
                while (cont_bool_locales < tamWhile) :
                    dir_bool_locales.append({'Valor' : '', 'Direccion' : inicia_bool_locales + cont_bool_locales, 'Arreglo' : ''})
                    cont_bool_locales += 1
            else :
                dir_bool_locales.append({'Valor' : '', 'Direccion' : inicia_bool_locales + cont_bool_locales, 'Arreglo' : ''})
                cont_bool_locales += 1
        elif(translate(p[-1]) == 3): 
            cantStringLocales += 1 + sumaArr
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_string_locales + cont_string_locales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_string_locales + tamArreglo
                while (cont_string_locales < tamWhile) :
                    dir_string_locales.append({'Valor' : '', 'Direccion' : inicia_string_locales + cont_string_locales, 'Arreglo' : ''})
                    cont_string_locales += 1
            else :
                dir_string_locales.append({'Valor' : '', 'Direccion' : inicia_string_locales + cont_string_locales, 'Arreglo' : ''})
                cont_string_locales += 1
        elif(translate(p[-1]) == 4):
            cantFloatLocales += 1 + sumaArr
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_float_locales + cont_float_locales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_float_locales + tamArreglo
                while (cont_float_locales < tamWhile) :
                    dir_float_locales.append({'Valor' : 0.0, 'Direccion' : inicia_float_locales + cont_float_locales, 'Arreglo' : ''})
                    cont_float_locales += 1
            else :
                dir_float_locales.append({'Valor' : 0.0, 'Direccion' : inicia_float_locales + cont_float_locales, 'Arreglo' : ''})
                cont_float_locales += 1
        elif(translate(p[-1]) == 5):
            cantCharLocales += 1 + sumaArr
            varDirectoryMain[variable] = {'Tipo' : p[-1], 'Scope' : 'Main', 'Direccion': inicia_char_locales + cont_char_locales, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_char_locales + tamArreglo
                while (cont_char_locales < tamWhile) :
                    dir_char_locales.append({'Valor' : '', 'Direccion' : inicia_char_locales + cont_char_locales, 'Arreglo' : ''})
                    cont_char_locales += 1
            else :
                dir_char_locales.append({'Valor' : '', 'Direccion' : inicia_char_locales + cont_char_locales, 'Arreglo' : ''})
                cont_char_locales += 1
    #print("TERMINA addTypfunciones
    #print(varDirectoryMain)
    

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
    '''bloque : LBRACE cicloVarsMain cicloBloque recursivo RBRACE '''

def p_recursivo(p):
    '''recursivo : RETURN exp SEMICOLON paso23
        | '''

def p_cicloBloque(p): #Done
    '''cicloBloque : estatuto cicloBloque 
        | '''

def p_bloqueFuncion(p): #Done
    '''bloqueFuncion : LBRACE cicloVarsFuncion paso21 cicloBloqueFuncion RETURN exp SEMICOLON RBRACE'''

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
    global tamArr
    global boolArreglo
    global cantIntFunciones
    global cantBoolFunciones
    global cantFloatFunciones
    global cantCharFunciones
    global cantStringFunciones
    tamArreglo = int(tamArr)
    sumaArr = 0
    if not boolArreglo :
        tamArreglo = 0
    else :
        sumaArr = tamArreglo - 1
    while (len(varListFuncion) > 0):
        variable = varListFuncion.pop()
        if(translate(p[-1]) == 1):
            cantIntFunciones += 1 + sumaArr
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_int_funciones + cont_int_funciones, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_int_funciones + tamArreglo
                while (cont_int_funciones < tamWhile) :
                    dir_int_funciones.append({'Valor' : 0, 'Direccion' : inicia_int_funciones + cont_int_funciones, 'Arreglo' : ''})
                    cont_int_funciones += 1
            else :
                dir_int_funciones.append({'Valor' : 0, 'Direccion' : inicia_int_funciones + cont_int_funciones, 'Arreglo' : ''})
                cont_int_funciones += 1
        elif(translate(p[-1]) == 2):
            cantBoolFunciones += 1 + sumaArr
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_bool_funciones + cont_bool_funciones, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_bool_funciones + tamArreglo
                while (cont_bool_funciones < tamWhile) :
                    dir_bool_funciones.append({'Valor' : '', 'Direccion' : inicia_bool_funciones + cont_bool_funciones, 'Arreglo' : ''})
                    cont_bool_funciones += 1
            else :
                dir_bool_funciones.append({'Valor' : '', 'Direccion' : inicia_bool_funciones + cont_bool_funciones, 'Arreglo' : ''})
                cont_bool_funciones += 1
        elif(translate(p[-1]) == 3):
            cantStringFunciones += 1 + sumaArr
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_string_funciones + cont_string_funciones, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_string_funciones + tamArreglo
                while (cont_string_funciones < tamWhile) :
                    dir_string_funciones.append({'Valor' : '', 'Direccion' : inicia_string_funciones + cont_string_funciones, 'Arreglo' : ''})
                    cont_string_funciones += 1
            else :
                dir_string_funciones.append({'Valor' : '', 'Direccion' : inicia_string_funciones + cont_string_funciones, 'Arreglo' : ''})
                cont_string_funciones += 1
        elif(translate(p[-1]) == 4):
            cantFloatFunciones += 1 + sumaArr
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_float_funciones + cont_float_funciones, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_float_funciones + tamArreglo
                while (cont_float_funciones < tamWhile) :
                    dir_float_funciones.append({'Valor' : 0.0, 'Direccion' : inicia_float_funciones + cont_float_funciones, 'Arreglo' : ''})
                    cont_float_funciones += 1
            else :
                dir_float_funciones.append({'Valor' : 0.0, 'Direccion' : inicia_float_funciones + cont_float_funciones, 'Arreglo' : ''})
                cont_float_funciones += 1
        elif(translate(p[-1]) == 5):
            cantCharFunciones += 1 + sumaArr
            varDirectoryFunc[variable] = {'Tipo' : p[-1], 'Scope' : 'Funcion', 'Direccion': inicia_char_funciones + cont_char_funciones, 'TamanoArreglo': tamArreglo}
            if boolArreglo :
                tamWhile = cont_char_funciones + tamArreglo
                while (cont_char_funciones < tamWhile) :
                    dir_char_funciones.append({'Valor' : '', 'Direccion' : inicia_char_funciones + cont_char_funciones, 'Arreglo' : ''})
                    cont_char_funciones += 1
            else :
                dir_char_funciones.append({'Valor' : '', 'Direccion' : inicia_char_funciones + cont_char_funciones, 'Arreglo' : ''})
                cont_char_funciones += 1
    #print("TERMINA addTypeFuncion")
    #print(varDirectoryFunc)
    


def p_idVarsFuncion(p): #Done
    '''idVarsFuncion : ID addVariableDirFuncion ambIdVarsFuncion'''

def p_addVariableDirFuncion(p):
    '''addVariableDirFuncion : '''
    global contVarLocFunc
    #print("pasa por addVariableDirFuncion")
    if (p[-1] in varDirectoryFunc or p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
        exit()
    else:
        #print("Se agrego ")
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
    '''auxAsignacion1 : LBRACKET paso6b exp RBRACKET paso7b paso27
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
        | CTESTRING paso1 assignDirectionCteString'''

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
        #print("esto es: ", dir_int_constantes)


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
        dir_bool_constantes.append({'Valor' : p[-3], 'Direccion' : inicia_bool_constantes + cont_bool_constantes, 'Arreglo' : ''})
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
    global nombreArreglo
    global tipoArreglo
    if p[-2] in varDirectory.keys():
        #print(translate(varDirectory[p[-2]]['Tipo']))
        pTipos.append(translate(varDirectory[p[-2]]['Tipo']))
        if varDirectory[p[-2]].get('TamanoArreglo') > 0 :
            nombreArreglo = p[-2] 
            tipoArreglo = translate(varDirectory[p[-2]]['Tipo'])
    elif p[-2] in varDirectoryMain.keys():
        #print(translate(varDirectoryMain[p[-2]]['Tipo']))
        pTipos.append(translate(varDirectoryMain[p[-2]]['Tipo']))
        if varDirectoryMain[p[-2]].get('TamanoArreglo') > 0 :
            nombreArreglo = p[-2]
            tipoArreglo = translate(varDirectoryMain[p[-2]]['Tipo'])
    elif p[-2] in varDirectoryFunc.keys():
        #print(translate(varDirectoryFunc[p[-2]]['Tipo']))
        pTipos.append(translate(varDirectoryFunc[p[-2]]['Tipo']))
        if varDirectoryFunc[p[-2]].get('TamanoArreglo') > 0 :
            nombreArreglo = p[-2]
            tipoArreglo = translate(varDirectoryFunc[p[-2]]['Tipo'])
    else:
        nombreArreglo = "nada"
        return -1


def p_auxVarcte(p): #Done
    '''auxVarcte : LPAREN exp RPAREN
        | LBRACKET paso6b exp RBRACKET paso7b paso27
        | '''

def p_cicloFuncion(p): #Done
    '''cicloFuncion : funcion cicloFuncion 
        | '''

def p_funcion(p): #Done
    '''funcion : FUNCTION tipo ID initDicFunc LPAREN auxFunction RPAREN bloqueFuncion addProcDirectoryFunc paso23 paso22 '''

def p_addProcDirectoryFunc(p):
    '''addProcDirectoryFunc : '''
    global contParametros
    global contVarLocFunc
    global cantIntFunciones
    global cantBoolFunciones
    global cantFloatFunciones
    global cantCharFunciones
    global cantStringFunciones
    procDirectory[funcActual]['Variables'] = varDirectoryFunc.copy()
    procDirectory[funcActual]['Tipo'] = p[-7]
    procDirectory[funcActual]['# Parametros'] = contParametros
    procDirectory[funcActual]['Locales'] = contVarLocFunc
    procDirectory[funcActual]['TamanoMemoria'] = {'Int' : cantIntFunciones, 'Bool' : cantBoolFunciones, 'String' : cantStringFunciones, 'Float' : cantFloatFunciones, 'Char' : cantCharFunciones}

    cantIntFunciones = 0
    cantBoolFunciones = 0
    cantFloatFunciones = 0
    cantCharFunciones = 0
    cantStringFunciones = 0

    #procDirectory[p[-6]] = {'Variables' : varDirectoryFunc.copy(), 'Tipo' : p[-6], 'Parametros' : contParametros, 'Locales' : contVarLocFunc, 'Inicio' : contCuadruplos }
    #varDirectoryFunc.clear()
    contParametros = 0
    contVarLocFunc = 0
    #print("pasa por addProcDirectoryFunc")
    #print(procDirectory)

def p_initDicFunc(p):
    '''initDicFunc : '''
    global funcActual
    funcActual = p[-1]
    procDirectory[p[-1]] = {'Variables' : "", 'Tipo' : p[-2], '# Parametros' : 0, 'Locales' : 0, 'Inicio' : 0, 'Retorno' : {}, 'Parametros' : 0 }

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
    global cantIntFunciones
    global cantBoolFunciones
    global cantFloatFunciones
    global cantCharFunciones
    global cantStringFunciones
    if (p[-1] in varDirectoryFunc or p[-1] in varDirectoryMain or p[-1] in varDirectory):
        print("Ya existe la variable")
        exit()
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
    if p[-2] == 'int':
        cantIntFunciones += 1
    elif p[-2] == 'bool':
        cantBoolFunciones += 1
    elif p[-2] == 'string':
        cantStringFunciones += 1
    elif p[-2] == 'float':
        cantFloatFunciones += 1
    elif p[-2] == 'char':
        cantCharFunciones += 1
        

def p_ambAuxParamentros(p): #Done
    '''ambAuxParametros : COMMA auxParametros
        | '''

def p_ciclo(p): #Done
    '''ciclo : WHILE paso15 LPAREN expAndOr RPAREN paso16 bloque paso17'''
    #print("entra a ciclo")

def p_llamada(p): #Done
    '''llamada : CALL COLON ID paso24 cteLlamada LPAREN paso6 auxLlamada RPAREN paso7 paso26 paso28'''
    #print("entra a llamada")

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
    #print(encuentraOperando(p[-1]))
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
    #print("entra a suma aqui")
    #print(pOperandos)
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
                #print(cuadruplos)
            else:
                print("Error arimetico 4 - tipos no validos")
                exit()
    #print("Sale paso 4") 


def p_paso5(p):
    '''paso5 : '''
    global pTipos
    global pOperadores
    global contprueba

    #print("Entra paso 5")
    contprueba += 1
    #print(contprueba)
    #print(pTipos)
    #print(pOperandos)
    #print(pOperadores)
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
                #print(cuadruplos)
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

def p_paso6b(p):
    '''paso6b : '''
    global esArr 
    esArr = True
    pOperadores.append("[")

def p_paso7b(p):
    '''paso7b : '''
    if pOperadores[-1] == "[" :
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
                #print(cuadruplos)
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
                #print(cuadruplos)
            else:
                #print(tipoDer)
                #print(tipoIzq)
                #print(op)
                #print("EJELE", cubo[tipoDer][tipoIzq][op])
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
            #print(opdoIzq)
            #print(opdoDer)
            #print(tipoIzq)
            #print(tipoDer)
            #if opdoIzq in varDirectory.keys() or opdoIzq in varDirectoryMain.keys() or opdoIzq in varDirectoryFunc.keys() or opdoIzq in procDirectory.keys():
            if cubo[tipoDer][tipoIzq][op] != ERR:
                tipoRes = cubo[tipoDer][tipoIzq][op]
                #print(tipoRes)
                cuadruplos[contCuadruplos] = [op, opdoDerDir, "", opdoIzqDir ]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
                contCuadruplos+=1
                #print(cuadruplos)
            else:
                print("Error arimetico 11 - tipos no validos")
                exit()
            #else: 
                #print("La variable no existe ", opdoIzq)
                #exit()
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
    #print(cuadruplos)

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
    #print("entra print")
    cuadruplos[contCuadruplos] = [PRINT, "", "", translateToDirection(pOperandos.pop())]
    #print(cuadruplos)
    #print("sale print")
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
    global contRetorno
    procDirectory[funcActual]['Variables'].clear()
    cuadruplos[contCuadruplos] = [RET, "", "", ""]
    contCuadruplos += 1
    contRetorno = 0

    #print(cuadruplos)
    parametrosA.clear()
    decNumParametro = 0
    

def p_paso23(p):
    '''paso23 : '''
    global pOperandos
    global contCuadruplos
    global funcActual
    global pTipos
    global pSaltos
    global contRetorno
    global retornos
    res = pOperandos.pop()
    tipoRes = pTipos.pop()
    #contRetorno += 1
    #print(res, "RES")
    #print(tipoRes, "TIPORES")
    #print(tipoRes)
    #print(procDirectory[funcActual]['Tipo'])
    #print("Q U E  P A S A")
    #print((procDirectory[funcActual]))
    #print(translate(procDirectory[funcActual]['Tipo']))
    if tipoRes == translate(procDirectory[funcActual]['Tipo']) :
        #print("VOY A ENTRAR")
        cuadruplos[contCuadruplos] = [RETURN, "", "", translateToDirection(res)]

        #procDirectory[funcActual]['Retorno'][contRetorno] = translateToDirection(res)
        contCuadruplos += 1
        retornos.put(translateToDirection(res))
        
        #print(cuadruplos)
        #print("PROC DIRECTORY", procDirectory[funcActual])
    else :
        print("Tipo de retorno invalido")
        exit()

def p_paso24(p):
    '''paso24 : '''
    global funcActual
    global numArgumento
    global cuadruplos
    global contCuadruplos

    #print("entra a paso24")
    funcActual = p[-1]
    if p[-1] in procDirectory :
        #print("La funcion existe en procDirectory")
        cuadruplos[contCuadruplos] = [ERA, funcActual , "", ""]
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
    #print("pOperandos: a ", pOperandos)
    res = pOperandos.pop()
    tipo = pTipos.pop()
    #numArgumento = 1
    #try :
    #print("res:", res)
    #print("osoyogi:", procDirectory[funcActual]['Parametros'])
    #print(procDirectory[funcActual]['Parametros'][res]['NumParametro'])
    #print("print de direccion param ", procDirectory[funcActual]['Parametros'][res]['Direccion'])
    #print(numArgumento)
    #print(numPar)
    parametro = ""
    #print("AQUIIIIIIIIIIII", procDirectory[funcActual]['Parametros'])

    for key in procDirectory[funcActual]['Parametros']:
        if procDirectory[funcActual]['Parametros'][key]['NumParametro'] == numArgumento:
            parametro = procDirectory[funcActual]['Parametros'][key]['Direccion']

    #print("DIRECCION PARAMETRO", parametro)

    #print("############################", numPar)
    #if numPar == numArgumento :
        #tipoParam = translate(procDirectory[funcActual]['Parametros'][res]['Tipo'])
        #if tipo == tipoParam :
    cuadruplos[contCuadruplos] = [PARAM, translateToDirection(res), "", parametro]
    numArgumento += 1
    contCuadruplos += 1
    #print(cuadruplos)
    #     else :
    #         print("Tipo invalido, no se puede")
    #         exit()
    # else :
    #     print("Argumentos invalidos")
    #     exit()
    #except :
        #print("Error try")
        #exit()
        
def p_paso26(p):
    '''paso26 : '''
    global cuadruplos
    global contCuadruplos
    global funcActual
    cuadruplos[contCuadruplos] = [GOSUB, procDirectory[funcActual]['Inicio'], "", ""]
    contCuadruplos += 1



def translateToTamano(variable):
    #print("BEFORE IF:", variable)
    #print("vardirfunc", varDirectoryFunc)
    if variable in varDirectoryMain.keys():
        return varDirectoryMain[variable].get('TamanoArreglo')
    elif variable in varDirectory.keys():
        return varDirectory[variable].get('TamanoArreglo')
    elif variable in varDirectoryFunc.keys():
        #print("ELIF 3", varDirectoryFunc)
        return varDirectoryFunc[variable].get('TamanoArreglo')
    elif variable in dirConstantes.keys():
        return dirConstantes[variable].get('TamanoArreglo')
    elif variable in parametrosA.keys():
        #print("ELIF 5", parametrosA)
        return parametrosA[variable].get('TamanoArreglo')
    elif variable in dirConstantes.keys():
        return dirConstantes[variable].get('TamanoArreglo')
    else:
        return variable

def p_paso27(p):
    '''paso27 : '''
    global nombreArreglo
    global tipoArreglo
    global contCuadruplos
    global cuadruplos
    global inicia_arreglos_temporales
    global cont_arreglos_temporales
    global contprueba
    #print("entra paso27", nombreArreglo)
    #contprueba += 1
    #print(contprueba)
    #print("tamano arreglo" ,translateToTamano(nombreArreglo))
    res = pOperandos.pop()
    arr = pOperandos.pop()
    pTipos.pop()
    res = translateToDirection(res)  
    cuadruplos[contCuadruplos] = [VER, res, 0, translateToTamano(nombreArreglo) - 1]
    contCuadruplos += 1
    
    cuadruplos[contCuadruplos] = [SUMA, translateToDirection(arr), res, inicia_arreglos_temporales + cont_arreglos_temporales]
    contCuadruplos += 1

    pOperandos.append(inicia_arreglos_temporales + cont_arreglos_temporales)
    dir_arreglos_temporales.append({'Valor' : '', 'Direccion' : inicia_arreglos_temporales + cont_arreglos_temporales, 'Arreglo' : ''})
    cont_arreglos_temporales += 1
    #print("pOperandos ya", pOperandos)
    #a = pOperandos.pop()

def p_paso28(p):
    '''paso28 : '''
    global contCuadruplos
    global cuadruplos
    global retornos
    operando = retornos.get()

    #print(operando, "paso28")
    tipo = translate(procDirectory[p[-9]]['Tipo'])
    cuadruplos[contCuadruplos] = [ASIG, operando , "", getBaseTemporalDirection(tipo) + getTemporalCounter(tipo)]
    pOperandos.pop()
    pOperandos.append(getBaseTemporalDirection(tipo) + getTemporalCounter(tipo))

    #print(getBaseTemporalDirection(tipo) + getTemporalCounter(tipo), "Contador temporal")
    changeTemporalCounter(tipo)
    #print(getBaseTemporalDirection(tipo) + getTemporalCounter(tipo), "Contador temporal")
    contCuadruplos += 1

def p_pasoFinal(p):
    '''pasoFinal : '''
    global cuadruplos
    global contCuadruplos
    cuadruplos[contCuadruplos]=[ENDPROGRAM, '','','']
    contCuadruplos +=1
    varDirectory['TamanoMemoria'] = {'Int' : cantIntGlobales, 'Bool' : cantBoolGlobales, 'String' : cantStringGlobales, 'Float' : cantFloatGlobales, 'Char' : cantCharGlobales}
    varDirectoryMain['TamanoMemoria'] = {'Int' : cantIntLocales, 'Bool' : cantBoolLocales, 'String' : cantStringLocales, 'Float' : cantFloatLocales, 'Char' : cantCharLocales}
    dirTemporales['TamanoMemoria'] = {'Int' : cont_int_temporales, 'Bool' : cont_bool_temporales, 'String' : cont_string_temporales, 'Float' : cont_float_temporales, 'Char' : cont_char_temporales, 'Arr' : cont_arreglos_temporales}
    dirCompleto[nombrePrograma] = {'Directorio Globales' : varDirectory, 'Directorio Locales' : varDirectoryMain, 'Directorio Funciones' : procDirectory, 'Directorio Constantes' : dirConstantes, 'Directorio Temporales' : dirTemporales}
    #print(dirCompleto)

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
    #print(pTipos)

def p_cteString(p):
    '''cteString : '''
    pTipos.append(STRING)

def p_cteLlamada(p):
    '''cteLlamada : '''
    global pOperandos
    global pTipos
    global contRetorno
    global retornos
    #print("entra ctellamada", contRetorno)
    #print("heyeyeyeyeyeyeyye", procDirectory[p[-2]]['Retorno'][contRetorno])
    pTipos.append(translate(procDirectory[p[-2]]['Tipo']))
    #print("procDir1", procDirectory[p[-2]]['Retorno'])
    #print(contRetorno)
    pOperandos.append(retornos.queue[0])
    #print(pTipos, "pTipos")
    #print(pOperandos, "pOperandos AQUI")
    #print("sale ctellamada")

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
    #print('Programa valido')
    #print(varDirectory)
    #print(varDirectoryMain)
    #print(procDirectory)
    #print(cuadruplos)
    maquina()
    

archivo(sys.argv[1])
