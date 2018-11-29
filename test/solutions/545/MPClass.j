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
	ldc 20
	newarray float
	astore_1
	aload_1
	iconst_1
	iconst_5
	isub
	ineg
	bipush 100
	i2f
	fastore
	aload_1
	invokestatic MPClass/foo([F)V
	aload_1
	iconst_1
	iconst_5
	isub
	ineg
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 12
.limit locals 2
.end method

.method public static foo([F)V
Label0:
	aload_0
	iconst_1
	iconst_5
	isub
	ineg
	sipush 200
	i2f
	fastore
	aload_0
	iconst_1
	iconst_5
	isub
	ineg
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 11
.limit locals 1
.end method
