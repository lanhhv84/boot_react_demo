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
	iconst_1
	ifgt Label5
	iconst_1
	i2f
	iconst_1
	i2f
	iconst_0
	i2f
	fdiv
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	goto Label4
Label5:
	iconst_1
	goto Label6
Label4:
	iconst_0
Label6:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 6
.limit locals 1
.end method
