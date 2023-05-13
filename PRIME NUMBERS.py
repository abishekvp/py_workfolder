n=int(input("Enter upper limit : "))
for i in range(1,n+1):
    flag = 1
    for j in range(1,i):
        if i%j==0:
            flag+=1
    if flag==2:
        print(i)