# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u0257\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\39\39\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3B\3B\3C\3C\3C\3C\3D\3D\3E\3E\3F\3F\3F\3G\3")
        buf.write("G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3M\3N\3N\3O\6O\u01bb")
        buf.write("\nO\rO\16O\u01bc\3P\6P\u01c0\nP\rP\16P\u01c1\3P\3P\3P")
        buf.write("\3P\6P\u01c8\nP\rP\16P\u01c9\3P\6P\u01cd\nP\rP\16P\u01ce")
        buf.write("\3P\3P\6P\u01d3\nP\rP\16P\u01d4\3P\6P\u01d8\nP\rP\16P")
        buf.write("\u01d9\5P\u01dc\nP\3P\3P\5P\u01e0\nP\3P\7P\u01e3\nP\f")
        buf.write("P\16P\u01e6\13P\5P\u01e8\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\5Q\u01f5\nQ\3R\3R\3R\3R\7R\u01fb\nR\fR\16R\u01fe")
        buf.write("\13R\3R\3R\3R\3S\3S\3T\3T\3T\3T\3U\3U\3U\5U\u020c\nU\3")
        buf.write("U\3U\3V\3V\3V\3V\7V\u0214\nV\fV\16V\u0217\13V\3V\3V\3")
        buf.write("V\3W\3W\7W\u021e\nW\fW\16W\u0221\13W\3W\3W\3X\3X\3X\3")
        buf.write("X\7X\u0229\nX\fX\16X\u022c\13X\3Y\3Y\5Y\u0230\nY\3Y\3")
        buf.write("Y\3Y\7Y\u0235\nY\fY\16Y\u0238\13Y\3Z\3Z\3Z\3Z\7Z\u023e")
        buf.write("\nZ\fZ\16Z\u0241\13Z\3Z\3Z\3[\3[\3[\3[\7[\u0249\n[\f[")
        buf.write("\16[\u024c\13[\3[\3[\3[\5[\u0251\n[\3[\3[\3\\\3\\\3\\")
        buf.write("\4\u0215\u021f\2]\3\3\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23")
        buf.write("\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2")
        buf.write("/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\4C\5E\6G\7I\bK\t")
        buf.write("M\nO\13Q\fS\rU\16W\17Y\20[\21]\22_\23a\24c\25e\26g\27")
        buf.write("i\30k\31m\32o\33q\34s\35u\36w\37y {!}\"\177#\u0081$\u0083")
        buf.write("%\u0085&\u0087\'\u0089(\u008b)\u008d*\u008f+\u0091,\u0093")
        buf.write("-\u0095.\u0097/\u0099\60\u009b\61\u009d\62\u009f\63\u00a1")
        buf.write("\64\u00a3\65\u00a5\2\u00a7\66\u00a9\67\u00ab\2\u00ad\2")
        buf.write("\u00af\2\u00b18\u00b39\u00b5:\u00b7;\3\2%\4\2SSss\4\2")
        buf.write("YYyy\4\2GGgg\4\2TTtt\4\2VVvv\4\2[[{{\4\2WWww\4\2KKkk\4")
        buf.write("\2QQqq\4\2RRrr\4\2CCcc\4\2UUuu\4\2FFff\4\2HHhh\4\2IIi")
        buf.write("i\4\2JJjj\4\2LLll\4\2MMmm\4\2NNnn\4\2\\\\||\4\2ZZzz\4")
        buf.write("\2EEee\4\2XXxx\4\2DDdd\4\2PPpp\4\2OOoo\4\2C\\c|\3\2\62")
        buf.write(";\t\2$$))ddhhppttvv\n\2$$))^^ddhhppttvv\7\2\n\f\16\17")
        buf.write("$$))^^\4\2\f\f\17\17\5\2\13\f\17\17\"\"\6\2\n\f\16\17")
        buf.write("))^^\t\2))^^ddhhppttvv\2\u0251\2\3\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\3\u00b9\3\2\2\2\5\u00bc\3\2\2")
        buf.write("\2\7\u00be\3\2\2\2\t\u00c0\3\2\2\2\13\u00c2\3\2\2\2\r")
        buf.write("\u00c4\3\2\2\2\17\u00c6\3\2\2\2\21\u00c8\3\2\2\2\23\u00ca")
        buf.write("\3\2\2\2\25\u00cc\3\2\2\2\27\u00ce\3\2\2\2\31\u00d0\3")
        buf.write("\2\2\2\33\u00d2\3\2\2\2\35\u00d4\3\2\2\2\37\u00d6\3\2")
        buf.write("\2\2!\u00d8\3\2\2\2#\u00da\3\2\2\2%\u00dc\3\2\2\2\'\u00de")
        buf.write("\3\2\2\2)\u00e0\3\2\2\2+\u00e2\3\2\2\2-\u00e4\3\2\2\2")
        buf.write("/\u00e6\3\2\2\2\61\u00e8\3\2\2\2\63\u00ea\3\2\2\2\65\u00ec")
        buf.write("\3\2\2\2\67\u00ee\3\2\2\29\u00f0\3\2\2\2;\u00f2\3\2\2")
        buf.write("\2=\u00f4\3\2\2\2?\u00f6\3\2\2\2A\u00f9\3\2\2\2C\u0100")
        buf.write("\3\2\2\2E\u0106\3\2\2\2G\u010f\3\2\2\2I\u0113\3\2\2\2")
        buf.write("K\u0116\3\2\2\2M\u011d\3\2\2\2O\u0120\3\2\2\2Q\u0123\3")
        buf.write("\2\2\2S\u0128\3\2\2\2U\u012d\3\2\2\2W\u0133\3\2\2\2Y\u0138")
        buf.write("\3\2\2\2[\u013e\3\2\2\2]\u0142\3\2\2\2_\u014b\3\2\2\2")
        buf.write("a\u0155\3\2\2\2c\u0159\3\2\2\2e\u015f\3\2\2\2g\u0162\3")
        buf.write("\2\2\2i\u0167\3\2\2\2k\u016f\3\2\2\2m\u0177\3\2\2\2o\u017e")
        buf.write("\3\2\2\2q\u0180\3\2\2\2s\u0182\3\2\2\2u\u0186\3\2\2\2")
        buf.write("w\u0189\3\2\2\2y\u018c\3\2\2\2{\u018e\3\2\2\2}\u0191\3")
        buf.write("\2\2\2\177\u0195\3\2\2\2\u0081\u0197\3\2\2\2\u0083\u0199")
        buf.write("\3\2\2\2\u0085\u019d\3\2\2\2\u0087\u01a1\3\2\2\2\u0089")
        buf.write("\u01a3\3\2\2\2\u008b\u01a5\3\2\2\2\u008d\u01a8\3\2\2\2")
        buf.write("\u008f\u01aa\3\2\2\2\u0091\u01ac\3\2\2\2\u0093\u01ae\3")
        buf.write("\2\2\2\u0095\u01b0\3\2\2\2\u0097\u01b2\3\2\2\2\u0099\u01b4")
        buf.write("\3\2\2\2\u009b\u01b7\3\2\2\2\u009d\u01ba\3\2\2\2\u009f")
        buf.write("\u01db\3\2\2\2\u00a1\u01f4\3\2\2\2\u00a3\u01f6\3\2\2\2")
        buf.write("\u00a5\u0202\3\2\2\2\u00a7\u0204\3\2\2\2\u00a9\u020b\3")
        buf.write("\2\2\2\u00ab\u020f\3\2\2\2\u00ad\u021b\3\2\2\2\u00af\u0224")
        buf.write("\3\2\2\2\u00b1\u022f\3\2\2\2\u00b3\u0239\3\2\2\2\u00b5")
        buf.write("\u0244\3\2\2\2\u00b7\u0254\3\2\2\2\u00b9\u00ba\7<\2\2")
        buf.write("\u00ba\u00bb\7?\2\2\u00bb\4\3\2\2\2\u00bc\u00bd\t\2\2")
        buf.write("\2\u00bd\6\3\2\2\2\u00be\u00bf\t\3\2\2\u00bf\b\3\2\2\2")
        buf.write("\u00c0\u00c1\t\4\2\2\u00c1\n\3\2\2\2\u00c2\u00c3\t\5\2")
        buf.write("\2\u00c3\f\3\2\2\2\u00c4\u00c5\t\6\2\2\u00c5\16\3\2\2")
        buf.write("\2\u00c6\u00c7\t\7\2\2\u00c7\20\3\2\2\2\u00c8\u00c9\t")
        buf.write("\b\2\2\u00c9\22\3\2\2\2\u00ca\u00cb\t\t\2\2\u00cb\24\3")
        buf.write("\2\2\2\u00cc\u00cd\t\n\2\2\u00cd\26\3\2\2\2\u00ce\u00cf")
        buf.write("\t\13\2\2\u00cf\30\3\2\2\2\u00d0\u00d1\t\f\2\2\u00d1\32")
        buf.write("\3\2\2\2\u00d2\u00d3\t\r\2\2\u00d3\34\3\2\2\2\u00d4\u00d5")
        buf.write("\t\16\2\2\u00d5\36\3\2\2\2\u00d6\u00d7\t\17\2\2\u00d7")
        buf.write(" \3\2\2\2\u00d8\u00d9\t\20\2\2\u00d9\"\3\2\2\2\u00da\u00db")
        buf.write("\t\21\2\2\u00db$\3\2\2\2\u00dc\u00dd\t\22\2\2\u00dd&\3")
        buf.write("\2\2\2\u00de\u00df\t\23\2\2\u00df(\3\2\2\2\u00e0\u00e1")
        buf.write("\t\24\2\2\u00e1*\3\2\2\2\u00e2\u00e3\t\25\2\2\u00e3,\3")
        buf.write("\2\2\2\u00e4\u00e5\t\26\2\2\u00e5.\3\2\2\2\u00e6\u00e7")
        buf.write("\t\27\2\2\u00e7\60\3\2\2\2\u00e8\u00e9\t\30\2\2\u00e9")
        buf.write("\62\3\2\2\2\u00ea\u00eb\t\31\2\2\u00eb\64\3\2\2\2\u00ec")
        buf.write("\u00ed\t\32\2\2\u00ed\66\3\2\2\2\u00ee\u00ef\t\33\2\2")
        buf.write("\u00ef8\3\2\2\2\u00f0\u00f1\t\34\2\2\u00f1:\3\2\2\2\u00f2")
        buf.write("\u00f3\t\35\2\2\u00f3<\3\2\2\2\u00f4\u00f5\7a\2\2\u00f5")
        buf.write(">\3\2\2\2\u00f6\u00f7\7^\2\2\u00f7\u00f8\t\36\2\2\u00f8")
        buf.write("@\3\2\2\2\u00f9\u00fa\5\13\6\2\u00fa\u00fb\5\t\5\2\u00fb")
        buf.write("\u00fc\5\r\7\2\u00fc\u00fd\5\21\t\2\u00fd\u00fe\5\13\6")
        buf.write("\2\u00fe\u00ff\5\65\33\2\u00ffB\3\2\2\2\u0100\u0101\5")
        buf.write("\63\32\2\u0101\u0102\5\13\6\2\u0102\u0103\5\t\5\2\u0103")
        buf.write("\u0104\5\31\r\2\u0104\u0105\5\'\24\2\u0105D\3\2\2\2\u0106")
        buf.write("\u0107\5/\30\2\u0107\u0108\5\25\13\2\u0108\u0109\5\65")
        buf.write("\33\2\u0109\u010a\5\r\7\2\u010a\u010b\5\23\n\2\u010b\u010c")
        buf.write("\5\65\33\2\u010c\u010d\5\21\t\2\u010d\u010e\5\t\5\2\u010e")
        buf.write("F\3\2\2\2\u010f\u0110\5\37\20\2\u0110\u0111\5\25\13\2")
        buf.write("\u0111\u0112\5\13\6\2\u0112H\3\2\2\2\u0113\u0114\5\r\7")
        buf.write("\2\u0114\u0115\5\25\13\2\u0115J\3\2\2\2\u0116\u0117\5")
        buf.write("\35\17\2\u0117\u0118\5\25\13\2\u0118\u0119\5\7\4\2\u0119")
        buf.write("\u011a\5\65\33\2\u011a\u011b\5\r\7\2\u011b\u011c\5\25")
        buf.write("\13\2\u011cL\3\2\2\2\u011d\u011e\5\35\17\2\u011e\u011f")
        buf.write("\5\25\13\2\u011fN\3\2\2\2\u0120\u0121\5\23\n\2\u0121\u0122")
        buf.write("\5\37\20\2\u0122P\3\2\2\2\u0123\u0124\5\r\7\2\u0124\u0125")
        buf.write("\5#\22\2\u0125\u0126\5\t\5\2\u0126\u0127\5\65\33\2\u0127")
        buf.write("R\3\2\2\2\u0128\u0129\5\t\5\2\u0129\u012a\5)\25\2\u012a")
        buf.write("\u012b\5\33\16\2\u012b\u012c\5\t\5\2\u012cT\3\2\2\2\u012d")
        buf.write("\u012e\5\7\4\2\u012e\u012f\5#\22\2\u012f\u0130\5\23\n")
        buf.write("\2\u0130\u0131\5)\25\2\u0131\u0132\5\t\5\2\u0132V\3\2")
        buf.write("\2\2\u0133\u0134\5\7\4\2\u0134\u0135\5\23\n\2\u0135\u0136")
        buf.write("\5\r\7\2\u0136\u0137\5#\22\2\u0137X\3\2\2\2\u0138\u0139")
        buf.write("\5\63\32\2\u0139\u013a\5\t\5\2\u013a\u013b\5!\21\2\u013b")
        buf.write("\u013c\5\23\n\2\u013c\u013d\5\65\33\2\u013dZ\3\2\2\2\u013e")
        buf.write("\u013f\5\t\5\2\u013f\u0140\5\65\33\2\u0140\u0141\5\35")
        buf.write("\17\2\u0141\\\3\2\2\2\u0142\u0143\5\37\20\2\u0143\u0144")
        buf.write("\5\21\t\2\u0144\u0145\5\65\33\2\u0145\u0146\5/\30\2\u0146")
        buf.write("\u0147\5\r\7\2\u0147\u0148\5\23\n\2\u0148\u0149\5\25\13")
        buf.write("\2\u0149\u014a\5\65\33\2\u014a^\3\2\2\2\u014b\u014c\5")
        buf.write("\27\f\2\u014c\u014d\5\13\6\2\u014d\u014e\5\25\13\2\u014e")
        buf.write("\u014f\5/\30\2\u014f\u0150\5\t\5\2\u0150\u0151\5\35\17")
        buf.write("\2\u0151\u0152\5\21\t\2\u0152\u0153\5\13\6\2\u0153\u0154")
        buf.write("\5\t\5\2\u0154`\3\2\2\2\u0155\u0156\5\61\31\2\u0156\u0157")
        buf.write("\5\31\r\2\u0157\u0158\5\13\6\2\u0158b\3\2\2\2\u0159\u015a")
        buf.write("\5\31\r\2\u015a\u015b\5\13\6\2\u015b\u015c\5\13\6\2\u015c")
        buf.write("\u015d\5\31\r\2\u015d\u015e\5\17\b\2\u015ed\3\2\2\2\u015f")
        buf.write("\u0160\5\25\13\2\u0160\u0161\5\37\20\2\u0161f\3\2\2\2")
        buf.write("\u0162\u0163\5\13\6\2\u0163\u0164\5\t\5\2\u0164\u0165")
        buf.write("\5\31\r\2\u0165\u0166\5)\25\2\u0166h\3\2\2\2\u0167\u0168")
        buf.write("\5\63\32\2\u0168\u0169\5\25\13\2\u0169\u016a\5\25\13\2")
        buf.write("\u016a\u016b\5)\25\2\u016b\u016c\5\t\5\2\u016c\u016d\5")
        buf.write("\31\r\2\u016d\u016e\5\65\33\2\u016ej\3\2\2\2\u016f\u0170")
        buf.write("\5\23\n\2\u0170\u0171\5\65\33\2\u0171\u0172\5\r\7\2\u0172")
        buf.write("\u0173\5\t\5\2\u0173\u0174\5!\21\2\u0174\u0175\5\t\5\2")
        buf.write("\u0175\u0176\5\13\6\2\u0176l\3\2\2\2\u0177\u0178\5\33")
        buf.write("\16\2\u0178\u0179\5\r\7\2\u0179\u017a\5\13\6\2\u017a\u017b")
        buf.write("\5\23\n\2\u017b\u017c\5\65\33\2\u017c\u017d\5!\21\2\u017d")
        buf.write("n\3\2\2\2\u017e\u017f\7-\2\2\u017fp\3\2\2\2\u0180\u0181")
        buf.write("\7,\2\2\u0181r\3\2\2\2\u0182\u0183\5\65\33\2\u0183\u0184")
        buf.write("\5\25\13\2\u0184\u0185\5\r\7\2\u0185t\3\2\2\2\u0186\u0187")
        buf.write("\5\25\13\2\u0187\u0188\5\13\6\2\u0188v\3\2\2\2\u0189\u018a")
        buf.write("\7>\2\2\u018a\u018b\7@\2\2\u018bx\3\2\2\2\u018c\u018d")
        buf.write("\7>\2\2\u018dz\3\2\2\2\u018e\u018f\7>\2\2\u018f\u0190")
        buf.write("\7?\2\2\u0190|\3\2\2\2\u0191\u0192\5\35\17\2\u0192\u0193")
        buf.write("\5\23\n\2\u0193\u0194\5\61\31\2\u0194~\3\2\2\2\u0195\u0196")
        buf.write("\7/\2\2\u0196\u0080\3\2\2\2\u0197\u0198\7\61\2\2\u0198")
        buf.write("\u0082\3\2\2\2\u0199\u019a\5\67\34\2\u019a\u019b\5\25")
        buf.write("\13\2\u019b\u019c\5\35\17\2\u019c\u0084\3\2\2\2\u019d")
        buf.write("\u019e\5\31\r\2\u019e\u019f\5\65\33\2\u019f\u01a0\5\35")
        buf.write("\17\2\u01a0\u0086\3\2\2\2\u01a1\u01a2\7?\2\2\u01a2\u0088")
        buf.write("\3\2\2\2\u01a3\u01a4\7@\2\2\u01a4\u008a\3\2\2\2\u01a5")
        buf.write("\u01a6\7@\2\2\u01a6\u01a7\7?\2\2\u01a7\u008c\3\2\2\2\u01a8")
        buf.write("\u01a9\7]\2\2\u01a9\u008e\3\2\2\2\u01aa\u01ab\7_\2\2\u01ab")
        buf.write("\u0090\3\2\2\2\u01ac\u01ad\7<\2\2\u01ad\u0092\3\2\2\2")
        buf.write("\u01ae\u01af\7*\2\2\u01af\u0094\3\2\2\2\u01b0\u01b1\7")
        buf.write("+\2\2\u01b1\u0096\3\2\2\2\u01b2\u01b3\7=\2\2\u01b3\u0098")
        buf.write("\3\2\2\2\u01b4\u01b5\7\60\2\2\u01b5\u01b6\7\60\2\2\u01b6")
        buf.write("\u009a\3\2\2\2\u01b7\u01b8\7.\2\2\u01b8\u009c\3\2\2\2")
        buf.write("\u01b9\u01bb\t\35\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u009e\3\2\2\2\u01be\u01c0\5;\36\2\u01bf\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\7\60\2\2\u01c4")
        buf.write("\u01dc\3\2\2\2\u01c5\u01c7\7\60\2\2\u01c6\u01c8\5;\36")
        buf.write("\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01dc\3\2\2\2\u01cb")
        buf.write("\u01cd\5;\36\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01d0\u01d2\7\60\2\2\u01d1\u01d3\5;\36\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5\u01dc\3\2\2\2\u01d6\u01d8\5")
        buf.write(";\36\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db")
        buf.write("\u01bf\3\2\2\2\u01db\u01c5\3\2\2\2\u01db\u01cc\3\2\2\2")
        buf.write("\u01db\u01d7\3\2\2\2\u01dc\u01e7\3\2\2\2\u01dd\u01df\5")
        buf.write("\t\5\2\u01de\u01e0\7/\2\2\u01df\u01de\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e4\3\2\2\2\u01e1\u01e3\5;\36\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e5\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3")
        buf.write("\2\2\2\u01e7\u01dd\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u00a0")
        buf.write("\3\2\2\2\u01e9\u01ea\5\r\7\2\u01ea\u01eb\5\13\6\2\u01eb")
        buf.write("\u01ec\5\21\t\2\u01ec\u01ed\5\t\5\2\u01ed\u01f5\3\2\2")
        buf.write("\2\u01ee\u01ef\5\37\20\2\u01ef\u01f0\5\31\r\2\u01f0\u01f1")
        buf.write("\5)\25\2\u01f1\u01f2\5\33\16\2\u01f2\u01f3\5\t\5\2\u01f3")
        buf.write("\u01f5\3\2\2\2\u01f4\u01e9\3\2\2\2\u01f4\u01ee\3\2\2\2")
        buf.write("\u01f5\u00a2\3\2\2\2\u01f6\u01fc\7$\2\2\u01f7\u01f8\7")
        buf.write("^\2\2\u01f8\u01fb\t\37\2\2\u01f9\u01fb\n \2\2\u01fa\u01f7")
        buf.write("\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc")
        buf.write("\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2")
        buf.write("\u01fe\u01fc\3\2\2\2\u01ff\u0200\7$\2\2\u0200\u0201\b")
        buf.write("R\2\2\u0201\u00a4\3\2\2\2\u0202\u0203\t!\2\2\u0203\u00a6")
        buf.write("\3\2\2\2\u0204\u0205\t\"\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("\u0207\bT\3\2\u0207\u00a8\3\2\2\2\u0208\u020c\5\u00ab")
        buf.write("V\2\u0209\u020c\5\u00adW\2\u020a\u020c\5\u00afX\2\u020b")
        buf.write("\u0208\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020a\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u020e\bU\3\2\u020e\u00aa\3")
        buf.write("\2\2\2\u020f\u0210\7*\2\2\u0210\u0211\7,\2\2\u0211\u0215")
        buf.write("\3\2\2\2\u0212\u0214\13\2\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0216\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219\7")
        buf.write(",\2\2\u0219\u021a\7+\2\2\u021a\u00ac\3\2\2\2\u021b\u021f")
        buf.write("\7}\2\2\u021c\u021e\13\2\2\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("\u0221\3\2\2\2\u021f\u0220\3\2\2\2\u021f\u021d\3\2\2\2")
        buf.write("\u0220\u0222\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0223\7")
        buf.write("\177\2\2\u0223\u00ae\3\2\2\2\u0224\u0225\7\61\2\2\u0225")
        buf.write("\u0226\7\61\2\2\u0226\u022a\3\2\2\2\u0227\u0229\n!\2\2")
        buf.write("\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3")
        buf.write("\2\2\2\u022a\u022b\3\2\2\2\u022b\u00b0\3\2\2\2\u022c\u022a")
        buf.write("\3\2\2\2\u022d\u0230\5=\37\2\u022e\u0230\59\35\2\u022f")
        buf.write("\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230\u0236\3\2\2\2")
        buf.write("\u0231\u0235\5=\37\2\u0232\u0235\59\35\2\u0233\u0235\5")
        buf.write(";\36\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0237\u00b2\3\2\2\2\u0238\u0236\3\2\2\2")
        buf.write("\u0239\u023f\7$\2\2\u023a\u023b\7^\2\2\u023b\u023e\t\37")
        buf.write("\2\2\u023c\u023e\n \2\2\u023d\u023a\3\2\2\2\u023d\u023c")
        buf.write("\3\2\2\2\u023e\u0241\3\2\2\2\u023f\u023d\3\2\2\2\u023f")
        buf.write("\u0240\3\2\2\2\u0240\u0242\3\2\2\2\u0241\u023f\3\2\2\2")
        buf.write("\u0242\u0243\bZ\4\2\u0243\u00b4\3\2\2\2\u0244\u024a\7")
        buf.write("$\2\2\u0245\u0249\n \2\2\u0246\u0247\7^\2\2\u0247\u0249")
        buf.write("\t\37\2\2\u0248\u0245\3\2\2\2\u0248\u0246\3\2\2\2\u0249")
        buf.write("\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2")
        buf.write("\u024b\u0250\3\2\2\2\u024c\u024a\3\2\2\2\u024d\u0251\t")
        buf.write("#\2\2\u024e\u024f\7^\2\2\u024f\u0251\n$\2\2\u0250\u024d")
        buf.write("\3\2\2\2\u0250\u024e\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u0253\b[\5\2\u0253\u00b6\3\2\2\2\u0254\u0255\13\2\2\2")
        buf.write("\u0255\u0256\b\\\6\2\u0256\u00b8\3\2\2\2\34\2\u01bc\u01c1")
        buf.write("\u01c9\u01ce\u01d4\u01d9\u01db\u01df\u01e4\u01e7\u01f4")
        buf.write("\u01fa\u01fc\u020b\u0215\u021f\u022a\u022f\u0234\u0236")
        buf.write("\u023d\u023f\u0248\u024a\u0250\7\3R\2\b\2\2\3Z\3\3[\4")
        buf.write("\3\\\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    RETURN_KEY = 2
    BREAK_KEY = 3
    CONTINUE_KEY = 4
    FOR_KEY = 5
    TO_KEY = 6
    DOWNTO_KEY = 7
    DO_KEY = 8
    IF_KEY = 9
    THEN_KEY = 10
    ELSE_KEY = 11
    WHILE_KEY = 12
    WITH_KEY = 13
    BEGIN_KEY = 14
    END_KEY = 15
    FUNCTION_KEY = 16
    PROCEDURE_KEY = 17
    VAR_KEY = 18
    ARRAY_TYPE = 19
    OF_KEY = 20
    REAL_TYPE = 21
    BOOLEAN_TYPE = 22
    INTEGER_TYPE = 23
    STRING_TYPE = 24
    ADD_OP = 25
    MUL_OP = 26
    NOT_OP = 27
    OR_OP = 28
    NOTEQ_OP = 29
    LESS_OP = 30
    LESSEQ_OP = 31
    INT_DIV_OP = 32
    SUB_OP = 33
    DIV_OP = 34
    MOD_OP = 35
    AND_OP = 36
    EQ_OP = 37
    GREAT_OP = 38
    GREAT_EQ_OP = 39
    L_SQUARE_SEP = 40
    R_SQUARE_SEP = 41
    COLON = 42
    LB = 43
    RB = 44
    SEMI = 45
    DOUBLE_DOT_SEP = 46
    COMMA = 47
    INT_LIT = 48
    FLOAT_LIT = 49
    BOOLEAN_LIT = 50
    STRING_LIT = 51
    WS = 52
    COMMENT = 53
    ID = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", 
            "'>'", "'>='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "RETURN_KEY", "BREAK_KEY", "CONTINUE_KEY", "FOR_KEY", "TO_KEY", 
            "DOWNTO_KEY", "DO_KEY", "IF_KEY", "THEN_KEY", "ELSE_KEY", "WHILE_KEY", 
            "WITH_KEY", "BEGIN_KEY", "END_KEY", "FUNCTION_KEY", "PROCEDURE_KEY", 
            "VAR_KEY", "ARRAY_TYPE", "OF_KEY", "REAL_TYPE", "BOOLEAN_TYPE", 
            "INTEGER_TYPE", "STRING_TYPE", "ADD_OP", "MUL_OP", "NOT_OP", 
            "OR_OP", "NOTEQ_OP", "LESS_OP", "LESSEQ_OP", "INT_DIV_OP", "SUB_OP", 
            "DIV_OP", "MOD_OP", "AND_OP", "EQ_OP", "GREAT_OP", "GREAT_EQ_OP", 
            "L_SQUARE_SEP", "R_SQUARE_SEP", "COLON", "LB", "RB", "SEMI", 
            "DOUBLE_DOT_SEP", "COMMA", "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
            "STRING_LIT", "WS", "COMMENT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", 
                  "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", 
                  "C", "V", "B", "N", "M", "LETTER", "DIGIT", "UNDER_SCORE", 
                  "STRING_ESC", "RETURN_KEY", "BREAK_KEY", "CONTINUE_KEY", 
                  "FOR_KEY", "TO_KEY", "DOWNTO_KEY", "DO_KEY", "IF_KEY", 
                  "THEN_KEY", "ELSE_KEY", "WHILE_KEY", "WITH_KEY", "BEGIN_KEY", 
                  "END_KEY", "FUNCTION_KEY", "PROCEDURE_KEY", "VAR_KEY", 
                  "ARRAY_TYPE", "OF_KEY", "REAL_TYPE", "BOOLEAN_TYPE", "INTEGER_TYPE", 
                  "STRING_TYPE", "ADD_OP", "MUL_OP", "NOT_OP", "OR_OP", 
                  "NOTEQ_OP", "LESS_OP", "LESSEQ_OP", "INT_DIV_OP", "SUB_OP", 
                  "DIV_OP", "MOD_OP", "AND_OP", "EQ_OP", "GREAT_OP", "GREAT_EQ_OP", 
                  "L_SQUARE_SEP", "R_SQUARE_SEP", "COLON", "LB", "RB", "SEMI", 
                  "DOUBLE_DOT_SEP", "COMMA", "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                  "STRING_LIT", "ENDLINE", "WS", "COMMENT", "TRA_BLOCK_COMMENT", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "ID", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[80] = self.STRING_LIT_action 
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:len(self.text) - 1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


