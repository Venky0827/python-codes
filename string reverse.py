def rev1(str1):
    l = len(str1)
    spaces = [' ']
    words = []
    i = 0
    while i<l:
        if str1[i] not in spaces:
            start = i
            while i < l and str1[i] not in spaces:
                i+=1
            words.append(str1[start:i])
        i+=1
        
    return ' '.join(words[::-1])
    
    str1 = input("Enter string :")
    rev1(str1)
