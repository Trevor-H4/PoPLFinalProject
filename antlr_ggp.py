import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from GeniusGentlemenParsingLexer import GeniusGentlemenParsingLexer
from GeniusGentlemenParsingParser import GeniusGentlemenParsingParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GeniusGentlemenParsingLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GeniusGentlemenParsingParser(stream)
    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    main(sys.argv)
