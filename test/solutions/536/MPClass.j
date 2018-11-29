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
	newarray float
	astore_1
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	bipush 10
	i2f
	fastore
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	faload
	bipush 10
	i2f
	fmul
	iconst_2
	i2f
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	faload
	fmul
	fsub
	bipush 100
	i2f
	fadd
	fastore
	aload_1
	iconst_0
	iconst_2
	isub
	ineg
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	faload
	iconst_2
	i2f
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	faload
	fmul
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	faload
	fdiv
	fsub
	fastore
	aload_1
	iconst_0
	iconst_2
	isub
	ineg
	faload
	invokestatic io/putFloatLn(F)V
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 47
.limit locals 2
.end method
