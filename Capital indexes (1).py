def capital_indexes(s):
    kata = []
    for index,char in enumerate(s):
        if char.isupper():
            kata.append(index)
    return kata
print(capital_indexes("BeRhaSiL"))