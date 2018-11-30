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
.var 2 is b I from Label0 to Label1
	ldc 2
	newarray int
	astore_3
	aload_3
	iconst_1
	iconst_1
	isub
	ineg
	bipush 69
	iastore
	bipush 69
	invokestatic io/putInt(I)V
	bipush 69
	invokestatic MPClass/returnArray(I)V
Label1:
	return
.limit stack 9
.limit locals 4
.end method

.method public static returnArray(I)V
.var 0 is a69 I from Label0 to Label1
Label0:
	bipush 69
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
