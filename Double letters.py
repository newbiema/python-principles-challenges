def double_letters(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
    
print(double_letters("heii"))