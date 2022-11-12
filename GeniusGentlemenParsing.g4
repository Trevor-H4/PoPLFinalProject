grammar GeniusGentlemenParsing ;

start: (expr NEWLINE)* ;

expr: expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | INT
    | VAR
    | assign
    | '(' expr ')' ;

NEWLINE: ([\n] | [\r\n]) ;

INT    : [0-9]+ ;

CHARS  : [a-z] | [A-Z] | [0-9] | '_' ;

VAR    : [a-z] | [A-Z] | '_' CHARS* ;

assign : VAR ('=' | '+=' | '-=' | '*=' | '/=') expr;

