# n = int(input("n:"))
n=5
# 1111*    n=5 i=1
# 111***       i=2
# 11*****      i=3
# 1*******     i=4
# *********    i=5




# for i in range(1,n+1):
#     print(" " * (n-i) , end="")
#     for j in range((2*i) - 1):     
#         print("*", end="")      
#     print()                     # newline after each row

# l*********  n=5 i=1
# ll*******       i=2
# lll*****        i=3
# llll***         i=4
# lllll*          i=5
 
# for i in range (1,n+1):
#     print(" " * i , end="")
#     for j in range (2 *n - 2 *i +1):
#         print("*", end="")
#     print()



# llll*  n=5 
# lll***
# ll*****
# l*******
# *********
# *********
# l*******
# ll*****
# lll***
# llll*

# for i in range (1,(2 * n) +1):
#     if (i <= n):
#         print(" " * (n - i), end="")
#         print("*" * (2 * i - 1))
#     else:
#         k = i - n                    # 1, 2, 3... n
#         print(" " * (k - 1), end="") # spaces increase
#         print("*" * (2 * (n - k) + 1)) # stars decrease
    
\
    
    
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *



# for i in range (1, 2*n):
#     if (i <= n):
#         print("*" * i)
#     else:
#         print("*" * (2*n-i))


# 1
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1

# for i in range(1, n+1):
#     start = i % 2  # 1 for odd rows, 0 for even
#     for j in range(i):
#         print((start + j) % 2, end=" ")
#     print()  


# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j, end="")
#         # print(i,end="")
#     print(" " *(2*n-2*i), end="")
#     for k in range (i,0,-1):
#         print(k,end="")
#     print()

# 1        
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

# num=1
# for i in range (1,n+1):
#     for j in range (i):
#         print(num,end=" ")
#         num+=1
#     print()
    
    
# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range (1,n+1):
#     for  j in range (i):
#         print(chr(65+j),end="")
#     print()
    
# ABCDE
# ABCD
# ABC
# AB
# A

# for i in range (n,0,-1):
#     for j in range (i):
#         print( chr(65+j),end="")
#     print()
       
# A
# BB
# CCC
# DDDD
# EEEEE

# for i in range(1,n+1):
#     for j in range (i):
#         print (chr(64+i),end="")
#     print()
    
    
# llll A
# lll AB A
# ll ABC BA
# l ABCD CBA
#  ABCDE DCBA

# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     for j in range (i):
#         print(chr(65+j),end="")
#     if i >1:
#         for k in range (i-1,0,-1):
#             print(chr(64+k),end="")
#     print()
    
  
# E 
# D E 
# C D E 
# B C D E 
# A B C D E


# for i in range (1,n+1):
#     start = n - i + 1
#     for k in range (i):
#         print(chr(64+start+k),end=" ")
#     print()
    
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# Top half
for i in range(n, 0, -1):
    # Stars
    print("*" * i, end="")
    # Spaces
    print(" " * (2 * (n - i)), end="")
    # Stars
    print("*" * i)

# Bottom half
for i in range(1, n + 1):
    # Stars
    print("*" * i, end="")
    # Spaces
    print(" " * (2 * (n - i)), end="")
    # Stars
    print("*" * i)

