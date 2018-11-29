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
.var 2 is b F from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	invokestatic MPClass/foo(I)[F
	iconst_1
	iconst_5
	isub
	ineg
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static foo(I)[F
.var 0 is a I from Label0 to Label1
Label0:
	ldc 10
	newarray float
	astore_1
	aload_1
	iconst_1
	iconst_5
	isub
	ineg
	ldc 10.5
	fastore
	iload_0
	i2f
	aload_1
	iconst_1
	iconst_5
	isub
	ineg
	faload
	fadd
	invokestatic io/putFloat(F)V
	aload_1
	goto Label1
Label1:
	areturn
.limit stack 12
.limit locals 2
.end method
