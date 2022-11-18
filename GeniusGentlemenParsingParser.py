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
        4,1,21,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,51,8,4,1,4,1,4,3,4,55,8,4,1,
        4,1,4,3,4,59,8,4,1,4,1,4,1,4,3,4,64,8,4,1,4,1,4,3,4,68,8,4,1,4,1,
        4,1,4,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,1,5,1,5,3,5,83,8,5,
        1,5,3,5,86,8,5,1,5,1,5,3,5,90,8,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,98,
        8,6,1,6,1,6,1,6,1,6,4,6,104,8,6,11,6,12,6,105,1,6,3,6,109,8,6,1,
        7,1,7,3,7,113,8,7,1,7,1,7,1,7,1,7,4,7,119,8,7,11,7,12,7,120,1,7,
        0,1,8,8,0,2,4,6,8,10,12,14,0,0,140,0,19,1,0,0,0,2,32,1,0,0,0,4,34,
        1,0,0,0,6,36,1,0,0,0,8,50,1,0,0,0,10,80,1,0,0,0,12,93,1,0,0,0,14,
        110,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,
        0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,
        1,0,0,0,24,29,3,8,4,0,25,29,3,4,2,0,26,29,5,12,0,0,27,29,5,13,0,
        0,28,24,1,0,0,0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,28,29,
        1,0,0,0,29,30,1,0,0,0,30,33,5,16,0,0,31,33,3,6,3,0,32,28,1,0,0,0,
        32,31,1,0,0,0,33,3,1,0,0,0,34,35,3,10,5,0,35,5,1,0,0,0,36,37,3,12,
        6,0,37,7,1,0,0,0,38,39,6,4,-1,0,39,51,5,17,0,0,40,51,5,21,0,0,41,
        51,5,9,0,0,42,51,5,10,0,0,43,44,5,1,0,0,44,45,3,8,4,0,45,46,5,2,
        0,0,46,51,1,0,0,0,47,48,5,3,0,0,48,49,5,12,0,0,49,51,3,8,4,1,50,
        38,1,0,0,0,50,40,1,0,0,0,50,41,1,0,0,0,50,42,1,0,0,0,50,43,1,0,0,
        0,50,47,1,0,0,0,51,77,1,0,0,0,52,54,10,9,0,0,53,55,5,12,0,0,54,53,
        1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,58,5,15,0,0,57,59,5,12,0,
        0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,76,3,8,4,10,61,63,
        10,3,0,0,62,64,5,12,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,
        0,65,67,5,14,0,0,66,68,5,12,0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,
        1,0,0,0,69,76,3,8,4,4,70,71,10,2,0,0,71,72,5,12,0,0,72,73,5,5,0,
        0,73,74,5,12,0,0,74,76,3,8,4,3,75,52,1,0,0,0,75,61,1,0,0,0,75,70,
        1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,9,1,0,0,0,79,
        77,1,0,0,0,80,82,5,21,0,0,81,83,5,12,0,0,82,81,1,0,0,0,82,83,1,0,
        0,0,83,85,1,0,0,0,84,86,5,15,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,
        87,1,0,0,0,87,89,5,4,0,0,88,90,5,12,0,0,89,88,1,0,0,0,89,90,1,0,
        0,0,90,91,1,0,0,0,91,92,3,8,4,0,92,11,1,0,0,0,93,94,5,6,0,0,94,95,
        5,12,0,0,95,97,3,8,4,0,96,98,5,12,0,0,97,96,1,0,0,0,97,98,1,0,0,
        0,98,99,1,0,0,0,99,100,5,11,0,0,100,103,5,16,0,0,101,102,5,12,0,
        0,102,104,3,2,1,0,103,101,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,
        0,105,106,1,0,0,0,106,108,1,0,0,0,107,109,3,14,7,0,108,107,1,0,0,
        0,108,109,1,0,0,0,109,13,1,0,0,0,110,112,5,8,0,0,111,113,5,12,0,
        0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,11,0,
        0,115,118,5,16,0,0,116,117,5,12,0,0,117,119,3,2,1,0,118,116,1,0,
        0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,15,1,0,0,
        0,18,19,28,32,50,54,58,63,67,75,77,82,85,89,97,105,108,112,120
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
    RULE_structure = 3
    RULE_expr = 4
    RULE_assign = 5
    RULE_ifstat = 6
    RULE_else = 7

    ruleNames =  [ "start", "line", "statement", "structure", "expr", "assign", 
                   "ifstat", "else" ]

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 2307658) != 0:
                self.state = 16
                self.line()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
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

        def PASS(self):
            return self.getToken(GeniusGentlemenParsingParser.PASS, 0)

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
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 9, 10, 12, 13, 16, 17, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 24
                    self.expr(0)

                elif la_ == 2:
                    self.state = 25
                    self.statement()

                elif la_ == 3:
                    self.state = 26
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)

                elif la_ == 4:
                    self.state = 27
                    self.match(GeniusGentlemenParsingParser.PASS)


                self.state = 30
                self.match(GeniusGentlemenParsingParser.NEWLINE)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
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
            self.state = 34
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
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.ifstat()
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 39
                self.match(GeniusGentlemenParsingParser.INT)
                pass
            elif token in [21]:
                self.state = 40
                self.match(GeniusGentlemenParsingParser.VAR)
                pass
            elif token in [9]:
                self.state = 41
                self.match(GeniusGentlemenParsingParser.TRUE)
                pass
            elif token in [10]:
                self.state = 42
                self.match(GeniusGentlemenParsingParser.FALSE)
                pass
            elif token in [1]:
                self.state = 43
                self.match(GeniusGentlemenParsingParser.T__0)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(GeniusGentlemenParsingParser.T__1)
                pass
            elif token in [3]:
                self.state = 47
                self.match(GeniusGentlemenParsingParser.T__2)
                self.state = 48
                self.match(GeniusGentlemenParsingParser.WHITESPACE)
                self.state = 49
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 54
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 53
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 56
                        self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)
                        self.state = 58
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 57
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 60
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 63
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 62
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 65
                        self.match(GeniusGentlemenParsingParser.CONDIT)
                        self.state = 67
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==12:
                            self.state = 66
                            self.match(GeniusGentlemenParsingParser.WHITESPACE)


                        self.state = 69
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 71
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 72
                        self.match(GeniusGentlemenParsingParser.ANDOR)
                        self.state = 73
                        self.match(GeniusGentlemenParsingParser.WHITESPACE)
                        self.state = 74
                        self.expr(3)
                        pass

             
                self.state = 79
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
        self.enterRule(localctx, 10, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 81
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 84
                self.match(GeniusGentlemenParsingParser.ARITHMETIC_OPERATOR)


            self.state = 87
            self.match(GeniusGentlemenParsingParser.T__3)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 88
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 91
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
            self.state = 93
            self.match(GeniusGentlemenParsingParser.IF)
            self.state = 94
            self.match(GeniusGentlemenParsingParser.WHITESPACE)
            self.state = 95
            self.expr(0)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 96
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 99
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 100
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 103 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 101
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 102
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 105 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 107
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
            self.state = 110
            self.match(GeniusGentlemenParsingParser.ELSE)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 111
                self.match(GeniusGentlemenParsingParser.WHITESPACE)


            self.state = 114
            self.match(GeniusGentlemenParsingParser.COLON)
            self.state = 115
            self.match(GeniusGentlemenParsingParser.NEWLINE)
            self.state = 118 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 116
                    self.match(GeniusGentlemenParsingParser.WHITESPACE)
                    self.state = 117
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 120 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
         




