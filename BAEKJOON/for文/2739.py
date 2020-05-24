'''
https://www.acmicpc.net/problem/2739
문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

출력
출력형식과 같게 N*1부터 N*9까지 출력한다.
'''

#  方法１
a = int(input())
for i in range(1, 10):
    print(a, "*", i, "=", a * i)

# 気づいたこと
'''
①「、」の使い方を忘れた。
a, "*", i, "=",が正解なのに、"str(a) * str(i) = "に書いてた
https://qiita.com/ponsuke0531/items/c5ad5d4f643211ca6582
'''
