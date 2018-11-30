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
.var 3 is c I from Label0 to Label1
.var 4 is d I from Label0 to Label1
.var 5 is e F from Label0 to Label1
	ldc 2147483647
	ineg
	istore_1
	ldc 2147483647
	istore_2
	bipush 100
	istore_3
	bipush 100
	istore 4
	bipush 100
	i2f
	fstore 5
	iload_1
	iload_2
	iadd
	i2f
	invokestatic io/putFloat(F)V
	iload_1
	i2f
	iload_2
	i2f
	fdiv
	invokestatic io/putFloat(F)V
	iload_1
	iload_2
	idiv
	invokestatic io/putInt(I)V
	iload_3
	i2f
	invokestatic io/putFloat(F)V
	iload 4
	i2f
	invokestatic io/putFloat(F)V
	fload 5
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 7
.limit locals 6
.end method
