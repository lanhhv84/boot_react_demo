'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String
        self.value = value

class IntClass(Val):
    def __init__(self, value, isLong=False):
        #value: String
        self.isLong = False



class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.returnType = None

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)

        self.emit.printout('\n')

        for x in ast.decl:
            if type(x) is VarDecl:
                e.sym = [Symbol(x.variable.name, x.varType, CName(self.className))] + e.sym
                code = self.emit.emitATTRIBUTE(x.variable.name, x.varType, False, "")
                self.emit.printout(code)
        
                

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", Frame("<init>", VoidType)))

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<clinit>"), list(), list(filter(lambda x: type(x) is VarDecl and type(x.varType) is ArrayType, ast.decl)), list(),VoidType()), [], Frame("<clinit>", Frame("<clinit>", VoidType)))

        for x in ast.decl:
            if type(x) is FuncDecl:
                e.sym = [Symbol(x.name.name, MType([y.varType for y in x.param], x.returnType), CName(self.className))] + e.sym

        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, SubBody(None, e.sym.copy()))



        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)\
        self.returnType = consdecl.returnType
        frame.enterScope(True)

        isClinit = consdecl.name.name == "<clinit>"
        isInit = consdecl.name.name == "<init>"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name

        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        # Generate code for parameters + local variables
        for var in consdecl.param:
            sym = self.visit(var, (frame, False))
            glenv = [sym] + glenv
            self.emit.printout(self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        if not glenv is None:
            for sym in glenv[:len(consdecl.param)]:
                if type(sym.mtype) is ArrayType:
                    symCopy = Symbol(sym.name + "_copy", sym.mtype, Index(frame.getNewIndex()))
                    self.emit.printout(self.emit.emitVAR(symCopy.value.value, symCopy.name, symCopy.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
                    glenv = [symCopy] + glenv
                    self.emit.printout(self.copyArray(sym, symCopy, SubBody(frame, glenv)))
                    sym.value.value = symCopy.value.value
                    glenv = glenv[1: ]


        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        for var in consdecl.local:
            if consdecl.name.name != "<clinit>":
                sym = self.visit(var, (frame, True))
                glenv = [sym] + glenv
                if type(sym.mtype) != ArrayType:
                    self.emit.printout(self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
            else:
                sym = self.visit(var, (frame, True, True))
                glenv = [sym] + glenv
                if type(sym.mtype) != ArrayType:
                    self.emit.printout(self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))


        

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.emit.printout(self.visit(x, SubBody(frame, glenv))), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # Return statement
        if type(returnType) is ArrayType or type(returnType) is StringType:
            self.emit.printout(self.emit.jvm.emitARETURN())
        else:
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
        # End method
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [] + subctxt.sym)

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any
        return self.visitCall(ast, o)[0]

        

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, IntType(), frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(float(ast.value)), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitUnaryOp(self, ast, o):
        #op:string
        #body:Expr
        ctxt = o
        frame = ctxt.frame
        code = self.visit(ast.body, ctxt)
        if ast.op.lower() == 'not':
            """
                current_val
                if current_val == true:
                    goto putTrue
                push 0
                goto end
            
            putTrue:
                put 1

            end:
            """
            return code[0] + self.visitReverse(BoolType(), frame)[0], BoolType()
            
        elif ast.op.lower() == '-':
            """
                current_val
                current_val (dup) -> current_value*2
                sub
            """
            return code[0] + self.visitReverse(code[1], frame), code[1]
            


    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        leftCode, leftType = self.visit(ast.left, o)
        rightCode, rightType = self.visit(ast.right, o)
        op = ast.op.lower()
        # Same type
        if type(leftType) is type(rightType):
            # Both of them are integer
            if type(leftType) == IntType:
                return self.visitBinaryOpInt(leftCode, rightCode, op, frame)
            # Both of them are real
            if type(leftType) is FloatType:
                return self.visitBinaryOpReal(leftCode, rightCode, op, frame)
            # Both of them are boolean
            if type(leftType) is BoolType:
                return self.visitBinaryOpBool(leftCode, rightCode, op, frame)
                
        # Different type, need to cast
        else:
            if type(leftType) in [FloatType, IntType] and type(rightType) in [FloatType, IntType]:
                if type(leftType) is IntType:
                    leftCode = leftCode + self.emit.emitI2F(frame)
                else:
                    rightCode = rightCode + self.emit.emitI2F(frame)
                return self.visitBinaryOpReal(leftCode, rightCode, op, frame)

        return '', VoidType()

    def visitLazyOp(self, leftCode, rightCode, ifTrue, frame):
        """     
            {
                first_op
                if not first_op
                    goto return_false
            }
            {
                second_op
                if not second_op
                    goto return_false
            }
            goto return true:
        return_false:
            0
            goto end_op
        return_true:
            1
        end_op
        """
        returnFalseLabel = str(frame.getNewLabel())
        returnTrueLabel = str(frame.getNewLabel())
        endOpLabel = str(frame.getNewLabel())
        if ifTrue:
            leftCode = leftCode + self.emit.emitIFFALSE(returnFalseLabel, frame)
            rightCode = rightCode + self.emit.emitIFFALSE(returnFalseLabel, frame)
            code = leftCode +  rightCode + self.emit.emitGOTO(returnTrueLabel, frame)
            returnFalseCode = self.emit.emitLABEL(returnFalseLabel, frame) + self.emit.emitPUSHICONST(0, frame) + self.emit.emitGOTO(endOpLabel, frame)
            returnTrueCode = self.emit.emitLABEL(returnTrueLabel, frame) + self.emit.emitPUSHICONST(1, frame)
            code = code + returnFalseCode + returnTrueCode + self.emit.emitLABEL(endOpLabel, frame)
        else:
            leftCode = leftCode + self.emit.emitIFTRUE(returnTrueLabel, frame)
            rightCode = rightCode + self.emit.emitIFTRUE(returnTrueLabel, frame)
            code = leftCode +  rightCode + self.emit.emitGOTO(returnFalseLabel, frame)
            returnTrueCode = self.emit.emitLABEL(returnTrueLabel, frame) + self.emit.emitPUSHICONST(1, frame) + self.emit.emitGOTO(endOpLabel, frame)
            returnFalseCode = self.emit.emitLABEL(returnFalseLabel, frame) + self.emit.emitPUSHICONST(0, frame)
            code = code + returnTrueCode + returnFalseCode + self.emit.emitLABEL(endOpLabel, frame)
        return code

    def visitBinaryOpReal(self, leftCode, rightCode, op, frame):
        code = leftCode + rightCode
        if op in ['+', '-']:
            return code + self.emit.emitADDOP(op, FloatType(), frame), FloatType()
        elif op == '*':
            return code + self.emit.emitMULOP('*', FloatType(), frame), FloatType()
        elif op == '/':
            return code + self.emit.emitMULOP('/', FloatType(), frame), FloatType()
        elif op in ['<', '<=', '>', '>=', '<>', '=']:
            return self.visitRELOP(code, op, FloatType(), frame)

    def visitBinaryOpInt(self, leftCode, rightCode, op, frame):
        code = leftCode + rightCode
        if op == 'mod':
            return code  + self.emit.emitMOD(frame), IntType()
        elif op == '+':
            return code + self.emit.emitADDOP('+', IntType(), frame), IntType()
        elif op == '-':
            return code + self.emit.emitADDOP('-', IntType(), frame), IntType()
        elif op == '*':
            return code + self.emit.emitMULOP('*', IntType(), frame), IntType()
        elif op == 'div':
            return code + self.emit.emitDIV(frame), IntType()
        elif op == 'mod':
            return code + self.emit.emitMOD(frame), IntType()
        elif op in ['<', '<=', '>', '>=', '<>', '=']:
            return self.visitRELOP(code, op, IntType(), frame)
        elif op == '/':
            return leftCode + self.emit.emitI2F(frame) + rightCode + self.emit.emitI2F(frame) + self.emit.emitMULOP('/', FloatType(), frame), FloatType()

    def visitBinaryOpBool(self, leftCode, rightCode, op, frame):
        code = leftCode + rightCode
        if op == 'and':
            return code + self.emit.emitANDOP(frame), BoolType()
        elif op == 'or':
            return code + self.emit.emitOROP(frame), BoolType()
        elif op == 'andthen':
            return self.visitLazyOp(leftCode, rightCode, True, frame), BoolType()
        elif op == 'orelse':
            return self.visitLazyOp(leftCode, rightCode, False, frame), BoolType()

    def visitRELOP(self, code, op, opType, frame):
        """
        exp1
        exp2
        if gt:
            goto FalseLabel
        trueCode
        goto end
        FalseLabel:
            falseCode
        end:
        """
        falseLabel = str(frame.getNewLabel())
        endCompLabel = str(frame.getNewLabel())
        trueLabelCode = self.emit.emitPUSHICONST(1, frame) + self.emit.emitGOTO(endCompLabel, frame)
        falseLabelCode = self.emit.emitLABEL(falseLabel, frame) + self.emit.emitPUSHICONST(0, frame)
        
        return code  + self.emit.emitRELOP(op, opType, falseLabel, falseLabel, frame) + trueLabelCode + falseLabelCode + self.emit.emitLABEL(endCompLabel, frame), BoolType()

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookupCase(ast.name, nenv, lambda x: x.name)
        if sym is None:
            pass
        elif type(sym.value) is Index:
            if type(sym.mtype) is ArrayType:
                refCode = self.emit.emitREADVAR(sym.name, ArrayPointerType(sym.mtype.eleType), sym.value.value, frame)
                paddingCode = self.emit.emitPUSHICONST(sym.mtype.lower, frame)
                return refCode , sym.mtype
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
        else:
            return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame), sym.mtype

    def visitAssign(self, ast,o):
        #lhs:Expr
        #exp:Expr
        
        #_left = self.visit(ast.lhs)
        ctxt = o
        frame = ctxt.frame
        _left = self.visit(ast.lhs, ctxt)
        _right = self.visit(ast.exp, ctxt)
        """
        _left[0][0]: ref
        _left[0][1]: padding

        """
        if type(ast.lhs) is ArrayCell:
            return self.visitWriteArray(ast.lhs, _right, o)
        elif type(ast.lhs) is Id:
            nenv = ctxt.sym
            sym = self.lookupCase(ast.lhs.name, nenv, lambda x: x.name)
            ad = ''
            if type(_right[1]) is IntType and type(sym.mtype) is FloatType:
                ad = self.emit.emitI2F(frame)
            return _right[0] + ad + self.writeVar(sym, frame)
           

    def visitVarDecl(self, ast,o):
        #variable:Id
        #varType: Type
        index = o[0].getNewIndex()
        if type(ast.varType) is ArrayType and o[1]:
            if len(o) > 2:
                self.visitArrayCreate(ast, index, o[0], True)
            else:
                self.visitArrayCreate(ast, index, o[0])
        return Symbol(ast.variable.name, ast.varType, Index(index))

    def visitIf(self,ast,o):
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        """
        exp
            if exp == 0:
                goto LabelFalse
            truestmt
            goto endIf
        LabelFalse:
            falsestmt
        EndIf:
        """
        ctxt = o
        frame = ctxt.frame
        expr = self.visit(ast.expr, ctxt)
        falseLabel = frame.getNewLabel()
        endIfLabel = frame.getNewLabel()
        trueStmt = ''.join([self.visit(x, ctxt) for x in ast.thenStmt])
        falseStmt = ''.join([self.visit(x, ctxt) for x in ast.elseStmt])       

        checkCode = expr[0] + self.emit.emitIFFALSE(falseLabel, frame)
        trueCode = trueStmt + self.emit.emitGOTO(str(endIfLabel), frame)
        falseCode = self.emit.emitLABEL(str(falseLabel), frame) + falseStmt +  self.emit.emitLABEL(str(endIfLabel), frame) 
        ans = checkCode + trueCode + falseCode
        return ans
        
    def visitWhile(self, ast,o):
        #sl:list(Stmt)
        #exp: Expr

        """
            load expression
        checkCondition: (continue)
            check condition
            stmt
        endWhile: (break)

        """
        ctxt = o
        frame = ctxt.frame
        frame.enterLoop()
        stmt = ''.join([self.visit(x, ctxt) for x in ast.sl])
        checkCondLabel = str(frame.getContinueLabel())
        endLabel = str(frame.getBreakLabel())
        checkCondCode = self.emit.emitLABEL(checkCondLabel, frame) + self.visit(ast.exp, ctxt)[0] + self.emit.emitIFFALSE(endLabel, frame) + stmt + self.emit.emitGOTO(checkCondLabel, frame)
        endCode = self.emit.emitLABEL(endLabel, frame) 
        frame.exitLoop()
        return checkCondCode + endCode

    def visitBreak(self, ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitGOTO(str(frame.getBreakLabel()), frame)
    
    def visitContinue(self, ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitGOTO(str(frame.getContinueLabel()), frame)

    def visitFor(self, ast,o):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        ctxt = o
        frame = ctxt.frame
        frame.enterLoop()

        nenv = ctxt.sym
        sym = self.lookupCase(ast.id.name, nenv, lambda x: x.name)
        exp1 = self.visit(ast.expr1, ctxt)
        exp2 = self.visit(ast.expr2, ctxt)

        """
            Assign
        PreCondLabel:
            if id >/< threshold:
                goto EndForLabel
        
            Stmt
        PostCondition: (Continue)
            id = id - 1
            goto PreCondLabel
        EndForLabel:    (Break)
            return
        """

        stmt = ''.join([self.visit(x, ctxt) for x in ast.loop])
        preCondLabel = str(frame.getNewLabel())
        postCondLabel = str(frame.getContinueLabel())
        endLabel = str(frame.getBreakLabel())

        assignCode = exp1[0] + self.writeVar(sym, frame)
        preCondCode = self.emit.emitLABEL(preCondLabel, frame) + self.readVar(sym, frame)[0] + exp2[0]
        if ast.up:
            preCondCode += self.emit.emitIFICMPGT(endLabel, frame)
        else:
            preCondCode += self.emit.emitIFICMPLT(endLabel, frame)
        preCondCode += stmt
        postCondCode = self.emit.emitLABEL(postCondLabel, frame) + self.readVar(sym, frame)[0] + self.emit.emitPUSHICONST(1, frame)
        if ast.up:
            postCondCode += self.emit.emitADDOP('+', IntType(), frame)
        else:
            postCondCode += self.emit.emitADDOP('-', IntType(), frame)

        postCondCode += self.writeVar(sym, frame) + self.emit.emitGOTO(preCondLabel, frame)

        endCode = self.emit.emitLABEL(endLabel, frame)


        # Intialize loop 

        # Assign identifier
        frame.exitLoop()
        return assignCode + preCondCode + postCondCode + endCode

    def visitReturn(self, ast,o):
        ctxt = o
        frame = ctxt.frame
        if ast.expr is not None:
            ans = self.visit(ast.expr, o)
            d = ''
            if not self.returnType is None and type(self.returnType) is FloatType:
                if type(ans[1]) is IntType:
                    d = self.emit.emitI2F(frame)
            return ans[0] + d + self.emit.emitGOTO(str(frame.endLabel[0]), frame)
        else:
            return ''

    def visitCallExpr(self, ast, o):
        call = self.visitCall(ast, o)
        return call[0], call[1].mtype.rettype


    def visitCall(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookupCase(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        code = ''
        for ind, x in enumerate(ast.param):
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(str1) is tuple:
                in_ = (in_[0] + str1[0], in_[1] + [typ1]) 
            else:
                if type(typ1) is IntType and type(sym.mtype.partype[ind]) is FloatType:
                    in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1] + [typ1])
                else:
                    # if type(typ1) is ArrayType:
                    #     str1 = self.copyArray(typ1, frame)
                    in_ = (in_[0] + str1, in_[1] + [typ1])
        code = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), sym
        return code

    def visitWith(self, ast,o):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        ctxt = o
        frame = ctxt.frame
       
        frame.enterScope(False)
        vardecls = [self.visit(x, (ctxt.frame, True)) for x in ast.decl]
        subBody = SubBody(frame, vardecls + ctxt.sym)
        stmt = ''.join([self.visit(x, subBody) for x in ast.stmt])
        frame.exitScope()
        return stmt

    def visitArrayCreate(self, ast, index, o, isStatic=False):
        #lower:int
        #upper:int
        #eleType:Type

        #variable:Id
        #varType: Type
        ctxt = o
        frame = ctxt


        size = ast.varType.upper - ast.varType.lower + 1
        sizeCode = self.emit.emitPUSHCONST(str(size), ast.varType, frame)
        if type(ast.varType.eleType) is StringType:
            createCode =  self.emit.jvm.emitANEWARRAY(self.emit.getFullType(ast.varType.eleType)) 
        else:
            createCode =  self.emit.jvm.emitNEWARRAY(self.emit.getFullType(ast.varType.eleType)) 
        if not isStatic:
            writeVarCode = self.emit.emitWRITEVAR(ast.variable.name, ArrayPointerType(ast.varType.eleType), index, frame)
        else:
            writeVarCode = self.emit.emitPUTSTATIC(self.className + "/" + ast.variable.name, ast.varType, frame)
        return self.emit.printout(sizeCode + createCode + writeVarCode)

    def visitArrayCell(self, ast, o):
        #arr:Expr
        #idx:Expr
        # TODO: Type inference
        return self.visitReadArray(ast, o), self.visit(ast.arr, o)[1].eleType

    def visitReverse(self, typ, frame):
        if type(typ) is BoolType:
            return  self.emit.emitPUSHICONST(1, frame) + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG(), BoolType()
        elif type(typ) is IntType:
            return self.emit.jvm.emitINEG()
        else:
            return self.emit.jvm.emitFNEG()

    def visitReadArray(self, ast, o):
        """
            Input: Array call
            Return: Value on top of stack
        """
        ctxt = o
        frame = ctxt.frame
        arrayType = self.visit(ast.arr, o)  # array_ref + array_padding, arrayType
        if arrayType[1].lower >= 0:
            indexCode = self.emit.emitPUSHCONST(arrayType[1].lower, IntType(), frame) + self.visit(ast.idx, o)[0] + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG()
        else:
            indexCode = self.emit.emitPUSHCONST(-arrayType[1].lower, IntType(), frame) + self.emit.jvm.emitINEG() + self.visit(ast.idx, o)[0] + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG()
        code = arrayType[0] + indexCode
        return code + self.emit.emitALOAD(arrayType[1].eleType, frame)

    def visitWriteArray(self, ast, value, o):
        """
            Input: ArrayCell, value_code
            Return: None (Write value)
            #arr:Expr
            #idx:Expr
        """
        
        ctxt = o
        frame = ctxt.frame
        arrayType = self.visit(ast.arr, o)  # array_ref, arrayType
        ad = self.emit.emitI2F(o.frame) if type(arrayType[1].eleType) is FloatType and type(value[1]) is IntType else ''
        if arrayType[1].lower >= 0:
            indexCode = self.emit.emitPUSHCONST(arrayType[1].lower, IntType(), frame) + self.visit(ast.idx, o)[0] + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG()
        else:
            indexCode = self.emit.emitPUSHCONST(-arrayType[1].lower, IntType(), frame) + self.emit.jvm.emitINEG() + self.visit(ast.idx, o)[0] + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG()
        return arrayType[0] + indexCode + value[0] + ad + self.emit.emitASTORE(arrayType[1].eleType, frame)

    def lookupCase(self, lexeme, lst, func):
        for sym in lst:
            if func(sym).lower() == lexeme.lower():
                return sym
        return None

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' +ast.value+'"', StringType(), o.frame), StringType()

    def writeVar(self, sym, frame):
        if type(sym.value) is Index:
            return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame)
        else:
            return self.emit.emitPUTSTATIC(self.className + "/" + sym.name, sym.mtype, frame)
            
    def readVar(self, sym, frame):
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
        else:
            return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame), sym.mtype

    def copyArray(self, sym, symCopy, o):
        """
        input ArrayType
        #lower:int
        #upper:int
        #eleType:Type
        """
        frame = o.frame
        size = sym.mtype.upper - sym.mtype.lower + 1
        if type(sym.mtype.eleType) is StringType:
            createCode =  self.emit.jvm.emitANEWARRAY(self.emit.getFullType(sym.mtype.eleType)) 
        else:
            createCode =  self.emit.jvm.emitNEWARRAY(self.emit.getFullType(sym.mtype.eleType)) 
        createCode = self.emit.emitPUSHICONST(size, frame) + createCode + self.emit.emitWRITEVAR(symCopy.name, ArrayPointerType(sym.mtype.eleType), symCopy.value.value, frame)
        code = []
        for index in range(sym.mtype.lower, sym.mtype.upper + 1):
            sCode = self.visit(Id(sym.name), o)[0] + self.visitWriteArray(ArrayCell(Id(symCopy.name), IntLiteral(index)), (self.visitReadArray(ArrayCell(Id(sym.name), IntLiteral(index)), o), sym.mtype.eleType), o)
            code.append(sCode)
        return createCode + ''.join(code)

            


    
        




