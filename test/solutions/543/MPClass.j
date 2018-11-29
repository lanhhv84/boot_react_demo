.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static x I
.field static z [I

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
	ldc 23
	newarray int
	putstatic MPClass/z [I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/foo()[I
	iconst_1
	bipush 10
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static foo()[I
Label0:
	ldc 23
	newarray int
	astore_0
	aload_0
	iconst_1
	bipush 10
	isub
	ineg
	bipush 100
	iastore
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 10
.limit locals 1
.end method
