for T in range(int(input())):
    interger = int(input())
    a=""
    i=0
    b=""
    while interger>0:
        a=interger%10
        i=(i*10)+a
        interger//=10
    print(i)
    
