for x in range(1,1000):
    for y in range(1,1000):
        a = x*y
        s = list(str(a)) 
        if len(s) == 6: 
            if s[0] == s[len(s) - 1] and s[1] == s[len(s) -2] and s[2] == s[len(s) - 3] :
                print(x, y) 