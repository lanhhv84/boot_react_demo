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
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
	bipush 69
	i2f
	fstore_1
	bipush 96
	i2f
	fstore_2
	fload_1
	fload_2
	fadd
	invokestatic io/putFloat(F)V
	fload_1
	fload_2
	fsub
	invokestatic io/putFloat(F)V
	fload_1
	fload_2
	fmul
	invokestatic io/putFloat(F)V
	fload_1
	fload_2
	fdiv
	invokestatic io/putFloat(F)V
	fload_1
	fload_2
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
	fload_1
	fload_2
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBool(Z)V
	fload_1
	fload_2
	fcmpl
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBool(Z)V
	fload_1
	fload_2
	fcmpl
	iflt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBool(Z)V
	fload_1
	fload_2
	fcmpl
	ifeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBool(Z)V
	fload_1
	fload_2
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 11
.limit locals 3
.end method
