;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Thu Nov 29 07:27:54 ICT 2018

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
.limit stack 1
.limit locals 2
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label1 to Label1

Label0:
.line 5
	iconst_3
	invokestatic com/hvlpr/Main/foo(I)I
	istore_1
Label1:
.line 6
	return

.end method

.method public static foo(I)I
.limit stack 2
.limit locals 1
.var 0 is a I from Label1 to Label2

Label1:
.line 8
	iload_0
	iconst_1
	if_icmple Label0
.line 9
	iconst_1
	ireturn
Label0:
.line 12
	iconst_0
Label2:
	ireturn

.end method
