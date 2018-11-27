# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u0148\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\6\2H\n\2\r\2")
        buf.write("\16\2I\3\2\3\2\3\3\3\3\3\3\5\3Q\n\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\7\5X\n\5\f\5\16\5[\13\5\3\6\3\6\3\6\5\6`\n\6\3\6\3")
        buf.write("\6\3\6\5\6e\n\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\6\7n\n\7\r")
        buf.write("\7\16\7o\3\b\3\b\3\b\3\b\3\b\3\t\5\tx\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\7\f\u008e\n\f\f\f\16\f\u0091\13\f\5")
        buf.write("\f\u0093\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\7\16\u00a1\n\16\f\16\16\16\u00a4\13\16\3\17\3")
        buf.write("\17\5\17\u00a8\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\7\21\u00b3\n\21\f\21\16\21\u00b6\13\21\5\21")
        buf.write("\u00b8\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00c1")
        buf.write("\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ca\n")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\7\22\u00e1\n\22\f\22\16\22\u00e4\13\22\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00ea\n\23\3\24\3\24\3\25\3\25\3\26\3\26\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u00fe\n\30\3\31\3\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u0106\n\31\3\32\3\32\3\32\6\32\u010b\n\32\r\32\16")
        buf.write("\32\u010c\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0118\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \5 \u0130\n \3 \3 \3!\3!\7!\u0136\n!\f")
        buf.write("!\16!\u0139\13!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\2\3\"$\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BD\2\b\3\2\27\32\4\2\37!")
        buf.write("\')\5\2\33\33\36\36##\5\2\34\34\"\"$&\4\2\35\35##\3\2")
        buf.write("\b\t\2\u0152\2G\3\2\2\2\4P\3\2\2\2\6R\3\2\2\2\bT\3\2\2")
        buf.write("\2\n\\\3\2\2\2\fk\3\2\2\2\16q\3\2\2\2\20w\3\2\2\2\22y")
        buf.write("\3\2\2\2\24\u0086\3\2\2\2\26\u0092\3\2\2\2\30\u0094\3")
        buf.write("\2\2\2\32\u00a2\3\2\2\2\34\u00a7\3\2\2\2\36\u00a9\3\2")
        buf.write("\2\2 \u00b7\3\2\2\2\"\u00c9\3\2\2\2$\u00e9\3\2\2\2&\u00eb")
        buf.write("\3\2\2\2(\u00ed\3\2\2\2*\u00ef\3\2\2\2,\u00f1\3\2\2\2")
        buf.write(".\u00fd\3\2\2\2\60\u0105\3\2\2\2\62\u010a\3\2\2\2\64\u0111")
        buf.write("\3\2\2\2\66\u0119\3\2\2\28\u011e\3\2\2\2:\u0127\3\2\2")
        buf.write("\2<\u012a\3\2\2\2>\u012d\3\2\2\2@\u0133\3\2\2\2B\u013c")
        buf.write("\3\2\2\2D\u0142\3\2\2\2FH\5\4\3\2GF\3\2\2\2HI\3\2\2\2")
        buf.write("IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\7\2\2\3L\3\3\2\2\2MQ")
        buf.write("\5\22\n\2NQ\5\30\r\2OQ\5\f\7\2PM\3\2\2\2PN\3\2\2\2PO\3")
        buf.write("\2\2\2Q\5\3\2\2\2RS\t\2\2\2S\7\3\2\2\2TY\78\2\2UV\7\61")
        buf.write("\2\2VX\78\2\2WU\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2")
        buf.write("Z\t\3\2\2\2[Y\3\2\2\2\\]\7\25\2\2]_\7*\2\2^`\7#\2\2_^")
        buf.write("\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\62\2\2bd\7\60\2\2ce\7")
        buf.write("#\2\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\7\62\2\2gh\7+\2")
        buf.write("\2hi\7\26\2\2ij\5\6\4\2j\13\3\2\2\2km\7\24\2\2ln\5\16")
        buf.write("\b\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2p\r\3\2\2")
        buf.write("\2qr\5\b\5\2rs\7,\2\2st\5\34\17\2tu\7/\2\2u\17\3\2\2\2")
        buf.write("vx\5\f\7\2wv\3\2\2\2wx\3\2\2\2x\21\3\2\2\2yz\7\22\2\2")
        buf.write("z{\78\2\2{|\7-\2\2|}\5\26\f\2}~\7.\2\2~\177\7,\2\2\177")
        buf.write("\u0080\5\34\17\2\u0080\u0081\7/\2\2\u0081\u0082\5\20\t")
        buf.write("\2\u0082\u0083\7\20\2\2\u0083\u0084\5\32\16\2\u0084\u0085")
        buf.write("\7\21\2\2\u0085\23\3\2\2\2\u0086\u0087\5\b\5\2\u0087\u0088")
        buf.write("\7,\2\2\u0088\u0089\5\34\17\2\u0089\25\3\2\2\2\u008a\u008f")
        buf.write("\5\24\13\2\u008b\u008c\7/\2\2\u008c\u008e\5\24\13\2\u008d")
        buf.write("\u008b\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0092\u008a\3\2\2\2\u0092\u0093\3\2\2\2\u0093\27")
        buf.write("\3\2\2\2\u0094\u0095\7\23\2\2\u0095\u0096\78\2\2\u0096")
        buf.write("\u0097\7-\2\2\u0097\u0098\5\26\f\2\u0098\u0099\7.\2\2")
        buf.write("\u0099\u009a\7/\2\2\u009a\u009b\5\20\t\2\u009b\u009c\7")
        buf.write("\20\2\2\u009c\u009d\5\32\16\2\u009d\u009e\7\21\2\2\u009e")
        buf.write("\31\3\2\2\2\u009f\u00a1\5.\30\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\33\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a8\5\6")
        buf.write("\4\2\u00a6\u00a8\5\n\6\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\35\3\2\2\2\u00a9\u00aa\78\2\2\u00aa\u00ab")
        buf.write("\7-\2\2\u00ab\u00ac\5 \21\2\u00ac\u00ad\7.\2\2\u00ad\u00ae")
        buf.write("\7/\2\2\u00ae\37\3\2\2\2\u00af\u00b4\5\"\22\2\u00b0\u00b1")
        buf.write("\7\61\2\2\u00b1\u00b3\5\"\22\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00af\3")
        buf.write("\2\2\2\u00b7\u00b8\3\2\2\2\u00b8!\3\2\2\2\u00b9\u00c0")
        buf.write("\b\22\1\2\u00ba\u00c1\78\2\2\u00bb\u00c1\7\62\2\2\u00bc")
        buf.write("\u00c1\7\63\2\2\u00bd\u00c1\7\64\2\2\u00be\u00c1\5D#\2")
        buf.write("\u00bf\u00c1\7\65\2\2\u00c0\u00ba\3\2\2\2\u00c0\u00bb")
        buf.write("\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00ca\3\2\2\2")
        buf.write("\u00c2\u00c3\7-\2\2\u00c3\u00c4\5\"\22\2\u00c4\u00c5\7")
        buf.write(".\2\2\u00c5\u00ca\3\2\2\2\u00c6\u00c7\5,\27\2\u00c7\u00c8")
        buf.write("\5\"\22\7\u00c8\u00ca\3\2\2\2\u00c9\u00b9\3\2\2\2\u00c9")
        buf.write("\u00c2\3\2\2\2\u00c9\u00c6\3\2\2\2\u00ca\u00e2\3\2\2\2")
        buf.write("\u00cb\u00cc\f\6\2\2\u00cc\u00cd\5*\26\2\u00cd\u00ce\5")
        buf.write("\"\22\7\u00ce\u00e1\3\2\2\2\u00cf\u00d0\f\5\2\2\u00d0")
        buf.write("\u00d1\5(\25\2\u00d1\u00d2\5\"\22\6\u00d2\u00e1\3\2\2")
        buf.write("\2\u00d3\u00d4\f\4\2\2\u00d4\u00d5\5&\24\2\u00d5\u00d6")
        buf.write("\5\"\22\5\u00d6\u00e1\3\2\2\2\u00d7\u00d8\f\3\2\2\u00d8")
        buf.write("\u00d9\5$\23\2\u00d9\u00da\5\"\22\4\u00da\u00e1\3\2\2")
        buf.write("\2\u00db\u00dc\f\n\2\2\u00dc\u00dd\7*\2\2\u00dd\u00de")
        buf.write("\5\"\22\2\u00de\u00df\7+\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00cb\3\2\2\2\u00e0\u00cf\3\2\2\2\u00e0\u00d3\3\2\2\2")
        buf.write("\u00e0\u00d7\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1\u00e4\3")
        buf.write("\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3#")
        buf.write("\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7&\2\2\u00e6")
        buf.write("\u00ea\7\f\2\2\u00e7\u00e8\7\36\2\2\u00e8\u00ea\7\r\2")
        buf.write("\2\u00e9\u00e5\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea%\3\2")
        buf.write("\2\2\u00eb\u00ec\t\3\2\2\u00ec\'\3\2\2\2\u00ed\u00ee\t")
        buf.write("\4\2\2\u00ee)\3\2\2\2\u00ef\u00f0\t\5\2\2\u00f0+\3\2\2")
        buf.write("\2\u00f1\u00f2\t\6\2\2\u00f2-\3\2\2\2\u00f3\u00fe\5\62")
        buf.write("\32\2\u00f4\u00fe\5\64\33\2\u00f5\u00fe\58\35\2\u00f6")
        buf.write("\u00fe\5\66\34\2\u00f7\u00fe\5:\36\2\u00f8\u00fe\5<\37")
        buf.write("\2\u00f9\u00fe\5> \2\u00fa\u00fe\5\36\20\2\u00fb\u00fe")
        buf.write("\5@!\2\u00fc\u00fe\5B\"\2\u00fd\u00f3\3\2\2\2\u00fd\u00f4")
        buf.write("\3\2\2\2\u00fd\u00f5\3\2\2\2\u00fd\u00f6\3\2\2\2\u00fd")
        buf.write("\u00f7\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3\2\2\2")
        buf.write("\u00fd\u00fa\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3")
        buf.write("\2\2\2\u00fe/\3\2\2\2\u00ff\u0106\78\2\2\u0100\u0106\7")
        buf.write("\62\2\2\u0101\u0106\7\63\2\2\u0102\u0106\7\64\2\2\u0103")
        buf.write("\u0106\5D#\2\u0104\u0106\7\65\2\2\u0105\u00ff\3\2\2\2")
        buf.write("\u0105\u0100\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0102\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106\61")
        buf.write("\3\2\2\2\u0107\u0108\5\"\22\2\u0108\u0109\7\3\2\2\u0109")
        buf.write("\u010b\3\2\2\2\u010a\u0107\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\3")
        buf.write("\2\2\2\u010e\u010f\5\"\22\2\u010f\u0110\7/\2\2\u0110\63")
        buf.write("\3\2\2\2\u0111\u0112\7\13\2\2\u0112\u0113\5\"\22\2\u0113")
        buf.write("\u0114\7\f\2\2\u0114\u0117\5.\30\2\u0115\u0116\7\r\2\2")
        buf.write("\u0116\u0118\5.\30\2\u0117\u0115\3\2\2\2\u0117\u0118\3")
        buf.write("\2\2\2\u0118\65\3\2\2\2\u0119\u011a\7\16\2\2\u011a\u011b")
        buf.write("\5\"\22\2\u011b\u011c\7\n\2\2\u011c\u011d\5.\30\2\u011d")
        buf.write("\67\3\2\2\2\u011e\u011f\7\7\2\2\u011f\u0120\78\2\2\u0120")
        buf.write("\u0121\7\3\2\2\u0121\u0122\5\"\22\2\u0122\u0123\t\7\2")
        buf.write("\2\u0123\u0124\5\"\22\2\u0124\u0125\7\n\2\2\u0125\u0126")
        buf.write("\5.\30\2\u01269\3\2\2\2\u0127\u0128\7\5\2\2\u0128\u0129")
        buf.write("\7/\2\2\u0129;\3\2\2\2\u012a\u012b\7\6\2\2\u012b\u012c")
        buf.write("\7/\2\2\u012c=\3\2\2\2\u012d\u012f\7\4\2\2\u012e\u0130")
        buf.write("\5\"\22\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0132\7/\2\2\u0132?\3\2\2\2\u0133")
        buf.write("\u0137\7\20\2\2\u0134\u0136\5.\30\2\u0135\u0134\3\2\2")
        buf.write("\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\7\21\2\2\u013bA\3\2\2\2\u013c\u013d\7\17\2\2\u013d")
        buf.write("\u013e\5\26\f\2\u013e\u013f\7/\2\2\u013f\u0140\7\n\2\2")
        buf.write("\u0140\u0141\5.\30\2\u0141C\3\2\2\2\u0142\u0143\78\2\2")
        buf.write("\u0143\u0144\7-\2\2\u0144\u0145\5 \21\2\u0145\u0146\7")
        buf.write(".\2\2\u0146E\3\2\2\2\32IPY_dow\u008f\u0092\u00a2\u00a7")
        buf.write("\u00b4\u00b7\u00c0\u00c9\u00e0\u00e2\u00e9\u00fd\u0105")
        buf.write("\u010c\u0117\u012f\u0137")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'*'", "<INVALID>", "<INVALID>", "'<>'", "'<'", 
                     "'<='", "<INVALID>", "'-'", "'/'", "<INVALID>", "<INVALID>", 
                     "'='", "'>'", "'>='", "'['", "']'", "':'", "'('", "')'", 
                     "';'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "RETURN_KEY", "BREAK_KEY", 
                      "CONTINUE_KEY", "FOR_KEY", "TO_KEY", "DOWNTO_KEY", 
                      "DO_KEY", "IF_KEY", "THEN_KEY", "ELSE_KEY", "WHILE_KEY", 
                      "WITH_KEY", "BEGIN_KEY", "END_KEY", "FUNCTION_KEY", 
                      "PROCEDURE_KEY", "VAR_KEY", "ARRAY_TYPE", "OF_KEY", 
                      "REAL_TYPE", "BOOLEAN_TYPE", "INTEGER_TYPE", "STRING_TYPE", 
                      "ADD_OP", "MUL_OP", "NOT_OP", "OR_OP", "NOTEQ_OP", 
                      "LESS_OP", "LESSEQ_OP", "INT_DIV_OP", "SUB_OP", "DIV_OP", 
                      "MOD_OP", "AND_OP", "EQ_OP", "GREAT_OP", "GREAT_EQ_OP", 
                      "L_SQUARE_SEP", "R_SQUARE_SEP", "COLON", "LB", "RB", 
                      "SEMI", "DOUBLE_DOT_SEP", "COMMA", "INT_LIT", "FLOAT_LIT", 
                      "BOOLEAN_LIT", "STRING_LIT", "WS", "COMMENT", "ID", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_mpType = 2
    RULE_idList = 3
    RULE_arrayVal = 4
    RULE_varDec = 5
    RULE_subVarDec = 6
    RULE_nullableLocal = 7
    RULE_funcdec = 8
    RULE_parDec = 9
    RULE_listPar = 10
    RULE_proceduredec = 11
    RULE_body = 12
    RULE_returnType = 13
    RULE_callStmt = 14
    RULE_listExp = 15
    RULE_expr = 16
    RULE_exprOp = 17
    RULE_expr1Op = 18
    RULE_expr2Op = 19
    RULE_expr3Op = 20
    RULE_expr4Op = 21
    RULE_stmt = 22
    RULE_indexExprLeft = 23
    RULE_assignment = 24
    RULE_ifStmt = 25
    RULE_whileStmt = 26
    RULE_forStmt = 27
    RULE_breakStmt = 28
    RULE_continueStmt = 29
    RULE_returnStmt = 30
    RULE_compoundStmt = 31
    RULE_withStmt = 32
    RULE_callExpr = 33

    ruleNames =  [ "program", "decl", "mpType", "idList", "arrayVal", "varDec", 
                   "subVarDec", "nullableLocal", "funcdec", "parDec", "listPar", 
                   "proceduredec", "body", "returnType", "callStmt", "listExp", 
                   "expr", "exprOp", "expr1Op", "expr2Op", "expr3Op", "expr4Op", 
                   "stmt", "indexExprLeft", "assignment", "ifStmt", "whileStmt", 
                   "forStmt", "breakStmt", "continueStmt", "returnStmt", 
                   "compoundStmt", "withStmt", "callExpr" ]

    EOF = Token.EOF
    T__0=1
    RETURN_KEY=2
    BREAK_KEY=3
    CONTINUE_KEY=4
    FOR_KEY=5
    TO_KEY=6
    DOWNTO_KEY=7
    DO_KEY=8
    IF_KEY=9
    THEN_KEY=10
    ELSE_KEY=11
    WHILE_KEY=12
    WITH_KEY=13
    BEGIN_KEY=14
    END_KEY=15
    FUNCTION_KEY=16
    PROCEDURE_KEY=17
    VAR_KEY=18
    ARRAY_TYPE=19
    OF_KEY=20
    REAL_TYPE=21
    BOOLEAN_TYPE=22
    INTEGER_TYPE=23
    STRING_TYPE=24
    ADD_OP=25
    MUL_OP=26
    NOT_OP=27
    OR_OP=28
    NOTEQ_OP=29
    LESS_OP=30
    LESSEQ_OP=31
    INT_DIV_OP=32
    SUB_OP=33
    DIV_OP=34
    MOD_OP=35
    AND_OP=36
    EQ_OP=37
    GREAT_OP=38
    GREAT_EQ_OP=39
    L_SQUARE_SEP=40
    R_SQUARE_SEP=41
    COLON=42
    LB=43
    RB=44
    SEMI=45
    DOUBLE_DOT_SEP=46
    COMMA=47
    INT_LIT=48
    FLOAT_LIT=49
    BOOLEAN_LIT=50
    STRING_LIT=51
    WS=52
    COMMENT=53
    ID=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    ERROR_CHAR=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.DeclContext)
            else:
                return self.getTypedRuleContext(MPParser.DeclContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.decl()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.FUNCTION_KEY) | (1 << MPParser.PROCEDURE_KEY) | (1 << MPParser.VAR_KEY))) != 0)):
                    break

            self.state = 73
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdec(self):
            return self.getTypedRuleContext(MPParser.FuncdecContext,0)


        def proceduredec(self):
            return self.getTypedRuleContext(MPParser.ProceduredecContext,0)


        def varDec(self):
            return self.getTypedRuleContext(MPParser.VarDecContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MPParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.FUNCTION_KEY]:
                self.state = 75
                self.funcdec()
                pass
            elif token in [MPParser.PROCEDURE_KEY]:
                self.state = 76
                self.proceduredec()
                pass
            elif token in [MPParser.VAR_KEY]:
                self.state = 77
                self.varDec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MpTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_TYPE(self):
            return self.getToken(MPParser.INTEGER_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(MPParser.BOOLEAN_TYPE, 0)

        def REAL_TYPE(self):
            return self.getToken(MPParser.REAL_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(MPParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_mpType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMpType" ):
                return visitor.visitMpType(self)
            else:
                return visitor.visitChildren(self)




    def mpType(self):

        localctx = MPParser.MpTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mpType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.REAL_TYPE) | (1 << MPParser.BOOLEAN_TYPE) | (1 << MPParser.INTEGER_TYPE) | (1 << MPParser.STRING_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ID)
            else:
                return self.getToken(MPParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COMMA)
            else:
                return self.getToken(MPParser.COMMA, i)

        def getRuleIndex(self):
            return MPParser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = MPParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MPParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.COMMA:
                self.state = 83
                self.match(MPParser.COMMA)
                self.state = 84
                self.match(MPParser.ID)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_TYPE(self):
            return self.getToken(MPParser.ARRAY_TYPE, 0)

        def L_SQUARE_SEP(self):
            return self.getToken(MPParser.L_SQUARE_SEP, 0)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.INT_LIT)
            else:
                return self.getToken(MPParser.INT_LIT, i)

        def DOUBLE_DOT_SEP(self):
            return self.getToken(MPParser.DOUBLE_DOT_SEP, 0)

        def R_SQUARE_SEP(self):
            return self.getToken(MPParser.R_SQUARE_SEP, 0)

        def OF_KEY(self):
            return self.getToken(MPParser.OF_KEY, 0)

        def mpType(self):
            return self.getTypedRuleContext(MPParser.MpTypeContext,0)


        def SUB_OP(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SUB_OP)
            else:
                return self.getToken(MPParser.SUB_OP, i)

        def getRuleIndex(self):
            return MPParser.RULE_arrayVal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayVal" ):
                return visitor.visitArrayVal(self)
            else:
                return visitor.visitChildren(self)




    def arrayVal(self):

        localctx = MPParser.ArrayValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayVal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MPParser.ARRAY_TYPE)
            self.state = 91
            self.match(MPParser.L_SQUARE_SEP)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.SUB_OP:
                self.state = 92
                self.match(MPParser.SUB_OP)


            self.state = 95
            self.match(MPParser.INT_LIT)
            self.state = 96
            self.match(MPParser.DOUBLE_DOT_SEP)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.SUB_OP:
                self.state = 97
                self.match(MPParser.SUB_OP)


            self.state = 100
            self.match(MPParser.INT_LIT)
            self.state = 101
            self.match(MPParser.R_SQUARE_SEP)
            self.state = 102
            self.match(MPParser.OF_KEY)
            self.state = 103
            self.mpType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KEY(self):
            return self.getToken(MPParser.VAR_KEY, 0)

        def subVarDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.SubVarDecContext)
            else:
                return self.getTypedRuleContext(MPParser.SubVarDecContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_varDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDec" ):
                return visitor.visitVarDec(self)
            else:
                return visitor.visitChildren(self)




    def varDec(self):

        localctx = MPParser.VarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(MPParser.VAR_KEY)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.subVarDec()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubVarDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(MPParser.IdListContext,0)


        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def returnType(self):
            return self.getTypedRuleContext(MPParser.ReturnTypeContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_subVarDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubVarDec" ):
                return visitor.visitSubVarDec(self)
            else:
                return visitor.visitChildren(self)




    def subVarDec(self):

        localctx = MPParser.SubVarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subVarDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.idList()
            self.state = 112
            self.match(MPParser.COLON)
            self.state = 113
            self.returnType()
            self.state = 114
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NullableLocalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDec(self):
            return self.getTypedRuleContext(MPParser.VarDecContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_nullableLocal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableLocal" ):
                return visitor.visitNullableLocal(self)
            else:
                return visitor.visitChildren(self)




    def nullableLocal(self):

        localctx = MPParser.NullableLocalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nullableLocal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.VAR_KEY:
                self.state = 116
                self.varDec()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_KEY(self):
            return self.getToken(MPParser.FUNCTION_KEY, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def listPar(self):
            return self.getTypedRuleContext(MPParser.ListParContext,0)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def returnType(self):
            return self.getTypedRuleContext(MPParser.ReturnTypeContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def nullableLocal(self):
            return self.getTypedRuleContext(MPParser.NullableLocalContext,0)


        def BEGIN_KEY(self):
            return self.getToken(MPParser.BEGIN_KEY, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def END_KEY(self):
            return self.getToken(MPParser.END_KEY, 0)

        def getRuleIndex(self):
            return MPParser.RULE_funcdec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdec" ):
                return visitor.visitFuncdec(self)
            else:
                return visitor.visitChildren(self)




    def funcdec(self):

        localctx = MPParser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcdec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MPParser.FUNCTION_KEY)
            self.state = 120
            self.match(MPParser.ID)
            self.state = 121
            self.match(MPParser.LB)
            self.state = 122
            self.listPar()
            self.state = 123
            self.match(MPParser.RB)
            self.state = 124
            self.match(MPParser.COLON)
            self.state = 125
            self.returnType()
            self.state = 126
            self.match(MPParser.SEMI)
            self.state = 127
            self.nullableLocal()
            self.state = 128
            self.match(MPParser.BEGIN_KEY)
            self.state = 129
            self.body()
            self.state = 130
            self.match(MPParser.END_KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(MPParser.IdListContext,0)


        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def returnType(self):
            return self.getTypedRuleContext(MPParser.ReturnTypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_parDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParDec" ):
                return visitor.visitParDec(self)
            else:
                return visitor.visitChildren(self)




    def parDec(self):

        localctx = MPParser.ParDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.idList()
            self.state = 133
            self.match(MPParser.COLON)
            self.state = 134
            self.returnType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListParContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ParDecContext)
            else:
                return self.getTypedRuleContext(MPParser.ParDecContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SEMI)
            else:
                return self.getToken(MPParser.SEMI, i)

        def getRuleIndex(self):
            return MPParser.RULE_listPar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListPar" ):
                return visitor.visitListPar(self)
            else:
                return visitor.visitChildren(self)




    def listPar(self):

        localctx = MPParser.ListParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listPar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID:
                self.state = 136
                self.parDec()
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 137
                        self.match(MPParser.SEMI)
                        self.state = 138
                        self.parDec() 
                    self.state = 143
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProceduredecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_KEY(self):
            return self.getToken(MPParser.PROCEDURE_KEY, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def listPar(self):
            return self.getTypedRuleContext(MPParser.ListParContext,0)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def nullableLocal(self):
            return self.getTypedRuleContext(MPParser.NullableLocalContext,0)


        def BEGIN_KEY(self):
            return self.getToken(MPParser.BEGIN_KEY, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def END_KEY(self):
            return self.getToken(MPParser.END_KEY, 0)

        def getRuleIndex(self):
            return MPParser.RULE_proceduredec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProceduredec" ):
                return visitor.visitProceduredec(self)
            else:
                return visitor.visitChildren(self)




    def proceduredec(self):

        localctx = MPParser.ProceduredecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_proceduredec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MPParser.PROCEDURE_KEY)
            self.state = 147
            self.match(MPParser.ID)
            self.state = 148
            self.match(MPParser.LB)
            self.state = 149
            self.listPar()
            self.state = 150
            self.match(MPParser.RB)
            self.state = 151
            self.match(MPParser.SEMI)
            self.state = 152
            self.nullableLocal()
            self.state = 153
            self.match(MPParser.BEGIN_KEY)
            self.state = 154
            self.body()
            self.state = 155
            self.match(MPParser.END_KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.StmtContext)
            else:
                return self.getTypedRuleContext(MPParser.StmtContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MPParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.RETURN_KEY) | (1 << MPParser.BREAK_KEY) | (1 << MPParser.CONTINUE_KEY) | (1 << MPParser.FOR_KEY) | (1 << MPParser.IF_KEY) | (1 << MPParser.WHILE_KEY) | (1 << MPParser.WITH_KEY) | (1 << MPParser.BEGIN_KEY) | (1 << MPParser.NOT_OP) | (1 << MPParser.SUB_OP) | (1 << MPParser.LB) | (1 << MPParser.INT_LIT) | (1 << MPParser.FLOAT_LIT) | (1 << MPParser.BOOLEAN_LIT) | (1 << MPParser.STRING_LIT) | (1 << MPParser.ID))) != 0):
                self.state = 157
                self.stmt()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mpType(self):
            return self.getTypedRuleContext(MPParser.MpTypeContext,0)


        def arrayVal(self):
            return self.getTypedRuleContext(MPParser.ArrayValContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = MPParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.REAL_TYPE, MPParser.BOOLEAN_TYPE, MPParser.INTEGER_TYPE, MPParser.STRING_TYPE]:
                self.state = 163
                self.mpType()
                pass
            elif token in [MPParser.ARRAY_TYPE]:
                self.state = 164
                self.arrayVal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def listExp(self):
            return self.getTypedRuleContext(MPParser.ListExpContext,0)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_callStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStmt" ):
                return visitor.visitCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def callStmt(self):

        localctx = MPParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MPParser.ID)
            self.state = 168
            self.match(MPParser.LB)
            self.state = 169
            self.listExp()
            self.state = 170
            self.match(MPParser.RB)
            self.state = 171
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COMMA)
            else:
                return self.getToken(MPParser.COMMA, i)

        def getRuleIndex(self):
            return MPParser.RULE_listExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExp" ):
                return visitor.visitListExp(self)
            else:
                return visitor.visitChildren(self)




    def listExp(self):

        localctx = MPParser.ListExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.NOT_OP) | (1 << MPParser.SUB_OP) | (1 << MPParser.LB) | (1 << MPParser.INT_LIT) | (1 << MPParser.FLOAT_LIT) | (1 << MPParser.BOOLEAN_LIT) | (1 << MPParser.STRING_LIT) | (1 << MPParser.ID))) != 0):
                self.state = 173
                self.expr(0)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MPParser.COMMA:
                    self.state = 174
                    self.match(MPParser.COMMA)
                    self.state = 175
                    self.expr(0)
                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MPParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MPParser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MPParser.BOOLEAN_LIT, 0)

        def callExpr(self):
            return self.getTypedRuleContext(MPParser.CallExprContext,0)


        def STRING_LIT(self):
            return self.getToken(MPParser.STRING_LIT, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def expr4Op(self):
            return self.getTypedRuleContext(MPParser.Expr4OpContext,0)


        def expr3Op(self):
            return self.getTypedRuleContext(MPParser.Expr3OpContext,0)


        def expr2Op(self):
            return self.getTypedRuleContext(MPParser.Expr2OpContext,0)


        def expr1Op(self):
            return self.getTypedRuleContext(MPParser.Expr1OpContext,0)


        def exprOp(self):
            return self.getTypedRuleContext(MPParser.ExprOpContext,0)


        def L_SQUARE_SEP(self):
            return self.getToken(MPParser.L_SQUARE_SEP, 0)

        def R_SQUARE_SEP(self):
            return self.getToken(MPParser.R_SQUARE_SEP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.INT_LIT, MPParser.FLOAT_LIT, MPParser.BOOLEAN_LIT, MPParser.STRING_LIT, MPParser.ID]:
                self.state = 190
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 184
                    self.match(MPParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 185
                    self.match(MPParser.INT_LIT)
                    pass

                elif la_ == 3:
                    self.state = 186
                    self.match(MPParser.FLOAT_LIT)
                    pass

                elif la_ == 4:
                    self.state = 187
                    self.match(MPParser.BOOLEAN_LIT)
                    pass

                elif la_ == 5:
                    self.state = 188
                    self.callExpr()
                    pass

                elif la_ == 6:
                    self.state = 189
                    self.match(MPParser.STRING_LIT)
                    pass


                pass
            elif token in [MPParser.LB]:
                self.state = 192
                self.match(MPParser.LB)
                self.state = 193
                self.expr(0)
                self.state = 194
                self.match(MPParser.RB)
                pass
            elif token in [MPParser.NOT_OP, MPParser.SUB_OP]:
                self.state = 196
                self.expr4Op()
                self.state = 197
                self.expr(5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 201
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 202
                        self.expr3Op()
                        self.state = 203
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 206
                        self.expr2Op()
                        self.state = 207
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 209
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 210
                        self.expr1Op()
                        self.state = 211
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 213
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 214
                        self.exprOp()
                        self.state = 215
                        self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 218
                        self.match(MPParser.L_SQUARE_SEP)
                        self.state = 219
                        self.expr(0)
                        self.state = 220
                        self.match(MPParser.R_SQUARE_SEP)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExprOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_OP(self):
            return self.getToken(MPParser.AND_OP, 0)

        def THEN_KEY(self):
            return self.getToken(MPParser.THEN_KEY, 0)

        def OR_OP(self):
            return self.getToken(MPParser.OR_OP, 0)

        def ELSE_KEY(self):
            return self.getToken(MPParser.ELSE_KEY, 0)

        def getRuleIndex(self):
            return MPParser.RULE_exprOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOp" ):
                return visitor.visitExprOp(self)
            else:
                return visitor.visitChildren(self)




    def exprOp(self):

        localctx = MPParser.ExprOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.AND_OP]:
                self.state = 227
                self.match(MPParser.AND_OP)
                self.state = 228
                self.match(MPParser.THEN_KEY)
                pass
            elif token in [MPParser.OR_OP]:
                self.state = 229
                self.match(MPParser.OR_OP)
                self.state = 230
                self.match(MPParser.ELSE_KEY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr1OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_OP(self):
            return self.getToken(MPParser.EQ_OP, 0)

        def NOTEQ_OP(self):
            return self.getToken(MPParser.NOTEQ_OP, 0)

        def LESS_OP(self):
            return self.getToken(MPParser.LESS_OP, 0)

        def LESSEQ_OP(self):
            return self.getToken(MPParser.LESSEQ_OP, 0)

        def GREAT_OP(self):
            return self.getToken(MPParser.GREAT_OP, 0)

        def GREAT_EQ_OP(self):
            return self.getToken(MPParser.GREAT_EQ_OP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_expr1Op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1Op" ):
                return visitor.visitExpr1Op(self)
            else:
                return visitor.visitChildren(self)




    def expr1Op(self):

        localctx = MPParser.Expr1OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr1Op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.NOTEQ_OP) | (1 << MPParser.LESS_OP) | (1 << MPParser.LESSEQ_OP) | (1 << MPParser.EQ_OP) | (1 << MPParser.GREAT_OP) | (1 << MPParser.GREAT_EQ_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr2OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_OP(self):
            return self.getToken(MPParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(MPParser.SUB_OP, 0)

        def OR_OP(self):
            return self.getToken(MPParser.OR_OP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_expr2Op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2Op" ):
                return visitor.visitExpr2Op(self)
            else:
                return visitor.visitChildren(self)




    def expr2Op(self):

        localctx = MPParser.Expr2OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr2Op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.ADD_OP) | (1 << MPParser.OR_OP) | (1 << MPParser.SUB_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr3OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIV_OP(self):
            return self.getToken(MPParser.DIV_OP, 0)

        def MUL_OP(self):
            return self.getToken(MPParser.MUL_OP, 0)

        def INT_DIV_OP(self):
            return self.getToken(MPParser.INT_DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(MPParser.MOD_OP, 0)

        def AND_OP(self):
            return self.getToken(MPParser.AND_OP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_expr3Op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3Op" ):
                return visitor.visitExpr3Op(self)
            else:
                return visitor.visitChildren(self)




    def expr3Op(self):

        localctx = MPParser.Expr3OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr3Op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.MUL_OP) | (1 << MPParser.INT_DIV_OP) | (1 << MPParser.DIV_OP) | (1 << MPParser.MOD_OP) | (1 << MPParser.AND_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr4OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(MPParser.SUB_OP, 0)

        def NOT_OP(self):
            return self.getToken(MPParser.NOT_OP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_expr4Op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4Op" ):
                return visitor.visitExpr4Op(self)
            else:
                return visitor.visitChildren(self)




    def expr4Op(self):

        localctx = MPParser.Expr4OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr4Op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==MPParser.NOT_OP or _la==MPParser.SUB_OP):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MPParser.AssignmentContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MPParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MPParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MPParser.WhileStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MPParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MPParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MPParser.ReturnStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(MPParser.CallStmtContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(MPParser.CompoundStmtContext,0)


        def withStmt(self):
            return self.getTypedRuleContext(MPParser.WithStmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MPParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 247
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 248
                self.callStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 249
                self.compoundStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 250
                self.withStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndexExprLeftContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MPParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MPParser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MPParser.BOOLEAN_LIT, 0)

        def callExpr(self):
            return self.getTypedRuleContext(MPParser.CallExprContext,0)


        def STRING_LIT(self):
            return self.getToken(MPParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return MPParser.RULE_indexExprLeft

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExprLeft" ):
                return visitor.visitIndexExprLeft(self)
            else:
                return visitor.visitChildren(self)




    def indexExprLeft(self):

        localctx = MPParser.IndexExprLeftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_indexExprLeft)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(MPParser.ID)
                pass

            elif la_ == 2:
                self.state = 254
                self.match(MPParser.INT_LIT)
                pass

            elif la_ == 3:
                self.state = 255
                self.match(MPParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.state = 256
                self.match(MPParser.BOOLEAN_LIT)
                pass

            elif la_ == 5:
                self.state = 257
                self.callExpr()
                pass

            elif la_ == 6:
                self.state = 258
                self.match(MPParser.STRING_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MPParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 261
                    self.expr(0)
                    self.state = 262
                    self.match(MPParser.T__0)

                else:
                    raise NoViableAltException(self)
                self.state = 266 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 268
            self.expr(0)
            self.state = 269
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEY(self):
            return self.getToken(MPParser.IF_KEY, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def THEN_KEY(self):
            return self.getToken(MPParser.THEN_KEY, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.StmtContext)
            else:
                return self.getTypedRuleContext(MPParser.StmtContext,i)


        def ELSE_KEY(self):
            return self.getToken(MPParser.ELSE_KEY, 0)

        def getRuleIndex(self):
            return MPParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MPParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MPParser.IF_KEY)
            self.state = 272
            self.expr(0)
            self.state = 273
            self.match(MPParser.THEN_KEY)
            self.state = 274
            self.stmt()
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 275
                self.match(MPParser.ELSE_KEY)
                self.state = 276
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_KEY(self):
            return self.getToken(MPParser.WHILE_KEY, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def DO_KEY(self):
            return self.getToken(MPParser.DO_KEY, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MPParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MPParser.WHILE_KEY)
            self.state = 280
            self.expr(0)
            self.state = 281
            self.match(MPParser.DO_KEY)
            self.state = 282
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_KEY(self):
            return self.getToken(MPParser.FOR_KEY, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def DO_KEY(self):
            return self.getToken(MPParser.DO_KEY, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def TO_KEY(self):
            return self.getToken(MPParser.TO_KEY, 0)

        def DOWNTO_KEY(self):
            return self.getToken(MPParser.DOWNTO_KEY, 0)

        def getRuleIndex(self):
            return MPParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MPParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(MPParser.FOR_KEY)
            self.state = 285
            self.match(MPParser.ID)
            self.state = 286
            self.match(MPParser.T__0)
            self.state = 287
            self.expr(0)
            self.state = 288
            _la = self._input.LA(1)
            if not(_la==MPParser.TO_KEY or _la==MPParser.DOWNTO_KEY):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 289
            self.expr(0)
            self.state = 290
            self.match(MPParser.DO_KEY)
            self.state = 291
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_KEY(self):
            return self.getToken(MPParser.BREAK_KEY, 0)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = MPParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MPParser.BREAK_KEY)
            self.state = 294
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_KEY(self):
            return self.getToken(MPParser.CONTINUE_KEY, 0)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = MPParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MPParser.CONTINUE_KEY)
            self.state = 297
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KEY(self):
            return self.getToken(MPParser.RETURN_KEY, 0)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MPParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MPParser.RETURN_KEY)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.NOT_OP) | (1 << MPParser.SUB_OP) | (1 << MPParser.LB) | (1 << MPParser.INT_LIT) | (1 << MPParser.FLOAT_LIT) | (1 << MPParser.BOOLEAN_LIT) | (1 << MPParser.STRING_LIT) | (1 << MPParser.ID))) != 0):
                self.state = 300
                self.expr(0)


            self.state = 303
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_KEY(self):
            return self.getToken(MPParser.BEGIN_KEY, 0)

        def END_KEY(self):
            return self.getToken(MPParser.END_KEY, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.StmtContext)
            else:
                return self.getTypedRuleContext(MPParser.StmtContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_compoundStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStmt" ):
                return visitor.visitCompoundStmt(self)
            else:
                return visitor.visitChildren(self)




    def compoundStmt(self):

        localctx = MPParser.CompoundStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_compoundStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MPParser.BEGIN_KEY)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.RETURN_KEY) | (1 << MPParser.BREAK_KEY) | (1 << MPParser.CONTINUE_KEY) | (1 << MPParser.FOR_KEY) | (1 << MPParser.IF_KEY) | (1 << MPParser.WHILE_KEY) | (1 << MPParser.WITH_KEY) | (1 << MPParser.BEGIN_KEY) | (1 << MPParser.NOT_OP) | (1 << MPParser.SUB_OP) | (1 << MPParser.LB) | (1 << MPParser.INT_LIT) | (1 << MPParser.FLOAT_LIT) | (1 << MPParser.BOOLEAN_LIT) | (1 << MPParser.STRING_LIT) | (1 << MPParser.ID))) != 0):
                self.state = 306
                self.stmt()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
            self.match(MPParser.END_KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH_KEY(self):
            return self.getToken(MPParser.WITH_KEY, 0)

        def listPar(self):
            return self.getTypedRuleContext(MPParser.ListParContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def DO_KEY(self):
            return self.getToken(MPParser.DO_KEY, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_withStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithStmt" ):
                return visitor.visitWithStmt(self)
            else:
                return visitor.visitChildren(self)




    def withStmt(self):

        localctx = MPParser.WithStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_withStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MPParser.WITH_KEY)
            self.state = 315
            self.listPar()
            self.state = 316
            self.match(MPParser.SEMI)
            self.state = 317
            self.match(MPParser.DO_KEY)
            self.state = 318
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def listExp(self):
            return self.getTypedRuleContext(MPParser.ListExpContext,0)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def getRuleIndex(self):
            return MPParser.RULE_callExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)




    def callExpr(self):

        localctx = MPParser.CallExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_callExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MPParser.ID)
            self.state = 321
            self.match(MPParser.LB)
            self.state = 322
            self.listExp()
            self.state = 323
            self.match(MPParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         




