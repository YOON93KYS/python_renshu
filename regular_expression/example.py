import re


# a-z까지의문자들이 반복되어 표시된다면 (match)
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
## 결과:<re.Match object; span=(0, 6), match='python'>

p = re.compile('[a-z]+')
m = p.match('3 python')
print(m)

## 결과:None

# a-z까지의문자가 들어가 있다면(반복되어서) (search)
p = re.compile('[a-z]+')
m = p.search('python')
print(m)
## 결과:<re.Match object; span=(0, 6), match='python'>

p = re.compile('[a-z]+')
m = p.search('3 python')
print(m)
## 결과:<re.Match object; span=(2, 8), match='python'>