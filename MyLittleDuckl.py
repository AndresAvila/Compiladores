import ply.lex as lex


# List of reserved word that are going to be added to the tokens
reserved = {
  'program' : 'PROGRAM',
  'var' : 'VAR',
  'print' : 'PRINT',
  'if' : 'IF',
  'else' : 'ELSE',
  'int' : 'INT',
  'bool' : 'BOOL',
  'string' : 'STRING',
  'float' : 'FLOAT',
  'char' : 'CHAR',
  'while' : 'WHILE',
}

# List of token names. This is always required
tokens = [
  'ID', #DONE
  'PLUS',#DONE
  'MINUS',#DONE
  'MULTI',#DONE
  'DIVIDE',#DONE
  'LPAREN',#DONE
  'RPAREN',#DONE
  'LBRACE',#DONE
  'RBRACE',#DONE
  'CTEINT',#DONE
  'CTEFLOAT',#DONE
  'CTESTRING',#DONE
  'CTECHAR',#DONE
  'CTEBOOL',#DONE
  'EQUAL',#DONE
  'GTHAN',#DONE
  'LTHAN',#DONE
  'NOTEQUAL',#DONE
  'GETHAN',#DONE
  'LETHAN',#DONE
  'COMMA',#DONE
  'COLON',#DONE
  'SEMICOLON'#DONE
] + list(reserved.values())


    # Regular expression rules for simple tokens
t_CTEINT    = r'[\+-]?\d+'
t_CTEFLOAT  = r'[\+-]?\d+\.\d+'
t_CTECHAR      = r'.'
t_CTEBOOL      = r'true|false'
t_CTESTRING    = r'\'.*\''
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTI     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_EQUAL     = r'=='
t_GTHAN     = r'>'
t_LTHAN     = r'<'
t_GETHAN     = r'>='
t_LETHAN     = r'<='
t_NOTEQUAL    = r'<>'
t_COMMA     = r'\,'
t_COLON     = r':'
t_SEMICOLON = r';'
t_ignore    = ' \t'

    # A regular expression rule with some action code
def t_ID(t):
  r'[a-zA-Z][a-zA-Z0-9]*'
  t.type = reserved.get(t.value, 'ID')
  return t

    # Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

    # Error handling rule
def t_error(t):
  print("Illegal Character '", t.value[0], "' at line: ", t.lexer.lineno)
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
    id while HEHE XD 'GG' 3 + 4 * 10
    + -20 *2
    '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
