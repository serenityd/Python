rol=int(input('请输入行数:'))
a = rol
while a > 0:
    b = a
    while b > 0:
        print('* ',end='')
        b=b-1
        if b == 0:
            print('')
    a=a-1
    n=5-a
    while n > 0:
        print(' ',end='')
        n=n-1
