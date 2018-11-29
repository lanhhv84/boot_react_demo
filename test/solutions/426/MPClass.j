.source MPClass.java
.class public MPClass
.super java.lang.Object


.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	iconst_5
	istore_1
	bipush 9
	istore_2
	iload_1
	iload_2
	invokestatic MPClass/sum(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static sum(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method
