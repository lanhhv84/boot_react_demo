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
	ldc 101
	newarray int
	astore_1
.var 2 is i I from Label0 to Label1
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	iconst_1
	iastore
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	iconst_2
	iastore
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
	iaload
	iconst_2
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	iaload
	imul
	isub
	bipush 100
	isub
	iastore
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_2
	if_icmpgt Label3
	aload_1
	iconst_0
	iload_2
	isub
	ineg
	iaload
	invokestatic io/putIntLn(I)V
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 33
.limit locals 3
.end method
