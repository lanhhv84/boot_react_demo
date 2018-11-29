.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static c [F
.field static a Z

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
	putstatic MPClass/c [F
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b Z from Label0 to Label1
.var 2 is d Z from Label0 to Label1
.var 3 is i I from Label0 to Label1
	ldc 7
	newarray int
	astore 4
	aload 4
	iconst_1
	ineg
	iconst_1
	ineg
	isub
	ineg
	bipush 6
	iastore
	aload 4
	iconst_1
	ineg
	iconst_1
	ineg
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 11
.limit locals 5
.end method
