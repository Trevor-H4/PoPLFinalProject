grammar GeniusGentlemenParsing ;

start: (expr NEWLINE)* ;

expr: expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | INT
    | var
    | '(' expr ')' ;

NEWLINE: [\n]+ ;

INT    : [0-9]+ ;

CHARS  : [a-z] | [A-Z] | [0-9] | '_' ;

var    : ([a-z] | [A-Z] | '_') CHARS* ;

ASSIGN : var ('=' | '+=' | '-=' | '*=' | '/=') expr;
