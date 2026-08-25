n=153
num ,count=n ,0
digits=[]
while(num>0):
    last_digit=num%10
    digits.append(last_digit)
    count+=1
    num=num//10
arm=0
for i in digits :
    arm=arm+i**3
if arm==n:
    return True
else:
    return False
    
