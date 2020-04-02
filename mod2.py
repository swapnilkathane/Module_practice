import mod1
if__name__="__main__"
a=input('Hey user !!, what do you want to do ? prime number test or fibonacci series for prime number enter prime for fibonacci series enter fibo :')
if(a=='prime'):
    b=int(input('Enter the number'))
    d=(mod1.prime(b))
    if(d==1):
        print('Given number is prime')
    else:
        print('Number is not prime number')
if(a=='fibo'):
    c=int(input('Enter the number of terms do you want in series'))
    e=mod1.fibo(c)
    print(e)
