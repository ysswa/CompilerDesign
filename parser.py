from sly import Parser
from lexer import Lex
class calcParser(Parser):
    literals=Lex.literals
    tokens=Lex.tokens
    precedence=(('left',"+","-"),('left',"/","*"))
    @_('expr')
    def L(self,value):
        print(value[0])
    @_('L NEWLINE expr')
    def L(self,value):
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
    @_('INTEGER')
    def expr(self,value):
        return value[0]
    @_('ID')
    def expr(self,value):
        return value[0]
obj1=Lex()
obj2=calcParser()
expression='''2+3-9
5*8
4+99-3
a+b*c'''
obj2.parse(obj1.tokenize(expression))