.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static z I

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
	ldc 3
	newarray float
	astore_1
.var 2 is e I from Label0 to Label1
.var 3 is x F from Label0 to Label1
	bipush 12
	istore_2
	bipush 12
	bipush 100
	imul
	iload_2
	isub
	i2f
	fstore_3
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	iload_2
	i2f
	fload_3
	fmul
	sipush 200
	i2f
	fsub
	fastore
	bipush 122
	iconst_2
	imul
	putstatic MPClass/z I
	getstatic MPClass/z I
	i2f
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 12
.limit locals 4
.end method
