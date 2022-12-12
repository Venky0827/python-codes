def str_rev(s):
    rev = []
    
    #BAse case
    if len(s) <= 1:
        return s
    
    # recursive case
    return str_rev(s[1:])+s[0]
 
        
        
        
test = str_rev('Hello world')
print(test)
