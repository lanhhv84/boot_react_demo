from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        ans = [] 
        for a in ctx.decl():
            b = self.visit(a)
            if type(b) == list:
                ans += b
            else:
                ans.append(b)
        return Program(ans)

    # decl: (funcdec|proceduredec|vardec);
    def visitDecl(self,ctx:MPParser.DeclContext):
        if ctx.funcdec():
            return self.visit(ctx.funcdec())
        elif ctx.proceduredec():
            return self.visit(ctx.proceduredec())
        elif ctx.varDec():
            return self.visit(ctx.varDec())

    # funcdec: FUNCTION_KEY ID LB listPar RB COLON returnType SEMI nullableLocal BEGIN_KEY body END_KEY;
    def visitFuncdec(self,ctx:MPParser.FuncdecContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.listPar()), self.visit(ctx.nullableLocal()), self.visit(ctx.body()), self.visit(ctx.returnType()))

    # proceduredec: PROCEDURE_KEY ID LB listPar RB SEMI nullableLocal BEGIN_KEY body END_KEY;
    def visitProceduredec(self,ctx:MPParser.ProceduredecContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.listPar()), self.visit(ctx.nullableLocal()), self.visit(ctx.body()))

    # pardec: idlist COLON returnType;
    # Return: list(VarDecl)
    def visitParDec(self,ctx:MPParser.ParDecContext):
        return [VarDecl(x, self.visit(ctx.returnType())) for x in self.visit(ctx.idList())]
    
    # idList: ID (COMMA ID)*;
    # Return list(Id)
    def visitIdList(self,ctx:MPParser.IdListContext):
        return [Id(x.getText()) for x in ctx.ID()]

    # (pardec (SEMI pardec)*)?
    # return list(parDec)
    def visitListPar(self,ctx:MPParser.ListParContext):
            return reduce(lambda x, y: x + y, [self.visit(dec) for dec in ctx.parDec()], []) if ctx.parDec() else []
    
    # body: stmt?;
    # Return list(stmt)
    def visitBody(self,ctx:MPParser.BodyContext):
        stmt = []
        for s in ctx.stmt():
            a = self.visit(s)
            if type(a) == list:
                stmt += a
            else:
                stmt.append(a)
        return stmt

    # returnType: (mpType|arrayVal); 
    def visitReturnType(self,ctx:MPParser.ReturnTypeContext):
        return self.visit(ctx.mpType()) if ctx.mpType() else self.visit(ctx.arrayVal())

    # mpType: INTEGER_TYPE|BOOLEAN_TYPE|REAL_TYPE|STRING_TYPE ; 
    def visitMpType(self,ctx:MPParser.MpTypeContext):
        if ctx.INTEGER_TYPE():
            return IntType()
        elif ctx.BOOLEAN_TYPE():
            return BoolType()
        elif ctx.REAL_TYPE():
            return FloatType()
        elif ctx.STRING_TYPE():
            return StringType()
    
    # nullableLocal: varDec?; 
    # Return: list(VarDecl)
    def visitNullableLocal(self,ctx:MPParser.NullableLocalContext):
        return self.visit(ctx.varDec()) if ctx.varDec() else []
    
    # varDec: VAR_KEY subVarDec+; 
    # Return: list(VarDecl)
    def visitVarDec(self,ctx:MPParser.VarDecContext):
        return reduce(lambda x, y: x + y, [self.visit(sub) for sub in ctx.subVarDec()], [])

    # subVarDec: (idList COLON returnType SEMI);
    def visitSubVarDec(self,ctx:MPParser.SubVarDecContext):
        return [VarDecl(sub, self.visit(ctx.returnType())) for sub in self.visit(ctx.idList())]

    # arrayVal: ARRAY_TYPE L_SQUARE_SEP SUB_OP? INT_LIT DOUBLE_DOT_SEP SUB_OP? INT_LIT R_SQUARE_SEP OF_KEY mpType;
    def visitArrayVal(self,ctx:MPParser.ArrayValContext):
        # int(ctx.INTLIT().getText())
        lower = (- int(ctx.INT_LIT(0).getText())) if ctx.SUB_OP(0) else int(ctx.INT_LIT(0).getText())
        upper = (- int(ctx.INT_LIT(1).getText())) if ctx.SUB_OP(1) else int(ctx.INT_LIT(1).getText())
        return ArrayType(lower, upper, self.visit(ctx.mpType()))

    # callStmt: call SEMI; 
    def visitCallStmt(self,ctx:MPParser.CallStmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.listExp()))

    # call: ID LB listExp RB; 
    def visitCallExpr(self,ctx:MPParser.CallExprContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.listExp()))

    # listExp: (expr (COMMA expr)*)?
    def visitListExp(self,ctx:MPParser.ListExpContext):
        return [self.visit(expr) for expr in ctx.expr()] if ctx.expr() else []

    # expr: expr exprOp expr1| expr1;
    def visitExpr(self,ctx:MPParser.ExprContext):
        if ctx.exprOp():
            # <assoc=left> expr exprOp expr
            return BinaryOp(self.visit(ctx.exprOp()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        elif ctx.expr1Op():
            # expr expr1Op expr
            return BinaryOp(self.visit(ctx.expr1Op()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        elif ctx.expr2Op():
            # <assoc=left> expr expr2Op expr
            return BinaryOp(self.visit(ctx.expr2Op()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        elif ctx.expr3Op():
            # <assoc=left> expr expr3Op expr
            return BinaryOp(self.visit(ctx.expr3Op()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        elif ctx.expr4Op():
            # <assoc=right> expr4Op expr 
            return UnaryOp(self.visit(ctx.expr4Op()), self.visit(ctx.expr(0)))
        elif ctx.LB():
            return self.visit(ctx.expr(0))
        elif ctx.L_SQUARE_SEP():
            return ArrayCell(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        else:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.INT_LIT():
                return IntLiteral(int(ctx.INT_LIT().getText()))
            elif ctx.FLOAT_LIT():
                return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
            elif ctx.BOOLEAN_LIT():
                if ctx.BOOLEAN_LIT().getText().lower() == 'true':
                    return BooleanLiteral(True)
                else:
                    return BooleanLiteral(False)
            elif ctx.callExpr():
                return self.visit(ctx.callExpr())
            elif ctx.STRING_LIT():
                return StringLiteral(ctx.STRING_LIT().getText())
            elif ctx.indexExpr():
                return self.visit(ctx.indexExpr())
        
        

    # exprOp: (THEN_KEY|AND_OP|OR_OP|ELSE_KEY);
    def visitExprOp(self,ctx:MPParser.ExprOpContext):
        if ctx.AND_OP():
            return (ctx.AND_OP().getText() + ctx.THEN_KEY().getText()).lower() # AAAAAAA
        elif ctx.OR_OP():
            return (ctx.OR_OP().getText() + ctx.ELSE_KEY().getText()).lower() # AAAAAAAAA
    
    # expr1Op: (EQ_OP|NOTEQ_OP|LESS_OP|LESSEQ_OP|GREAT_OP|GREAT_EQ_OP);
    def visitExpr1Op(self,ctx:MPParser.Expr1OpContext):
        if ctx.EQ_OP():
            return '='
        elif ctx.NOTEQ_OP():
            return '<>'
        elif ctx.LESS_OP():
            return '<'
        elif ctx.LESSEQ_OP():
            return '<='
        elif ctx.GREAT_OP():
            return '>'
        elif ctx.GREAT_EQ_OP():
            return '>='

    # expr2Op: (ADD_OP|SUB_OP|OR_OP); 
    def visitExpr2Op(self,ctx:MPParser.Expr2OpContext):
        if ctx.ADD_OP():
            return '+'
        elif ctx.SUB_OP():
            return '-'
        elif ctx.OR_OP():
            return ctx.OR_OP().getText()

    # expr3Op: (DIV_OP|MUL_OP|INT_DIV_OP|MOD_OP|AND_OP);
    def visitExpr3Op(self,ctx:MPParser.Expr3OpContext):
        if ctx.DIV_OP():
            return ctx.DIV_OP().getText()
        elif ctx.MUL_OP():
            return '*'
        elif ctx.INT_DIV_OP():
            return ctx.INT_DIV_OP().getText()
        elif ctx.MOD_OP():
            return ctx.MOD_OP().getText()
        elif ctx.AND_OP():
            return ctx.AND_OP().getText()

    # expr4Op: (SUB_OP|NOT_OP);
    def visitExpr4Op(self,ctx:MPParser.Expr4OpContext):
        return '-' if ctx.SUB_OP() else ctx.NOT_OP().getText()
    
    # stmt: assignment|ifStmt|forStmt|whileStmt|breakStmt|continueStmt|returnStmt|callStmt|compoundStmt|withStmt;
    def visitStmt(self,ctx:MPParser.StmtContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        elif ctx.compoundStmt():
            return self.visit(ctx.compoundStmt())
        elif ctx.withStmt():
            return self.visit(ctx.withStmt())

    # assignment: (expr ':=')+ expr SEMI; 
    def visitAssignment(self,ctx:MPParser.AssignmentContext):
        listExpr = ctx.expr()
        ans = []
        for i in range(len(listExpr) - 1):
            ans.append(Assign(self.visit(listExpr[i]), self.visit(listExpr[i + 1])))
        if len(ans) == 1:
            return ans[0]
        return list(reversed(ans))
    # ifStmt: IF_KEY expr THEN_KEY stmt (ELSE_KEY stmt)?; 
    def visitIfStmt(self,ctx:MPParser.IfStmtContext):
        thenStmt = self.visit(ctx.stmt(0))
        elseStmt = self.visit(ctx.stmt(1)) if len(ctx.stmt()) > 1 else []
        if type(thenStmt) != list:
            thenStmt = [thenStmt]
        if type(elseStmt) != list:
            elseStmt = [elseStmt]
        return If(self.visit(ctx.expr()), thenStmt, elseStmt)

    # forStmt: FOR_KEY ID ':=' expr (TO_KEY|DOWNTO_KEY) expr DO_KEY stmt;
    def visitForStmt(self,ctx:MPParser.ForStmtContext):
        stmt = self.visit(ctx.stmt())
        if type(stmt) != list:
            stmt = [stmt]
        upDown = True if ctx.TO_KEY() else False
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), upDown, stmt)

    # breakStmt: BREAK_KEY SEMI;
    def visitBreakStmt(self,ctx:MPParser.BreakStmtContext):
        return Break()

    # continueStmt: CONTINUE_KEY SEMI;
    def visitContinueStmt(self,ctx:MPParser.ContinueStmtContext):
        return Continue()

    # returnStmt: RETURN_KEY expr? SEMI; 
    def visitReturnStmt(self,ctx:MPParser.ReturnStmtContext):
        return Return(self.visit(ctx.expr())) if ctx.expr() else Return()
    
    # compoundStmt: BEGIN_KEY stmt* END_KEY; // Done
    def visitCompoundStmt(self,ctx:MPParser.CompoundStmtContext):
        ans = []
        for stmt in ctx.stmt():
            a = self.visit(stmt)
            if type(a) == list:
                ans += a
            else:
                ans.append(a)
        return ans

    # whileStmt: WHILE_KEY expr DO_KEY stmt;
    def visitWhileStmt(self,ctx:MPParser.WhileStmtContext):
        ls = self.visit(ctx.stmt())
        if type(ls) == list:
            return While(self.visit(ctx.expr()), ls)
        else:
            return While(self.visit(ctx.expr()), [ls]) 

    # withStmt: WITH_KEY listPar SEMI DO_KEY stmt;
    def visitWithStmt(self,ctx:MPParser.WithStmtContext):
        stmt = self.visit(ctx.stmt())
        if type(stmt) != list:
            stmt = [stmt]
        return With(self.visit(ctx.listPar()), stmt)


   
