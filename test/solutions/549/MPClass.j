.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static i I
.field static g F

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

.method public static f()I
Label0:
	sipush 200
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is main I from Label0 to Label1
	invokestatic MPClass/f()I
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
	bipush 100
	istore_2
	iload_2
	istore 4
	iload 4
	istore_3
	iload_2
	invokestatic io/putIntLn(I)V
	iload_3
	invokestatic io/putIntLn(I)V
	iload 4
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 5
.limit locals 5
.end method
