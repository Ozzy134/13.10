def more_than_five(a):
	new_lst = ()
	for number in a:
            if abs(number) > 5:
                new_lst.append(number)
	return new_lst

a = input()
print(more_than_five(a))
