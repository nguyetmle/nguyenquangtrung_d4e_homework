n=int(input('enter a number n : '))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>col:
            n1=int(row-col)
            if n1%2==0:
                print(1,end=' ')
            else:
                print(0,end=' ')
        else:
            n1=int(col-row)
            if n1%2==0:
                print(1,end=' ')
            else:
                print(0,end=' ')
    print()