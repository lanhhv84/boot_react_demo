.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static b [F

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
	ldc 3
	newarray float
	putstatic MPClass/b [F
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_1
	iconst_0
	istore_3
Label4:
	iload_3
	iconst_5
	if_icmpgt Label3
	iload_1
	iconst_1
	iadd
	istore_1
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 4
.end method
