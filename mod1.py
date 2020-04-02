def prime (num):
    a=2
    p=0
    #print(type(a))
    while(a<num):
        if(num%a!=0):
            b=1
        else:
            p+=1
        a+=1
    #print(p)
    if(p==0):
        return 1
    else:
        return 0




def fibo (num):
    prev=0
    curr=1
    l=[]
    l.append(curr)
    a=0
    while(a<num-1):
        nxt=prev+curr
        prev=curr
        curr=nxt
        l.append(nxt)
        a+=1
    return l