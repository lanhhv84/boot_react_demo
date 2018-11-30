import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_putINT_2(self):
        inp = """
        procedure main();
        begin
            putIntLn(10);
        end
        """
        exp = "10\n"
        self.assertTrue(TestCodeGen.test(inp,exp,402))

    def test_putINT_3(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            putInt(a);
        end
        """
        exp = "10"
        self.assertTrue(TestCodeGen.test(inp,exp,403))

    def test_putINT_4(self):
        inp = """
        
        procedure main();
        var a: real;
        begin
            a := 10;
            putFloat(a + 3);
        end
        """
        exp = "13.0"
        self.assertTrue(TestCodeGen.test(inp,exp,404))

    def test_if_5(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            if (a > 5) then
            begin
                putInt(1);
            end
            else
            begin
                putInt(0);
            end
        end
        """
        exp = "1"
        self.assertTrue(TestCodeGen.test(inp,exp,405))

    def test_if_6(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            if (a = 5) then
            begin
                putInt(1);
            end
            else
            begin
                putInt(0);
            end
        end
        """
        exp = "0"
        self.assertTrue(TestCodeGen.test(inp,exp,406))

    def test_if_7(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            if (a <> 5) then
                if (a > 5) then
                    putInt(1);
                else
                    putInt(0);
            else
            begin
                putInt(0);
            end

            
        end
        """
        exp = "1"
        self.assertTrue(TestCodeGen.test(inp,exp,407))

    def test_while_8(self):
        inp = """
        procedure main();
         var a: integer;
         begin
             a := 10;
             while (a <> 5) do
             begin
                putInt(a);
                a := a - 1;
             end
         end
        """
        exp = "109876"
        self.assertTrue(TestCodeGen.test(inp,exp,408))

    def test_while_9(self):
        inp = """
        procedure main();
         var a: integer;
         begin
             a := 5;
             while (a <> 5) do
             begin
                putInt(a);
                a := a - 1;
             end
         end
        """
        exp = ""
        self.assertTrue(TestCodeGen.test(inp,exp,409))

    def test_break_10(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            while (a > 0) do
            begin
                if (a = 5) then
                    break;
                a := a - 1;
                putInt(a);
            end
        end
        """
        exp = "98765"
        self.assertTrue(TestCodeGen.test(inp,exp,410))

    def test_break_11(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            a := 10;
            while (a > 0) do
            begin
                b := 10;
                while (b > 0) do
                begin 
                    if (b = 5) then
                        break;
                    b := b - 1;
                    putInt(b);
                end 
                a := a - 1;
                putInt(a);
            end
        end
        """
        exp = "987659987658987657987656987655987654987653987652987651987650"
        self.assertTrue(TestCodeGen.test(inp,exp,411))

    def test_continue_12(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            b := 10;
            while (b > 0) do
            begin
                if ((b mod 5) = 0) then
                begin
                    b := b - 1;
                    continue;
                end
                b := b - 1;
                putInt(b);
            
            end
        end
        """
        exp = "87653210"
        self.assertTrue(TestCodeGen.test(inp,exp,412))

    def test_mode_13(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            b := 9;
            putInt(b mod 5);
        end
        """
        exp = "4"
        self.assertTrue(TestCodeGen.test(inp,exp,413))

    def test_for_14(self):
        inp = """
        procedure main();
        var i : integer;
        begin
        for i := 0 to 10 do 
            putInt(i);
        end
        """
        exp = "012345678910"
        self.assertTrue(TestCodeGen.test(inp,exp,414))

    def test_for_15(self):
        inp = """
        procedure main();
        var i : integer;
        begin
        for i := 10 downto 0 do 
            putInt(i);
        end
        """
        exp = "109876543210"
        self.assertTrue(TestCodeGen.test(inp,exp,415))

    def test_for_16(self):
        inp = """
        procedure main();
        var i : integer;
        begin
        for i := 0 to 10 do 
        begin
            if (i = 5) then
                continue;
            putInt(i);
        end
        end
        """
        exp = "01234678910"
        self.assertTrue(TestCodeGen.test(inp,exp,416))

    def test_for_17(self):
        inp = """
        procedure main();
        var i : integer;
        begin
        for i := 0 to 10 do 
        begin
            if (i = 5) then
                break;
            putInt(i);
        end
        end
        """
        exp = "01234"
        self.assertTrue(TestCodeGen.test(inp,exp,417))

    def test_for_18(self):
        inp = """
        procedure main();
        begin
            putInt(abc());
            return;
        end

        function abc(): integer;
        var ans, i: integer;
        begin
            ans := 0;
            for i := 0 to 10 do
                ans := ans + i;
            return ans;
        end
        """

        exp = "55"
        self.assertTrue(TestCodeGen.test(inp,exp,418))

    def test_with_419(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            a := 3;
            b := 3;
            with a, b: integer; do
                begin
                    a := 10;
                    b := 10;
                end

            putIntLn(a);
            putIntLn(b);
        end
        """
        exp = "3\n3\n"
        self.assertTrue(TestCodeGen.test(inp,exp,419))

    def test_array_20(self):
        inp = """
        procedure main();
        var a, b: integer;
            c: array [99 .. 102] of integer;
        begin
            c[99] := 123;
            a := c[99];
            putIntLn(a);
            putIntLn(c[99]);
        end
        """
        exp = "123\n123\n"
        self.assertTrue(TestCodeGen.test(inp,exp,420))

    def test_array_21(self):
        inp = """
        
        procedure main();
        var a, b: integer;
            c: array [1 .. 2] of integer;
        begin
            c[1] := 69;
            putInt(69);
            returnArray(69);
        end

        procedure returnArray(a69: integer);
        begin
            putInt(69);
        end
        
        """
        
        exp = "6969"
        self.assertTrue(TestCodeGen.test(inp,exp,421))

    def test_global_22(self):
        inp = """
        var hxhx: integer;
        procedure main();
        begin
            hxhx := 69;
            ts();
        end

        procedure ts();
        begin
            putInt(hxhx);
        end
        """
        exp = "69"
        self.assertTrue(TestCodeGen.test(inp,exp,422))

    def test_global_23(self):
        inp = """
        var hxhx: integer;
        procedure main();
        begin
            hxhx := 69;
            ts(hxhx);
        end

        procedure ts(a: integer);
        begin
            putInt(a);
        end
        """
        exp = "69"
        self.assertTrue(TestCodeGen.test(inp,exp,423))

    def test_func_24(self):
        inp = """
        procedure main();
        begin
            main2(60);
        end

        procedure main2(a: integer);
        begin
            putInt(a);
        end
        """

        exp = "60"
        self.assertTrue(TestCodeGen.test(inp,exp,424))

    def test_func_25(self):
        inp = """
        procedure main();
        var ar: array [99 .. 102] of integer;
            ind: integer;
        begin
            ind := 101;
            ar[ind] := 69;
            main2(ar, ind);
        end

        procedure main2(arr: array [99 .. 102] of integer; a: integer);
        begin
            putInt(arr[a]);
        end
        """
        exp = "69"
        self.assertTrue(TestCodeGen.test(inp,exp,425))

    def test_func_26(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            a := 5;
            b := 9;
            putInt(sum(a, b));
        end

        function sum(x, y: integer): integer;
        begin
            return x + y;
        end
        """
        exp = "14"
        self.assertTrue(TestCodeGen.test(inp,exp,426))

    def test_func_27(self):
        inp = """
        procedure main();
        var a, b: integer;
            c: array [69 .. 96] of integer;
        begin
            a := 5;
            b := 9;
            c[80] := 100;
            putInt(sum(sum(a, b), c[80]));
        end

        function sum(x, y: integer): integer;
        begin
            return x + y;
        end
        """
        exp = "114"
        self.assertTrue(TestCodeGen.test(inp,exp,427))

    def test_arr_428(self):
        inp = """
        procedure main();
        var a: array [1 .. 10] of integer;
        begin
            putInt(a[2]);
        end
        """
        exp = "0"
        self.assertTrue(TestCodeGen.test(inp,exp,428))

    def test_arr_429(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            putInt(arrret());
        end

        function arrret(): integer;
        var i: integer;
        begin
            i := 2;
            return i;
        end
        """
        exp = "2"
        self.assertTrue(TestCodeGen.test(inp,exp,429))

    def test_arr_430(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 10 do
                putInt(arrret()[i]);
        end
        function arrSum(a: array [0 .. 10] of integer; b: array [0 .. 10] of integer): array [1 .. 10] of integer;
        var ans: array [0 .. 10] of integer;
            i: integer;
        begin
            for i := 0 to 10 do
                ans[i] := a[i] + b[i];
            return ans;
        end

        function arrret(): array [0 .. 10] of integer;
        var i: integer;
            arr:  array [0 .. 10] of integer;
        begin
            for i := 0 to 10 do
                arr[i] := i;
            return arr;
        end
        """
        exp = "012345678910"
        self.assertTrue(TestCodeGen.test(inp,exp,430))

    def test_arr_431(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 10 do
                putInt(arrSum(arrret(), arrret())[i]);
        end
        function arrSum(a: array [0 .. 10] of integer; b: array [0 .. 10] of integer): array [0 .. 10] of integer;
        var ans: array [0 .. 10] of integer;
            i: integer;
        begin
            for i := 0 to 10 do
                ans[i] := a[i] + b[i];
            return ans;
        end

        function arrret(): array [0 .. 10] of integer;
        var i: integer;
            arr:  array [0 .. 10] of integer;
        begin
            for i := 0 to 10 do
                arr[i] := i;
            return arr;
        end
        """
        exp = "02468101214161820"
        self.assertTrue(TestCodeGen.test(inp,exp,431))

    def test_for_32(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 2 to 10 do
                putInt(i);
        end
        """
        exp = "2345678910"
        self.assertTrue(TestCodeGen.test(inp,exp,432))

    def test_arr_433(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 1 to 10 do
                putInt(arrSum(arrret(), arrret())[i]);
        end
        function arrSum(a: array [1 .. 10] of integer; b: array [1 .. 10] of integer): array [1 .. 10] of integer;
        var ans: array [1 .. 10] of integer;
            i: integer;
        begin
            for i := 1 to 10 do
                ans[i] := a[i] + b[i];
            return ans;
        end

        function arrret(): array [1 .. 10] of integer;
        var i: integer;
            arr:  array [1 .. 10] of integer;
        begin
            for i := 1 to 10 do
                arr[i] := i;
            return arr;
        end
        """
        exp = "2468101214161820"
        self.assertTrue(TestCodeGen.test(inp,exp,433))

    def test_cmp_434(self):
        inp = """
        procedure main();
        begin
            if (1.0 > 2.0) then
                putInt(1);
            else
                putInt(2);
        end
        """
        exp = "2"
        self.assertTrue(TestCodeGen.test(inp,exp,434))

    def test_cmp_435(self):
        inp = """
        procedure main();
        begin
            if (1 > 2) then
                putInt(1);
            else
                putInt(2);
        end
        """
        exp = "2"
        self.assertTrue(TestCodeGen.test(inp,exp,435))

    def test_arr_global_36(self):
        inp = """
        var hxhx: array [1 .. 10] of integer;
        procedure main();
        begin
            hxhx[3] := 10;
            putInt(hxhx[3]);
        end
        """
        exp = "10"
        self.assertTrue(TestCodeGen.test(inp,exp,436))

    def test_shortcut_37(self):
        inp = """
        procedure main();
        var b: array[0 .. 10] of integer;
        begin
            b[0] := 1 + 1*1;
            putInt(b[0]);
        end
        """
        exp = "2"
        self.assertTrue(TestCodeGen.test(inp,exp,437))

    def test_advanced_binary_op_4(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                putBoolLn(12 < 5.0);
                putBoolLn(12 < 12.0);
                putBoolLn(78.34 < 12.0);
                putBoolLn(78.34 < 12);
                putBoolLn(12.0 < 24);
                putBoolLn(78.0 < 120);
            end
        """
        expect = """false
false
false
false
true
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,438))

    def test_advanced_binary_op_5(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                x := 12;
                y := 4/5 * x / 34 - 3 + 76 /4 - -----4 * 7 -----7 ----- 7;
                putFloatLn(y);
                putBoolLn(y <= 5.0);
                putBoolLn(y >= 5.0);
                putBoolLn(y = 5);
                putBoolLn(x >= 12.0);
                putBoolLn(x <= 12);
                putBoolLn(x = 12);
            end
        """
        expect = """30.282352
false
true
false
true
true
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,439))

    def test_advanced_binary_op_6(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                x := 12;
                y := x * x / x / x;
                putFloatLn(y);
                putFloatLn(x);
                x := x * -7 mod 19 div 2 mod 4;
                y := (87 * x mod 12) / 45 * 78 + -------34;
                putFloatLn(y);
                putFloatLn(x);
            end
        """
        expect = """1.0
12.0
-34.0
0.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,440))

    def test_unary__op_advanced_1(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                putBoolLn( not true and not false);
                putBoolLn( not (12/5=9) and (4 = 4));
            end
        """
        expect = """false
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,441))

    def test_unary__op_advanced_2(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                putFloatLn(-23-34);
                putFloatLn(-3232323.23232665656);
            end
        """
        expect = """-57.0
-3232323.2
"""
        self.assertTrue(TestCodeGen.test(input,expect,442))

    def test_call_recursive_complex_1(self):
        input = """
            function fibo(n: integer): integer;
            begin
                if (n = 0) or (n = 1) then
                    return n;
                else 
                    return fibo(n-1) + fibo(n-2);
            end

            procedure main();
            var x: integer; 
            begin 
                x := 28;
                putIntLn(fibo(x));
                putIntLn(fibo(7));
            end
        """
        expect = """317811
13
"""
        self.assertTrue(TestCodeGen.test(input,expect,443))

    def test_call_recursive_complex_2(self):
        input = """
            function foo1(n: integer): integer;
            begin
                if (n = 0) then
                    return 0;
                putIntLn(n);
                return foo2(n-1);
            end

            function foo2(n: integer): integer;
            begin
                if (n = 0) then
                    return 0;
                putIntLn(n);
                return foo3(n-1);
            end

            function foo3(n: integer): integer;
            begin
                if (n = 0) then
                    return 0;
                putIntLn(n);
                return foo1(n-1);
            end

            var n: integer;

            procedure main();
            var x: integer; 
            begin 
                n := 10;
                x := foo1(n);
            end
        """
        expect = """10
9
8
7
6
5
4
3
2
1
"""
        self.assertTrue(TestCodeGen.test(input,expect,444))

    def test_build_in_function(self):
        input = """
            procedure main();
            var x: integer; 
            begin 
                putSTRING("PPL \\n 2018");
                putLN();
                putSTRINGLn("PPL \\n 2018");
                putBOOL(true);
                putBoolLN(false);
                putFloat(45);
                putFloat(45.6);
                putFloatLn(45);
                putFloatLN(45.25);
                putInt(89);
                putINTLN(343);  
            end
        """
        expect = """PPL 
 2018
PPL 
 2018
truefalse
45.045.645.0
45.25
89343
"""
        self.assertTrue(TestCodeGen.test(input,expect,445))

    def test_with_446(self):
        input = """
        var i:integer;
        procedure main();
        begin
            i := 1;
            with i:integer; do
            begin
                i := 2;
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 446))

    def test_if_447(self):
        input = """
        procedure main();
        begin
            if true then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 447))

    def test_if_448(self):
        input = """
        procedure main();
        begin
            if false then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 448))

    def test_for_449(self):
        input = """
        var i:integer;
        procedure main();
        var x:integer;
        begin
            x := 0;
            for x:=1 to 3 do
            begin
                putInt(x);
            end
        end
        """
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 449))

    def test_array_450(self):
        input = """
        var a:array[-1 .. 1] of integer;
        var b:array[3 .. 5] of real;
        procedure main();
        begin
            a[0] := 1;
            b[4] := 2.0;
            putInt(a[0]);
            putFloat(b[4]);
        end
        """
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 450))

    def test_array_khoa_451(self):
        input = """
		procedure main();
		var x: array [1 .. 5] of integer;
		begin
			x[2] := 3;
			putInt(x[2]);
			return;
		end
		"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 451))

    def test_binop_452(self):
        input = """
		procedure main();
		begin
			putIntLn(1+2);
            putIntLn(1-2);
            putIntLn(1*2);
            putIntLn(1 div 2);
            putIntLn(31 mod 4);
            putFloatLn(1/2);
            putBoolLn(1 > 2);
            putBoolLn(1 < 2);
            putBoolLn(1 <= 2);
			return;
		end
		"""
        expect = "3\n-1\n2\n0\n3\n0.5\nfalse\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 452))

    def test_binop_453(self):
        input = """
		procedure main();
		begin
            // same result as AND
			putBoolLn(true and then false);
            putBoolLn(true and then true);
            putBoolLn(false and then true);
            putBoolLn(false and then false);
            // skip evaluation of the second operand --> no error
            putBoolLn(false and then 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 453))

    def test_binop_454(self):
        input = """
		procedure main();
		begin
            // same result as OR
			putBoolLn(false or else false);
            putBoolLn(false or else true);
            putBoolLn(true or else true);
            putBoolLn(true or else false);
            // skip evaluation of the second operand --> no error
            putBoolLn(true or else 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 454))

    def test_binop_455(self):
        input = """
        function foo():real;
        begin
            return 1;
        end

		procedure main();
		begin
            putFloat(foo());
		end
		"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 455))

    def test_array_456(self):
        input = """
        function foo(): array [-2 .. 2] of string;
        var x: array [-2 .. 2] of string;
        i:integer;
        begin
            for i := -2 to 2 do
                x[i] := "HELLO";
            return x;
        end

        procedure printArray(a : array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                putStringLn(a[i]);
        end

		procedure main();
		begin
            printArray(foo());
		end
		"""
        expect = "HELLO\nHELLO\nHELLO\nHELLO\nHELLO\n"
        self.assertTrue(TestCodeGen.test(input, expect, 456))

    def test_array_457(self):
        input = """
        procedure hello(x: array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                x[i] := "HELLO";
        end

        procedure goodbye(x: array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                x[i] := "GOODBYE";
        end

        procedure printArray(a : array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                putStringLn(a[i]);
        end

		procedure main();
        var arr : array[-2 .. 2] of string;
        i:integer;
		begin
            // Init array
            for i := -2 to 2 do
                arr[i] := "HI"; 
            hello(arr);
            printArray(arr);
            goodbye(arr);
            printArray(arr);
		end
		"""
        expect = "HI\nHI\nHI\nHI\nHI\nHI\nHI\nHI\nHI\nHI\n"
        self.assertTrue(TestCodeGen.test(input, expect, 457))

    

    def test_while_514(self):
        input = """
        procedure main();
        var i:integer;
        begin
            i := 0;
            while i < 5 do
            begin
                putInt(i);
                i := i + 1;
            end
        end
		"""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 458))

    def test_while_459(self):
        input = """
        procedure main();
        var i:integer;
        begin
            i := 0;
            while true do
            begin
                if i = 5 then break;
                putInt(i);
                i := i + 1;
            end
        end
		"""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 459))

    def test_array_460(self):
        input = """
        procedure main();
        var a:array [1 .. 3] of integer;
        i:integer;
        begin
            for i:=1 to 3 do
            begin
                a[i] := i;
                putInt(a[i]);
            end     
        end
		"""
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 460))
    
    def test_exp_461(self):
        input = """
        procedure main();
        begin
            putInt(1+1-2*3);
        end
		"""
        expect = "-4"
        self.assertTrue(TestCodeGen.test(input, expect, 461))

    def test_exp_462(self):
        input = """
        procedure main();
        begin
            putFloatLn(-2/5);
            putIntLn((27 mod 8));
            putIntLn(27 div -3);
            putInt(-28 div -3);
        end
		"""
        expect = "-0.4\n3\n-9\n9"
        self.assertTrue(TestCodeGen.test(input, expect, 462))

    def test_exp_463(self):
        input = """
        procedure main();
        begin
            putFloatLn(1/1);
            putFloatLn(1./1);
            putFloatLn(1/1.);
            putFloatLn(1./1.);
            putFloat(1./1. - 1/1);
        end
		"""
        expect = "1.0\n1.0\n1.0\n1.0\n0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 463))

    def test_exp_464(self):
        input = """
        procedure main();
        begin
            putFloatLn(----------3.14e10);
            putIntLn(0 div 1);
            putFloat(-0 / -1);
        end
		"""
        expect = "3.13999995E10\n0\n-0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 464))

    def test_exp_465(self):
        input = """
        procedure main();
        var x,y,z:integer;
        begin
            x := 1;
            y := 2;
            z := -5;
            putInt(x+y-z*3);
        end
		"""
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 465))

    def test_global_array_init_466(self):
        input = """
        var a : array [0 .. 4] of integer;

        procedure main();
        begin
        end
		"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 466))

    def test_467(self):
        inp = """
        procedure main();
        begin
            putBool(true or else (1 = (1/0)));
        end
        """
        exp = "true"
        self.assertTrue(TestCodeGen.test(inp, exp, 467))


    def test_468(self):
        inp = """
        procedure main();
        begin
            putBool(False and then (1 = (1/0)));
        end
        """
        exp = "false"
        self.assertTrue(TestCodeGen.test(inp, exp, 468))

    def test_469(self):
        inp = """
        procedure main();
        begin
            putiNt(100);
        end
        """
        exp = "100"
        self.assertTrue(TestCodeGen.test(inp, exp, 469))

    def test_470(self):
        inp = """
            var x: integer;
            procedure main();
            var x: integer;
            begin
                x := 2;
                foo();
                putInT(x);
            end

            procedure foo();
            begin
                x := 10;
            end
        """
        exp = "2"
        self.assertTrue(TestCodeGen.test(inp, exp, 470))

    def test_471(self):
        inp = """
        procedure main();
        var A, B: integer;
        begin
            a := 96;
            b := 96;
            with a, b: integer; do
                begin
                    a := 69;
                    b := 69;
                    putINT(A);
                    putInt(B);
                end
            putInt(A);
            putInt(B);
        end
        """
        exp = "69699696"
        self.assertTrue(TestCodeGen.test(inp, exp, 471))

    def test_472(self):
        inp = """
        var XxX: integer;
        procedure main();
        var xXx: integer;
        begin
        xxx := 10;
        with xxx: integer; do
            begin
            xxx := 100;
            foo();
            if (xxx > 10) then
                putInt(10);
            else
                putInt(0);
            end
        end

        procedure foo();
        begin
            xxx := 10;
        end
        """

        exp = "10"
        self.assertTrue(TestCodeGen.test(inp, exp, 472))

    def test_num_473(self):
        inp = """
        procedure main();
        var a, b: integer;
            c, d: integer;
            e: real;
        begin
            a := -2147483647;
            b := 2147483647;
            c := 100;
            d := 100;
            e := 100;
            putFloat(a + b);
            putFloat(a/b);
            putInt(a div b);
            putFloat(c);
            putFloat(d);
            putFLoat(e);
        end
        """

        exp = "0.0-1.0-1100.0100.0100.0"
        self.assertTrue(TestCodeGen.test(inp, exp, 473))

    def test_bin_op_int_474(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            a := 69;
            b := 96;
            putInt(a + b);
            putInt(a - b);
            putInt(a div b);
            putInt(a mod b);
            putInt(a * b);
            putBool(a < b);
            putBool(a > b);
            putBool(a <= b);
            putBool(a >= b);
            putBool(a <> b);
            putBool(a = b);
        end
        """
        exp = "165-270696624truefalsetruefalsetruefalse"
        self.assertTrue(TestCodeGen.test(inp, exp, 474))

    def test_bin_op_real_475(self):
        inp = """
        procedure main();
        var a, b: real;
        begin
        a := 69;
        b := 96;
        putFloat(a + b);
        putFloat(a - b);
        putFloat(a * b);
        putFloat(a/b);
        putBool(a < b);
        putBool(a > b);
        putBool(a <= b);
        putBool(a >= b);
        putBool(a <> b);
        putBool(a = b);
        end
        """
        exp = "165.0-27.06624.00.71875truefalsetruefalsetruefalse"
        self.assertTrue(TestCodeGen.test(inp, exp, 475))

    def test_476(self):
        inp = """
        procedure main();
        var a: integer;
            b: array [1 .. 3] of integer;
            x: integer;
        begin
            a := b[3] := foo()[3] := x := 1;
            putInt(a);
            putInt(b[3]);
            putInt(foo()[3]);
            putInt(x);
            return;
        end

        function foo(): array [1 .. 3] of integer;
        var arr: array [1 .. 3] of integer;
        begin
            return arr;
        end
        """

        exp = "0001"
        self.assertTrue(TestCodeGen.test(inp, exp, 476))

    def test_assign_477(self):
        inp = """
        procedure main();
        var a: integer;
            b: array [1 .. 3] of integer;
            x: integer;
        begin
            foo()[3] := a := b[3] := x := 1;
            putInt(a);
            putInt(b[3]);
            putInt(foo()[3]);
            putInt(x);
            return;
        end

        function foo(): array [1 .. 3] of integer;
        var arr: array [1 .. 3] of integer;
        begin
            return arr;
        end
        """

        exp = "1101"
        self.assertTrue(TestCodeGen.test(inp, exp, 477))

    def test_for_478(self):
        inp = """

        procedure main();
        var i: real;
            sum: integer;
        begin
            sum := 0;
            with i: integer; do
            begin
                for i :=0 to 100 do
                    sum := sum + i;
            end
            putInt(Sum);
        end
        """
        exp = "5050"
        self.assertTrue(TestCodeGen.test(inp, exp, 478))

    def test_bin_op_real_479(self):
        inp = """
        procedure main();
        var a, b: real;
        begin
        a := 69;
        b := 96;
        putFloat(a + b);
        putFloat(a - b);
        putFloat(a * b);
        putFloat(a/b);
        putBool(a < b);
        putBool(a > b);
        putBool(a <= b);
        putBool(a >= b);
        putBool(a <> b);
        putBool(a = b);
        end
        """
        exp = "165.0-27.06624.00.71875truefalsetruefalsetruefalse"
        self.assertTrue(TestCodeGen.test(inp, exp, 479))

    def test_480(self):
        inp = """
        procedure main();
        var a: integer;
            b: array [1 .. 3] of integer;
            x: integer;
        begin
            a := b[3] := foo()[3] := x := 1;
            putInt(a);
            putInt(b[3]);
            putInt(foo()[3]);
            putInt(x);
            return;
        end

        function foo(): array [1 .. 3] of integer;
        var arr: array [1 .. 3] of integer;
        begin
            return arr;
        end
        """

        exp = "0001"
        self.assertTrue(TestCodeGen.test(inp, exp, 480))

    def test_assign_481(self):
        inp = """
        procedure main();
        var a: integer;
            b: array [1 .. 3] of integer;
            x: integer;
        begin
            foo()[3] := a := b[3] := x := 1;
            putInt(a);
            putInt(b[3]);
            putInt(foo()[3]);
            putInt(x);
            return;
        end

        function foo(): array [1 .. 3] of integer;
        var arr: array [1 .. 3] of integer;
        begin
            return arr;
        end
        """

        exp = "1101"
        self.assertTrue(TestCodeGen.test(inp, exp, 481))

    def test_for_482(self):
        inp = """

        procedure main();
        var i: real;
            sum: integer;
        begin
            sum := 0;
            with i: integer; do
            begin
                for i :=0 to 100 do
                    sum := sum + i;
            end
            putInt(Sum);
        end
        """
        exp = "5050"
        self.assertTrue(TestCodeGen.test(inp, exp, 482))

    def test_for_483(self):
        inp = """

        procedure main();
        var i: real;
        begin
            with i: integer; do
            begin
                for i := 0 to 100 do
                    begin
                        putInt(i);
                        if (i = 5) then
                            return;
                    end
            end
            PutSTRING("Chackhongindau");
        end
        """
        exp = "012345"
        self.assertTrue(TestCodeGen.test(inp, exp, 483))

    def test_for_484(self):
        inp = """

        procedure main();
        var i: real;
        begin
            with i: integer; do
            begin
                for i := 0 to 100 do
                    begin
                        putInt(i);
                        if (i = 5) then
                            BREAK;
                    end
            end
            PutSTRING("Chackhongindau");
        end
        """
        exp = "012345Chackhongindau"
        self.assertTrue(TestCodeGen.test(inp, exp, 484))

    def test_for_485(self):
        inp = """
        procedure main();
        var d: real;
        begin
        d := 0;
            with a , b :integer ; c:array [1 .. 2] of real ; do
            begin
                a := 2;
                b := 4;
                c[a] := 0;
                d := c[a] + b;
            end
            putFloat(d);
        end
        """
        exp = "4.0"
        self.assertTrue(TestCodeGen.test(inp, exp, 485))
    
    
    def test_putINT_486(self):
        inp = """
        procedure main();
        begin
            putIntLn(10);
        end
        """
        exp = "10\n"
        self.assertTrue(TestCodeGen.test(inp,exp,486))

    def test_putINT_487(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            putInt(a);
        end
        """
        exp = "10"
        self.assertTrue(TestCodeGen.test(inp,exp,487))

    def test_putINT_488(self):
        inp = """
        
        procedure main();
        var a: real;
        begin
            a := 10;
            putFloat(a + 3);
        end
        """
        exp = "13.0"
        self.assertTrue(TestCodeGen.test(inp,exp,488))

    def test_if_489(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            if (a > 5) then
            begin
                putInt(1);
            end
            else
            begin
                putInt(0);
            end
        end
        """
        exp = "1"
        self.assertTrue(TestCodeGen.test(inp,exp,489))

    def test_if_490(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            if (a = 5) then
            begin
                putInt(1);
            end
            else
            begin
                putInt(0);
            end
        end
        """
        exp = "0"
        self.assertTrue(TestCodeGen.test(inp,exp,490))

    def test_if_491(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            if (a <> 5) then
                if (a > 5) then
                    putInt(1);
                else
                    putInt(0);
            else
            begin
                putInt(0);
            end

            
        end
        """
        exp = "1"
        self.assertTrue(TestCodeGen.test(inp,exp,491))

    def test_while_492(self):
        inp = """
        procedure main();
         var a: integer;
         begin
             a := 10;
             while (a <> 5) do
             begin
                putInt(a);
                a := a - 1;
             end
         end
        """
        exp = "109876"
        self.assertTrue(TestCodeGen.test(inp,exp,492))

    def test_while_493(self):
        inp = """
        procedure main();
         var a: integer;
         begin
             a := 5;
             while (a <> 5) do
             begin
                putInt(a);
                a := a - 1;
             end
         end
        """
        exp = ""
        self.assertTrue(TestCodeGen.test(inp,exp,493))

    def test_break_494(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := 10;
            while (a > 0) do
            begin
                if (a = 5) then
                    break;
                a := a - 1;
                putInt(a);
            end
        end
        """
        exp = "98765"
        self.assertTrue(TestCodeGen.test(inp,exp,494))

    def test_break_495(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            a := 10;
            while (a > 0) do
            begin
                b := 10;
                while (b > 0) do
                begin 
                    if (b = 5) then
                        break;
                    b := b - 1;
                    putInt(b);
                end 
                a := a - 1;
                putInt(a);
            end
        end
        """
        exp = "987659987658987657987656987655987654987653987652987651987650"
        self.assertTrue(TestCodeGen.test(inp,exp,495))

    def test_continue_496(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            b := 10;
            while (b > 0) do
            begin
                if ((b mod 5) = 0) then
                begin
                    b := b - 1;
                    continue;
                end
                b := b - 1;
                putInt(b);
            
            end
        end
        """
        exp = "87653210"
        self.assertTrue(TestCodeGen.test(inp,exp,496))

    def test_mode_97(self):
        inp = """
        procedure main();
        var a, b: integer;
        begin
            b := 9;
            putInt(b mod 5);
        end
        """
        exp = "4"
        self.assertTrue(TestCodeGen.test(inp,exp,497))

    def test_for_498(self):
        inp = """
        procedure main();
        var i : integer;
        begin
        for i := 0 to 10 do 
            putInt(i);
        end
        """
        exp = "012345678910"
        self.assertTrue(TestCodeGen.test(inp,exp,498))

    def test_for_499(self):
        inp = """
        procedure main();
        var i : integer;
        begin
        for i := 10 downto 0 do 
            putInt(i);
        end
        """
        exp = "109876543210"
        self.assertTrue(TestCodeGen.test(inp,exp,499))

