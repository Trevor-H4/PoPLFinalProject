grammar GeniusGentlemenParsing ;

start: ((expr | statement NEWLINE) | NEWLINE)* EOF;

statement : (assign | ifstat);

expr: expr ARITHMETIC_OPERATOR expr
    | INT
    | VAR
    | '(' expr ')' ;

assign : VAR ARITHMETIC_OPERATOR?'=' expr;

ifstat : IF WHITESPACE expr WHITESPACE CONDIT WHITESPACE expr WHITESPACE COLON NEWLINE '\t' statement (EL ifstat | else)?;

else : ELSE WHITESPACE? NEWLINE statement;

IF : 'if';

EL : 'el';

ELSE : 'else:';

COLON : ':';

WHITESPACE : ' '+;

CONDIT : ('<' | '>' | '=' | '!')'='?;

ARITHMETIC_OPERATOR: ('+' | '-' | '*' | '/' | '%');

NEWLINE: [\r]?[\n] ; 

INT    : '-'?[0-9]+ ;

LETTERS : [a-z] | [A-Z] ; 

CHARS  : LETTERS | [0-9] | '_' ;

VAR    : ( LETTERS | '_') CHARS* ;
