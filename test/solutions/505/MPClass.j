.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static x I
.field static z [I

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
	newarray int
	putstatic MPClass/z [I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	putstatic MPClass/x I
	invokestatic MPClass/foo()V
	getstatic MPClass/z [I
	iconst_0
	iconst_2
	isub
	ineg
	iaload
	invokestatic io/putIntLn(I)V
	getstatic MPClass/x I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static foo()V
Label0:
	getstatic MPClass/z [I
	iconst_0
	iconst_2
	isub
	ineg
	bipush 100
	iastore
Label1:
	return
.limit stack 7
.limit locals 0
.end method
