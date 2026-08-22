n = int(input("n:"))
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


