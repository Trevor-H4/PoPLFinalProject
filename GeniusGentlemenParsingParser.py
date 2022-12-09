# Generated from GeniusGentlemenParsing.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,256,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,37,8,1,1,1,3,1,40,8,1,
        1,1,3,1,43,8,1,1,1,1,1,3,1,47,8,1,1,2,3,2,50,8,2,1,2,1,2,1,2,1,2,
        3,2,56,8,2,1,2,1,2,3,2,60,8,2,1,2,1,2,3,2,64,8,2,1,2,1,2,3,2,68,
        8,2,1,2,1,2,3,2,72,8,2,5,2,74,8,2,10,2,12,2,77,9,2,3,2,79,8,2,1,
        2,1,2,3,2,83,8,2,1,2,1,2,3,2,87,8,2,1,2,3,2,90,8,2,1,2,1,2,1,2,4,
        2,95,8,2,11,2,12,2,96,1,3,1,3,1,4,1,4,1,4,1,4,3,4,105,8,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,120,8,5,1,5,1,
        5,3,5,124,8,5,1,5,1,5,3,5,128,8,5,1,5,1,5,1,5,3,5,133,8,5,1,5,1,
        5,3,5,137,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,145,8,5,10,5,12,5,148,
        9,5,1,6,1,6,3,6,152,8,6,1,6,3,6,155,8,6,1,6,1,6,3,6,159,8,6,1,6,
        1,6,1,7,1,7,1,7,1,7,3,7,167,8,7,1,7,1,7,3,7,171,8,7,1,7,3,7,174,
        8,7,1,7,1,7,1,7,4,7,179,8,7,11,7,12,7,180,1,7,3,7,184,8,7,1,8,1,
        8,3,8,188,8,8,1,8,1,8,3,8,192,8,8,1,8,3,8,195,8,8,1,8,1,8,1,8,4,
        8,200,8,8,11,8,12,8,201,1,9,1,9,1,9,1,9,3,9,208,8,9,1,9,1,9,3,9,
        212,8,9,1,9,3,9,215,8,9,1,9,1,9,1,9,4,9,220,8,9,11,9,12,9,221,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,232,8,10,1,10,1,10,3,
        10,236,8,10,1,10,3,10,239,8,10,1,10,1,10,1,10,4,10,244,8,10,11,10,
        12,10,245,1,11,1,11,1,11,5,11,251,8,11,10,11,12,11,254,9,11,1,11,
        1,252,1,10,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,301,0,27,1,0,0,
        0,2,46,1,0,0,0,4,49,1,0,0,0,6,98,1,0,0,0,8,104,1,0,0,0,10,119,1,
        0,0,0,12,149,1,0,0,0,14,162,1,0,0,0,16,185,1,0,0,0,18,203,1,0,0,
        0,20,223,1,0,0,0,22,247,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,
        30,31,5,0,0,1,31,1,1,0,0,0,32,37,3,10,5,0,33,37,3,6,3,0,34,37,5,
        20,0,0,35,37,5,21,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,
        36,35,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,40,5,20,0,0,39,38,1,
        0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,43,3,22,11,0,42,41,1,0,0,0,
        42,43,1,0,0,0,43,44,1,0,0,0,44,47,5,24,0,0,45,47,3,8,4,0,46,36,1,
        0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,50,5,20,0,0,49,48,1,0,0,0,49,
        50,1,0,0,0,50,51,1,0,0,0,51,52,5,8,0,0,52,53,5,20,0,0,53,55,5,30,
        0,0,54,56,5,20,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,
        59,5,1,0,0,58,60,5,20,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,78,1,0,
        0,0,61,63,5,30,0,0,62,64,5,20,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,
        75,1,0,0,0,65,67,5,2,0,0,66,68,5,20,0,0,67,66,1,0,0,0,67,68,1,0,
        0,0,68,69,1,0,0,0,69,71,5,30,0,0,70,72,5,20,0,0,71,70,1,0,0,0,71,
        72,1,0,0,0,72,74,1,0,0,0,73,65,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,
        0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,78,61,1,0,0,0,78,79,
        1,0,0,0,79,80,1,0,0,0,80,82,5,3,0,0,81,83,5,20,0,0,82,81,1,0,0,0,
        82,83,1,0,0,0,83,84,1,0,0,0,84,86,5,19,0,0,85,87,5,20,0,0,86,85,
        1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,90,3,22,11,0,89,88,1,0,0,
        0,89,90,1,0,0,0,90,91,1,0,0,0,91,94,5,24,0,0,92,93,5,20,0,0,93,95,
        3,2,1,0,94,92,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,
        97,5,1,0,0,0,98,99,3,12,6,0,99,7,1,0,0,0,100,105,3,14,7,0,101,105,
        3,18,9,0,102,105,3,20,10,0,103,105,3,4,2,0,104,100,1,0,0,0,104,101,
        1,0,0,0,104,102,1,0,0,0,104,103,1,0,0,0,105,9,1,0,0,0,106,107,6,
        5,-1,0,107,120,5,25,0,0,108,120,5,30,0,0,109,120,5,17,0,0,110,120,
        5,18,0,0,111,112,5,1,0,0,112,113,3,10,5,0,113,114,5,3,0,0,114,120,
        1,0,0,0,115,116,5,4,0,0,116,117,5,20,0,0,117,120,3,10,5,2,118,120,
        5,9,0,0,119,106,1,0,0,0,119,108,1,0,0,0,119,109,1,0,0,0,119,110,
        1,0,0,0,119,111,1,0,0,0,119,115,1,0,0,0,119,118,1,0,0,0,120,146,
        1,0,0,0,121,123,10,10,0,0,122,124,5,20,0,0,123,122,1,0,0,0,123,124,
        1,0,0,0,124,125,1,0,0,0,125,127,5,23,0,0,126,128,5,20,0,0,127,126,
        1,0,0,0,127,128,1,0,0,0,128,129,1,0,0,0,129,145,3,10,5,11,130,132,
        10,4,0,0,131,133,5,20,0,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,
        1,0,0,0,134,136,5,22,0,0,135,137,5,20,0,0,136,135,1,0,0,0,136,137,
        1,0,0,0,137,138,1,0,0,0,138,145,3,10,5,5,139,140,10,3,0,0,140,141,
        5,20,0,0,141,142,5,10,0,0,142,143,5,20,0,0,143,145,3,10,5,4,144,
        121,1,0,0,0,144,130,1,0,0,0,144,139,1,0,0,0,145,148,1,0,0,0,146,
        144,1,0,0,0,146,147,1,0,0,0,147,11,1,0,0,0,148,146,1,0,0,0,149,151,
        5,30,0,0,150,152,5,20,0,0,151,150,1,0,0,0,151,152,1,0,0,0,152,154,
        1,0,0,0,153,155,5,23,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,156,
        1,0,0,0,156,158,5,5,0,0,157,159,5,20,0,0,158,157,1,0,0,0,158,159,
        1,0,0,0,159,160,1,0,0,0,160,161,3,10,5,0,161,13,1,0,0,0,162,163,
        5,11,0,0,163,164,5,20,0,0,164,166,3,10,5,0,165,167,5,20,0,0,166,
        165,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,170,5,19,0,0,169,
        171,5,20,0,0,170,169,1,0,0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,
        174,3,22,11,0,173,172,1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,
        178,5,24,0,0,176,177,5,20,0,0,177,179,3,2,1,0,178,176,1,0,0,0,179,
        180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,
        184,3,16,8,0,183,182,1,0,0,0,183,184,1,0,0,0,184,15,1,0,0,0,185,
        187,5,13,0,0,186,188,5,20,0,0,187,186,1,0,0,0,187,188,1,0,0,0,188,
        189,1,0,0,0,189,191,5,19,0,0,190,192,5,20,0,0,191,190,1,0,0,0,191,
        192,1,0,0,0,192,194,1,0,0,0,193,195,3,22,11,0,194,193,1,0,0,0,194,
        195,1,0,0,0,195,196,1,0,0,0,196,199,5,24,0,0,197,198,5,20,0,0,198,
        200,3,2,1,0,199,197,1,0,0,0,200,201,1,0,0,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,17,1,0,0,0,203,204,5,14,0,0,204,205,5,20,0,0,205,
        207,3,10,5,0,206,208,5,20,0,0,207,206,1,0,0,0,207,208,1,0,0,0,208,
        209,1,0,0,0,209,211,5,19,0,0,210,212,5,20,0,0,211,210,1,0,0,0,211,
        212,1,0,0,0,212,214,1,0,0,0,213,215,3,22,11,0,214,213,1,0,0,0,214,
        215,1,0,0,0,215,216,1,0,0,0,216,219,5,24,0,0,217,218,5,20,0,0,218,
        220,3,2,1,0,219,217,1,0,0,0,220,221,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,19,1,0,0,0,223,224,5,15,0,0,224,225,5,20,0,0,225,
        226,5,30,0,0,226,227,5,20,0,0,227,228,5,16,0,0,228,229,5,20,0,0,
        229,231,3,10,5,0,230,232,5,20,0,0,231,230,1,0,0,0,231,232,1,0,0,
        0,232,233,1,0,0,0,233,235,5,19,0,0,234,236,5,20,0,0,235,234,1,0,
        0,0,235,236,1,0,0,0,236,238,1,0,0,0,237,239,3,22,11,0,238,237,1,
        0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,243,5,24,0,0,241,242,5,
        20,0,0,242,244,3,2,1,0,243,241,1,0,0,0,244,245,1,0,0,0,245,243,1,
        0,0,0,245,246,1,0,0,0,246,21,1,0,0,0,247,252,5,6,0,0,248,251,9,0,
        0,0,249,251,5,7,0,0,250,248,1,0,0,0,250,249,1,0,0,0,251,254,1,0,
        0,0,252,253,1,0,0,0,252,250,1,0,0,0,253,23,1,0,0,0,254,252,1,0,0,
        0,47,27,36,39,42,46,49,55,59,63,67,71,75,78,82,86,89,96,104,119,
        123,127,132,136,144,146,151,154,158,166,170,173,180,183,187,191,
        194,201,207,211,214,221,231,235,238,245,250,252
    ]

class GeniusGentlemenParsingParser ( Parser ):

    grammarFileName = "GeniusGentlemenParsing.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'not'", "'='", "'#'", 
                     "'?'", "'def'", "<INVALID>", "<INVALID>", "'if'", "'el'", 
                     "'else'", "'while'", "'for'", "'in'", "'True'", "'False'", 
                     "':'", "<INVALID>", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DEF", "FUNCCALL", "ANDOR", "IF", "EL", "ELSE", "WHILE", 
                      "FOR", "IN", "TRUE", "FALSE", "COLON", "WHITESPACE", 
                      "PASS", "CONDIT", "ARITHMETIC_OPERATOR", "NEWLINE", 
                      "INT", "LETTERS", "DIGITS", "SYMBOLS", "CHARS", "VAR" ]

    RULE_start = 0
    RULE_line = 1
    RULE_funcdec = 2
    RULE_statement = 3
    RULE_structure = 4
    RULE_expr = 5
    RULE_assign = 6
    RULE_ifstat = 7
    RULE_else = 8
    RULE_while = 9
    RULE_for = 10
    RULE_comment = 11

    ruleNames =  [ "start", "line", "funcdec", "statement", "structure", 
                   "expr", "assign", "ifstat", "else", "while", "for", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    DEF=8
    FUNCCALL=9
    ANDOR=10
    IF=11
    EL=12
    ELSE=13
    WHILE=14
    FOR=15
    IN=16
    TRUE=17
    FALSE=18
    COLON=19
    WHITESPACE=20
    PASS=21
    CONDIT=22
    ARITHMETIC_OPERATOR=23
    NEWLINE=24
    INT=25
    LETTERS=26
    DIGITS=27
    SYMBOLS=28
    CHARS=29
    VAR=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GeniusGentlemenParsingParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = GeniusGentlemenParsingParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1127664466) != 0:
                self.state = 24
                self.line()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(GeniusGentlemenParsingParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(GeniusGentlemenParsingParser.NEWLINE, 0)

        def expr(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.StatementContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def PASS(self):
            return self.getToken(GeniusGentlemenParsingParser.PASS, 0)

        def comment(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.CommentContext,0)


        def structure(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.StructureContext,0)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = GeniusGentlemenParsingParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.expr(0)

                elif la_ == 2:
                    self.state = 33
                    self.statement()

                elif la_ == 3:
                    self.state = 34
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)

                elif la_ == 4:
                    self.state = 35
                    self.match(GeniusGentlemenParsingParser.PASS)


                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 38
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)


                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 41
                    self.comment()


                self.state = 44
                self.match(GeniusGentlemenParsingParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.structure()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(GeniusGentlemenParsingParser.DEF, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.VAR)
            else:
                return self.getToken(GeniusGentlemenParsingParser.VAR, i)

        def COLON(self):
            return self.getToken(GeniusGentlemenParsingParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(GeniusGentlemenParsingParser.NEWLINE, 0)

        def comment(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.CommentContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_funcdec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdec" ):
                listener.enterFuncdec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdec" ):
                listener.exitFuncdec(self)




    def funcdec(self):

        localctx = GeniusGentlemenParsingParser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 48
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 51
            self.match(GeniusGentlemenParsingParser.DEF)
            self.state = 52
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 53
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 54
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 57
            self.match(GeniusGentlemenParsingParser.T__0)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 58
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 61
                self.match(GeniusGentlemenParsingParser.VAR)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 62
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)


                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 65
                    self.match(GeniusGentlemenParsingParser.T__1)
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 66
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)


                    self.state = 69
                    self.match(GeniusGentlemenParsingParser.VAR)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 70
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)


                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 80
            self.match(GeniusGentlemenParsingParser.T__2)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 81
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 84
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 85
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 88
                self.comment()


            self.state = 91
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 94 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 92
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 93
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 96 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.AssignContext,0)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GeniusGentlemenParsingParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstat(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.IfstatContext,0)


        def while_(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.WhileContext,0)


        def for_(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ForContext,0)


        def funcdec(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.FuncdecContext,0)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure" ):
                listener.enterStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure" ):
                listener.exitStructure(self)




    def structure(self):

        localctx = GeniusGentlemenParsingParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_structure)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.ifstat()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.while_()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.for_()
                pass
            elif token in [8, 20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.funcdec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GeniusGentlemenParsingParser.INT, 0)

        def VAR(self):
            return self.getToken(GeniusGentlemenParsingParser.VAR, 0)

        def TRUE(self):
            return self.getToken(GeniusGentlemenParsingParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GeniusGentlemenParsingParser.FALSE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def FUNCCALL(self):
            return self.getToken(GeniusGentlemenParsingParser.FUNCCALL, 0)

        def ARITHMETIC_OPERATOR(self):
            return self.getToken(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR, 0)

        def CONDIT(self):
            return self.getToken(GeniusGentlemenParsingParser.CONDIT, 0)

        def ANDOR(self):
            return self.getToken(GeniusGentlemenParsingParser.ANDOR, 0)

        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GeniusGentlemenParsingParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 107
                self.match(GeniusGentlemenParsingParser.INT)
                pass
            elif token in [30]:
                self.state = 108
                self.match(GeniusGentlemenParsingParser.VAR)
                pass
            elif token in [17]:
                self.state = 109
                self.match(GeniusGentlemenParsingParser.TRUE)
                pass
            elif token in [18]:
                self.state = 110
                self.match(GeniusGentlemenParsingParser.FALSE)
                pass
            elif token in [1]:
                self.state = 111
                self.match(GeniusGentlemenParsingParser.T__0)
                self.state = 112
                self.expr(0)
                self.state = 113
                self.match(GeniusGentlemenParsingParser.T__2)
                pass
            elif token in [4]:
                self.state = 115
                self.match(GeniusGentlemenParsingParser.T__3)
                self.state = 116
                self.match(GeniusGentlemenParsingParser.WHITESPACE)
                self.state = 117
                self.expr(2)
                pass
            elif token in [9]:
                self.state = 118
                self.match(GeniusGentlemenParsingParser.FUNCCALL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 144
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 121
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 123
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 122
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 125
                        self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)
                        self.state = 127
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 126
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 129
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 131
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 134
                        self.match(GeniusGentlemenParsingParser.CONDIT)
                        self.state = 136
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 135
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 138
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 139
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 140
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 141
                        self.match(GeniusGentlemenParsingParser.ANDOR)
                        self.state = 142
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 143
                        self.expr(4)
                        pass

             
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GeniusGentlemenParsingParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def ARITHMETIC_OPERATOR(self):
            return self.getToken(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR, 0)

        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = GeniusGentlemenParsingParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 150
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 153
                self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)


            self.state = 156
            self.match(GeniusGentlemenParsingParser.T__4)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 157
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 160
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GeniusGentlemenParsingParser.IF, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def expr(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,0)


        def COLON(self):
            return self.getToken(GeniusGentlemenParsingParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(GeniusGentlemenParsingParser.NEWLINE, 0)

        def comment(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.CommentContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


        def else_(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ElseContext,0)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_ifstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstat" ):
                listener.enterIfstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstat" ):
                listener.exitIfstat(self)




    def ifstat(self):

        localctx = GeniusGentlemenParsingParser.IfstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(GeniusGentlemenParsingParser.IF)
            self.state = 163
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 164
            self.expr(0)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 165
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 168
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 169
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 172
                self.comment()


            self.state = 175
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 178 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 176
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 177
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 180 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 182
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GeniusGentlemenParsingParser.ELSE, 0)

        def COLON(self):
            return self.getToken(GeniusGentlemenParsingParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(GeniusGentlemenParsingParser.NEWLINE, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def comment(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.CommentContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = GeniusGentlemenParsingParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(GeniusGentlemenParsingParser.ELSE)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 186
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 189
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 190
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 193
                self.comment()


            self.state = 196
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 199 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 197
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 198
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 201 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GeniusGentlemenParsingParser.WHILE, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def expr(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,0)


        def COLON(self):
            return self.getToken(GeniusGentlemenParsingParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(GeniusGentlemenParsingParser.NEWLINE, 0)

        def comment(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.CommentContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)




    def while_(self):

        localctx = GeniusGentlemenParsingParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(GeniusGentlemenParsingParser.WHILE)
            self.state = 204
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 205
            self.expr(0)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 206
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 209
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 210
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 213
                self.comment()


            self.state = 216
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 219 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 217
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 218
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 221 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GeniusGentlemenParsingParser.FOR, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def VAR(self):
            return self.getToken(GeniusGentlemenParsingParser.VAR, 0)

        def IN(self):
            return self.getToken(GeniusGentlemenParsingParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,0)


        def COLON(self):
            return self.getToken(GeniusGentlemenParsingParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(GeniusGentlemenParsingParser.NEWLINE, 0)

        def comment(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.CommentContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)




    def for_(self):

        localctx = GeniusGentlemenParsingParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(GeniusGentlemenParsingParser.FOR)
            self.state = 224
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 225
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 226
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 227
            self.match(GeniusGentlemenParsingParser.IN)
            self.state = 228
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 229
            self.expr(0)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 230
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 233
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 234
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 237
                self.comment()


            self.state = 240
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 243 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 241
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 242
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 245 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = GeniusGentlemenParsingParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(GeniusGentlemenParsingParser.T__5)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 250
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 248
                        self.matchWildcard()
                        pass

                    elif la_ == 2:
                        self.state = 249
                        self.match(GeniusGentlemenParsingParser.T__6)
                        pass

             
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




