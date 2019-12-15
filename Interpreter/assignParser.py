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
# assignParser.py


from sly import Lexer
from sly import Parser
from assignlex import AssignmentLexer



class AssignmentParser(Parser):
    tokens = AssignmentLexer.tokens


  
    def __init__(self):
        self.symbolTable = {}
    

    
    # Program:
    #       Assignment*
    #---------------------------------------------------------------
    @_('assignment')
    def program(self, p):
        if p.assignment is not None:
            return p.assignment 
    @_('assignment program')
    def program(self, p):
        if p.assignment is not None and p.program is not None:
            return p.assignment +'\n'+ p.program
        
    #---------------------------------------------------------------

    # Assignment:
    #       Identifier = Exp;
    #
    #       Identifer -> error: variable not initialized.....
    #---------------------------------------------------------------
    @_('IDENTIFIER ASSIGN exp COLON')
    def assignment(self, p):
        if p.exp is not None:
            self.symbolTable[p.IDENTIFIER] = p.exp
            print(p.IDENTIFIER + " "+ p.ASSIGN + " " + p.exp)
            
    @_('IDENTIFIER COLON')
    def assignment(self, p):
        if p.IDENTIFIER in self.symbolTable.keys():
            print(p.IDENTIFIER + " = " + self.symbolTable[p.IDENTIFIER])
        else:
            print("error: variable '"+p.IDENTIFIER+"' not initialized")
    #---------------------------------------------------------------
    # Exp:
    #       Exp + Term | Exp - Term | Term
    #---------------------------------------------------------------
    @_('exp PLUS term')
    def exp(self, p):
        if p.exp is not None and p.term is not None:
            return str(int(p.exp) + int(p.term))

    @_('exp MINUS term')
    def exp(self, p):
        return str(int(p.exp) - int(p.term))

    @_('term')
    def exp(self, p):
        return p.term
    #---------------------------------------------------------------
    # Term:
    #       Term * Fact | Fact
    #---------------------------------------------------------------
    @_('term TIMES fact')
    def term(self, p):
        if p.term is not None and p.fact is not None:
            return str(int(p.term) * int(p.fact))
    
    @_('fact')
    def term(self, p):
        return p.fact
    #---------------------------------------------------------------
    # Fact:
    #       ( Exp ) | - Fact | + Fact | Literal | Identifier
    #---------------------------------------------------------------
    @_('LPAREN exp RPAREN')
    def fact(self, p):
        return p.exp
    
    @_('MINUS fact')
    def fact(self, p):
        if p.fact is not None:
            return str(-1*int(p.fact))
    
    @_('PLUS fact')
    def fact(self, p):
        return p.fact
    
    @_('LITERAL')
    def fact(self, p):
        return p.LITERAL
    
    @_('IDENTIFIER')
    def fact(self, p):
        if p.IDENTIFIER in self.symbolTable.keys():
            return self.symbolTable[p.IDENTIFIER]
        else:
           print("Identifier '"+p.IDENTIFIER+ "' does not exist")


if __name__ == '__main__':
    lexer = AssignmentLexer()
    parser = AssignmentParser()
    symbolTable = parser.symbolTable;
    while True:
        try:
            text = input('assignment > ')
            result = parser.parse(lexer.tokenize(text))
            #print(symbolTable)
        except EOFError:
            break


    
