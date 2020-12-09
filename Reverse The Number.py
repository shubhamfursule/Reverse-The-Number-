for T in range(int(input())):
    interger = int(input())
    i=0
    while interger>0:
        a=interger%10
        i=(i*10)+a
        interger//=10
    print(i)
    
