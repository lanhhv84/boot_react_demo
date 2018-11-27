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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	ldc 10
	newarray int
	astore_1
Label0:
	aload_1
	iconst_1
	iconst_2
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method
