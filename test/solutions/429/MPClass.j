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
	invokestatic MPClass/arrret()I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static arrret()I
Label0:
.var 0 is i I from Label0 to Label1
	iconst_2
	istore_0
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method
