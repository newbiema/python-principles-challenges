def count(s):
    kata = []  
    jumlah = 0
    for i in s :
        kata.append(i)
    x = kata.count('-')
    if '-' in kata:
        jumlah += x+1
        return jumlah
    else:
        return 1

print(count("hai"))