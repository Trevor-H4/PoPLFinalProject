grammar GeniusGentlemenParsing ;

start: ((expr | statement NEWLINE) | NEWLINE)* EOF;

statement : assign ;

expr: expr ARITHMETIC_OPERATOR expr
    | INT
    | VAR
    | '(' expr ')' ;

assign : VAR ARITHMETIC_OPERATOR?'=' expr;

ARITHMETIC_OPERATOR: ('+' | '-' | '*' | '/' | '%');

NEWLINE: [\r]?[\n] ; 

INT    : [0-9]+ ;

LETTERS : [a-z] | [A-Z] ; 

CHARS  : LETTERS | [0-9] | '_' ;

VAR    : ( LETTERS | '_') CHARS* ;
