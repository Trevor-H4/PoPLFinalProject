import sys
from antlr4 import *
from GeniusGentlemenParsingLexer import GeniusGentlemenParsingLexer
from GeniusGentlemenParsingParser import GeniusGentlemenParsingParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GeniusGentlemenParsingLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GeniusGentlemenParsingParser(stream)
    tree = parser.start()
 
if __name__ == '__main__':
    main(sys.argv)
