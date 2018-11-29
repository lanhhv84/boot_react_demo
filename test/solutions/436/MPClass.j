.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static hxhx [I

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
	ldc 10
	newarray int
	putstatic MPClass/hxhx [I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass/hxhx [I
	iconst_1
	iconst_3
	isub
	ineg
	bipush 10
	iastore
	getstatic MPClass/hxhx [I
	iconst_1
	iconst_3
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
.limit locals 1
.end method
