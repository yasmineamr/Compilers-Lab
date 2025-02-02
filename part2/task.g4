grammar task;

NEWLINE     : [\r\n]+;
REG         : [A-D]'X';
MEMORY      : ('['REG']');
IMMEDIATE   : ([1-9]+[0-9]* | [0-1]+'b');
SPACE       : (' '|'\t');
SEPARATOR   : (','SPACE);
COMMAND     : ('AAA'|'ADD'|'INC');

expr        : COMMAND NEWLINE
            | COMMAND SPACE REG SEPARATOR MEMORY NEWLINE
            | COMMAND SPACE MEMORY SEPARATOR REG NEWLINE
            | COMMAND SPACE REG SEPARATOR REG NEWLINE
            | COMMAND SPACE MEMORY SEPARATOR IMMEDIATE NEWLINE
            | COMMAND SPACE IMMEDIATE SEPARATOR MEMORY NEWLINE
            | COMMAND SPACE REG NEWLINE
            | COMMAND SPACE MEMORY NEWLINE;

start       : (expr)*;

// expr: unary|binary|noop
/* AAA

ADD REG MEM
ADD MEM REG
ADD REG REG
ADD MEM IMMEDIATE
ADD REG IMMEDIATE

INC REG
INC MEM */
