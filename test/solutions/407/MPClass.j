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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 10
	istore_1
	iload_1
	iconst_5
	if_icmpeq Label3
	goto Label2
Label2:
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label6
Label5:
	iload_1
	iconst_5
	if_icmple Label9
	goto Label8
	goto Label8
Label8:
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label12
Label11:
	iconst_1
	invokestatic io/putInt(I)V
	goto Label13
Label12:
	iconst_0
	invokestatic io/putInt(I)V
Label13:
	goto Label7
Label6:
	iconst_0
	invokestatic io/putInt(I)V
Label7:
Label1:
	return
.limit stack 7
.limit locals 2
.end method
