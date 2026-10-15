#Print Natural Numbers up to n
#n = int(input("Enter n: "))
#for i in range(1, n + 1):
#   print(i)

##Print Even Numbers up to n
# n = int(input("Enter n: "))
# for i in range(2, n + 1, 2):
#     print(i)

# #Print Odd Numbers up to n
# n = int(input("Enter n: "))
# for i in range(1, n + 1, 2):
#     print(i)

# Print Series: 1 2 4 8 16 ... n Terms
# n = int(input("Enter n: "))
# num = 1
# for i in range(n):
#     print(num, end=" ")
#     num = num * 2

# Sum the Series: 1 + 1/1! + 1/2! + ... + 1/n!
# n = int(input("Enter n: "))
# fact = 1
# sum = 1
# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + 1 / fact
# print("Sum is:", sum)

# Compute the Cosine Series
# import math
# x = float(input("Enter x: "))
# n = int(input("Enter number of terms: "))
# sum = 0
# for i in range(n):
#     sum = sum + ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)

# print("Cosine is:", sum)

# Check Whether the Square Root of a Number Is Prime
# import math
# num = int(input("Enter a number: "))
# root = int(math.sqrt(num))
# flag = 0
# for i in range(2, root):
#     if root % i == 0:
#         flag = 1
#         break
# if root < 2:
#     flag = 1
# if flag == 0:
#     print("Square root is a prime number")
# else:
#     print("Square root is not a prime number")

# Print ABC Pattern Three Times
# for i in range(3):
#     for j in range(3):
#         print(chr(65 + j), end=" ")
#     print()

# Print Increasing Alphabet Pattern
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

# Print Decreasing Alphabet Pattern
# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

# Print Increasing Number Pattern
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

#Print Repeated Number Pattern
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()