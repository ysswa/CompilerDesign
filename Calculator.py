from sly import Parser
from lexer import Lex
class Cal(Parser):
    tokens=Lex.tokens
    literals=Lex.literals
    precedence=Lex.precedence
    @_(' expr ')
    def yss(self,value):
        print(value[0])
    @_(' yss NEWLINE expr ')
    def yss(self,value):
        print(value[2])
    @_('expr "+" expr')
    def expr(self,value):
        return value[0]+value[2]
    @_('expr "-" expr')
    def expr(self,value):
        return value[0]-value[2]
    @_('expr "*" expr')
    def expr(self,value):
        return value[0]*value[2]
    @_('expr "/" expr')
    def expr(self,value):
        return value[0]/value[2]
    @_('"(" expr ")"')
    def expr(self,value):
        return value[1]
    @_(' INTEGER ')
    def expr(self,value):
        return value[0]
    @_(' ID ')
    def expr(self,value):
        return value[0]
obj=Cal()
obj2=Lex()
expr='''(2+3)*9
56/4
a+b'''
print(obj.parse(obj2.tokenize(expr)))
    
    