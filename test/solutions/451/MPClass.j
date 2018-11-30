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
	ldc 5
	newarray int
	astore_1
	aload_1
	iconst_1
	iconst_2
	isub
	ineg
	iconst_3
	iastore
	aload_1
	iconst_1
	iconst_2
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
	goto Label1
Label1:
	return
.limit stack 9
.limit locals 2
.end method
