import sys
sys.path.insert(0, "../..")

tokens = ('VAR',)  # var represents the literal string 'VAR'

literals = ['=', '+', '-', '*', '/']

def t_VAR(t):
    r'VAR '
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

while True:
  code = input("Enter a line of code: ")
  lexer.input(code)

  for token in lexer:
    print(token)
