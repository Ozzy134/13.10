def camel(st):
    new_st = ''
    a = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if a % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            a += 1
        else:
            new_st += val
    return new_st

st = input()
print(camel(st))