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
Label4:
	iload_1
	bipush 10
	if_icmpgt Label3
	invokestatic MPClass/arrret()[I
	iconst_1
	iload_1
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static arrSum([I[I)[I
	ldc 10
	newarray int
	astore_2
Label0:
	iconst_1
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpgt Label3
	aload_2
	iconst_1
	iload_1
	isub
	ineg
	aload_0
	iconst_1
	iload_1
	isub
	ineg
	iaload
	aload_1
	iconst_1
	iload_1
	isub
	ineg
	iaload
	iadd
	iastore
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	aload_2
	areturn
Label1:
.limit stack 23
.limit locals 3
.end method

.method public static arrret()[I
.var 0 is i I from Label0 to Label1
	ldc 10
	newarray int
	astore_1
Label0:
	iconst_1
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpgt Label3
	aload_1
	iconst_1
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
	aload_1
	areturn
Label1:
.limit stack 13
.limit locals 2
.end method
