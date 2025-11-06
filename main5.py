def fibonocci(n):
    if(n<=0):
        print('invalid input')
    elif(n==1):
        return 0;
    elif(n==2):
        return 1;
    else:
        return fibonocci(n-1)+fibonocci(n-2);
print(fibonocci(5))
        
        
