'''

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

'''
C = int(input())

for i in range(1, C + 1):
    A, B = map(int, input().split())
    if A > 0 & B < 10:
        print('Case #{}: {}'.format(i, A + B))
'''
欲しい結果

Case #1: 2
Case #2: 5

今の結果
Case # 1 : 2
Case # 2 : 5
原因：print( ~~~ end='')を別々に入れる？


for i in range(1, C + 1):
    A, B = map(int, input().split())
    if A > 0 & B < 10:
        print("Case #{index}:", A + B, end='').format(index=i)
AttributeError: 'NoneType' object has no attribute 'format'


これで Clear
C = int(input())

for i in range(1, C + 1):
    A, B = map(int, input().split())
    if A > 0 & B < 10:
        print('Case #{}: {}'.format(i, A + B))


参考:https://withcoding.com/64

i = 123
f = 3.14
s = 'Hello'



input print('i: %d, f: %f, s: %s' % (i, f, s))
output i: 123, f: 3.140000, s: Hello

input print('i: %9d, f: %5.2f, s: %7s' % (i, f, s))
output i:       123, f:  3.14, s:   Hello

input print('i: %09d, f: %05.2f, s: %7s' % (i, f, s))
output i: 000000123, f: 03.14, s:   Hello

input print('i: {}, f: {}, s: {}'.format(i, f, s))
output i: 123, f: 3.14, s: Hello

input print('f: {1}, i: {0}, s: {2}'.format(i, f, s))
output f: 3.14, i: 123, s: Hello

input print('f: {ff}, i: {ii}, s: {ss}'.format(ii=i, ff=f, ss=s))
output f: 3.14, i: 123, s: Hello


a = 'apple'

b = 'banana'

input print('a is {0[a]}, b is {0[b]}'.format(locals()))
output a is apple, b is banana

input print('a is {a}, b is {b}'.format(**locals()))
output a is apple, b is banana




'''
