grammar GeniusGentlemenParsing ;

start: ((expr | statement NEWLINE) | NEWLINE)* EOF;

statement : assign ;

expr: expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | INT
    | VAR
    | '(' expr ')' ;

NEWLINE: ([\n] | ([\r][\n])) ;

INT    : [0-9]+ ;

CHARS  : [a-z] | [A-Z] | [0-9] | '_' ;

VAR    : CHARS+ ;

assign : VAR ('=' | '+=' | '-=' | '*=' | '/=') expr;

