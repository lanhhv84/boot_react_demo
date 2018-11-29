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
.var 1 is i I from Label0 to Label1
.var 2 is max I from Label0 to Label1
	ldc 11
	newarray int
	astore_3
	aload_3
	iconst_0
	iconst_0
	isub
	ineg
	bipush 9
	iastore
	aload_3
	iconst_0
	iconst_1
	isub
	ineg
	iconst_3
	iastore
	aload_3
	iconst_0
	iconst_2
	isub
	ineg
	bipush 12
	iastore
	aload_3
	iconst_0
	iconst_3
	isub
	ineg
	bipush 7
	iastore
	aload_3
	iconst_0
	iconst_4
	isub
	ineg
	bipush 43
	iastore
	aload_3
	iconst_0
	iconst_5
	isub
	ineg
	bipush 32
	iastore
	aload_3
	iconst_0
	bipush 6
	isub
	ineg
	bipush 17
	iastore
	aload_3
	iconst_0
	bipush 7
	isub
	ineg
	iconst_4
	iastore
	aload_3
	iconst_0
	bipush 8
	isub
	ineg
	iconst_2
	ineg
	iastore
	aload_3
	iconst_0
	bipush 9
	isub
	ineg
	bipush 12
	iastore
	aload_3
	iconst_0
	bipush 10
	isub
	ineg
	bipush 9
	iastore
	aload_3
	iconst_0
	iconst_0
	isub
	ineg
	iaload
	istore_2
	iconst_1
	istore_1
Label8:
	iload_1
	bipush 10
	if_icmpgt Label3
	aload_3
	iconst_0
	iload_1
	isub
	ineg
	iaload
	iload_2
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	aload_3
	iconst_0
	iload_1
	isub
	ineg
	iaload
	istore_2
	goto Label7
Label6:
Label7:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label3:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 85
.limit locals 4
.end method
