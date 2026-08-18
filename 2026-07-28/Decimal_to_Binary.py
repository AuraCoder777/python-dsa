def convert(d,b=""):
    
    if d == 1:
        return "1"
    
    if d%2 == 0:
        return convert(d//2,b)+"0"
        
    elif d%2 == 1:
        return convert(d//2,b)+"1"
    

print(convert(125))
    