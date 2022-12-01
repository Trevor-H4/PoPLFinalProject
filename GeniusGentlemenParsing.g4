grammar GeniusGentlemenParsing ;

start: line* EOF ;

line : ((expr | statement | WHITESPACE | PASS)? NEWLINE) | structure ;

statement : assign ;

structure : ifstat ;

expr: expr WHITESPACE? ARITHMETIC_OPERATOR WHITESPACE? expr
    | INT
    | VAR
    | TRUE | FALSE
    | '(' expr ')'
    | expr WHITESPACE? CONDIT WHITESPACE? expr 
    | expr WHITESPACE ANDOR WHITESPACE expr
    | 'not' WHITESPACE expr ;

assign 	: VAR WHITESPACE? ARITHMETIC_OPERATOR?'=' WHITESPACE? expr ;

ifstat 	: IF WHITESPACE expr WHITESPACE? COLON NEWLINE
          (WHITESPACE line)+
          else? ;

else 	: ELSE WHITESPACE? COLON NEWLINE
       	  (WHITESPACE line)+ ;

while 	: WHILE WHITESPACE expr WHITESPACE? COLON NEWLINE
	  (WHITESPACE line)+ ;

for	: FOR WHITESPACE VAR WHITESPACE IN WHITESPACE expr WHITESPACE? COLON NEWLINE
	  (WHITESPACE line)+ ;

comment	: COMMENT ANYTHING ;

ANDOR   : ('and' | 'or') ;

IF      : 'if' ;

EL      : 'el' ;

ELSE    : 'else' ;

WHILE	: 'while' ;

FOR	: 'for' ;

IN	: 'in' ;

COMMENT	: '#' ;

ANYTHING: ;

TRUE    : 'True' ;

FALSE   : 'False' ;

COLON   : ':' ;

WHITESPACE : ('\t'|' ')+ ;

PASS    : 'pass' ;

CONDIT  : (('<' | '>' | '=' | '!')'=') | '<' | '>' ;

ARITHMETIC_OPERATOR : ('+' | '-' | '*' | '/' | '%') ;

NEWLINE : [\r]?[\n] ;

INT     : '-'?DIGITS+ ;

LETTERS : [a-z] | [A-Z] ;

DIGITS  : [0-9] ;

CHARS   : LETTERS | DIGITS | '_' ;

VAR     : (LETTERS | '_') CHARS* ;
