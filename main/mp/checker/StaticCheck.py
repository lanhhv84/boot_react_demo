
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from collections import namedtuple

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType(Param: " + ' '.join([a.__str__() for a in self.partype]) + " Return: " + self.rettype.__str__()  + ")"


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


    def __str__(self):
        return "Symbol(" + self.name + "," + self.mtype.__str__() + ")"
    
class StmtInOut:

    # (last_return, last_break, last_continue, is_loop, c function return type)
    def __init__(self, last_return, last_break, last_continue, is_loop=False, var=None, return_type=None):
        self.var = var
        self.last_return = last_return
        self.last_break = last_break
        self.last_continue = last_continue
        self.is_loop = is_loop
        self.return_type = return_type

    

class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType())),
                   Symbol("putInt",MType([IntType()],VoidType())),
                   Symbol("getFloat",MType([],FloatType())),
                   Symbol("putFloat",MType([FloatType()],VoidType())),
                   Symbol("putFloatLn",MType([FloatType()],VoidType())),
                   Symbol("putBool",MType([BoolType()],VoidType())),
                   Symbol("putBoolLn",MType([BoolType()],VoidType())),
                   Symbol("putString",MType([StringType()],VoidType())),
                   Symbol("putStringLn",MType([StringType()],VoidType())),
                   Symbol("putLn",MType([],VoidType()))]
            
    def __init__(self,ast):
        self.ast = ast
        self.visitFunc = {}
        self.builtinName = [x.name.lower() for x in self.global_envi]
   
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        # TODO: Check for redeclaring variable/Function/Procedure/Parameter 
        global_var = []
        # Update global environment
        for f in ast.decl:
            if type(f) == FuncDecl:
                if not self.existName(global_var, f.name.name) and not self.existName(c, f.name.name):
                    global_var.append(Symbol(f.name.name, MType(f.param, f.returnType)))
                    self.visitFunc[f.name.name.lower()] = [f.returnType, False]
                else:
                    if type(f.returnType) == VoidType:
                        raise Redeclared(Procedure(), f.name.name)
                    else:
                        raise Redeclared(Function(), f.name.name)
            else:
                if not StaticChecker.existName(global_var, f.variable.name) and not self.existName(c, f.variable.name):
                    global_var.append(Symbol(f.variable.name, f.varType))
                else:
                    raise Redeclared(Variable(), f.variable.name)

        ans = [self.visit(y, global_var + c) for y in [x for x in ast.decl if type(x) is FuncDecl]]
        
        if not any(ans):
            raise NoEntryPoint()
        for name, (returnType, val) in self.visitFunc.items():
            if not val and name != "main" and name not in self.builtinName:
                if type(returnType) == VoidType:
                    raise Unreachable(Procedure(), name)
                else:
                    raise Unreachable(Function(), name)

        return [True]

    def visitFuncDecl(self,ast,c): 
    
        # Visit all statement inside function
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)

        # Check for redeclaring
        vardecl = reduce(lambda x, y: x + [self.visit(y, (x,False))], ast.param, [])
        vardecl = reduce(lambda x, y: x + [self.visit(y, (x,True))], ast.local, vardecl)

        # Visit statements, check for undeclared identifiers
        stmt_out = self.reduceStmt(ast.body, StmtInOut(last_return=False, last_break=False,last_continue=False), var=vardecl + c, return_type=ast.returnType, is_loop=False)

        # TODO: Find return inside other stmt
        if type(ast.returnType) != VoidType and not stmt_out.last_return:
            raise FunctionNotReturn(ast.name.name)

        return StaticChecker.entryPoint(ast)

    def visitVarDecl(self,ast,c):
        envi, var = c
        if self.lookupSymbol(ast.variable.name, envi) is not None:
            if var:
                raise Redeclared(Variable(), ast.variable.name)
            else:
                raise Redeclared(Parameter(), ast.variable.name)
        return Symbol(ast.variable.name, ast.varType)


    def visitReturn(self,ast,c):
        """
        Check return value
        """
        StaticChecker.checkUnreachable(c, ast)
        if type(c.return_type) != VoidType:
            if ast.expr is None or not StaticChecker.isCompatible(c.return_type, self.visit(ast.expr, c.var)):
                raise TypeMismatchInStatement(ast)
        else:
            if not ast.expr is None:
                raise TypeMismatchInStatement(ast)

        return StmtInOut(last_return=True,last_break=False,last_continue=False,is_loop=c.is_loop)
    
    def visitContinue(self,ast,c):
        StaticChecker.checkUnreachable(c, ast)
        if not c.is_loop:
            raise ContinueNotInLoop() 
        return StmtInOut(last_return=False,last_break=False,last_continue=True,is_loop=c.is_loop)

    def visitBreak(self,ast,c):
        StaticChecker.checkUnreachable(c, ast)
        if not c.is_loop:
            raise BreakNotInLoop()
        return StmtInOut(last_return=False,last_break=True,last_continue=False,is_loop=c.is_loop)
    
    def visitWith(self, ast, c):
        """
        Check for redeclaring block variables
        Visit substatements
        """
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        StaticChecker.checkUnreachable(c, ast)
        block_var = reduce(lambda x, y: x + [self.visit(y, (x,True))], ast.decl, [])
        ans = self.reduceStmt(ast.stmt, StmtInOut(last_return=False, last_break=False, last_continue=False), var=block_var + c.var, return_type=c.return_type, is_loop=c.is_loop)
        return ans

    def visitAssign(self,ast,c):
        """
        Check undeclared: Done
        Check type mismatch statement: Done
        """
        if type(ast.lhs) != Id and type(ast.lhs) != ArrayCell:
            raise TypeMismatchInStatement(ast)
        StaticChecker.checkUnreachable(c, ast)
        leftType = self.visit(ast.lhs, c.var)
        rightType = self.visit(ast.exp, c.var)
        if type(leftType) == StringType or type(leftType) == ArrayType or not StaticChecker.isCompatible(leftType, rightType):
            raise TypeMismatchInStatement(ast)
        return StmtInOut(last_return=False, last_break=False, last_continue=False, is_loop=c.is_loop)

    def visitIf(self,ast,c):
        """
        Check condition is boolean: Done
        Check unreachable statement: May be done
        Break/Continue not in loop
        """
        StaticChecker.checkUnreachable(c, ast)
        cond = self.visit(ast.expr, c.var)
        if not StaticChecker.isCompatible(BoolType(), cond):
            raise TypeMismatchInStatement(ast)
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        thenStmt = self.reduceStmt(ast.thenStmt, StmtInOut(last_return=False, last_break=False, last_continue=False, is_loop=c.is_loop), c.var, c.return_type, c.is_loop)
        elseStmt = self.reduceStmt(ast.elseStmt, StmtInOut(last_return=False, last_break=False, last_continue=False, is_loop=c.is_loop), c.var, c.return_type, c.is_loop)
        if type(ast.expr) == BoolType:
            if ast.expr.value == True:
                return thenStmt
            else:
                return elseStmt
        lreturn = thenStmt.last_return and elseStmt.last_return
        lbreak = thenStmt.last_break and elseStmt.last_break
        lcontinue = thenStmt.last_continue and elseStmt.last_continue
        lbreak1 = thenStmt.last_break or thenStmt.last_continue or thenStmt.last_return
        lbreak2 = elseStmt.last_break or elseStmt.last_continue or elseStmt.last_return
        lbreak = lbreak1 and lbreak2 # Notice
        return StmtInOut(last_return=lreturn, last_break=lbreak, last_continue=lcontinue, is_loop=c.is_loop)

    def visitWhile(self,ast,c):
        """
        Check condition is boolean
        Check return value
        """

        #sl:list(Stmt)
        #exp: Expr
        StaticChecker.checkUnreachable(c, ast)
        cond = self.visit(ast.exp, c.var)
        if not StaticChecker.isCompatible(BoolType(), cond):
            raise TypeMismatchInStatement(ast)
        sub_last_break = False
        last_break = False
        if type(ast.exp) == BoolType:
            if ast.exp.value == True:
                last_break = True
            else:
                sub_last_break = True
        ans = self.reduceStmt(ast.sl, StmtInOut(last_return=False, last_break=sub_last_break, last_continue=False), var=c.var, return_type=c.return_type, is_loop=True)
        last_return = type(ast.exp) == BoolType and ast.exp.value and ans.last_return
        return StmtInOut(last_return=last_return, last_break=last_break,last_continue=False, is_loop=c.is_loop)
        
    def visitFor(self,ast,c):
        """
        Check expression is boolean compatible
        Check unreachable statement
        """
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        #
        StaticChecker.checkUnreachable(c, ast)
        cond1 = StaticChecker.isCompatible(IntType(), self.visit(ast.id,c.var))
        cond2 = StaticChecker.isCompatible(IntType(), self.visit(ast.expr1,c.var))
        cond3 = StaticChecker.isCompatible(IntType(), self.visit(ast.expr2,c.var))

        if not cond1 or not cond2 or not cond3:
            raise TypeMismatchInStatement(ast)

        ans = self.reduceStmt(ast.loop, StmtInOut(last_return=False, last_break=False, last_continue=False, is_loop=True), c.var, c.return_type, True)
        return StmtInOut(last_return=False, last_break=False, last_continue=False, is_loop=c.is_loop)

    def visitCallStmt(self, ast, c): 
        """
        Must be a precedure
        Check undeclared procedure, function, identifier
        """
        StaticChecker.checkUnreachable(c, ast)
        self.visitCall(ast,(c.var, False))
        return StmtInOut(last_return=False, last_break=False, last_continue=False, is_loop=False)

    def visitCallExpr(self, ast, c):
        return self.visitCall(ast, (c, True))
    

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()
    
    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    def visitArrayType(self,ast,c):
        return ast

    def visitArrayCell(self,ast,c):
        #arr:Expr
        #idx:Expr
        arr = self.visit(ast.arr,c)
        cond1 = type(arr) == ArrayType
        cond2 = type(self.visit(ast.idx,c)) == IntType
        if not cond1 or not cond2:
            raise TypeMismatchInExpression(ast)
        return arr.eleType

    def visitId(self,ast,c):
        ans = self.lookupSymbol(ast.name, c)
        if ans == None or type(ans.mtype) == MType:
            raise Undeclared(Identifier(), ast.name)
        else:
            return ans.mtype
    
    def visitBinaryOp(self,ast,c):
        #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #left:Expr
        #right:Expr

        leftType = type(self.visit(ast.left,c))
        rightType = type(self.visit(ast.right,c))
        op = ast.op.lower()
        numType = [FloatType, IntType]


        if leftType in numType and rightType in numType:
            boolOp = ['<', '<=', '>', '>=', '=', '<>']
            intOp = ['+', '-', '*', 'div', 'mod']
            realOp = ['+', '-', '*', '/']
            if leftType == IntType and rightType == IntType:
                
                if op in intOp:
                    return IntType()
                elif op in boolOp:
                    return BoolType()
                elif op == '/':
                    return FloatType()
            else:
                # Real type operation
                if op in realOp:
                    return FloatType()
                elif op in boolOp:
                    return BoolType()

        if leftType == BoolType and rightType == BoolType:
            boolOp = ['and', 'andthen', 'or', 'orelse']
            if op in boolOp:
                return BoolType()

        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        #op:string
        #body:Expr
        op = ast.op.lower()
        bodyType = type(self.visit(ast.body, c))
        if op == '-' and bodyType == IntType:
            return IntType()
        elif op == '-' and bodyType == FloatType:
            return FloatType()
        elif op == 'not' and bodyType == BoolType:
            return BoolType()

        raise TypeMismatchInExpression(ast)

    @staticmethod
    def entryPoint(ast):
        return ast.name.name.lower() == "main" and len(ast.param) == 0 and type(ast.returnType) == VoidType

    # Utility method
    @staticmethod
    def isCompatible(recvType, passType):
        if type(recvType) == VarDecl:
            recvType = recvType.varType
        if type(recvType) == ArrayType:
            if type(passType) != ArrayType:
                return False
            else:
                return recvType.lower == passType.lower and recvType.upper == passType.upper and type(recvType.eleType) == type(passType.eleType)
        numType = [FloatType, IntType]
        if type(recvType) == FloatType and type(passType) in numType:
            return True
        if type(recvType) == type(passType):
            return True
        return False

    @staticmethod
    def existName(lst_name, name):
        for symbol in lst_name:
            if symbol.name.lower() == name.lower():
                return True
        return False

    @staticmethod
    def checkUnreachable(c, ast):
        if c.last_break or c.last_return or c.last_continue:
            raise UnreachableStatement(ast)

    def lookupSymbol(self, name, listSymbol):
        for symbol in listSymbol:
            if symbol.name.lower() == name.lower():
                return symbol
        return None

    def reduceStmt(self, lst_stmt, init_input, var, return_type, is_loop):
        return reduce(lambda x, y: self.visit(y, StmtInOut(x.last_return, x.last_break, x.last_continue, is_loop, var, return_type)), lst_stmt, init_input)

    def visitCall(self,ast,c):
        
        param = [self.visit(x,c[0]) for x in ast.param]
        symbol = self.lookupSymbol(ast.method.name, c[0])
        if not c[1]:
            if symbol == None or not type(symbol.mtype) is MType or not type(symbol.mtype.rettype) is VoidType:
                raise Undeclared(Procedure(), ast.method.name)
        else:
            if symbol == None or not type(symbol.mtype) is MType or type(symbol.mtype.rettype) is VoidType:
                raise Undeclared(Function(), ast.method.name)

        if ast.method.name.lower() not in self.builtinName:
            self.visitFunc[ast.method.name.lower()][1] = True

        ex = TypeMismatchInExpression if c[1] else TypeMismatchInStatement
        if len(symbol.mtype.partype) != len(param):
            raise ex(ast)
        for recvType, passType in zip([x for x in symbol.mtype.partype], param):

            if not StaticChecker.isCompatible(recvType, passType):
                raise ex(ast)
        return symbol.mtype.rettype


