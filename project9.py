''' Inverted Half Pyramid
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1   '''


for i in range(7,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
