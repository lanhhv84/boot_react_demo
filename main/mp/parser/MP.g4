grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF; // Done
decl: (funcdec|proceduredec|varDec); // Done
// My code

mpType: INTEGER_TYPE|BOOLEAN_TYPE|REAL_TYPE|STRING_TYPE ; 

// Comma-seperated list of identifier
idList: ID (COMMA ID)*; // Done

// Value of an array EX: (array [1..2] of integer)
arrayVal: ARRAY_TYPE L_SQUARE_SEP SUB_OP? INT_LIT DOUBLE_DOT_SEP SUB_OP? INT_LIT R_SQUARE_SEP OF_KEY mpType; // Done

// Variable declaration
varDec: VAR_KEY subVarDec+; // Done
subVarDec: (idList COLON returnType SEMI); // Done
nullableLocal: varDec?; // Done

// Function declaration
funcdec: FUNCTION_KEY ID LB listPar RB COLON returnType SEMI nullableLocal BEGIN_KEY body END_KEY; // Done
// List parameters
parDec: idList COLON returnType; // Done
listPar: (parDec (SEMI parDec)*)?; // Done
// Procedure declaration
proceduredec: PROCEDURE_KEY ID LB listPar RB SEMI nullableLocal BEGIN_KEY body END_KEY; // Done
body: stmt*; // Done
returnType: (mpType|arrayVal); // Done

// Call stmt
callStmt: ID LB listExp RB SEMI; // Done
listExp: (expr (COMMA expr)*)?; // Done

// Expression

// a: a '+' INT_LIT | b;
// b: a '[' a ']';

expr:  expr L_SQUARE_SEP expr R_SQUARE_SEP 
	| (ID|INT_LIT|FLOAT_LIT|BOOLEAN_LIT|callExpr|STRING_LIT)
	| LB expr RB // Exp5
	| <assoc=right> expr4Op expr // Expr4
	| <assoc=left> expr expr3Op expr // Expr3
	| <assoc=left> expr expr2Op expr // expr2
	| expr expr1Op expr // expr1
	| <assoc=left> expr exprOp expr // Expr0
	;

exprOp: ((AND_OP THEN_KEY) |(OR_OP ELSE_KEY)); // Done
expr1Op: (EQ_OP|NOTEQ_OP|LESS_OP|LESSEQ_OP|GREAT_OP|GREAT_EQ_OP); // Done
expr2Op: (ADD_OP|SUB_OP|OR_OP); // Done
expr3Op: (DIV_OP|MUL_OP|INT_DIV_OP|MOD_OP|AND_OP); // Done
expr4Op: (SUB_OP|NOT_OP); // Done





// Statement -Tested
stmt: assignment|ifStmt|forStmt|whileStmt|breakStmt|continueStmt|returnStmt|callStmt|compoundStmt|withStmt; // Done
// Index expression - Tested
indexExprLeft: (ID|INT_LIT|FLOAT_LIT|BOOLEAN_LIT|callExpr|STRING_LIT);
// Assignment statement - Tested
assignment: (expr ':=')+ expr SEMI; // Done 
// If statement 
ifStmt: IF_KEY expr THEN_KEY stmt (ELSE_KEY stmt)?; // Done
// While statement
whileStmt: WHILE_KEY expr DO_KEY stmt; // Done
// For statement
forStmt: FOR_KEY ID ':=' expr (TO_KEY|DOWNTO_KEY) expr DO_KEY stmt; // Done
// Break statement
breakStmt: BREAK_KEY SEMI; // Done
// Continue statement
continueStmt: CONTINUE_KEY SEMI; // Done
// Return statement
returnStmt: RETURN_KEY expr? SEMI; // Done
// Compound statement
compoundStmt: BEGIN_KEY stmt* END_KEY; // Done
// With statement - Tested - Done
withStmt: WITH_KEY listPar SEMI DO_KEY stmt; // Done
// Fragment

callExpr: ID LB listExp RB;

fragment Q: 'Q'|'q';
fragment W: 'W'|'w';
fragment E: 'E'|'e';
fragment R: 'R'|'r';
fragment T: 'T'|'t';
fragment Y: 'Y'|'y';
fragment U: 'U'|'u';
fragment I: 'I'|'i';
fragment O: 'O'|'o';
fragment P: 'P'|'p';
fragment A: 'A'|'a';
fragment S: 'S'|'s';
fragment D: 'D'|'d';
fragment F: 'F'|'f';
fragment G: 'G'|'g';
fragment H: 'H'|'h';
fragment J: 'J'|'j';
fragment K: 'K'|'k';
fragment L: 'L'|'l';
fragment Z: 'Z'|'z';
fragment X: 'X'|'x';
fragment C: 'C'|'c';
fragment V: 'V'|'v';
fragment B: 'B'|'b';
fragment N: 'N'|'n';
fragment M: 'M'|'m';



fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment UNDER_SCORE: '_';

fragment STRING_ESC: '\\'('n'|'b'|'f'|'r'|'t'|'\''|'"');

// Token 2: Key words
RETURN_KEY: R E T U R N;
BREAK_KEY: B R E A K;
CONTINUE_KEY: C O N T I N U E;
FOR_KEY: F O R;
TO_KEY: T O;
DOWNTO_KEY: D O W N T O;
DO_KEY: D O;
IF_KEY: I F;
THEN_KEY: T H E N;
ELSE_KEY: E L S E;
WHILE_KEY: W H I L E;
WITH_KEY: W I T H;
BEGIN_KEY: B E G I N;
END_KEY: E N D;
FUNCTION_KEY: F U N C T I O N;
PROCEDURE_KEY: P R O C E D U R E;
VAR_KEY: V A R;

ARRAY_TYPE: A R R A Y;
OF_KEY: O F;
REAL_TYPE: R E A L;
BOOLEAN_TYPE: B O O L E A N;
INTEGER_TYPE: I N T E G E R;
STRING_TYPE: S T R I N G;



// Token 3: Operator
ADD_OP: '+';
MUL_OP: '*';
NOT_OP: N O T;
OR_OP: O R;
NOTEQ_OP: '<>';
LESS_OP: '<';
LESSEQ_OP: '<=';
INT_DIV_OP: D I V;
SUB_OP: '-';
DIV_OP: '/';
MOD_OP: M O D;
AND_OP: A N D;
EQ_OP: '=';
GREAT_OP: '>';
GREAT_EQ_OP: '>=';
// Token 4: Seperators
L_SQUARE_SEP: '[';
R_SQUARE_SEP: ']';
COLON: ':';
LB: '(' ;
RB: ')' ;
SEMI: ';' ;
DOUBLE_DOT_SEP: '..';
COMMA: ',';
// Token 5: Literals
INT_LIT: [0-9]+;
FLOAT_LIT: ((DIGIT+'.')|('.'DIGIT+)|(DIGIT+'.'DIGIT+)|DIGIT+)(E'-'?DIGIT*)?;
BOOLEAN_LIT: (T R U E)|(F A L S E);
STRING_LIT:'"' ( '\\' [btnfr'\\"] | ~[\b\t\f\r\n\\'"] )* '"' {self.text = self.text[1:len(self.text) - 1]};

// End token
fragment ENDLINE: [\r\n];


WS : [ \t\r\n] -> skip ; // skip spaces, tabs, newlines

// End of my code
// Token 1: Identifiers

COMMENT: (TRA_BLOCK_COMMENT|BLOCK_COMMENT|LINE_COMMENT) -> skip;
fragment TRA_BLOCK_COMMENT: '(*' .*? '*)';
fragment BLOCK_COMMENT: '{' .*? '}';
fragment LINE_COMMENT: '//'~('\r'|'\n')*;

ID:  (UNDER_SCORE|LETTER)(UNDER_SCORE|LETTER|DIGIT)*;
UNCLOSE_STRING: '"' ( '\\' [btnfr'\\"] | ~[\b\t\f\r\n\\'"] )* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' (~[\b\f\n\t\r\\'"] | '\\' [tnfbr'"\\])* ([\b\f\n\t\r'\\] | ('\\' ~[btnfr'\\])) { raise IllegalEscape(self.text[1:])}; //xem lại?
ERROR_CHAR: . {raise ErrorToken(self.text)};