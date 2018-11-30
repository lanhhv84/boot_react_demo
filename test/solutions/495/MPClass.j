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
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	bipush 10
	istore_1
Label2:
	iload_1
	iconst_0
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label3
	bipush 10
	istore_2
Label4:
	iload_2
	iconst_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	iload_2
	iconst_5
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label5
	goto Label9
Label8:
Label9:
	iload_2
	iconst_1
	isub
	istore_2
	iload_2
	invokestatic io/putInt(I)V
	goto Label4
Label5:
	iload_1
	iconst_1
	isub
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 10
.limit locals 3
.end method
