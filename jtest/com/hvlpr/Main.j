;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Fri Nov 30 08:11:10 ICT 2018

.source Main.java
.class public com/hvlpr/Main
.super java/lang/Object


.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this Lcom/hvlpr/Main; from Label0 to Label1

Label0:
.line 2
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 2
.limit locals 2
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label2 to Label1

Label0:
.line 5
	ldc 2147483647
	istore_1
Label2:
.line 6
	getstatic java.lang.System.out Ljava/io/PrintStream;
	iload_1
	invokevirtual java/io/PrintStream/println(I)V
Label1:
.line 7
	return

.end method
