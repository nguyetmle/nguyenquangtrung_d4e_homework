n=int(input('enter a number n : '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, end="\t")
    print()