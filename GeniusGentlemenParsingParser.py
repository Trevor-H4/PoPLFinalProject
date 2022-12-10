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
        4,1,30,264,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,41,8,
        1,1,1,3,1,44,8,1,1,1,3,1,47,8,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,3,1,
        3,1,3,1,3,3,3,59,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,75,8,4,1,4,1,4,3,4,79,8,4,1,4,1,4,3,4,83,8,4,1,4,
        1,4,1,4,3,4,88,8,4,1,4,1,4,3,4,92,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,100,8,4,10,4,12,4,103,9,4,1,5,1,5,3,5,107,8,5,1,5,3,5,110,8,5,
        1,5,1,5,3,5,114,8,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,122,8,6,1,6,1,6,
        3,6,126,8,6,1,6,3,6,129,8,6,1,6,1,6,1,6,4,6,134,8,6,11,6,12,6,135,
        1,6,3,6,139,8,6,1,7,1,7,3,7,143,8,7,1,7,1,7,3,7,147,8,7,1,7,3,7,
        150,8,7,1,7,1,7,1,7,4,7,155,8,7,11,7,12,7,156,1,8,1,8,1,8,1,8,3,
        8,163,8,8,1,8,1,8,3,8,167,8,8,1,8,3,8,170,8,8,1,8,1,8,1,8,4,8,175,
        8,8,11,8,12,8,176,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,187,8,9,1,
        9,1,9,3,9,191,8,9,1,9,3,9,194,8,9,1,9,1,9,1,9,4,9,199,8,9,11,9,12,
        9,200,1,10,1,10,1,10,5,10,206,8,10,10,10,12,10,209,9,10,1,11,3,11,
        212,8,11,1,11,1,11,1,11,1,11,3,11,218,8,11,1,11,1,11,3,11,222,8,
        11,1,11,3,11,225,8,11,1,11,1,11,1,11,4,11,230,8,11,11,11,12,11,231,
        1,12,1,12,3,12,236,8,12,1,12,1,12,1,12,1,12,1,13,3,13,243,8,13,1,
        13,1,13,3,13,247,8,13,1,13,1,13,3,13,251,8,13,1,13,5,13,254,8,13,
        10,13,12,13,257,9,13,3,13,259,8,13,1,13,3,13,262,8,13,1,13,1,207,
        1,8,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,308,0,31,1,0,0,0,
        2,50,1,0,0,0,4,52,1,0,0,0,6,58,1,0,0,0,8,74,1,0,0,0,10,104,1,0,0,
        0,12,117,1,0,0,0,14,140,1,0,0,0,16,158,1,0,0,0,18,178,1,0,0,0,20,
        202,1,0,0,0,22,211,1,0,0,0,24,233,1,0,0,0,26,242,1,0,0,0,28,30,3,
        2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        34,1,0,0,0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,41,3,8,4,
        0,37,41,3,4,2,0,38,41,5,20,0,0,39,41,5,21,0,0,40,36,1,0,0,0,40,37,
        1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,
        42,44,5,20,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,47,3,
        20,10,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,51,5,24,0,0,
        49,51,3,6,3,0,50,40,1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,53,3,10,
        5,0,53,5,1,0,0,0,54,59,3,12,6,0,55,59,3,16,8,0,56,59,3,18,9,0,57,
        59,3,22,11,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,
        0,0,59,7,1,0,0,0,60,61,6,4,-1,0,61,75,5,25,0,0,62,75,5,30,0,0,63,
        75,5,17,0,0,64,75,5,18,0,0,65,66,5,1,0,0,66,67,3,8,4,0,67,68,5,2,
        0,0,68,75,1,0,0,0,69,70,5,3,0,0,70,71,5,20,0,0,71,75,3,8,4,3,72,
        75,5,9,0,0,73,75,3,24,12,0,74,60,1,0,0,0,74,62,1,0,0,0,74,63,1,0,
        0,0,74,64,1,0,0,0,74,65,1,0,0,0,74,69,1,0,0,0,74,72,1,0,0,0,74,73,
        1,0,0,0,75,101,1,0,0,0,76,78,10,11,0,0,77,79,5,20,0,0,78,77,1,0,
        0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,82,5,23,0,0,81,83,5,20,0,0,82,
        81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,100,3,8,4,12,85,87,10,
        5,0,0,86,88,5,20,0,0,87,86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,
        91,5,22,0,0,90,92,5,20,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,93,1,0,
        0,0,93,100,3,8,4,6,94,95,10,4,0,0,95,96,5,20,0,0,96,97,5,10,0,0,
        97,98,5,20,0,0,98,100,3,8,4,5,99,76,1,0,0,0,99,85,1,0,0,0,99,94,
        1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,9,1,0,
        0,0,103,101,1,0,0,0,104,106,5,30,0,0,105,107,5,20,0,0,106,105,1,
        0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,110,5,23,0,0,109,108,1,
        0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,113,5,4,0,0,112,114,5,
        20,0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,3,
        8,4,0,116,11,1,0,0,0,117,118,5,11,0,0,118,119,5,20,0,0,119,121,3,
        8,4,0,120,122,5,20,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,1,
        0,0,0,123,125,5,19,0,0,124,126,5,20,0,0,125,124,1,0,0,0,125,126,
        1,0,0,0,126,128,1,0,0,0,127,129,3,20,10,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,130,1,0,0,0,130,133,5,24,0,0,131,132,5,20,0,0,132,134,
        3,2,1,0,133,131,1,0,0,0,134,135,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,138,1,0,0,0,137,139,3,14,7,0,138,137,1,0,0,0,138,139,
        1,0,0,0,139,13,1,0,0,0,140,142,5,13,0,0,141,143,5,20,0,0,142,141,
        1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,146,5,19,0,0,145,147,
        5,20,0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,150,
        3,20,10,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,154,
        5,24,0,0,152,153,5,20,0,0,153,155,3,2,1,0,154,152,1,0,0,0,155,156,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,15,1,0,0,0,158,159,5,
        14,0,0,159,160,5,20,0,0,160,162,3,8,4,0,161,163,5,20,0,0,162,161,
        1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,166,5,19,0,0,165,167,
        5,20,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,170,
        3,20,10,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,174,
        5,24,0,0,172,173,5,20,0,0,173,175,3,2,1,0,174,172,1,0,0,0,175,176,
        1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,17,1,0,0,0,178,179,5,
        15,0,0,179,180,5,20,0,0,180,181,5,30,0,0,181,182,5,20,0,0,182,183,
        5,16,0,0,183,184,5,20,0,0,184,186,3,8,4,0,185,187,5,20,0,0,186,185,
        1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,190,5,19,0,0,189,191,
        5,20,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,194,
        3,20,10,0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,198,
        5,24,0,0,196,197,5,20,0,0,197,199,3,2,1,0,198,196,1,0,0,0,199,200,
        1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,19,1,0,0,0,202,207,5,
        5,0,0,203,206,9,0,0,0,204,206,5,6,0,0,205,203,1,0,0,0,205,204,1,
        0,0,0,206,209,1,0,0,0,207,208,1,0,0,0,207,205,1,0,0,0,208,21,1,0,
        0,0,209,207,1,0,0,0,210,212,5,20,0,0,211,210,1,0,0,0,211,212,1,0,
        0,0,212,213,1,0,0,0,213,214,5,8,0,0,214,215,5,20,0,0,215,217,5,9,
        0,0,216,218,5,20,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,1,0,
        0,0,219,221,5,19,0,0,220,222,5,20,0,0,221,220,1,0,0,0,221,222,1,
        0,0,0,222,224,1,0,0,0,223,225,3,20,10,0,224,223,1,0,0,0,224,225,
        1,0,0,0,225,226,1,0,0,0,226,229,5,24,0,0,227,228,5,20,0,0,228,230,
        3,2,1,0,229,227,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,
        1,0,0,0,232,23,1,0,0,0,233,235,5,30,0,0,234,236,5,20,0,0,235,234,
        1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,238,5,1,0,0,238,239,
        3,26,13,0,239,240,5,2,0,0,240,25,1,0,0,0,241,243,5,20,0,0,242,241,
        1,0,0,0,242,243,1,0,0,0,243,258,1,0,0,0,244,255,3,8,4,0,245,247,
        5,20,0,0,246,245,1,0,0,0,246,247,1,0,0,0,247,248,1,0,0,0,248,250,
        5,7,0,0,249,251,5,20,0,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,
        1,0,0,0,252,254,3,8,4,0,253,246,1,0,0,0,254,257,1,0,0,0,255,253,
        1,0,0,0,255,256,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,258,244,
        1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,262,5,20,0,0,261,260,
        1,0,0,0,261,262,1,0,0,0,262,27,1,0,0,0,47,31,40,43,46,50,58,74,78,
        82,87,91,99,101,106,109,113,121,125,128,135,138,142,146,149,156,
        162,166,169,176,186,190,193,200,205,207,211,217,221,224,231,235,
        242,246,250,255,258,261
    ]

class GeniusGentlemenParsingParser ( Parser ):

    grammarFileName = "GeniusGentlemenParsing.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'not'", "'='", "'#'", "'?'", 
                     "','", "'def'", "<INVALID>", "<INVALID>", "'if'", "'el'", 
                     "'else'", "'while'", "'for'", "'in'", "'True'", "'False'", 
                     "':'", "<INVALID>", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DEF", "FUNCDEF", "ANDOR", "IF", "EL", "ELSE", "WHILE", 
                      "FOR", "IN", "TRUE", "FALSE", "COLON", "WHITESPACE", 
                      "PASS", "CONDIT", "ARITHMETIC_OPERATOR", "NEWLINE", 
                      "INT", "LETTERS", "DIGITS", "SYMBOLS", "CHARS", "VAR" ]

    RULE_start = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_structure = 3
    RULE_expr = 4
    RULE_assign = 5
    RULE_ifstat = 6
    RULE_else = 7
    RULE_while = 8
    RULE_for = 9
    RULE_comment = 10
    RULE_funcdec = 11
    RULE_funccall = 12
    RULE_params = 13

    ruleNames =  [ "start", "line", "statement", "structure", "expr", "assign", 
                   "ifstat", "else", "while", "for", "comment", "funcdec", 
                   "funccall", "params" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    DEF=8
    FUNCDEF=9
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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1127664426) != 0:
                self.state = 28
                self.line()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
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
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.expr(0)

                elif la_ == 2:
                    self.state = 37
                    self.statement()

                elif la_ == 3:
                    self.state = 38
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)

                elif la_ == 4:
                    self.state = 39
                    self.match(GeniusGentlemenParsingParser.PASS)


                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 42
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)


                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 45
                    self.comment()


                self.state = 48
                self.match(GeniusGentlemenParsingParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.structure()
                pass


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
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
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
        self.enterRule(localctx, 6, self.RULE_structure)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.ifstat()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.while_()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.for_()
                pass
            elif token in [8, 20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
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

        def FUNCDEF(self):
            return self.getToken(GeniusGentlemenParsingParser.FUNCDEF, 0)

        def funccall(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.FunccallContext,0)


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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 61
                self.match(GeniusGentlemenParsingParser.INT)
                pass

            elif la_ == 2:
                self.state = 62
                self.match(GeniusGentlemenParsingParser.VAR)
                pass

            elif la_ == 3:
                self.state = 63
                self.match(GeniusGentlemenParsingParser.TRUE)
                pass

            elif la_ == 4:
                self.state = 64
                self.match(GeniusGentlemenParsingParser.FALSE)
                pass

            elif la_ == 5:
                self.state = 65
                self.match(GeniusGentlemenParsingParser.T__0)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(GeniusGentlemenParsingParser.T__1)
                pass

            elif la_ == 6:
                self.state = 69
                self.match(GeniusGentlemenParsingParser.T__2)
                self.state = 70
                self.match(GeniusGentlemenParsingParser.WHITESPACE)
                self.state = 71
                self.expr(3)
                pass

            elif la_ == 7:
                self.state = 72
                self.match(GeniusGentlemenParsingParser.FUNCDEF)
                pass

            elif la_ == 8:
                self.state = 73
                self.funccall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 78
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 77
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 80
                        self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)
                        self.state = 82
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 81
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 84
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 87
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 86
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 89
                        self.match(GeniusGentlemenParsingParser.CONDIT)
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 90
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 93
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 96
                        self.match(GeniusGentlemenParsingParser.ANDOR)
                        self.state = 97
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 98
                        self.expr(5)
                        pass

             
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 105
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 108
                self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)


            self.state = 111
            self.match(GeniusGentlemenParsingParser.T__3)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 112
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 115
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
        self.enterRule(localctx, 12, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(GeniusGentlemenParsingParser.IF)
            self.state = 118
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 119
            self.expr(0)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 120
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 123
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 124
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 127
                self.comment()


            self.state = 130
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 133 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 131
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 132
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 135 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 137
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
        self.enterRule(localctx, 14, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(GeniusGentlemenParsingParser.ELSE)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 141
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 144
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 145
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 148
                self.comment()


            self.state = 151
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 154 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 152
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 153
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 156 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(GeniusGentlemenParsingParser.WHILE)
            self.state = 159
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 160
            self.expr(0)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 161
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 164
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 165
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 168
                self.comment()


            self.state = 171
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 174 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 172
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 173
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 176 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(GeniusGentlemenParsingParser.FOR)
            self.state = 179
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 180
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 181
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 182
            self.match(GeniusGentlemenParsingParser.IN)
            self.state = 183
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 184
            self.expr(0)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 185
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 188
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 189
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 192
                self.comment()


            self.state = 195
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 198 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 196
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 197
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 200 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(GeniusGentlemenParsingParser.T__4)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 205
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        self.state = 203
                        self.matchWildcard()
                        pass

                    elif la_ == 2:
                        self.state = 204
                        self.match(GeniusGentlemenParsingParser.T__5)
                        pass

             
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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

        def FUNCDEF(self):
            return self.getToken(GeniusGentlemenParsingParser.FUNCDEF, 0)

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
        self.enterRule(localctx, 22, self.RULE_funcdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 210
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 213
            self.match(GeniusGentlemenParsingParser.DEF)
            self.state = 214
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 215
            self.match(GeniusGentlemenParsingParser.FUNCDEF)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 216
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 219
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 220
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 223
                self.comment()


            self.state = 226
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 229 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 227
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 228
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 231 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GeniusGentlemenParsingParser.VAR, 0)

        def params(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ParamsContext,0)


        def WHITESPACE(self):
            return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_funccall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunccall" ):
                listener.enterFunccall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunccall" ):
                listener.exitFunccall(self)




    def funccall(self):

        localctx = GeniusGentlemenParsingParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 234
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 237
            self.match(GeniusGentlemenParsingParser.T__0)
            self.state = 238
            self.params()
            self.state = 239
            self.match(GeniusGentlemenParsingParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.WHITESPACE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,i)


        def getRuleIndex(self):
            return GeniusGentlemenParsingParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = GeniusGentlemenParsingParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1107689994) != 0:
                self.state = 244
                self.expr(0)
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 246
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 245
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 248
                        self.match(GeniusGentlemenParsingParser.T__6)
                        self.state = 250
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 249
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 252
                        self.expr(0) 
                    self.state = 257
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)



            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 260
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




