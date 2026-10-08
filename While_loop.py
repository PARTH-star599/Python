#Below Average Programs


#Write a Python Program to print natural numbers up to n.

# n=int(input("Enter number: "))
# i=1
# while i<=n:
#     print(i)
#     i=i+1

#Write a Python Program to Print even number up to n.
# n=int(input("Enter number: "))
# i=2
# while i<=n:
#     if(i%2==0):
#         print(i)
#     i=i+1


#Write a Python program to print odd numbers up to n
# n=int(input("Enter number: "))
# i=1
# while i<=n:
#     if(i%2!=0):
#         print(i)
#     i=i+1


#Write a Python Program to  print sum of natural numbers.
# n=int(input("Enter number: "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)


#Average Programs


#Write a Python Program to Print sum of odd numbers up to n.

# n=int(input("Enter number: "))
# i=1
# sum=0
# while i<=n:
#     if i%2!=0:
#         sum=sum+i
#     i=i+1
# print(sum)


#Write a Python Program to print sum of even numbers up to n.

# n=int(input("Enter number: "))
# i=2
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print(sum)
      
#Write a Python Program to print natural numbers up to n in reverse order.
# n=int(input("Enter Number: "))
# i=n
# while i>=1:
#     print(i)
#     i=i-1


#Write a Python Program to print Fabonacci Series
# n=int(input("Enter Number: "))
# i=0
# a=0
# b=1
# while i<=n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     i +=1


#Factorial of a given nmber
#Print factorial of n number
# n=int(input("Enter a number:-"))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print("Factorial of n number:-",fact)


#Above Average Programs

#Check entered number is prime or not
# Take input from the user
# num = int(input("Enter a number: "))
# # Check if the number is greater than 1
# if num > 1:   
#     # Check divisibility from 2 to num-1
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")



# Program to find the sum of digits of a number
# Take input from the user
# num = int(input("Enter a number: "))
# # Variable to store the sum
# sum = 0
# # Repeat until the number becomes 0
# while num > 0:   
#     # Get the last digit
#     digit = num % 10    
#     # Add the digit to sum
#     sum = sum + digit    
#     # Remove the last digit
#     num = num // 10
# # Display the result
# print("Sum of digits =", sum)


# # Program to check whether a number is palindrome or not
# # Take input from the user
# num = int(input("Enter a number: "))
# # Store the original number
# original_num = num
# # Variable to store the reversed number
# reverse = 0
# # Reverse the number
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# # Check whether original number and reversed number are equal
# if original_num == reverse:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")


# # Program to reverse a number
# # Take input from the user
# num = int(input("Enter a number: "))
# # Variable to store the reversed number
# reverse = 0
# # Reverse the number
# while num > 0:
#     digit = num % 10          # Get the last digit
#     reverse = reverse * 10 + digit
#     num = num // 10           # Remove the last digit
# # Display the reversed number
# print("Reversed number =", reverse)


# Program to print multiplication table
# Take input from the user
# num = int(input("Enter a number: "))
# # Print multiplication table from 1 to 10
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# Program to find the largest among n numbers
# # Enter how many numbers you want to compare
# n = int(input("Enter the number of elements: "))
# # Take the first number as the largest
# largest = int(input("Enter number 1: "))
# # Input the remaining numbers
# for i in range(2, n + 1):
#     num = int(input("Enter number " + str(i) + ": "))
#     # Check if the entered number is greater than largest
#     if num > largest:
#         largest = num
# # Display the largest number
# print("The largest number is:", largest)


# Program to find the smallest among n numbers
# Enter the number of elements
# n = int(input("Enter the number of elements: "))
# # Take the first number as the smallest
# smallest = int(input("Enter number 1: "))
# # Input the remaining numbers
# for i in range(2, n + 1):
#     num = int(input("Enter number " + str(i) + ": "))
#     # Check if the entered number is smaller
#     if num < smallest:
#         smallest = num
# # Display the smallest number
# print("The smallest number is:", smallest)