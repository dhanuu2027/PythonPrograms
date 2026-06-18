#to reverse the given integer

n=int(input())
negative=n<0
n=abs(n)
sum=0
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if negative:
    sum=-sum
if sum<-2**31 or sum>2**31-1:
    print(0)
print(sum)