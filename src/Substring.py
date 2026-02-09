def substring(a):
    b=[]
    c=[]
    for i in a:
        if i not in c:
            length=a.count(i)
            string=i*length 
            b.append(string)
            c.append(i)
    print(b)
    





a="aaabcgggfi"
substring(a)