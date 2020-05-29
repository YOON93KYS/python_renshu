# Printの使い方
```
i = 123
f = 3.14
s = 'Hello'
```

```
input print('i: %d, f: %f, s: %s' % (i, f, s))

output i: 123, f: 3.140000, s: Hello
```
```
input print('i: %9d, f: %5.2f, s: %7s' % (i, f, s))

output i:       123, f:  3.14, s:   Hello
```
```
input print('i: %09d, f: %05.2f, s: %7s' % (i, f, s))

output i: 000000123, f: 03.14, s:   Hello
```
```
input print('i: {}, f: {}, s: {}'.format(i, f, s))

output i: 123, f: 3.14, s: Hello
```
```
input print('f: {1}, i: {0}, s: {2}'.format(i, f, s))

output f: 3.14, i: 123, s: Hello
```
```
input print('f: {ff}, i: {ii}, s: {ss}'.format(ii=i, ff=f, ss=s))

output f: 3.14, i: 123, s: Hello
```

```
a = 'apple'

b = 'banana'
```
```
input print('a is {0[a]}, b is {0[b]}'.format(locals()))

output a is apple, b is banana
```
```
input print('a is {a}, b is {b}'.format(**locals()))

output a is apple, b is banana
```# Printの使い方
```
i = 123
f = 3.14
s = 'Hello'
```

```
input print('i: %d, f: %f, s: %s' % (i, f, s))

output i: 123, f: 3.140000, s: Hello
```
```
input print('i: %9d, f: %5.2f, s: %7s' % (i, f, s))

output i:       123, f:  3.14, s:   Hello
```
```
input print('i: %09d, f: %05.2f, s: %7s' % (i, f, s))

output i: 000000123, f: 03.14, s:   Hello
```
```
input print('i: {}, f: {}, s: {}'.format(i, f, s))

output i: 123, f: 3.14, s: Hello
```
```
input print('f: {1}, i: {0}, s: {2}'.format(i, f, s))

output f: 3.14, i: 123, s: Hello
```
```
input print('f: {ff}, i: {ii}, s: {ss}'.format(ii=i, ff=f, ss=s))

output f: 3.14, i: 123, s: Hello
```

```
a = 'apple'

b = 'banana'
```
```
input print('a is {0[a]}, b is {0[b]}'.format(locals()))

output a is apple, b is banana
```
```
input print('a is {a}, b is {b}'.format(**locals()))

output a is apple, b is banana
```