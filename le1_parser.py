from sly import Parser
from sly import Lexer
class ParL1(Parser,Lexer):
    tokens=[ID,INT,PRINT]
    literals=["+","-","*","/","%",";",",","(",")","{","}","[","]","="]
    INT=r'[0-9]+'
    ID['print']=PRINT
    ID['int']=INT
    ID=r'[a-zA-Z][0-9_]*'
    
