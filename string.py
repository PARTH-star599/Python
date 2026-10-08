#Program to input string and display length wihout using len() function
# A=input()
# count=0
# for i in A:
#     count=count+1
# print(count)


#Character Count
# A=input()
# constant=0
# vowel=0
# digit=0
# spaces=0
# s=0
# for i in A:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         vowel=vowel+1
#     elif i==' ':
#       spaces=spaces+1
#     elif ('a'<=i>='z') or ('A'<=i>='Z'):
#        constant=constant+1
#     elif '0'<=i<='9':
#        digit=digit+1
#     else:
#        s=s+1
# print(spaces)
# print(vowel)
# print(constant)
# print(digit)
# print(s)


#Reverse String
# A=input()
# print(A[ : :-1])


#Palidrome  Check
# A=input()
# reverse=(A[ : :-1])
# if A==reverse:
#     print('Palidrome')
# else:
#     print('not palidrome')


#Uppercase and lowercase count
# A=input()
# Uppercase=0
# lowercase=0
# for i in A:
#     if 'A'<=i<='Z':
#         Uppercase=Uppercase+1
#     if 'a'<=i<='z':
#         lowercase=lowercase+1
# print(Uppercase)
# print(lowercase)


#Replace character
# s=input()
# old=input()
# new=input()
# for i in s:
#     if i==old:
#         print(new,end=' ')
#     else:
#         print(i,end=' ')


#Remove Spaces
# A=input()
# s=''
# for i in A:
#     if i!=' ':
#         s=s+i
# print(s)


#Frequency of character
# A=input()
# C=input()
# d=0
# for i in A:
#     if i==C:
#         d=d+1
# print(d)


#First and last character  
# A=input()
# print(A[0:1])
# print(A[-1:-2:-1])


#ASCII value
# A=input()
# for i in A:
#     print(i,'-',ord(i))


#Word count
# A=input()
# count=0
# for i in A:
#     if i==' ':
#         count=count+1
# count=count+1
# print(count)


#Longest Word
# s = input("Enter a sentence: ")
# words = s.split()
# longest = max(words, key=len)
# print("Longest word:", longest)


#Shortest Word
# s = input("Enter a sentence: ")
# words = s.split()
# shortest = min(words, key=len)
# print("Shortest word:", shortest)


#Title Case
# s = input("Enter a sentence: ")
# print("Title Case:", s.title())


#Duplicate Character
# s = input("Enter a string: ")
# for ch in set(s):
#     if s.count(ch) > 1:
#         print(ch)


#Character Frequency
# s = input("Enter a string: ")
# for ch in set(s):
#     print(ch, ":", s.count(ch))


#Anagram Check
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


#Remove Duplicate Ch
# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch not in result:
#         result += ch
# print("After removing duplicates:", result)


#Substring Search
# s = input("Enter main string: ")
# sub = input("Enter substring: ")
# if sub in s:
#     print("Substring found")
# else:
#     print("Substring not found")


#count occurences of a word
# sentence = input("Enter a sentence: ")
# word = input("Enter word to search: ")
# words = sentence.split()
# print("Occurrences:", words.count(word))


#Password validation
# password=input("Enter a password:-")
# upper=False
# lower=False
# digit=False
# special=False
# for ch in password:
#     if ch.isupper():
#         upper=True
#     elif ch.lower():
#         lower=True
#     elif ch.digit():
#         digit=True
#     else:
#         special=True
# if len(password) >=8 and upper and lower and digit and special:
#     print("Password is valid")
# else:
#     print("Password is invalid")


# Run-Length Encoding
# s = input("Enter a string: ")
# result = ""
# count = 1
# for i in range(len(s)):
#     if i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1
# print("Encoded string:", result)


# # String Compression
# s = input("Enter a string: ")
# compressed = ""
# count = 1
# for i in range(len(s)):
#     if i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#     else:
#         compressed += s[i] + str(count)
#         count = 1
# if len(compressed) < len(s):
#     print("Compressed string:", compressed)
# else:
#     print("Original string:", s)


# # Most Frequent Character
# s = input("Enter a string: ")
# frequency = {}
# for ch in s:
#     frequency[ch] = frequency.get(ch, 0) + 1
# most_frequent = max(frequency, key=frequency.get)
# print("Most frequent character:", most_frequent)
# print("Frequency:", frequency[most_frequent])


# # Second Most Frequent Character
# s = input("Enter a string: ")
# frequency = {}
# for ch in s:
#     frequency[ch] = frequency.get(ch, 0) + 1
# sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
# if len(sorted_chars) >= 2:
#     print("Second most frequent character:", sorted_chars[1][0])
#     print("Frequency:", sorted_chars[1][1])
# else:
#     print("Second most frequent character does not exist.")


# # Caesar Cipher
# text = input("Enter the message: ")
# shift = int(input("Enter the shift value: "))
# encrypted = ""
# for ch in text:
#     if ch.isupper():
#         encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
#     elif ch.islower():
#         encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
#     else:
#         encrypted += ch
# print("Encrypted message:", encrypted)
# decrypted = ""
# for ch in encrypted:
#     if ch.isupper():
#         decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
#     elif ch.islower():
#         decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
#     else:
#         decrypted += ch
# print("Decrypted message:", decrypted)


# # Email Validator
# email = input("Enter email address: ")
# if "@" in email and "." in email and email.index("@") < email.rindex("."):
#     print("Valid email address")
# else:
#     print("Invalid email address")


# # Word Frequency Dictionary
# paragraph = input("Enter a paragraph: ")
# words = paragraph.lower().split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1
# print("Word Frequency:")
# for word, count in frequency.items():
#     print(word, ":", count)


# # Sentence Reversal
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print("Reversed sentence:", reversed_sentence)


# # String Rotation
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# if len(str1) == len(str2) and str2 in (str1 + str1):
#     print("Yes, the second string is a rotation of the first string.")
# else:
#     print("No, the second string is not a rotation of the first string.")