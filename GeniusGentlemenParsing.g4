grammar GeniusGentlemenParsing ;

start: (line)* EOF ;

funcdec   : WHITESPACE? DEF WHITESPACE FUNCCALL WHITESPACE? COLON WHITESPACE? comment? NEWLINE
	    (WHITESPACE line)+;

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
    | FUNCCALL ;

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

DEF	: 'def' ;

FUNCCALL: VAR WHITESPACE? '(' WHITESPACE? (VAR (WHITESPACE? ',' WHITESPACE? VAR)*)? WHITESPACE? ')' ;

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
