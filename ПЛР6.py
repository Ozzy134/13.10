def first_last(letter, st):
    first = st.find(letter)
    last = st.rfind(letter)

    return (None, None) if last == -1 else (first, last)

str = input()
y = input()
print(first_last(y, str))