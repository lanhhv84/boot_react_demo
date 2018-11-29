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
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
	ldc 101
	newarray int
	astore_3
	bipush 6
	istore_1
	aload_3
	iconst_0
	iconst_1
	isub
	ineg
	bipush 12
	iastore
	iload_1
	aload_3
	iconst_0
	iconst_1
	isub
	ineg
	iaload
	iadd
	iload_1
	iconst_2
	imul
	aload_3
	iconst_0
	iconst_1
	isub
	ineg
	iaload
	iadd
	invokestatic MPClass/gcd(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 18
.limit locals 4
.end method

.method public static gcd(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	goto Label1
	goto Label5
Label4:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MPClass/gcd(II)I
	goto Label1
Label5:
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method
