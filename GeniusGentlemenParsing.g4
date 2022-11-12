grammar GeniusGentlemenParsing ;

start: (expr NEWLINE)* ;

expr: expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | INT
    | var
    | '(' expr ')' ;

NEWLINE: [\n]+ ;

INT    : [0-9]+ ;

var    : ([a-z] | [A-Z]) [a-z][A-Z][0-9]'_''-'+ ;
