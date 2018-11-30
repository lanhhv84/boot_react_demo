.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static XxX I

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
.var 1 is xXx I from Label0 to Label1
	bipush 10
	istore_1
	bipush 100
	istore_2
	invokestatic MPClass/foo()V
	iload_2
	bipush 10
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	bipush 10
	invokestatic io/putInt(I)V
	goto Label7
Label6:
	iconst_0
	invokestatic io/putInt(I)V
Label7:
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static foo()V
Label0:
	bipush 10
	putstatic MPClass/XxX I
Label1:
	return
.limit stack 2
.limit locals 0
.end method
