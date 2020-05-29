'''
https://www.acmicpc.net/problem/8393
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
'''
a = 0
n = int(input())
for i in range(1, n + 1):
    a = a + i
print(a)

'''
気づいたこと
print()をどこに置くのかによって結果が違うので注意
'''