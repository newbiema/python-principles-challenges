def add_dots(s):
    x = ".".join(s)
    return x
    
def remove_dots(s):
    x = s.replace(".","")
    return x
        
print(remove_dots("s.a.y.a"))