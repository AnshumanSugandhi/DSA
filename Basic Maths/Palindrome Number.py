original_num=121
def palindrome_check (original_num):
    palindrome=0
    num=original_num
    while num >0 :
        palindrome = palindrome *10 + num%10
        num=num//10
    if original_num == palindrome :
        return True
    else:
        return False
    
palindrome_check(121)
    