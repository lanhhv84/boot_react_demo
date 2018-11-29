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
	bipush 6
	istore_2
	iload_2
	invokestatic MPClass/factor(I)I
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static factor(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	goto Label1
	goto Label5
Label4:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/factor(I)I
	imul
	goto Label1
Label5:
Label1:
	ireturn
.limit stack 6
.limit locals 1
.end method
