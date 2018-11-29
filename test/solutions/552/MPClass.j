.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static f [F

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
	ldc 20
	newarray float
	putstatic MPClass/f [F
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 10
	newarray int
	astore_1
.var 2 is b I from Label0 to Label1
	aload_1
	bipush 10
	bipush 12
	isub
	ineg
	bipush 6
	iastore
	aload_1
	bipush 10
	bipush 12
	isub
	ineg
	iaload
	bipush 12
	iadd
	invokestatic io/putInt(I)V
	getstatic MPClass/f [F
	iconst_1
	iconst_3
	isub
	ineg
	ldc 3.5
	fastore
	getstatic MPClass/f [F
	iconst_1
	iconst_3
	isub
	ineg
	faload
	ldc 4.5
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 17
.limit locals 3
.end method
