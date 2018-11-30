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
	ldc 4
	newarray int
	astore_3
	aload_3
	bipush 99
	bipush 99
	isub
	ineg
	bipush 123
	iastore
	aload_3
	bipush 99
	bipush 99
	isub
	ineg
	iaload
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
	aload_3
	bipush 99
	bipush 99
	isub
	ineg
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 13
.limit locals 4
.end method
