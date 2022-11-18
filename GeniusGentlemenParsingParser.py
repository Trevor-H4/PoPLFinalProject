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
        4,1,21,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,3,1,26,8,1,
        1,1,1,1,1,2,1,2,3,2,32,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,46,8,3,1,3,1,3,3,3,50,8,3,1,3,1,3,3,3,54,8,3,1,3,1,
        3,1,3,3,3,59,8,3,1,3,1,3,3,3,63,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        71,8,3,10,3,12,3,74,9,3,1,4,1,4,3,4,78,8,4,1,4,3,4,81,8,4,1,4,1,
        4,3,4,85,8,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,93,8,5,1,5,1,5,1,5,1,5,
        4,5,99,8,5,11,5,12,5,100,1,5,3,5,104,8,5,1,5,1,5,3,5,108,8,5,1,6,
        1,6,3,6,112,8,6,1,6,1,6,1,6,1,6,4,6,118,8,6,11,6,12,6,119,1,6,3,
        6,123,8,6,1,6,0,1,6,7,0,2,4,6,8,10,12,0,0,145,0,17,1,0,0,0,2,25,
        1,0,0,0,4,31,1,0,0,0,6,45,1,0,0,0,8,75,1,0,0,0,10,88,1,0,0,0,12,
        109,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,
        0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,
        1,0,0,0,22,26,3,6,3,0,23,26,3,4,2,0,24,26,5,12,0,0,25,22,1,0,0,0,
        25,23,1,0,0,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,
        16,0,0,28,3,1,0,0,0,29,32,3,8,4,0,30,32,3,10,5,0,31,29,1,0,0,0,31,
        30,1,0,0,0,32,5,1,0,0,0,33,34,6,3,-1,0,34,46,5,17,0,0,35,46,5,21,
        0,0,36,46,5,9,0,0,37,46,5,10,0,0,38,39,5,1,0,0,39,40,3,6,3,0,40,
        41,5,2,0,0,41,46,1,0,0,0,42,43,5,3,0,0,43,44,5,12,0,0,44,46,3,6,
        3,1,45,33,1,0,0,0,45,35,1,0,0,0,45,36,1,0,0,0,45,37,1,0,0,0,45,38,
        1,0,0,0,45,42,1,0,0,0,46,72,1,0,0,0,47,49,10,9,0,0,48,50,5,12,0,
        0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,53,5,15,0,0,52,54,
        5,12,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,71,3,6,3,10,
        56,58,10,3,0,0,57,59,5,12,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,
        1,0,0,0,60,62,5,14,0,0,61,63,5,12,0,0,62,61,1,0,0,0,62,63,1,0,0,
        0,63,64,1,0,0,0,64,71,3,6,3,4,65,66,10,2,0,0,66,67,5,12,0,0,67,68,
        5,5,0,0,68,69,5,12,0,0,69,71,3,6,3,3,70,47,1,0,0,0,70,56,1,0,0,0,
        70,65,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,7,1,0,
        0,0,74,72,1,0,0,0,75,77,5,21,0,0,76,78,5,12,0,0,77,76,1,0,0,0,77,
        78,1,0,0,0,78,80,1,0,0,0,79,81,5,15,0,0,80,79,1,0,0,0,80,81,1,0,
        0,0,81,82,1,0,0,0,82,84,5,4,0,0,83,85,5,12,0,0,84,83,1,0,0,0,84,
        85,1,0,0,0,85,86,1,0,0,0,86,87,3,6,3,0,87,9,1,0,0,0,88,89,5,6,0,
        0,89,90,5,12,0,0,90,92,3,6,3,0,91,93,5,12,0,0,92,91,1,0,0,0,92,93,
        1,0,0,0,93,94,1,0,0,0,94,95,5,11,0,0,95,96,5,16,0,0,96,103,5,12,
        0,0,97,99,3,2,1,0,98,97,1,0,0,0,99,100,1,0,0,0,100,98,1,0,0,0,100,
        101,1,0,0,0,101,104,1,0,0,0,102,104,5,13,0,0,103,98,1,0,0,0,103,
        102,1,0,0,0,104,107,1,0,0,0,105,108,3,10,5,0,106,108,3,12,6,0,107,
        105,1,0,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,11,1,0,0,0,109,111,
        5,8,0,0,110,112,5,12,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,
        1,0,0,0,113,114,5,11,0,0,114,115,5,16,0,0,115,122,5,12,0,0,116,118,
        3,2,1,0,117,116,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,123,1,0,0,0,121,123,5,13,0,0,122,117,1,0,0,0,122,121,
        1,0,0,0,123,13,1,0,0,0,20,17,25,31,45,49,53,58,62,70,72,77,80,84,
        92,100,103,107,111,119,122
    ]

class GeniusGentlemenParsingParser ( Parser ):

    grammarFileName = "GeniusGentlemenParsing.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'not'", "'='", "<INVALID>", 
                     "'if'", "'el'", "'else'", "'True'", "'False'", "':'", 
                     "<INVALID>", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ANDOR", "IF", "EL", "ELSE", "TRUE", 
                      "FALSE", "COLON", "WHITESPACE", "PASS", "CONDIT", 
                      "ARITHMETIC_OPERATOR", "NEWLINE", "INT", "LETTERS", 
                      "DIGITS", "CHARS", "VAR" ]

    RULE_start = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_expr = 3
    RULE_assign = 4
    RULE_ifstat = 5
    RULE_else = 6

    ruleNames =  [ "start", "line", "statement", "expr", "assign", "ifstat", 
                   "else" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ANDOR=5
    IF=6
    EL=7
    ELSE=8
    TRUE=9
    FALSE=10
    COLON=11
    WHITESPACE=12
    PASS=13
    CONDIT=14
    ARITHMETIC_OPERATOR=15
    NEWLINE=16
    INT=17
    LETTERS=18
    DIGITS=19
    CHARS=20
    VAR=21

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 2299466) != 0:
                self.state = 14
                self.line()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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


        def WHITESPACE(self):
            return self.getToken(GeniusGentlemenParsingParser.WHITESPACE, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 22
                self.expr(0)

            elif la_ == 2:
                self.state = 23
                self.statement()

            elif la_ == 3:
                self.state = 24
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 27
            self.match(GeniusGentlemenParsingParser.NEWLINE)
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


        def ifstat(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.IfstatContext,0)


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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 29
                self.assign()
                pass
            elif token in [6]:
                self.state = 30
                self.ifstat()
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 34
                self.match(GeniusGentlemenParsingParser.INT)
                pass
            elif token in [21]:
                self.state = 35
                self.match(GeniusGentlemenParsingParser.VAR)
                pass
            elif token in [9]:
                self.state = 36
                self.match(GeniusGentlemenParsingParser.TRUE)
                pass
            elif token in [10]:
                self.state = 37
                self.match(GeniusGentlemenParsingParser.FALSE)
                pass
            elif token in [1]:
                self.state = 38
                self.match(GeniusGentlemenParsingParser.T__0)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(GeniusGentlemenParsingParser.T__1)
                pass
            elif token in [3]:
                self.state = 42
                self.match(GeniusGentlemenParsingParser.T__2)
                self.state = 43
                self.match(GeniusGentlemenParsingParser.WHITESPACE)
                self.state = 44
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 48
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 51
                        self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)
                        self.state = 53
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 52
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 55
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 58
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 57
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 60
                        self.match(GeniusGentlemenParsingParser.CONDIT)
                        self.state = 62
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 61
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 64
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 66
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 67
                        self.match(GeniusGentlemenParsingParser.ANDOR)
                        self.state = 68
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 69
                        self.expr(3)
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 76
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 79
                self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)


            self.state = 82
            self.match(GeniusGentlemenParsingParser.T__3)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 83
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 86
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

        def PASS(self):
            return self.getToken(GeniusGentlemenParsingParser.PASS, 0)

        def ifstat(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.IfstatContext,0)


        def else_(self):
            return self.getTypedRuleContext(GeniusGentlemenParsingParser.ElseContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.LineContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.LineContext,i)


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
        self.enterRule(localctx, 10, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(GeniusGentlemenParsingParser.IF)
            self.state = 89
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 90
            self.expr(0)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 91
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 94
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 95
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 96
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 6, 9, 10, 12, 16, 17, 21]:
                self.state = 98 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 97
                        self.line()

                    else:
                        raise NoViableAltException(self)
                    self.state = 100 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass
            elif token in [13]:
                self.state = 102
                self.match(GeniusGentlemenParsingParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 105
                self.ifstat()
                pass
            elif token in [8]:
                self.state = 106
                self.else_()
                pass
            elif token in [16]:
                pass
            else:
                pass
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

        def PASS(self):
            return self.getToken(GeniusGentlemenParsingParser.PASS, 0)

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
        self.enterRule(localctx, 12, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(GeniusGentlemenParsingParser.ELSE)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 110
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 113
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 114
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 115
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 6, 9, 10, 12, 16, 17, 21]:
                self.state = 117 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 116
                        self.line()

                    else:
                        raise NoViableAltException(self)
                    self.state = 119 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass
            elif token in [13]:
                self.state = 121
                self.match(GeniusGentlemenParsingParser.PASS)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
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
         




