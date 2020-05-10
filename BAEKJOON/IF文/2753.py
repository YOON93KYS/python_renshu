'''
IF文・論理演算子・比較演算子関連
https://www.acmicpc.net/problem/2753
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
'''
x = int(input())

# 間違った１ (1をinputしたら1が出る）
# if x % 400 == 0 & x % 4 == 0:
#     print(1)
# elif x % 100 != 0 & x % 4 == 0:
#     print(1)
# else:
#     print(0)



# 正解1
if (x % 4 == 0) & (x % 100 != 0):
    print(1)
elif x % 400 == 0:
    print(1)
else:
    print(0)

# 正解2
if x % 4 == 0 and x % 100 != 0:
    print(1)
elif x % 400 == 0:
    print(1)
else:
    print(0)

'''
気づいたこと
①：計算順番の把握
②：論理演算子・比較演算子の区分
③：&を使う時は()を入れましょう

and
・論理演算子
・'True'・'False'演算
&
・比較演算子
・bitwise演算子

https://docs.python.org/ja/3/reference/expressions.html#operator-precedence
・6.16. 評価順序参考
　Python は、式を左から右へと順に評価します。 ただし、代入式を評価するときは、右辺が左辺よりも先に評価されます。
expr1, expr2, expr3, expr4
(expr1, expr2, expr3, expr4)
{expr1: expr2, expr3: expr4}
expr1 + expr2 * (expr3 - expr4)
expr1(expr2, expr3, *expr4, **expr5)
expr3, expr4 = expr1, expr2
・6.17.演算子優先順位参考

以下のExampleの順番なら
① *, @, /, //, %
② &
③ in, not in, is, is not, <, <=, >, >=, !=, ==
'''

# x = 1
# if x % 4 == 0 & x % 100 != 0:  # print(0)を出力
#     print(1)
# else:
#     print(0)
'''
x = 1 
① x % 4 : 1
② x % 100 : 1
③ 0 & (x % 100) : 0
④(x % 4) == (0 & (x % 100)) != 0　→ 1 == 0 != 0 : Flase
結論：False → print(0)
'''

# x = 1
# if x % 100 != 0 & x % 4 == 0:  # print(1)を出力
#     print(1)
# else:
#     print(0)

'''
x = 1
① x % 100 : 1
② x % 4 : 1
③ 0 & (x % 4) : 0
④ (x % 100) != (0 & (x % 4)) == 0  → 1 != 0 == 0 : True
結論: True → print(1)
'''