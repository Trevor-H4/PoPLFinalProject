# Generated from GeniusGentlemenParsing.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,3,4,29,
        8,4,1,4,1,4,1,5,4,5,34,8,5,11,5,12,5,35,1,6,3,6,39,8,6,1,7,1,7,3,
        7,43,8,7,1,8,1,8,3,8,47,8,8,1,8,5,8,50,8,8,10,8,12,8,53,9,8,0,0,
        9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,6,4,0,37,37,42,43,
        45,45,47,47,1,0,13,13,1,0,10,10,1,0,48,57,2,0,65,90,97,122,2,0,48,
        57,95,95,58,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,
        1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,0,7,25,1,0,0,0,9,28,1,0,0,0,11,33,
        1,0,0,0,13,38,1,0,0,0,15,42,1,0,0,0,17,46,1,0,0,0,19,20,5,40,0,0,
        20,2,1,0,0,0,21,22,5,41,0,0,22,4,1,0,0,0,23,24,5,61,0,0,24,6,1,0,
        0,0,25,26,7,0,0,0,26,8,1,0,0,0,27,29,7,1,0,0,28,27,1,0,0,0,28,29,
        1,0,0,0,29,30,1,0,0,0,30,31,7,2,0,0,31,10,1,0,0,0,32,34,7,3,0,0,
        33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,12,1,
        0,0,0,37,39,7,4,0,0,38,37,1,0,0,0,39,14,1,0,0,0,40,43,3,13,6,0,41,
        43,7,5,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,16,1,0,0,0,44,47,3,13,
        6,0,45,47,5,95,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,51,1,0,0,0,48,
        50,3,15,7,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,
        0,0,52,18,1,0,0,0,53,51,1,0,0,0,7,0,28,35,38,42,46,51,0
    ]

class GeniusGentlemenParsingLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ARITHMETIC_OPERATOR = 4
    NEWLINE = 5
    INT = 6
    LETTERS = 7
    CHARS = 8
    VAR = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ARITHMETIC_OPERATOR", "NEWLINE", "INT", "LETTERS", "CHARS", 
            "VAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ARITHMETIC_OPERATOR", "NEWLINE", 
                  "INT", "LETTERS", "CHARS", "VAR" ]

    grammarFileName = "GeniusGentlemenParsing.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


