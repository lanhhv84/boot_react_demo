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
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label3
	iconst_0
	istore_2
Label10:
	iload_2
	bipush 10
	if_icmpgt Label5
	iload_2
	iconst_2
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label4
	goto Label9
Label8:
Label9:
	iload_1
	iload_2
	invokestatic MPClass/foo(II)I
	invokestatic io/putIntLn(I)V
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label5:
	iload_1
	iconst_2
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	goto Label3
	goto Label14
Label13:
Label14:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public static foo(II)I
.var 0 is i I from Label0 to Label1
.var 1 is j I from Label0 to Label1
Label0:
	iload_0
	bipush 10
	imul
	iload_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method
