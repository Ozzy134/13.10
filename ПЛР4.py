def s_divisible_by_6(n):
    a = list(map(int, str(abs(n))))
    b = a[-1] % 2 == 0
    c = sum(a) % 3 == 0
    return b and c

n = int(input())
print(s_divisible_by_6(n))