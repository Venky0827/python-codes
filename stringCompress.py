def compress(s):
    if len(s)<1:
        return ""

    if len(s)<2:
        return s+"1"

    r = ''
    cnt = 1
    last = s[0]
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r+s[i-1]+str(cnt)
            cnt = 1
        
        i +=1
    r = r+s[i-1]+str(cnt)

    print(r)


compress('AASS')

