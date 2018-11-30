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
	iconst_0
	istore_2
Label10:
	iload_2
	bipush 100
	if_icmpgt Label5
	iload_2
	invokestatic io/putInt(I)V
	iload_2
	iconst_5
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label1
	goto Label9
Label8:
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label5:
	ldc "Chackhongindau"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
