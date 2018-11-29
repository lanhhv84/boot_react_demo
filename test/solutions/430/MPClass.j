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
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpgt Label3
	invokestatic MPClass/arrret()[I
	iconst_0
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
Label0:
	ldc 11
	newarray int
	astore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label4:
	iload_3
	bipush 10
	if_icmpgt Label3
	aload_2
	iconst_0
	iload_3
	isub
	ineg
	aload_0
	iconst_0
	iload_3
	isub
	ineg
	iaload
	aload_1
	iconst_0
	iload_3
	isub
	ineg
	iaload
	iadd
	iastore
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
	aload_2
	goto Label1
Label1:
	areturn
.limit stack 20
.limit locals 4
.end method

.method public static arrret()[I
Label0:
.var 0 is i I from Label0 to Label1
	ldc 11
	newarray int
	astore_1
	iconst_0
	istore_0
Label4:
	iload_0
	bipush 10
	if_icmpgt Label3
	aload_1
	iconst_0
	iload_0
	isub
	ineg
	iload_0
	iastore
Label2:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label4
Label3:
	aload_1
	goto Label1
Label1:
	areturn
.limit stack 12
.limit locals 2
.end method
