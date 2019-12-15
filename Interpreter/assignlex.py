# assignlex.py

'''
-------------------------------------------------------------------------
* Aniss Fadel
* CISC 3160
* Final Project:
*    http://www.sci.brooklyn.cuny.edu/~zhou/teaching/cis3160/project.html
-------------------------------------------------------------------------
The following command will install the sly module into your computer
for python 3.7:
    pip3 install sly
'''  
# assignlex.py
from sly import Lexer
class AssignmentLexer(Lexer):
    tokens = {IDENTIFIER,LITERAL, PLUS, MINUS, TIMES, ASSIGN, LPAREN, RPAREN, COLON}
    ignore =' \t'

    '''
    Identifier:
     	Letter [Letter | Digit]*

    Letter:
        a|...|z|A|...|Z|_

    Literal:
	0 | NonZeroDigit Digit*
		
    NonZeroDigit:
	1|...|9

    Digit:
	0|1|...|9
    '''
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
    LITERAL = r'0|[1-9][0-9]*'
    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    COLON = r';'

    
if __name__ == '__main__':
    data = 'x = 5 '
    lexer = AssignmentLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
    
