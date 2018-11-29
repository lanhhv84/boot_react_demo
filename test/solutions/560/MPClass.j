.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static arr [I

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
	ldc 10
	newarray int
	putstatic MPClass/arr [I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 9
	if_icmpgt Label3
	getstatic MPClass/arr [I
	iconst_0
	iload_1
	isub
	ineg
	iload_1
	iastore
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iconst_0
	istore_1
Label7:
	iload_1
	bipush 9
	if_icmpgt Label6
	getstatic MPClass/arr [I
	iconst_0
	iload_1
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label7
Label6:
Label1:
	return
.limit stack 10
.limit locals 3
.end method
