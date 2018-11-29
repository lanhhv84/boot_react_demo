.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static z [F

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
	ldc 4
	newarray float
	putstatic MPClass/z [F
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	getstatic MPClass/z [F
	iconst_0
	iconst_0
	isub
	ineg
	bipush 10
	i2f
	fastore
	bipush 20
	istore_1
	getstatic MPClass/z [F
	iconst_0
	iconst_1
	isub
	ineg
	getstatic MPClass/z [F
	iconst_0
	iconst_0
	isub
	ineg
	faload
	iload_1
	i2f
	fmul
	iconst_2
	i2f
	fmul
	iconst_3
	iload_1
	imul
	i2f
	fsub
	getstatic MPClass/z [F
	iconst_0
	iconst_0
	isub
	ineg
	faload
	fadd
	fastore
	getstatic MPClass/z [F
	iconst_0
	iconst_1
	isub
	ineg
	faload
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/bar()V
Label1:
	return
.limit stack 15
.limit locals 2
.end method

.method public static bar()V
Label0:
	getstatic MPClass/z [F
	iconst_0
	iconst_1
	isub
	ineg
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 4
.limit locals 0
.end method
