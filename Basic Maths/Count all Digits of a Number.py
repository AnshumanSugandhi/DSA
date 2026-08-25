num= int(input("Emter a Number:"))
digit=0
while(num>0):
    last_digit=num%10
    digit+=1
    num=num//10
print(f"Number of Digits is: {digit} ")