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

.method public static isPrime(I)Z
.var 0 is x I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_2
	istore_1
Label8:
	iload_1
	iload_0
	iconst_2
	idiv
	if_icmpgt Label3
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	iconst_0
	goto Label1
	goto Label7
Label6:
Label7:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label3:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
	bipush 100
	istore_1
Label2:
	iload_2
	iload_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_2
	invokestatic MPClass/isPrime(I)Z
	ifle Label4
	iload_2
	invokestatic io/putIntLn(I)V
	goto Label5
Label4:
Label5:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method
