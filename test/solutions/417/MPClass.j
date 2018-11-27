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
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label10:
	iload_1
	bipush 10
	if_icmpgt Label3
	iload_1
	iconst_5
	if_icmpne Label5
	goto Label4
Label4:
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label8
Label7:
	goto Label3
	goto Label9
Label8:
Label9:
	iload_1
	invokestatic io/putInt(I)V
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label3:
Label1:
	return
.limit stack 6
.limit locals 2
.end method
