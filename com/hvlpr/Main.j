;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Nov 27 16:52:14 ICT 2018

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
.limit locals 3
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label2 to Label1
.var 2 is b F from Label4 to Label1

Label0:
.line 5
	iconst_1
	istore_1
Label2:
.line 6
	fconst_2
	fstore_2
Label4:
.line 7
	iload_1
	i2f
	fload_2
	fadd
	fstore_2
Label1:
.line 8
	return

.end method

.method public static foo([FFZ)I
.limit stack 1
.limit locals 3
.var 0 is x [F from Label0 to Label1
.var 1 is y F from Label0 to Label1
.var 2 is m Z from Label0 to Label1

Label0:
.line 11
	iconst_1
Label1:
	ireturn

.end method
