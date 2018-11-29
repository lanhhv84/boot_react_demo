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
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
	iconst_1
	istore_1
	iconst_0
	istore_2
	iload_1
	iload_2
	iand
	ifle Label2
	iload_1
	iload_2
	iconst_1
	isub
	ineg
	iand
	invokestatic MPClass/test()Z
	iand
	ifle Label2
	goto Label3
Label2:
	iconst_0
	goto Label4
Label3:
	iconst_1
Label4:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 8
.limit locals 3
.end method

.method public static test()Z
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is res Z from Label0 to Label1
	iconst_0
	istore_1
	ldc 9.5
	fstore_0
	iload_1
	goto Label1
Label1:
	ireturn
.limit stack 4
.limit locals 2
.end method
