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
	ldc 2
	newarray float
	astore_1
.var 2 is a I from Label0 to Label1
	aload_1
	iconst_1
	iconst_2
	isub
	ineg
	ldc 8.45
	fastore
	bipush 9
	istore_2
	aload_1
	iconst_1
	iconst_1
	isub
	ineg
	iload_2
	i2f
	invokestatic MPClass/foo(F)F
	fastore
	aload_1
	iconst_1
	iconst_1
	isub
	ineg
	faload
	aload_1
	iconst_1
	iconst_2
	isub
	ineg
	faload
	fadd
	invokestatic io/putFloatLn(F)V
	iconst_1
	invokestatic io/putBoolLn(Z)V
	iconst_1
	invokestatic io/putIntLn(I)V
	ldc "ahihi"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 23
.limit locals 3
.end method

.method public static foo(F)F
.var 0 is a F from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	bipush 10
	istore_1
	fload_0
	iload_1
	i2f
	fadd
	goto Label1
Label1:
	freturn
.limit stack 3
.limit locals 2
.end method
