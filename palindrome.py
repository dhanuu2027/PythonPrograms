n=int(input())
sum=0
newn=n
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if sum==newn:
    print("Yes")
else:
    print("No")