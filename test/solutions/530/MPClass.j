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
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
.var 4 is temp I from Label0 to Label1
	invokestatic MPClass/bbsort()V
Label1:
	return
.limit stack 1
.limit locals 5
.end method

.method public static bbsort()V
Label0:
.var 0 is n I from Label0 to Label1
.var 1 is temp I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	ldc 5
	newarray int
	astore 4
	iconst_5
	istore_0
	aload 4
	iconst_0
	iconst_0
	isub
	ineg
	iconst_5
	iastore
	aload 4
	iconst_0
	iconst_1
	isub
	ineg
	iconst_2
	iastore
	aload 4
	iconst_0
	iconst_2
	isub
	ineg
	bipush 8
	iastore
	aload 4
	iconst_0
	iconst_3
	isub
	ineg
	bipush 9
	iastore
	aload 4
	iconst_0
	iconst_4
	isub
	ineg
	iconst_1
	iastore
	iconst_0
	istore_2
Label11:
	iload_2
	iload_0
	iconst_2
	isub
	if_icmpgt Label3
	iconst_0
	istore_3
Label10:
	iload_3
	iload_0
	iload_2
	isub
	iconst_2
	isub
	if_icmpgt Label5
	aload 4
	iconst_0
	iload_3
	isub
	ineg
	iaload
	aload 4
	iconst_0
	iload_3
	iconst_1
	iadd
	isub
	ineg
	iaload
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	aload 4
	iconst_0
	iload_3
	isub
	ineg
	iaload
	istore_1
	aload 4
	iconst_0
	iload_3
	isub
	ineg
	aload 4
	iconst_0
	iload_3
	iconst_1
	iadd
	isub
	ineg
	iaload
	iastore
	aload 4
	iconst_0
	iload_3
	iconst_1
	iadd
	isub
	ineg
	iload_1
	iastore
	goto Label9
Label8:
Label9:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label10
Label5:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label11
Label3:
	iconst_0
	istore_2
Label14:
	iload_2
	iload_0
	iconst_1
	isub
	if_icmpgt Label13
	iload_2
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label14
Label13:
Label1:
	return
.limit stack 71
.limit locals 5
.end method
