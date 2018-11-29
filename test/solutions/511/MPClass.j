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
.var 1 is s I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	iconst_1
	istore_2
Label2:
	iload_2
	bipush 10
	if_icmpgt Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label3
	iload_2
	iconst_4
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_2
	bipush 7
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ifle Label8
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
	goto Label9
Label8:
Label9:
	iconst_0
	istore_1
	iload_2
	bipush 10
	imul
	istore_3
Label16:
	iload_3
	iload_2
	iconst_1
	iadd
	bipush 10
	imul
	if_icmpgt Label11
	iload_3
	iconst_2
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	goto Label10
	goto Label15
Label14:
Label15:
	iload_1
	iload_3
	iadd
	istore_1
Label10:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label16
Label11:
	iload_2
	invokestatic io/putInt(I)V
	ldc ", "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 13
.limit locals 4
.end method

.method public static fact(I)I
.var 0 is x I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is f I from Label0 to Label1
	iconst_1
	istore_2
	iconst_1
	istore_1
Label4:
	iload_1
	iload_0
	if_icmpgt Label3
	iload_2
	iload_1
	imul
	istore_2
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 3
.end method
