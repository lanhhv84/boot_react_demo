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
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName))
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

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)

        self.emit.printout('\n')

        for x in ast.decl:
            if type(x) is VarDecl:
                e.sym += [Symbol(x.variable.name, x.varType, CName(self.className))]
                code = self.emit.emitATTRIBUTE(x.variable.name, x.varType, False, "")
                self.emit.printout(code)
        
                

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", Frame("<init>", VoidType)))

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
        frame.enterScope(True)

        isInit = consdecl.returnType is None
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
            glenv += [sym]
            if type(sym.mtype) != ArrayType:
                self.emit.printout(self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))

        for var in consdecl.local:
            sym = self.visit(var, (frame, True))
            glenv += [sym]
            if type(sym.mtype) != ArrayType:
                self.emit.printout(self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.emit.printout(self.visit(x, SubBody(frame, glenv))), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
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
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

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
            return self.visitReverse(BoolType(), frame)
            
        elif ast.op.lower() == '-':
            """
                current_val
                current_val (dup) -> current_value*2
                sub
            """
            return self.visitReverse(code[1], frame)
            


    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        leftCode, leftType = self.visit(ast.left, o)
        rightCode, rightType = self.visit(ast.right, o)
        op = ast.op.lower()
        # Same type
        if type(leftType) == type(rightType):
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
            return code + self.emit.emitDIV(frame), FloatType()
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
            return code + self.emit.emitIDIV(frame), IntType()
        elif op == 'mod':
            return code + self.emit.emitMOD(frame), IntType()
        elif op in ['<', '<=', '>', '>=', '<>', '=']:
            return self.visitRELOP(code, op, IntType(), frame)
        elif op == '/':
            return leftCode + self.emit.emitI2F(frame) + rightCode + self.emit.emitI2F(frame) + self.emit.emitDIV(frame), FloatType()

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
        trueLabel = frame.getNewLabel()
        trueLabelCode = self.emit.emitLABEL(str(trueLabel), frame) + self.emit.emitPUSHICONST(1, frame)
        falseLabel = frame.getNewLabel()
        falseLabelCode = self.emit.emitLABEL(str(falseLabel), frame) + self.emit.emitPUSHICONST(0, frame)
        endCompLabel = frame.getNewLabel()
        return code + self.emit.emitRELOP(op, opType, str(trueLabel), str(falseLabel), frame) + trueLabelCode + self.emit.emitGOTO(str(endCompLabel), frame) + falseLabelCode + self.emit.emitLABEL(endCompLabel, frame), BoolType()

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        if sym is None:
            print(ast.name)
        if type(sym.mtype) is ArrayType:
            refCode = self.emit.emitREADVAR(sym.name, ArrayPointerType(sym.mtype.eleType), sym.value.value, frame)
            paddingCode = self.emit.emitPUSHICONST(sym.mtype.lower, frame)
            return refCode , sym.mtype
        elif type(sym.value) is Index:
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
            sym = self.lookup(ast.lhs.name, nenv, lambda x: x.name)
            ad = ''
            if type(_right[1]) is IntType and type(sym.mtype) is FloatType:
                ad = self.emit.emitI2F(frame)
            if type(sym.value) is Index:
                return _right[0] + ad + self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame)
            else:
                return _right[0] + ad + self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame)

    def visitVarDecl(self, ast,o):
        #variable:Id
        #varType: Type
        index = o[0].getNewIndex()
        if type(ast.varType) is ArrayType and o[1]:
            self.visitArrayCreate(ast, index, o[0])
        return Symbol(ast.variable.name, ast.varType, Index(index))

    def visitIf(self,ast,o):
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        ctxt = o
        frame = ctxt.frame
        expr = self.visit(ast.expr, ctxt)
        trueLabel = frame.getNewLabel()
        falseLabel = frame.getNewLabel()
        endIfLabel = frame.getNewLabel()
        trueStmt = ''.join([self.visit(x, ctxt) for x in ast.thenStmt])
        falseStmt = ''.join([self.visit(x, ctxt) for x in ast.elseStmt])       

        ans = expr[0]
        ans += self.emit.emitIFFALSE(falseLabel, frame)
        trueStmt = trueStmt + self.emit.emitGOTO(str(endIfLabel), frame)
        ans += self.emit.emitLABEL(str(trueLabel), frame) + trueStmt
        ans += self.emit.emitLABEL(str(falseLabel), frame) 
        ans += falseStmt 
        ans += self.emit.emitLABEL(str(endIfLabel), frame) 

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
        sym = self.lookup(ast.id.name, nenv, lambda x: x.name)
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

        assignCode = exp1[0] + self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame)
        preCondCode = self.emit.emitLABEL(preCondLabel, frame) + self.emit.emitREADVAR(sym.name, IntType(), sym.value.value, frame) + exp2[0]
        if ast.up:
            preCondCode += self.emit.emitIFICMPGT(endLabel, frame)
        else:
            preCondCode += self.emit.emitIFICMPLT(endLabel, frame)
        preCondCode += stmt
        postCondCode = self.emit.emitLABEL(postCondLabel, frame) + self.emit.emitREADVAR(sym.name, IntType(), sym.value.value, frame) + self.emit.emitPUSHICONST(1, frame)
        if ast.up:
            postCondCode += self.emit.emitADDOP('+', IntType(), frame)
        else:
            postCondCode += self.emit.emitADDOP('-', IntType(), frame)

        postCondCode += self.emit.emitWRITEVAR(sym.name, IntType(), sym.value.value, frame) + self.emit.emitGOTO(preCondLabel, frame)

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
            if type(ans[1]) is ArrayType:
                return ans[0] + self.emit.jvm.emitARETURN()
            return ans[0] + self.emit.emitRETURN(ans[1], frame)
        else:
            return ''

    def visitCallExpr(self, ast, o):
        call = self.visitCall(ast, o)
        return call[0], call[1].mtype.rettype


    def visitCall(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        code = ''
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True)) # (array_ref + array_padding), arrayType
            # import pdb
            # pdb.set_trace()
            if type(str1) is tuple:
                in_ = (in_[0] + str1[0], in_[1] + [typ1]) 
            else:
                in_ = (in_[0] + str1, in_[1] + [typ1])
        code = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame), sym
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

    def visitArrayCreate(self, ast, index, o):
        #lower:int
        #upper:int
        #eleType:Type

        #variable:Id
        #varType: Type
        ctxt = o
        frame = ctxt


        size = ast.varType.upper - ast.varType.lower + 1
        sizeCode = self.emit.emitPUSHCONST(str(size), ast.varType, frame)
        createCode =  self.emit.jvm.emitNEWARRAY(self.emit.getFullType(ast.varType.eleType)) 
        writeVarCode = self.emit.emitWRITEVAR(ast.variable.name, ArrayPointerType(ast.varType.eleType), index, frame)
        return self.emit.printout(sizeCode + createCode + writeVarCode)

    def visitArrayCell(self, ast, o):
        #arr:Expr
        #idx:Expr
        index = self.visit(ast.idx, o)
        # TODO: Type inference
        return self.visitReadArray(ast, index, o), self.visit(ast.arr, o)[1].eleType

    def visitReverse(self, typ, frame):
        if type(typ) is BoolType:
            return  self.emit.emitPUSHICONST(1, frame) + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG(), BoolType()
        else:
            return self.emit.jvm.emitINEG()

    def visitReadArray(self, ast, value, o):
        """
            Input: Array call
            Return: Value on top of stack
        """
        ctxt = o
        frame = ctxt.frame
        arrayType = self.visit(ast.arr, o)  # array_ref + array_padding, arrayType
        indexCode = self.emit.emitPUSHCONST(arrayType[1].lower, IntType(), frame) + self.visit(ast.idx, o)[0] + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG()
        code = arrayType[0] + indexCode
        return code + self.emit.jvm.emitIALOAD()

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
        indexCode = self.emit.emitPUSHCONST(arrayType[1].lower, IntType(), frame) + self.visit(ast.idx, o)[0] + self.emit.emitADDOP('-', IntType(), frame) + self.emit.jvm.emitINEG()
        return arrayType[0] + indexCode + value[0] + self.emit.jvm.emitIASTORE()


    

        


    





            


    
        




