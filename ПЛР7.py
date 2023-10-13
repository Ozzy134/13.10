def top3(s):
    t = ([(s.count(i), i) for i in s])
    return (sorted(set(t))[::-1][:3])

s = input()
print(top3(s))