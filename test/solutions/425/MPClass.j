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
	ldc 4
	newarray int
	astore_1
.var 2 is ind I from Label0 to Label1
	bipush 101
	istore_2
	aload_1
	bipush 99
	iload_2
	isub
	ineg
	bipush 69
	iastore
	aload_1
	iload_2
	invokestatic MPClass/main2([II)V
Label1:
	return
.limit stack 10
.limit locals 3
.end method

.method public static main2([II)V
.var 0 is arr [I from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is arr_copy [I from Label0 to Label1
	iconst_4
	newarray int
	astore_2
	aload_0
	aload_2
	bipush 99
	bipush 99
	isub
	ineg
	aload_0
	bipush 99
	bipush 99
	isub
	ineg
	iaload
	iastore
	aload_0
	aload_2
	bipush 99
	bipush 100
	isub
	ineg
	aload_0
	bipush 99
	bipush 100
	isub
	ineg
	iaload
	iastore
	aload_0
	aload_2
	bipush 99
	bipush 101
	isub
	ineg
	aload_0
	bipush 99
	bipush 101
	isub
	ineg
	iaload
	iastore
	aload_0
	aload_2
	bipush 99
	bipush 102
	isub
	ineg
	aload_0
	bipush 99
	bipush 102
	isub
	ineg
	iaload
	iastore
Label0:
	aload_2
	bipush 99
	iload_1
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 20
.limit locals 3
.end method
