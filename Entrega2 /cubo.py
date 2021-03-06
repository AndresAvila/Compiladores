from collections import defaultdict
cubo = defaultdict(lambda :defaultdict(lambda :defaultdict(int)))

# Significado de cada dimención del cubo.
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


# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# * y /
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
cubo[3][3][2] = -1
cubo[3][4][2] = -1
cubo[3][5][2] = -1
cubo[4][1][2] = 4
cubo[4][2][2] = -1
cubo[4][3][2] = -1
cubo[4][4][2] = 4
cubo[4][5][2] = -1
cubo[5][1][2] = -1
cubo[5][2][2] = -1
cubo[5][3][2] = -1
cubo[5][4][2] = -1
cubo[5][5][2] = -1

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# & y |
cubo[1][1][3] = -1
cubo[1][2][3] = -1
cubo[1][3][3] = -1
cubo[1][4][3] = -1
cubo[1][5][3] = -1
cubo[2][1][3] = -1
cubo[2][2][3] = 2
cubo[2][3][3] = -1
cubo[2][4][3] = -1
cubo[2][5][3] = -1
cubo[3][1][3] = -1
cubo[3][2][3] = -1
cubo[3][3][3] = -1
cubo[3][4][3] = -1
cubo[3][5][3] = -1
cubo[4][1][3] = -1
cubo[4][2][3] = -1
cubo[4][3][3] = -1
cubo[4][4][3] = -1
cubo[4][5][3] = -1
cubo[5][1][3] = -1
cubo[5][2][3] = -1
cubo[5][3][3] = -1
cubo[5][4][3] = -1
cubo[5][5][3] = -1

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# < y >
cubo[1][1][4] = 2
cubo[1][2][4] = -1
cubo[1][3][4] = -1
cubo[1][4][4] = 2
cubo[1][5][4] = -1
cubo[2][1][4] = -1
cubo[2][2][4] = -1
cubo[2][3][4] = -1
cubo[2][4][4] = -1
cubo[2][5][4] = -1
cubo[3][1][4] = -1
cubo[3][2][4] = -1
cubo[3][3][4] = 2
cubo[3][4][4] = -1
cubo[3][5][4] = 2
cubo[4][1][4] = 2
cubo[4][2][4] = -1
cubo[4][3][4] = -1
cubo[4][4][4] = 2
cubo[4][5][4] = -1
cubo[5][1][4] = -1
cubo[5][2][4] = -1
cubo[5][3][4] = 2
cubo[5][4][4] = -1
cubo[5][5][4] = 2

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# <= y >=
cubo[1][1][5] = 2
cubo[1][2][5] = -1
cubo[1][3][5] = -1
cubo[1][4][5] = 2
cubo[1][5][5] = -1
cubo[2][1][5] = -1
cubo[2][2][5] = -1
cubo[2][3][5] = -1
cubo[2][4][5] = -1
cubo[2][5][5] = -1
cubo[3][1][5] = -1
cubo[3][2][5] = -1
cubo[3][3][5] = 2
cubo[3][4][5] = -1
cubo[3][5][5] = 2
cubo[4][1][5] = 2
cubo[4][2][5] = -1
cubo[4][3][5] = -1
cubo[4][4][5] = 2
cubo[4][5][5] = -1
cubo[5][1][5] = -1
cubo[5][2][5] = -1
cubo[5][3][5] = 2
cubo[5][4][5] = -1
cubo[5][5][5] = 2

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# == y !=
cubo[1][1][6] = 2
cubo[1][2][6] = -1
cubo[1][3][6] = -1
cubo[1][4][6] = 2
cubo[1][5][6] = -1
cubo[2][1][6] = -1
cubo[2][2][6] = -1
cubo[2][3][6] = -1
cubo[2][4][6] = -1
cubo[2][5][6] = -1
cubo[3][1][6] = -1
cubo[3][2][6] = -1
cubo[3][3][6] = 2
cubo[3][4][6] = -1
cubo[3][5][6] = 2
cubo[4][1][6] = 2
cubo[4][2][6] = -1
cubo[4][3][6] = -1
cubo[4][4][6] = 2
cubo[4][5][6] = -1
cubo[5][1][6] = -1
cubo[5][2][6] = -1
cubo[5][3][6] = 2
cubo[5][4][6] = -1
cubo[5][5][6] = 2

# Equivalencia numerica de cada tipo de dato.
# Int:    1
# Bool:   2
# String: 3
# Float:  4
# Char:   5
# =
cubo[1][1][7] = 1
cubo[1][2][7] = -1
cubo[1][3][7] = -1
cubo[1][4][7] = 1
cubo[1][5][7] = -1
cubo[2][1][7] = -1
cubo[2][2][7] = 2
cubo[2][3][7] = -1
cubo[2][4][7] = -1
cubo[2][5][7] = -1
cubo[3][1][7] = -1
cubo[3][2][7] = -1
cubo[3][3][7] = 3
cubo[3][4][7] = -1
cubo[3][5][7] = 3
cubo[4][1][7] = 4
cubo[4][2][7] = -1
cubo[4][3][7] = -1
cubo[4][4][7] = 4
cubo[4][5][7] = -1
cubo[5][1][7] = -1
cubo[5][2][7] = -1
cubo[5][3][7] = -1
cubo[5][4][7] = -1
cubo[5][5][7] = 5

# Funcion para consultar tipo de dato resultante.
def getResultType(op1, op2, s):
	return cubo[op1][op2][s]
