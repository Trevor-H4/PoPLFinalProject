# Generated from .\GeniusGentlemenParsing.g4 by ANTLR 4.11.1
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
        4,1,27,202,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,35,8,1,1,1,3,1,38,8,1,1,1,3,1,41,
        8,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,3,1,3,1,3,3,3,52,8,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,66,8,4,1,4,1,4,3,4,70,
        8,4,1,4,1,4,3,4,74,8,4,1,4,1,4,1,4,3,4,79,8,4,1,4,1,4,3,4,83,8,4,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,1,5,1,5,3,5,
        98,8,5,1,5,3,5,101,8,5,1,5,1,5,3,5,105,8,5,1,5,1,5,1,6,1,6,1,6,1,
        6,3,6,113,8,6,1,6,1,6,3,6,117,8,6,1,6,3,6,120,8,6,1,6,1,6,1,6,4,
        6,125,8,6,11,6,12,6,126,1,6,3,6,130,8,6,1,7,1,7,3,7,134,8,7,1,7,
        1,7,3,7,138,8,7,1,7,3,7,141,8,7,1,7,1,7,1,7,4,7,146,8,7,11,7,12,
        7,147,1,8,1,8,1,8,1,8,3,8,154,8,8,1,8,1,8,3,8,158,8,8,1,8,3,8,161,
        8,8,1,8,1,8,1,8,4,8,166,8,8,11,8,12,8,167,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,178,8,9,1,9,1,9,3,9,182,8,9,1,9,3,9,185,8,9,1,9,1,
        9,1,9,4,9,190,8,9,11,9,12,9,191,1,10,1,10,1,10,5,10,197,8,10,10,
        10,12,10,200,9,10,1,10,1,198,1,8,11,0,2,4,6,8,10,12,14,16,18,20,
        0,0,234,0,25,1,0,0,0,2,44,1,0,0,0,4,46,1,0,0,0,6,51,1,0,0,0,8,65,
        1,0,0,0,10,95,1,0,0,0,12,108,1,0,0,0,14,131,1,0,0,0,16,149,1,0,0,
        0,18,169,1,0,0,0,20,193,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,
        28,29,5,0,0,1,29,1,1,0,0,0,30,35,3,8,4,0,31,35,3,4,2,0,32,35,5,17,
        0,0,33,35,5,18,0,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,
        33,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,38,5,17,0,0,37,36,1,0,
        0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,41,3,20,10,0,40,39,1,0,0,0,40,
        41,1,0,0,0,41,42,1,0,0,0,42,45,5,21,0,0,43,45,3,6,3,0,44,34,1,0,
        0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,47,3,10,5,0,47,5,1,0,0,0,48,52,
        3,12,6,0,49,52,3,16,8,0,50,52,3,18,9,0,51,48,1,0,0,0,51,49,1,0,0,
        0,51,50,1,0,0,0,52,7,1,0,0,0,53,54,6,4,-1,0,54,66,5,22,0,0,55,66,
        5,27,0,0,56,66,5,14,0,0,57,66,5,15,0,0,58,59,5,1,0,0,59,60,3,8,4,
        0,60,61,5,2,0,0,61,66,1,0,0,0,62,63,5,3,0,0,63,64,5,17,0,0,64,66,
        3,8,4,1,65,53,1,0,0,0,65,55,1,0,0,0,65,56,1,0,0,0,65,57,1,0,0,0,
        65,58,1,0,0,0,65,62,1,0,0,0,66,92,1,0,0,0,67,69,10,9,0,0,68,70,5,
        17,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,73,5,20,0,0,
        72,74,5,17,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,91,3,
        8,4,10,76,78,10,3,0,0,77,79,5,17,0,0,78,77,1,0,0,0,78,79,1,0,0,0,
        79,80,1,0,0,0,80,82,5,19,0,0,81,83,5,17,0,0,82,81,1,0,0,0,82,83,
        1,0,0,0,83,84,1,0,0,0,84,91,3,8,4,4,85,86,10,2,0,0,86,87,5,17,0,
        0,87,88,5,7,0,0,88,89,5,17,0,0,89,91,3,8,4,3,90,67,1,0,0,0,90,76,
        1,0,0,0,90,85,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,
        93,9,1,0,0,0,94,92,1,0,0,0,95,97,5,27,0,0,96,98,5,17,0,0,97,96,1,
        0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,101,5,20,0,0,100,99,1,0,0,
        0,100,101,1,0,0,0,101,102,1,0,0,0,102,104,5,4,0,0,103,105,5,17,0,
        0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,3,8,4,
        0,107,11,1,0,0,0,108,109,5,8,0,0,109,110,5,17,0,0,110,112,3,8,4,
        0,111,113,5,17,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,
        0,114,116,5,16,0,0,115,117,5,17,0,0,116,115,1,0,0,0,116,117,1,0,
        0,0,117,119,1,0,0,0,118,120,3,20,10,0,119,118,1,0,0,0,119,120,1,
        0,0,0,120,121,1,0,0,0,121,124,5,21,0,0,122,123,5,17,0,0,123,125,
        3,2,1,0,124,122,1,0,0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,
        1,0,0,0,127,129,1,0,0,0,128,130,3,14,7,0,129,128,1,0,0,0,129,130,
        1,0,0,0,130,13,1,0,0,0,131,133,5,10,0,0,132,134,5,17,0,0,133,132,
        1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,137,5,16,0,0,136,138,
        5,17,0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,141,
        3,20,10,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,145,
        5,21,0,0,143,144,5,17,0,0,144,146,3,2,1,0,145,143,1,0,0,0,146,147,
        1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,15,1,0,0,0,149,150,5,
        11,0,0,150,151,5,17,0,0,151,153,3,8,4,0,152,154,5,17,0,0,153,152,
        1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,157,5,16,0,0,156,158,
        5,17,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,161,
        3,20,10,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,165,
        5,21,0,0,163,164,5,17,0,0,164,166,3,2,1,0,165,163,1,0,0,0,166,167,
        1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,17,1,0,0,0,169,170,5,
        12,0,0,170,171,5,17,0,0,171,172,5,27,0,0,172,173,5,17,0,0,173,174,
        5,13,0,0,174,175,5,17,0,0,175,177,3,8,4,0,176,178,5,17,0,0,177,176,
        1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,181,5,16,0,0,180,182,
        5,17,0,0,181,180,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,185,
        3,20,10,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,189,
        5,21,0,0,187,188,5,17,0,0,188,190,3,2,1,0,189,187,1,0,0,0,190,191,
        1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,19,1,0,0,0,193,198,5,
        5,0,0,194,197,9,0,0,0,195,197,5,6,0,0,196,194,1,0,0,0,196,195,1,
        0,0,0,197,200,1,0,0,0,198,199,1,0,0,0,198,196,1,0,0,0,199,21,1,0,
        0,0,200,198,1,0,0,0,35,25,34,37,40,44,51,65,69,73,78,82,90,92,97,
        100,104,112,116,119,126,129,133,137,140,147,153,157,160,167,177,
        181,184,191,196,198
    ]

class GeniusGentlemenParsingParser ( Parser ):

    grammarFileName = "GeniusGentlemenParsing.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'not'", "'='", "'#'", "'?'", 
                     "<INVALID>", "'if'", "'el'", "'else'", "'while'", "'for'", 
                     "'in'", "'True'", "'False'", "':'", "<INVALID>", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ANDOR", "IF", 
                      "EL", "ELSE", "WHILE", "FOR", "IN", "TRUE", "FALSE", 
                      "COLON", "WHITESPACE", "PASS", "CONDIT", "ARITHMETIC_OPERATOR", 
                      "NEWLINE", "INT", "LETTERS", "DIGITS", "SYMBOLS", 
                      "CHARS", "VAR" ]

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

    ruleNames =  [ "start", "line", "statement", "structure", "expr", "assign", 
                   "ifstat", "else", "while", "for", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ANDOR=7
    IF=8
    EL=9
    ELSE=10
    WHILE=11
    FOR=12
    IN=13
    TRUE=14
    FALSE=15
    COLON=16
    WHITESPACE=17
    PASS=18
    CONDIT=19
    ARITHMETIC_OPERATOR=20
    NEWLINE=21
    INT=22
    LETTERS=23
    DIGITS=24
    SYMBOLS=25
    CHARS=26
    VAR=27

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 140957994) != 0:
                self.state = 22
                self.line()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 14, 15, 17, 18, 21, 22, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.expr(0)

                elif la_ == 2:
                    self.state = 31
                    self.statement()

                elif la_ == 3:
                    self.state = 32
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)

                elif la_ == 4:
                    self.state = 33
                    self.match(GeniusGentlemenParsingParser.PASS)


                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 36
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)


                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 39
                    self.comment()


                self.state = 42
                self.match(GeniusGentlemenParsingParser.NEWLINE)
                pass
            elif token in [8, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.structure()
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
            self.state = 46
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.ifstat()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.while_()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.for_()
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
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 54
                self.match(GeniusGentlemenParsingParser.INT)
                pass
            elif token in [27]:
                self.state = 55
                self.match(GeniusGentlemenParsingParser.VAR)
                pass
            elif token in [14]:
                self.state = 56
                self.match(GeniusGentlemenParsingParser.TRUE)
                pass
            elif token in [15]:
                self.state = 57
                self.match(GeniusGentlemenParsingParser.FALSE)
                pass
            elif token in [1]:
                self.state = 58
                self.match(GeniusGentlemenParsingParser.T__0)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(GeniusGentlemenParsingParser.T__1)
                pass
            elif token in [3]:
                self.state = 62
                self.match(GeniusGentlemenParsingParser.T__2)
                self.state = 63
                self.match(GeniusGentlemenParsingParser.WHITESPACE)
                self.state = 64
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 69
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==17:
                            self.state = 68
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 71
                        self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)
                        self.state = 73
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==17:
                            self.state = 72
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 75
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 78
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==17:
                            self.state = 77
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 80
                        self.match(GeniusGentlemenParsingParser.CONDIT)
                        self.state = 82
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==17:
                            self.state = 81
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 84
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 86
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 87
                        self.match(GeniusGentlemenParsingParser.ANDOR)
                        self.state = 88
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 89
                        self.expr(3)
                        pass

             
                self.state = 94
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
            self.state = 95
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 96
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 99
                self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)


            self.state = 102
            self.match(GeniusGentlemenParsingParser.T__3)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 103
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 106
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
            self.state = 108
            self.match(GeniusGentlemenParsingParser.IF)
            self.state = 109
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 110
            self.expr(0)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 111
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 114
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 115
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 118
                self.comment()


            self.state = 121
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 124 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 122
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 123
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 126 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 128
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
            self.state = 131
            self.match(GeniusGentlemenParsingParser.ELSE)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 132
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 135
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 136
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 139
                self.comment()


            self.state = 142
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 145 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 143
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 144
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 147 
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
            self.state = 149
            self.match(GeniusGentlemenParsingParser.WHILE)
            self.state = 150
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 151
            self.expr(0)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 152
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 155
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 156
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 159
                self.comment()


            self.state = 162
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 165 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 163
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 164
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 167 
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
            self.state = 169
            self.match(GeniusGentlemenParsingParser.FOR)
            self.state = 170
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 171
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 172
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 173
            self.match(GeniusGentlemenParsingParser.IN)
            self.state = 174
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 175
            self.expr(0)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 176
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 179
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 180
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 183
                self.comment()


            self.state = 186
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 189 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 187
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 188
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 191 
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
            self.state = 193
            self.match(GeniusGentlemenParsingParser.T__4)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 196
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        self.state = 194
                        self.matchWildcard()
                        pass

                    elif la_ == 2:
                        self.state = 195
                        self.match(GeniusGentlemenParsingParser.T__5)
                        pass

             
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




