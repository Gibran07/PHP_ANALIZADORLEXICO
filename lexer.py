import ply.lex as lex
import re
import sys 

tokens = ("VARIABLE","SUMAR","RESTAR","MULTIPLICAR","DIVIDIR","NUMBER","COMMA",
"RPARENT","LPARENT","COMILLA","STRING","MENOR_QUE","MAYOR_QUE","MENOR_IGUAL","MAYOR_IGUAL",
"DECIMAL","BOLEAN","EXCLAMACION","PREGUNTA","PUNTOCOMA","EXCLAMACION2","PESOS",
#Palabras reservadasa
"END","PRINT","PUTS","IF","ELSE","AND","CASE","DEF","DO","WHEN"          

          )

t_ignore = '\t'

def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(chr(27) + "[1;31m" + "\t ERROR: Caracter Illegal" + chr(27) + "[0m")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)

t_RESTAR = r'\-'
t_SUMAR = r'\+'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'\/'
t_COMMA = r'\,'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMILLA = r'\"'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_IGUAL = r'\<\='
t_MAYOR_IGUAL = r'\>\='
t_EXCLAMACION = r'\!'
t_PREGUNTA = r'\?'
t_EXCLAMACION2 = r'\¡'
t_PUNTOCOMA = r'\;'
t_PESOS = r'\$'


def t_END(t):
    r'end'
    return t
def t_AND(t):
    r'and'
    return t
def t_CASE(t):
    r'case'
    return t
def t_DEF(t):
    r'def'
    return t
def t_DO(t):
    r'do'
    return t
def t_WHEN(t):
    r'when'
    return t
def t_VARIABLE(t):
    r'\w+\=|\w+\s\='
    return t
def t_PRINT(t):
    r'print'
    return t
def t_PUTS(t):
    r'puts'
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t

def t_NUMBER(t):
    r'\d+\s'
    t.value = int(t.value)
    return t
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_BOLEAN(t):
    r'true|false'
    return t
def t_STRING(t):
    r'\w+|:'
    return t

lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script = sys.argv[1]

        scriptfile = open(script, "r")
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print(chr(27) + "[0;36m" + "INICIA ANALISIS LEXICO" + chr(27) + "[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(
                "\t"
                + str(i)
                + " - "
                + "Line: "
                + str(tok.lineno)
                + "\t"
                + str(tok.type)
                + "\t-->  "
                + str(tok.value)
            )
            i += 1

        print(chr(27) + "[0;36m" + "TERMINA ANALISIS LEXICO" + chr(27) + "[0m")

    else:
        print(chr(27) + "[0;31m" + "Pase el archivo de scritp Cs como parametro")
        print(
            chr(27)
            + "[0;36m"
            + "\t$ python lexer.py"
            + chr(27)
            + "[1;31m"
            + " <filename>.php"
            + chr(27)
            + "[0m"
        )
