;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Nov 27 17:00:23 ICT 2018

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
.limit locals 1
.var 0 is args [Ljava/lang/String; from Label0 to Label1

Label0:
.line 5
	getstatic java.lang.System.out Ljava/io/PrintStream;
	invokestatic com/hvlpr/Main/arrret()I
	invokevirtual java/io/PrintStream/println(I)V
Label1:
.line 6
	return

.end method

.method public static arrret()I
.limit stack 2
.limit locals 1
.var 0 is i I from Label1 to Label3

.line 9
	iconst_1
	istore_0
Label1:
	iload_0
	bipush 10
	if_icmpge Label0
	iinc 0 1
	goto Label1
Label0:
.line 12
	iload_0
Label3:
	ireturn

.end method
