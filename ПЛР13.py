def all_divisors(number):
    lst = [1, number]
    for i in range(2, 1 + int(number ** 0.5)):
        if number % i == 0:
            lst.extend({number // i, i})
    return sorted(lst)

number = int(input())
print(all_divisors(number))