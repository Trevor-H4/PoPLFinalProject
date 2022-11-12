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
        4,1,16,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,32,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,3,1,3,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,3,1,0,1,3,1,
        0,4,5,1,0,8,12,51,0,17,1,0,0,0,2,22,1,0,0,0,4,31,1,0,0,0,6,44,1,
        0,0,0,8,13,3,4,2,0,9,10,3,2,1,0,10,11,5,13,0,0,11,13,1,0,0,0,12,
        8,1,0,0,0,12,9,1,0,0,0,13,16,1,0,0,0,14,16,5,13,0,0,15,12,1,0,0,
        0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,
        1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,6,3,0,23,
        3,1,0,0,0,24,25,6,2,-1,0,25,32,5,14,0,0,26,32,5,16,0,0,27,28,5,6,
        0,0,28,29,3,4,2,0,29,30,5,7,0,0,30,32,1,0,0,0,31,24,1,0,0,0,31,26,
        1,0,0,0,31,27,1,0,0,0,32,41,1,0,0,0,33,34,10,5,0,0,34,35,7,0,0,0,
        35,40,3,4,2,6,36,37,10,4,0,0,37,38,7,1,0,0,38,40,3,4,2,5,39,33,1,
        0,0,0,39,36,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,
        5,1,0,0,0,43,41,1,0,0,0,44,45,5,16,0,0,45,46,7,2,0,0,46,47,3,4,2,
        0,47,7,1,0,0,0,6,12,15,17,31,39,41
    ]

class GeniusGentlemenParsingParser ( Parser ):

    grammarFileName = "GeniusGentlemenParsing.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'('", 
                     "')'", "'='", "'+='", "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NEWLINE", "INT", "CHARS", "VAR" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_assign = 3

    ruleNames =  [ "start", "statement", "expr", "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NEWLINE=13
    INT=14
    CHARS=15
    VAR=16

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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GeniusGentlemenParsingParser.NEWLINE)
            else:
                return self.getToken(GeniusGentlemenParsingParser.NEWLINE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.StatementContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.StatementContext,i)


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
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 90176) != 0:
                self.state = 15
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 14, 16]:
                    self.state = 12
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 8
                        self.expr(0)
                        pass

                    elif la_ == 2:
                        self.state = 9
                        self.statement()
                        self.state = 10
                        self.match(GeniusGentlemenParsingParser.NEWLINE)
                        pass


                    pass
                elif token in [13]:
                    self.state = 14
                    self.match(GeniusGentlemenParsingParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

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
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.assign()
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeniusGentlemenParsingParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeniusGentlemenParsingParser.ExprContext,i)


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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 25
                self.match(GeniusGentlemenParsingParser.INT)
                pass
            elif token in [16]:
                self.state = 26
                self.match(GeniusGentlemenParsingParser.VAR)
                pass
            elif token in [6]:
                self.state = 27
                self.match(GeniusGentlemenParsingParser.T__5)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(GeniusGentlemenParsingParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = GeniusGentlemenParsingParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 37
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expr(5)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(GeniusGentlemenParsingParser.VAR)
            self.state = 45
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 46
            self.expr(0)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




