grammar GeniusGentlemenParsing ;

start: line* EOF;

line : (expr | statement | WHITESPACE)? NEWLINE ;

statement : (assign | ifstat);

expr: expr WHITESPACE? ARITHMETIC_OPERATOR WHITESPACE? expr
    | INT
    | VAR
    | TRUE | FALSE
    | '(' expr ')'
    | expr WHITESPACE? CONDIT WHITESPACE? expr 
    | expr WHITESPACE ANDOR WHITESPACE expr
    | 'not' WHITESPACE expr ;

assign : VAR WHITESPACE? ARITHMETIC_OPERATOR?'=' WHITESPACE? expr;

ifstat : IF WHITESPACE expr WHITESPACE? COLON NEWLINE
         WHITESPACE (line+ | (PASS))
         ((EL ifstat) | else)? ;

else : ELSE WHITESPACE? NEWLINE statement;

ANDOR   : ('and' | 'or') ;

IF      : 'if';

EL      : 'el';

ELSE    : 'else:';

TRUE    : 'True' ;

FALSE   : 'False' ;

COLON   : ':';

WHITESPACE : ('\t'|' ')+;

PASS    : 'pass' ;

CONDIT  : ('<' | '>' | '=' | '!')'='?;

ARITHMETIC_OPERATOR : ('+' | '-' | '*' | '/' | '%');

NEWLINE : [\r]?[\n] ;

INT     : '-'?DIGITS+ ;

LETTERS : [a-z] | [A-Z] ;

DIGITS  : [0-9] ;

CHARS   : LETTERS | DIGITS | '_' ;

VAR     : ( LETTERS | '_') CHARS* ;
