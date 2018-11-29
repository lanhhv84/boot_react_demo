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
	aload_1
	iconst_0
	iconst_0
	isub
	ineg
	iconst_5
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
	bipush 8
	iastore
	aload_1
	iconst_0
	iconst_3
	isub
	ineg
	bipush 9
	iastore
	aload_1
	iconst_0
	iconst_4
	isub
	ineg
	iconst_1
	iastore
	aload_1
	invokestatic MPClass/bbsort([I)V
	invokestatic io/putLn()V
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_4
	if_icmpgt Label3
	aload_1
	iconst_0
	iload_2
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 38
.limit locals 5
.end method

.method public static bbsort([I)V
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is temp I from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is j I from Label0 to Label1
	iconst_5
	istore_1
	iconst_0
	istore_3
Label14:
	iload_3
	iload_1
	iconst_1
	isub
	if_icmpgt Label3
	iconst_0
	istore_3
Label13:
	iload_3
	iload_1
	iconst_2
	isub
	if_icmpgt Label5
	iconst_0
	istore 4
Label12:
	iload 4
	iload_1
	iload_3
	isub
	iconst_2
	isub
	if_icmpgt Label7
	aload_0
	iconst_0
	iload 4
	isub
	ineg
	iaload
	aload_0
	iconst_0
	iload 4
	iconst_1
	iadd
	isub
	ineg
	iaload
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	aload_0
	iconst_0
	iload 4
	isub
	ineg
	iaload
	istore_2
	aload_0
	iconst_0
	iload 4
	isub
	ineg
	aload_0
	iconst_0
	iload 4
	iconst_1
	iadd
	isub
	ineg
	iaload
	iastore
	aload_0
	iconst_0
	iload 4
	iconst_1
	iadd
	isub
	ineg
	iload_2
	iastore
	goto Label11
Label10:
Label11:
Label6:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label12
Label7:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label13
Label5:
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label14
Label3:
	iconst_0
	istore_3
Label17:
	iload_3
	iload_1
	iconst_1
	isub
	if_icmpgt Label16
	aload_0
	iconst_0
	iload_3
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
Label15:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label17
Label16:
Label1:
	return
.limit stack 43
.limit locals 5
.end method
