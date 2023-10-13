def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
    	return 'Мимо!'

subst = input()
st = input()
print(search_substr(subst, st))