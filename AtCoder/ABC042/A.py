'''
https://atcoder.jp/contests/abc042
'''

A, B, C = map(int, input().split())

if (A == 5 or A == 7) & (B == 5 or B == 7) & (C == 5 or C == 7):
    if (A + B + C) == 17:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

'''
気づいたこと：
countを使えばより効率的だった。
l=list(map(int,input().split()))
if(l.count(5)==2 and l.count(7)==1):
  print("YES")
else:
  print("NO")
'''
