from collections import defaultdict
cubo = defaultdict(lambda :defaultdict(lambda :defaultdict(int)))

# Significado de cada dimencion del cubo.
# x = operando 1
# y = operando 2
# z = operador

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5

# Equivalencia numerica de cada operando.
#	+,-:   1
#	*,/:   2
#	&,|:   3
#	<,>:   4
#	<=,>=: 5
#	==,!=: 6
#   =:     7

#	+	1
#	-   2
#	*	3
#	/   4
#	&	5
#	|   6
#	<	7
#	>   8
#	<=	9
#	>= 	10
#	==	11
#	!= 	12
#   =   13
#	GOTO 14
#	GOTOF 15

# NOTA: ERROR = -1

# + y -
cubo[1][1][1] = 1
cubo[1][2][1] = -1
cubo[1][3][1] = -1
cubo[1][4][1] = 4
cubo[1][5][1] = -1
cubo[2][1][1] = -1
cubo[2][2][1] = -1
cubo[2][3][1] = -1
cubo[2][4][1] = -1
cubo[2][5][1] = -1
cubo[3][1][1] = -1
cubo[3][2][1] = -1
cubo[3][3][1] = 3
cubo[3][4][1] = -1
cubo[3][5][1] = 3
cubo[4][1][1] = 4
cubo[4][2][1] = -1
cubo[4][3][1] = -1
cubo[4][4][1] = 4
cubo[4][5][1] = -1
cubo[5][1][1] = -1
cubo[5][2][1] = -1
cubo[5][3][1] = 3
cubo[5][4][1] =-1
cubo[5][5][1] = 5

cubo[1][1][2] = 1
cubo[1][2][2] = -1
cubo[1][3][2] = -1
cubo[1][4][2] = 4
cubo[1][5][2] = -1
cubo[2][1][2] = -1
cubo[2][2][2] = -1
cubo[2][3][2] = -1
cubo[2][4][2] = -1
cubo[2][5][2] = -1
cubo[3][1][2] = -1
cubo[3][2][2] = -1
cubo[3][3][2] = 3
cubo[3][4][2] = -1
cubo[3][5][2] = 3
cubo[4][1][2] = 4
cubo[4][2][2] = -1
cubo[4][3][2] = -1
cubo[4][4][2] = 4
cubo[4][5][2] = -1
cubo[5][1][2] = -1
cubo[5][2][2] = -1
cubo[5][3][2] = 3
cubo[5][4][2] =-1
cubo[5][5][2] = 5


# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# * y /
cubo[1][1][3] = 1
cubo[1][2][3] = -1
cubo[1][3][3] = -1
cubo[1][4][3] = 4
cubo[1][5][3] = -1
cubo[2][1][3] = -1
cubo[2][2][3] = -1
cubo[2][3][3] = -1
cubo[2][4][3] = -1
cubo[2][5][3] = -1
cubo[3][1][3] = -1
cubo[3][2][3] = -1
cubo[3][3][3] = -1
cubo[3][4][3] = -1
cubo[3][5][3] = -1
cubo[4][1][3] = 4
cubo[4][2][3] = -1
cubo[4][3][3] = -1
cubo[4][4][3] = 4
cubo[4][5][3] = -1
cubo[5][1][3] = -1
cubo[5][2][3] = -1
cubo[5][3][3] = -1
cubo[5][4][3] = -1
cubo[5][5][3] = -1

cubo[1][1][4] = 1
cubo[1][2][4] = -1
cubo[1][3][4] = -1
cubo[1][4][4] = 4
cubo[1][5][4] = -1
cubo[2][1][4] = -1
cubo[2][2][4] = -1
cubo[2][3][4] = -1
cubo[2][4][4] = -1
cubo[2][5][4] = -1
cubo[3][1][4] = -1
cubo[3][2][4] = -1
cubo[3][3][4] = -1
cubo[3][4][4] = -1
cubo[3][5][4] = -1
cubo[4][1][4] = 4
cubo[4][2][4] = -1
cubo[4][3][4] = -1
cubo[4][4][4] = 4
cubo[4][5][4] = -1
cubo[5][1][4] = -1
cubo[5][2][4] = -1
cubo[5][3][4] = -1
cubo[5][4][4] = -1
cubo[5][5][4] = -1

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# & y |
cubo[1][1][5] = -1
cubo[1][2][5] = -1
cubo[1][3][5] = -1
cubo[1][4][5] = -1
cubo[1][5][5] = -1
cubo[2][1][5] = -1
cubo[2][2][5] = 2
cubo[2][3][5] = -1
cubo[2][4][5] = -1
cubo[2][5][5] = -1
cubo[3][1][5] = -1
cubo[3][2][5] = -1
cubo[3][3][5] = -1
cubo[3][4][5] = -1
cubo[3][5][5] = -1
cubo[4][1][5] = -1
cubo[4][2][5] = -1
cubo[4][3][5] = -1
cubo[4][4][5] = -1
cubo[4][5][5] = -1
cubo[5][1][5] = -1
cubo[5][2][5] = -1
cubo[5][3][5] = -1
cubo[5][4][5] = -1
cubo[5][5][5] = -1

cubo[1][1][6] = -1
cubo[1][2][6] = -1
cubo[1][3][6] = -1
cubo[1][4][6] = -1
cubo[1][5][6] = -1
cubo[2][1][6] = -1
cubo[2][2][6] = 2
cubo[2][3][6] = -1
cubo[2][4][6] = -1
cubo[2][5][6] = -1
cubo[3][1][6] = -1
cubo[3][2][6] = -1
cubo[3][3][6] = -1
cubo[3][4][6] = -1
cubo[3][5][6] = -1
cubo[4][1][6] = -1
cubo[4][2][6] = -1
cubo[4][3][6] = -1
cubo[4][4][6] = -1
cubo[4][5][6] = -1
cubo[5][1][6] = -1
cubo[5][2][6] = -1
cubo[5][3][6] = -1
cubo[5][4][6] = -1
cubo[5][5][6] = -1

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# < y >
cubo[1][1][7] = 2
cubo[1][2][7] = -1
cubo[1][3][7] = -1
cubo[1][4][7] = 2
cubo[1][5][7] = -1
cubo[2][1][7] = -1
cubo[2][2][7] = -1
cubo[2][3][7] = -1
cubo[2][4][7] = -1
cubo[2][5][7] = -1
cubo[3][1][7] = -1
cubo[3][2][7] = -1
cubo[3][3][7] = 2
cubo[3][4][7] = -1
cubo[3][5][7] = 2
cubo[4][1][7] = 2
cubo[4][2][7] = -1
cubo[4][3][7] = -1
cubo[4][4][7] = 2
cubo[4][5][7] = -1
cubo[5][1][7] = -1
cubo[5][2][7] = -1
cubo[5][3][7] = 2
cubo[5][4][7] = -1
cubo[5][5][7] = 2

cubo[1][1][8] = 2
cubo[1][2][8] = -1
cubo[1][3][8] = -1
cubo[1][4][8] = 2
cubo[1][5][8] = -1
cubo[2][1][8] = -1
cubo[2][2][8] = -1
cubo[2][3][8] = -1
cubo[2][4][8] = -1
cubo[2][5][8] = -1
cubo[3][1][8] = -1
cubo[3][2][8] = -1
cubo[3][3][8] = 2
cubo[3][4][8] = -1
cubo[3][5][8] = 2
cubo[4][1][8] = 2
cubo[4][2][8] = -1
cubo[4][3][8] = -1
cubo[4][4][8] = 2
cubo[4][5][8] = -1
cubo[5][1][8] = -1
cubo[5][2][8] = -1
cubo[5][3][8] = 2
cubo[5][4][8] = -1
cubo[5][5][8] = 2

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# <= y >=
cubo[1][1][9] = 2
cubo[1][2][9] = -1
cubo[1][3][9] = -1
cubo[1][4][9] = 2
cubo[1][5][9] = -1
cubo[2][1][9] = -1
cubo[2][2][9] = -1
cubo[2][3][9] = -1
cubo[2][4][9] = -1
cubo[2][5][9] = -1
cubo[3][1][9] = -1
cubo[3][2][9] = -1
cubo[3][3][9] = 2
cubo[3][4][9] = -1
cubo[3][5][9] = 2
cubo[4][1][9] = 2
cubo[4][2][9] = -1
cubo[4][3][9] = -1
cubo[4][4][9] = 2
cubo[4][5][9] = -1
cubo[5][1][9] = -1
cubo[5][2][9] = -1
cubo[5][3][9] = 2
cubo[5][4][9] = -1
cubo[5][5][9] = 2

cubo[1][1][10] = 2
cubo[1][2][10] = -1
cubo[1][3][10] = -1
cubo[1][4][10] = 2
cubo[1][5][10] = -1
cubo[2][1][10] = -1
cubo[2][2][10] = -1
cubo[2][3][10] = -1
cubo[2][4][10] = -1
cubo[2][5][10] = -1
cubo[3][1][10] = -1
cubo[3][2][10] = -1
cubo[3][3][10] = 2
cubo[3][4][10] = -1
cubo[3][5][10] = 2
cubo[4][1][10] = 2
cubo[4][2][10] = -1
cubo[4][3][10] = -1
cubo[4][4][10] = 2
cubo[4][5][10] = -1
cubo[5][1][10] = -1
cubo[5][2][10] = -1
cubo[5][3][10] = 2
cubo[5][4][10] = -1
cubo[5][5][10] = 2

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# == y !=
cubo[1][1][11] = 2
cubo[1][2][11] = -1
cubo[1][3][11] = -1
cubo[1][4][11] = 2
cubo[1][5][11] = -1
cubo[2][1][11] = -1
cubo[2][2][11] = -1
cubo[2][3][11] = -1
cubo[2][4][11] = -1
cubo[2][5][11] = -1
cubo[3][1][11] = -1
cubo[3][2][11] = -1
cubo[3][3][11] = 2
cubo[3][4][11] = -1
cubo[3][5][11] = 2
cubo[4][1][11] = 2
cubo[4][2][11] = -1
cubo[4][3][11] = -1
cubo[4][4][11] = 2
cubo[4][5][11] = -1
cubo[5][1][11] = -1
cubo[5][2][11] = -1
cubo[5][3][11] = 2
cubo[5][4][11] = -1
cubo[5][5][11] = 2

cubo[1][1][12] = 2
cubo[1][2][12] = -1
cubo[1][3][12] = -1
cubo[1][4][12] = 2
cubo[1][5][12] = -1
cubo[2][1][12] = -1
cubo[2][2][12] = -1
cubo[2][3][12] = -1
cubo[2][4][12] = -1
cubo[2][5][12] = -1
cubo[3][1][12] = -1
cubo[3][2][12] = -1
cubo[3][3][12] = 2
cubo[3][4][12] = -1
cubo[3][5][12] = 2
cubo[4][1][12] = 2
cubo[4][2][12] = -1
cubo[4][3][12] = -1
cubo[4][4][12] = 2
cubo[4][5][12] = -1
cubo[5][1][12] = -1
cubo[5][2][12] = -1
cubo[5][3][12] = 2
cubo[5][4][12] = -1
cubo[5][5][12] = 2

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# =
cubo[1][1][13] = 1
cubo[1][2][13] = -1
cubo[1][3][13] = -1
cubo[1][4][13] = -1
cubo[1][5][13] = -1
cubo[2][1][13] = -1
cubo[2][2][13] = 2
cubo[2][3][13] = -1
cubo[2][4][13] = -1
cubo[2][5][13] = -1
cubo[3][1][13] = -1
cubo[3][2][13] = -1
cubo[3][3][13] = 3
cubo[3][4][13] = -1
cubo[3][5][13] = 3
cubo[4][1][13] = -1
cubo[4][2][13] = -1
cubo[4][3][13] = -1
cubo[4][4][13] = 4
cubo[4][5][13] = -1
cubo[5][1][13] = -1
cubo[5][2][13] = -1
cubo[5][3][13] = -1
cubo[5][4][13] = -1
cubo[5][5][13] = 5

# Funcion para consultar tipo de dato resultante.
def getResultType(op1, op2, s):
	return cubo[op1][op2][s]
