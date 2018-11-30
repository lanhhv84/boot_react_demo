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
	invokestatic MPClass/abc()I
	invokestatic io/putInt(I)V
	goto Label1
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static abc()I
Label0:
.var 0 is ans I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_0
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpgt Label3
	iload_0
	iload_1
	iadd
	istore_0
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method
