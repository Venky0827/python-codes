def uni_char(s):  # method 1
    l = len(s)
    seen = []
    i = 0
    while i < l:
        if s[i] not in seen:
            seen.append(s[i])
        else:
            return False
        i +=1
    seen = ''.join(seen)
    if s == seen:
        return True
    
def unique_character2(s):  # method 2
    return len(set(s)) == len(s)

r1 = uni_char('abcd')                # method 1 calling
r2 = unique_character2('askhgsa')    # method 2 calling
print(r1,r2)
