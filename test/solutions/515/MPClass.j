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
	newarray boolean
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is z Z from Label0 to Label1
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	iconst_0
	bastore
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	iconst_1
	bastore
	aload_1
	iconst_0
	iconst_2
	isub
	ineg
	bipush 10
	bipush 12
	bipush 100
	isub
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	aload_1
	iconst_0
	iconst_1
	isub
	ineg
	baload
	iand
	bastore
	aload_1
	iconst_0
	iconst_2
	isub
	ineg
	baload
	istore_3
	iconst_0
	istore_2
Label6:
	iload_2
	iconst_2
	if_icmpgt Label5
	aload_1
	iconst_0
	iload_2
	isub
	ineg
	baload
	invokestatic io/putBoolLn(Z)V
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
	iload_3
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 37
.limit locals 4
.end method
