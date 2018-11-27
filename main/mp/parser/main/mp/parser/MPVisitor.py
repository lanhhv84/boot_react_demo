# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mpType.
    def visitMpType(self, ctx:MPParser.MpTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idList.
    def visitIdList(self, ctx:MPParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayVal.
    def visitArrayVal(self, ctx:MPParser.ArrayValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varDec.
    def visitVarDec(self, ctx:MPParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#subVarDec.
    def visitSubVarDec(self, ctx:MPParser.SubVarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#nullableLocal.
    def visitNullableLocal(self, ctx:MPParser.NullableLocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdec.
    def visitFuncdec(self, ctx:MPParser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parDec.
    def visitParDec(self, ctx:MPParser.ParDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listPar.
    def visitListPar(self, ctx:MPParser.ListParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proceduredec.
    def visitProceduredec(self, ctx:MPParser.ProceduredecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnType.
    def visitReturnType(self, ctx:MPParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callStmt.
    def visitCallStmt(self, ctx:MPParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listExp.
    def visitListExp(self, ctx:MPParser.ListExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exprOp.
    def visitExprOp(self, ctx:MPParser.ExprOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr1Op.
    def visitExpr1Op(self, ctx:MPParser.Expr1OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr2Op.
    def visitExpr2Op(self, ctx:MPParser.Expr2OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr3Op.
    def visitExpr3Op(self, ctx:MPParser.Expr3OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr4Op.
    def visitExpr4Op(self, ctx:MPParser.Expr4OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexExprLeft.
    def visitIndexExprLeft(self, ctx:MPParser.IndexExprLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment.
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifStmt.
    def visitIfStmt(self, ctx:MPParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whileStmt.
    def visitWhileStmt(self, ctx:MPParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forStmt.
    def visitForStmt(self, ctx:MPParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakStmt.
    def visitBreakStmt(self, ctx:MPParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continueStmt.
    def visitContinueStmt(self, ctx:MPParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnStmt.
    def visitReturnStmt(self, ctx:MPParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundStmt.
    def visitCompoundStmt(self, ctx:MPParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withStmt.
    def visitWithStmt(self, ctx:MPParser.WithStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callExpr.
    def visitCallExpr(self, ctx:MPParser.CallExprContext):
        return self.visitChildren(ctx)



del MPParser