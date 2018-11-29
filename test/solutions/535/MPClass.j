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
	ldc 11
	newarray int
	astore_1
.var 2 is y I from Label0 to Label1
	iconst_3
	ineg
	invokestatic MPClass/foo(I)[I
	astore_1
	aload_1
	iconst_5
	ineg
	iconst_3
	ineg
	isub
	ineg
	iaload
	invokestatic io/putIntLn(I)V
	bipush 12
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 8
.limit locals 3
.end method

.method public static foo(I)[I
.var 0 is x I from Label0 to Label1
Label0:
	ldc 11
	newarray int
	astore_1
	aload_1
	iconst_5
	ineg
	iconst_3
	ineg
	isub
	ineg
	bipush 10
	iastore
	aload_1
	iconst_5
	ineg
	iload_0
	isub
	ineg
	aload_1
	iconst_5
	ineg
	iload_0
	isub
	ineg
	iaload
	iload_0
	iload_0
	imul
	iadd
	iastore
	aload_1
	iconst_5
	ineg
	iconst_3
	ineg
	isub
	ineg
	iaload
	invokestatic io/putIntLn(I)V
	aload_1
	goto Label1
Label1:
	areturn
.limit stack 22
.limit locals 2
.end method
