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
.var 1 is i F from Label0 to Label1
.var 2 is sum I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_3
Label6:
	iload_3
	bipush 100
	if_icmpgt Label5
	iload_2
	iload_3
	iadd
	istore_2
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label6
Label5:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 4
.end method
