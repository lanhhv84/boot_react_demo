import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin putInt(100); end"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_putINT_2(self):
    #     inp = """
    #     procedure main();
    #     begin
    #         putIntLn(10);
    #     end
    #     """
    #     exp = "10\n"
    #     self.assertTrue(TestCodeGen.test(inp,exp,402))

    # def test_putINT_3(self):
    #     inp = """
    #     procedure main();
    #     var a: integer;
    #     begin
    #         a := 10;
    #         putInt(a);
    #     end
    #     """
    #     exp = "10"
    #     self.assertTrue(TestCodeGen.test(inp,exp,403))

    # def test_putINT_4(self):
    #     inp = """
        
    #     procedure main();
    #     var a: real;
    #     begin
    #         a := 10;
    #         putFloat(a + 3);
    #     end
    #     """
    #     exp = "13.0"
    #     self.assertTrue(TestCodeGen.test(inp,exp,404))

    # def test_if_5(self):
    #     inp = """
    #     procedure main();
    #     var a: integer;
    #     begin
    #         a := 10;
    #         if (a > 5) then
    #         begin
    #             putInt(1);
    #         end
    #         else
    #         begin
    #             putInt(0);
    #         end
    #     end
    #     """
    #     exp = "1"
    #     self.assertTrue(TestCodeGen.test(inp,exp,405))

    # def test_if_6(self):
    #     inp = """
    #     procedure main();
    #     var a: integer;
    #     begin
    #         a := 10;
    #         if (a = 5) then
    #         begin
    #             putInt(1);
    #         end
    #         else
    #         begin
    #             putInt(0);
    #         end
    #     end
    #     """
    #     exp = "0"
    #     self.assertTrue(TestCodeGen.test(inp,exp,406))

    # def test_if_7(self):
    #     inp = """
    #     procedure main();
    #     var a: integer;
    #     begin
    #         a := 10;
    #         if (a <> 5) then
    #             if (a > 5) then
    #                 putInt(1);
    #             else
    #                 putInt(0);
    #         else
    #         begin
    #             putInt(0);
    #         end

            
    #     end
    #     """
    #     exp = "1"
    #     self.assertTrue(TestCodeGen.test(inp,exp,407))

    # def test_while_8(self):
    #     inp = """
    #     procedure main();
    #      var a: integer;
    #      begin
    #          a := 10;
    #          while (a <> 5) do
    #          begin
    #             putInt(a);
    #             a := a - 1;
    #          end
    #      end
    #     """
    #     exp = "109876"
    #     self.assertTrue(TestCodeGen.test(inp,exp,408))

    # def test_while_9(self):
    #     inp = """
    #     procedure main();
    #      var a: integer;
    #      begin
    #          a := 5;
    #          while (a <> 5) do
    #          begin
    #             putInt(a);
    #             a := a - 1;
    #          end
    #      end
    #     """
    #     exp = ""
    #     self.assertTrue(TestCodeGen.test(inp,exp,409))

    # def test_break_10(self):
    #     inp = """
    #     procedure main();
    #     var a: integer;
    #     begin
    #         a := 10;
    #         while (a > 0) do
    #         begin
    #             if (a = 5) then
    #                 break;
    #             a := a - 1;
    #             putInt(a);
    #         end
    #     end
    #     """
    #     exp = "98765"
    #     self.assertTrue(TestCodeGen.test(inp,exp,410))

    # def test_break_11(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #     begin
    #         a := 10;
    #         while (a > 0) do
    #         begin
    #             b := 10;
    #             while (b > 0) do
    #             begin 
    #                 if (b = 5) then
    #                     break;
    #                 b := b - 1;
    #                 putInt(b);
    #             end 
    #             a := a - 1;
    #             putInt(a);
    #         end
    #     end
    #     """
    #     exp = "987659987658987657987656987655987654987653987652987651987650"
    #     self.assertTrue(TestCodeGen.test(inp,exp,411))

    # def test_continue_12(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #     begin
    #         b := 10;
    #         while (b > 0) do
    #         begin
    #             if ((b mod 5) = 0) then
    #             begin
    #                 b := b - 1;
    #                 continue;
    #             end
    #             b := b - 1;
    #             putInt(b);
            
    #         end
    #     end
    #     """
    #     exp = "87653210"
    #     self.assertTrue(TestCodeGen.test(inp,exp,412))

    # def test_mode_13(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #     begin
    #         b := 9;
    #         putInt(b mod 5);
    #     end
    #     """
    #     exp = "4"
    #     self.assertTrue(TestCodeGen.test(inp,exp,413))

    # def test_for_14(self):
    #     inp = """
    #     procedure main();
    #     var i : integer;
    #     begin
    #     for i := 0 to 10 do 
    #         putInt(i);
    #     end
    #     """
    #     exp = "012345678910"
    #     self.assertTrue(TestCodeGen.test(inp,exp,414))

    # def test_for_15(self):
    #     inp = """
    #     procedure main();
    #     var i : integer;
    #     begin
    #     for i := 10 downto 0 do 
    #         putInt(i);
    #     end
    #     """
    #     exp = "109876543210"
    #     self.assertTrue(TestCodeGen.test(inp,exp,415))

    # def test_for_16(self):
    #     inp = """
    #     procedure main();
    #     var i : integer;
    #     begin
    #     for i := 0 to 10 do 
    #     begin
    #         if (i = 5) then
    #             continue;
    #         putInt(i);
    #     end
    #     end
    #     """
    #     exp = "01234678910"
    #     self.assertTrue(TestCodeGen.test(inp,exp,416))

    # def test_for_17(self):
    #     inp = """
    #     procedure main();
    #     var i : integer;
    #     begin
    #     for i := 0 to 10 do 
    #     begin
    #         if (i = 5) then
    #             break;
    #         putInt(i);
    #     end
    #     end
    #     """
    #     exp = "01234"
    #     self.assertTrue(TestCodeGen.test(inp,exp,417))

    # def test_for_18(self):
    #     inp = """
    #     procedure main();
    #     begin
    #         putInt(abc());
    #         return;
    #     end

    #     function abc(): integer;
    #     var ans, i: integer;
    #     begin
    #         ans := 0;
    #         for i := 0 to 10 do
    #             ans := ans + i;
    #         return ans;
    #     end
    #     """

    #     exp = "55"
    #     self.assertTrue(TestCodeGen.test(inp,exp,418))

    # def test_with_419(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #     begin
    #         a := 3;
    #         b := 3;
    #         with a, b: integer; do
    #             begin
    #                 a := 10;
    #                 b := 10;
    #             end

    #         putIntLn(a);
    #         putIntLn(b);
    #     end
    #     """
    #     exp = "3\n3\n"
    #     self.assertTrue(TestCodeGen.test(inp,exp,419))

    # def test_array_20(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #         c: array [99 .. 102] of integer;
    #     begin
    #         c[99] := 123;
    #         a := c[99];
    #         putIntLn(a);
    #         putIntLn(c[99]);
    #     end
    #     """
    #     exp = "123\n123\n"
    #     self.assertTrue(TestCodeGen.test(inp,exp,420))

    # def test_array_21(self):
    #     inp = """
        
    #     procedure main();
    #     var a, b: integer;
    #         c: array [1 .. 2] of integer;
    #     begin
    #         c[1] := 69;
    #         putInt(69);
    #         returnArray(69);
    #     end

    #     procedure returnArray(a69: integer);
    #     begin
    #         putInt(69);
    #     end
        
    #     """
        
    #     exp = "6969"
    #     self.assertTrue(TestCodeGen.test(inp,exp,421))

    # def test_global_22(self):
    #     inp = """
    #     var hxhx: integer;
    #     procedure main();
    #     begin
    #         hxhx := 69;
    #         ts();
    #     end

    #     procedure ts();
    #     begin
    #         putInt(hxhx);
    #     end
    #     """
    #     exp = "69"
    #     self.assertTrue(TestCodeGen.test(inp,exp,422))

    # def test_global_23(self):
    #     inp = """
    #     var hxhx: integer;
    #     procedure main();
    #     begin
    #         hxhx := 69;
    #         ts(hxhx);
    #     end

    #     procedure ts(a: integer);
    #     begin
    #         putInt(a);
    #     end
    #     """
    #     exp = "69"
    #     self.assertTrue(TestCodeGen.test(inp,exp,423))

    # def test_func_24(self):
    #     inp = """
    #     procedure main();
    #     begin
    #         main2(60);
    #     end

    #     procedure main2(a: integer);
    #     begin
    #         putInt(a);
    #     end
    #     """

    #     exp = "60"
    #     self.assertTrue(TestCodeGen.test(inp,exp,424))

    # def test_func_25(self):
    #     inp = """
    #     procedure main();
    #     var ar: array [99 .. 102] of integer;
    #         ind: integer;
    #     begin
    #         ind := 101;
    #         ar[ind] := 69;
    #         main2(ar, ind);
    #     end

    #     procedure main2(arr: array [99 .. 102] of integer; a: integer);
    #     begin
    #         putInt(arr[a]);
    #     end
    #     """
    #     exp = "69"
    #     self.assertTrue(TestCodeGen.test(inp,exp,425))

    # def test_func_26(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #     begin
    #         a := 5;
    #         b := 9;
    #         putInt(sum(a, b));
    #     end

    #     function sum(x, y: integer): integer;
    #     begin
    #         return x + y;
    #     end
    #     """
    #     exp = "14"
    #     self.assertTrue(TestCodeGen.test(inp,exp,426))

    # def test_func_27(self):
    #     inp = """
    #     procedure main();
    #     var a, b: integer;
    #         c: array [69 .. 96] of integer;
    #     begin
    #         a := 5;
    #         b := 9;
    #         c[80] := 100;
    #         putInt(sum(sum(a, b), c[80]));
    #     end

    #     function sum(x, y: integer): integer;
    #     begin
    #         return x + y;
    #     end
    #     """
    #     exp = "114"
    #     self.assertTrue(TestCodeGen.test(inp,exp,427))

    # def test_arr_428(self):
    #     inp = """
    #     procedure main();
    #     var a: array [1 .. 10] of integer;
    #     begin
    #         putInt(a[2]);
    #     end
    #     """
    #     exp = "0"
    #     self.assertTrue(TestCodeGen.test(inp,exp,428))

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
            for i := 1 to 10 do
                putInt(i);
            return i;
        end
        """
        exp = "2"
        self.assertTrue(TestCodeGen.test(inp,exp,429))

    # def test_arr_430(self):
    #     inp = """
    #     procedure main();
    #     var i: integer;
    #     begin
    #         for i := 0 to 10 do
    #             putInt(arrret()[i]);
    #     end
    #     function arrSum(a: array [1 .. 10] of integer; b: array [1 .. 10] of integer): array [1 .. 10] of integer;
    #     var ans: array [1 .. 10] of integer;
    #     begin
    #         for i := 1 to 10 do
    #             ans[i] := a[i] + b[i];
    #         return ans;
    #     end

    #     function arrret(): array [1 .. 10] of integer;
    #     var i: integer;
    #         arr:  array [1 .. 10] of integer;
    #     begin
    #         for i := 1 to 10 do
    #             arr[i] := i;
    #         return arr;
    #     end
    #     """
    #     exp = "2468101214161820"
    #     self.assertTrue(TestCodeGen.test(inp,exp,430))




    
