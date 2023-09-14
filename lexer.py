from sly import Lexer
class Lex(Lexer):
    literals={"+","-","*","/","(",")"}
    tokens={INTEGER,NEWLINE,ID,IF}
    ignore=' '
    ignore_comment='\#'
    INTEGER=r'[0-9]+'
    ID=r'[a-zA-Z]+'
    NEWLINE=r'\n'
    def INTEGER(self,t):
        t.value=int(t.value)
        return t
    def ID(self,t):
        t.value=int(input(f"enter value of {t.value}:"))
        return t
obj=Lex()
expression='2+3*6'
for t in obj.tokenize(expression):
    print(f"type={t.type} value={t.value}")
