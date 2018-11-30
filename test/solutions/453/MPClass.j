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
	ifle Label2
	iconst_0
	ifle Label2
	goto Label3
Label2:
	iconst_0
	goto Label4
Label3:
	iconst_1
Label4:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifle Label5
	iconst_1
	ifle Label5
	goto Label6
Label5:
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifle Label8
	iconst_1
	ifle Label8
	goto Label9
Label8:
	iconst_0
	goto Label10
Label9:
	iconst_1
Label10:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifle Label11
	iconst_0
	ifle Label11
	goto Label12
Label11:
	iconst_0
	goto Label13
Label12:
	iconst_1
Label13:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifle Label16
	iconst_0
	iconst_0
	idiv
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	goto Label17
Label16:
	iconst_0
	goto Label18
Label17:
	iconst_1
Label18:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 18
.limit locals 1
.end method
