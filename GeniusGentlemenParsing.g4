grammar GeniusGentlemenParsing ;

start: (line)* EOF ;

line : ((expr | statement | WHITESPACE | PASS)? WHITESPACE? comment? NEWLINE) | structure;

statement : assign ;

structure : ifstat | while | for | funcdec ;

expr: expr WHITESPACE? ARITHMETIC_OPERATOR WHITESPACE? expr
    | INT
    | VAR
    | TRUE | FALSE
    | '(' expr ')'
    | expr WHITESPACE? CONDIT WHITESPACE? expr 
    | expr WHITESPACE ANDOR WHITESPACE expr
    | 'not' WHITESPACE expr 
    | funccall ; 

assign 	: VAR WHITESPACE? ARITHMETIC_OPERATOR?'=' WHITESPACE? expr ;

ifstat 	: IF WHITESPACE expr WHITESPACE? COLON WHITESPACE? comment? NEWLINE
          (WHITESPACE line)+
          else? ;

else 	: ELSE WHITESPACE? COLON WHITESPACE? comment? NEWLINE
       	  (WHITESPACE line)+ ;

while 	: WHILE WHITESPACE expr WHITESPACE? COLON WHITESPACE? comment? NEWLINE
	  (WHITESPACE line)+ ;

for	: FOR WHITESPACE VAR WHITESPACE IN WHITESPACE expr WHITESPACE? COLON WHITESPACE? comment? NEWLINE
	  (WHITESPACE line)+ ;

comment	: '#' (. | '?')*? ;

funcdec   : WHITESPACE? DEF WHITESPACE VAR WHITESPACE? '(' WHITESPACE? (VAR (WHITESPACE? ',' WHITESPACE? VAR)*)? WHITESPACE? ')' WHITESPACE? COLON WHITESPACE? comment? NEWLINE
	    (WHITESPACE line)+;

DEF	: 'def' ;

funccall: VAR WHITESPACE? '(' params ')' ;

params  : WHITESPACE? (expr (WHITESPACE? ',' WHITESPACE? expr)*)? WHITESPACE? ;

ANDOR   : ('and' | 'or') ;

IF      : 'if' ;

EL      : 'el' ;

ELSE    : 'else' ;

WHILE	: 'while' ;

FOR	: 'for' ;

IN	: 'in' ;

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

SYMBOLS : ('#' | '`' | '~' | '!' | '@' | '$' | '%' | '^' | '&' | '*' | '(' | ')' | '_' | '-' | '+' | '=' | '{' |
           '[' | ']' | '}' | '\\' | '|' | '\'' | '"' | ';' | ':' | ',' | '<' | '.' | '>' | '/' | '?');

CHARS   : LETTERS | DIGITS | '_' ;

VAR     : (LETTERS | '_') CHARS* ;
