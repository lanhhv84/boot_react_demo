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
	ldc 3
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	bipush 100
	iastore
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	sipush 200
	iastore
	aload_1
	invokestatic MPClass/swap([I)V
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 22
.limit locals 2
.end method

.method public static swap([I)V
Label0:
.var 1 is temp I from Label0 to Label1
	aload_0
	iconst_0
	iconst_1
	isub
	ineg
	iaload
	istore_1
	aload_0
	iconst_0
	iconst_1
	isub
	ineg
	aload_0
	iconst_0
	iconst_0
	isub
	ineg
	iaload
	iastore
	aload_0
	iconst_0
	iconst_0
	isub
	ineg
	iload_1
	iastore
Label1:
	return
.limit stack 25
.limit locals 2
.end method
