s = input()
r = ''
a = 0

for sym in s:
    a += sym == '('
    if not a:
        r += sym
    a -= sym == ')'
print(r)
