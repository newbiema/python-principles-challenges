def mid(str):
    length = len(str)
    if length % 2 == 0:
        return ""
    else:
        kata = []
        for i in str:
            kata.append(i)
            median = {len(kata)//2}
            a=list(median) #a = [3] index ke-0
            b = 0
            for j in a:
                b +=j
        return kata[b]
print(mid("abc")) 