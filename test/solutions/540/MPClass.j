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
.var 2 is j I from Label0 to Label1
.var 3 is n I from Label0 to Label1
.var 4 is max I from Label0 to Label1
.var 5 is temp I from Label0 to Label1
	ldc 11
	newarray int
	astore 6
	aload 6
	iconst_0
	iconst_0
	isub
	ineg
	bipush 9
	iastore
	aload 6
	iconst_0
	iconst_1
	isub
	ineg
	iconst_3
	iastore
	aload 6
	iconst_0
	iconst_2
	isub
	ineg
	bipush 12
	iastore
	aload 6
	iconst_0
	iconst_3
	isub
	ineg
	bipush 7
	iastore
	aload 6
	iconst_0
	iconst_4
	isub
	ineg
	bipush 43
	iastore
	aload 6
	iconst_0
	iconst_5
	isub
	ineg
	bipush 32
	iastore
	aload 6
	iconst_0
	bipush 6
	isub
	ineg
	bipush 17
	iastore
	aload 6
	iconst_0
	bipush 7
	isub
	ineg
	iconst_4
	iastore
	aload 6
	iconst_0
	bipush 8
	isub
	ineg
	iconst_2
	ineg
	iastore
	aload 6
	iconst_0
	bipush 9
	isub
	ineg
	bipush 12
	iastore
	aload 6
	iconst_0
	bipush 10
	isub
	ineg
	bipush 9
	iastore
	bipush 10
	istore_3
	iconst_0
	istore_1
Label11:
	iload_1
	iload_3
	if_icmpgt Label3
	iload_1
	istore 4
	iload_1
	iconst_1
	iadd
	istore_2
Label10:
	iload_2
	iload_3
	if_icmpgt Label5
	aload 6
	iconst_0
	iload 4
	isub
	ineg
	iaload
	aload 6
	iconst_0
	iload_2
	isub
	ineg
	iaload
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload_2
	istore 4
	goto Label9
Label8:
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label5:
	aload 6
	iconst_0
	iload_1
	isub
	ineg
	iaload
	istore 5
	aload 6
	iconst_0
	iload_1
	isub
	ineg
	aload 6
	iconst_0
	iload 4
	isub
	ineg
	iaload
	iastore
	aload 6
	iconst_0
	iload 4
	isub
	ineg
	iload 5
	iastore
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label11
Label3:
	iconst_0
	istore_1
Label14:
	iload_1
	iload_3
	if_icmpgt Label13
	aload 6
	iconst_0
	iload_1
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
	ldc "a"
	invokestatic io/putString(Ljava/lang/String;)V
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label14
Label13:
Label1:
	return
.limit stack 108
.limit locals 7
.end method
