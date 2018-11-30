.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static a [I
.field static b [F

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
	ldc 3
	newarray int
	putstatic MPClass/a [I
	ldc 3
	newarray float
	putstatic MPClass/b [F
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass/a [I
	iconst_1
	ineg
	iconst_0
	isub
	ineg
	iconst_1
	iastore
	getstatic MPClass/b [F
	iconst_3
	iconst_4
	isub
	ineg
	ldc 2.0
	fastore
	getstatic MPClass/a [I
	iconst_1
	ineg
	iconst_0
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/b [F
	iconst_3
	iconst_4
	isub
	ineg
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 8
.limit locals 1
.end method
