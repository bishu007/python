arm=0
c=0
n=int(input("your number"))
a=n
k=n
while a>0:
    temp=a%10
    c=c+1
    a//=10
    
while k>0:
    
    arm+=(k % 10)**c
    print (k,arm)
    k//=10
if n == arm:    
   print("armstrong number") 
else:  
   print("is not an Armstrong number")  

