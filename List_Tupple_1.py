# programs from 15 to 33.
# # 15
# import re
# from datetime import datetime
# # Function to extract and convert dates
# def extract_dates(text):
#     dates = []
#     # Regular expression for different date formats
#     pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{4}\.\d{2}\.\d{2}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b'

#     matches = re.findall(pattern, text)
#     for date in matches:
#         try:
#             # DD/MM/YYYY
#             if "/" in date:
#                 new_date = datetime.strptime(date, "%d/%m/%Y")
#             # MM-DD-YYYY
#             elif "-" in date:
#                 new_date = datetime.strptime(date, "%m-%d-%Y")
#             # YYYY.MM.DD
#             elif "." in date:
#                 new_date = datetime.strptime(date, "%Y.%m.%d")
#             # Month Day, Year
#             else:
#                 new_date = datetime.strptime(date, "%B %d, %Y")
#             # Convert to YYYY-MM-DD
#             dates.append(new_date.strftime("%Y-%m-%d"))
#         except ValueError:
#             # Ignore invalid dates
#             pass
#     return dates
# # Take input from user
# text = input("Enter a block of text: ")
# # Extract dates
# result = extract_dates(text)
# # Display result
# print("\nDates in YYYY-MM-DD format:")
# if result:
#     for date in result:
#         print(date)
# else:
#     print("No valid dates found.")



# 16
# import re
# # Function to remove HTML tags
# def remove_html_tags(html):
#     # Regular expression to find HTML tags
#     pattern = r'<[^>]*>'
#     # Remove HTML tags
#     clean_text = re.sub(pattern, '', html)
#     return clean_text
# # Take HTML input from user
# html = input("Enter HTML content: ")
# # Remove HTML tags
# result = remove_html_tags(html)
# # Display cleaned text
# print("\nCleaned Text:")
# print(result)


# 17
# import re
# # Function to extract hashtags
# def extract_hashtags(text):
#     pattern = r'#[A-Za-z0-9_]+'
#     hashtags = re.findall(pattern, text)
#     return hashtags
# # Take input from user
# text = input("Enter a social media post: ")
# # Extract hashtags
# result = extract_hashtags(text)
# # Display hashtags
# print("\nExtracted Hashtags:")
# if result:
#     for hashtag in result:
#         print(hashtag)
# else:
#     print("No hashtags found.")


# 18
# import re
# # Function to extract and count file extensions
# def count_extensions(filenames):
#     extension_count = {}
#     for filename in filenames:
#         # Find file extension
#         match = re.search(r'(\.[A-Za-z0-9]+)$', filename)
#         if match:
#             extension = match.group(1).lower()
#             if extension in extension_count:
#                 extension_count[extension] += 1
#             else:
#                 extension_count[extension] = 1
#     return extension_count
# # Take number of files from user
# n = int(input("Enter number of files: "))
# filenames = []
# # Take filenames as input
# for i in range(n):
#     filename = input("Enter filename " + str(i + 1) + ": ")
#     filenames.append(filename)
# # Count extensions
# result = count_extensions(filenames)
# # Display result
# print("\nFile Extension Count:")
# print(result)


# 19
# import re
# # Function to validate IP address
# def validate_ip(ip):  
#     # IPv4 pattern
#     ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
#     # IPv6 pattern
#     ipv6_pattern = r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$'
#     # Check IPv4
#     if re.match(ipv4_pattern, ip):
#         return True
#     # Check IPv6
#     if re.match(ipv6_pattern, ip):
#         return True
#     return False
# # Take IP address from user
# ip = input("Enter an IP address: ")
# # Validate IP address
# if validate_ip(ip):
#     print("Valid IP address")
# else:
#     print("Invalid IP address")


#21 Simple Text Editor
# import re

# # Take text and search query from user
# text = input("Enter the text: ")
# query = input("Enter the word to search: ")

# # Count occurrences ignoring case
# count = len(re.findall(re.escape(query), text, re.IGNORECASE))

# # Highlight all occurrences
# highlighted_text = re.sub(
#     re.escape(query),
#     lambda match: "**" + match.group(0) + "**",
#     text,
#     flags=re.IGNORECASE
# )

# # Display results
# print("\nNumber of occurrences:", count)
# print("\nHighlighted text:")
# print(highlighted_text)

#22 Tool For cleaning text data
# import string
# # Predefined list of common stopwords
# stopwords = {
#     "is", "am", "are", "was", "were", "the", "a", "an",
#     "and", "or", "but", "in", "on", "at", "to", "of",
#     "for", "with", "this", "that", "it", "as", "by",
#     "from", "be", "has", "have", "had"
# }
# # Function to remove stopwords
# import string
# # Define stopwords
# stopwords = {
#     "a", "an", "the", "is", "am", "are", "was", "were",
#     "in", "on", "at", "to", "for", "of", "and", "or",
#     "with", "this", "that", "it", "as", "by", "from"
# }
# def remove_stopwords(text):
#     words = text.split()
#     cleaned_words = []
#     for word in words:
#         # Remove punctuation for checking the word
#         clean_word = word.strip(string.punctuation)

#         if clean_word.lower() not in stopwords:
#             cleaned_words.append(word)
#     # Join words with proper spacing
#     return " ".join(cleaned_words)
# # Take input from user
# text = input("Enter a paragraph: ")
# # Remove stopwords
# cleaned_text = remove_stopwords(text)
# # Display result
# print("\nOriginal Text:")
# print(text)
# print("\nCleaned Text:")
# print(cleaned_text)


# 23 find and replace operations.
# import re

# # Take input from user
# filename = input("Enter the input file name: ")
# target = input("Enter the word or phrase to find: ")
# replacement = input("Enter the replacement word or phrase: ")
# choice = input("Case-sensitive replacement? (yes/no): ")

# # Read the file
# with open(filename, "r") as file:
#     text = file.read()

# # Perform replacement
# if choice.lower() == "yes":
#     # Case-sensitive replacement
#     new_text = text.replace(target, replacement)
# else:
#     # Case-insensitive replacement
#     new_text = re.sub(re.escape(target), replacement, text, flags=re.IGNORECASE)

# # Create output file name
# output_file = "modified_" + filename

# # Write modified text to new file
# with open(output_file, "w") as file:
#     file.write(new_text)

# # Count occurrences
# if choice.lower() == "yes":
#     count = text.count(target)
# else:
#     count = len(re.findall(re.escape(target), text, re.IGNORECASE))

# # Display result
# print("\nReplacement completed successfully.")
# print("Number of occurrences replaced:", count)
# print("Modified file saved as:", output_file)

# 24
# import re

# # Function to split text into sentences
# def sentence_segmentation(text):

#     # Protect common abbreviations
#     abbreviations = {
#         "Mr.": "Mr",
#         "Mrs.": "Mrs",
#         "Ms.": "Ms",
#         "Dr.": "Dr",
#         "Prof.": "Prof",
#         "Sr.": "Sr",
#         "Jr.": "Jr",
#         "etc.": "etc"
#     }

#     for abbr, replacement in abbreviations.items():
#         text = text.replace(abbr, replacement)

#     # Split at ., !, or ? followed by whitespace
#     sentences = re.split(r'(?<=[.!?])\s+', text.strip())

#     # Restore abbreviations
#     for i in range(len(sentences)):
#         for abbr, replacement in abbreviations.items():
#             sentences[i] = sentences[i].replace(
#                 replacement, abbr
#             )

#     return sentences


# # Take input from user
# text = input("Enter a block of text: ")

# # Perform sentence segmentation
# sentences = sentence_segmentation(text)

# # Display sentences
# print("\nSentences:")

# for i, sentence in enumerate(sentences, 1):
#     print(i, ".", sentence)


# 25
# import re
# from collections import Counter
# # Function to summarize text
# def summarize_text(text, num_sentences=2):
#     # Split text into sentences
#     sentences = re.split(r'(?<=[.!?])\s+', text.strip())
#     # Remove punctuation and convert words to lowercase
#     words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
#     # Common stopwords
#     stopwords = {
#         "the", "is", "a", "an", "and", "or", "of", "to",
#         "in", "on", "for", "with", "this", "that", "it",
#         "are", "was", "were", "be", "as", "by", "from"
#     }
#     # Count important words
#     word_frequency = Counter(
#         word for word in words if word not in stopwords
#     )
#     # Calculate score for each sentence
#     sentence_scores = {}
#     for sentence in sentences:
#         sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
#         score = 0
#         for word in sentence_words:
#             score += word_frequency.get(word, 0)
#         sentence_scores[sentence] = score
#     # Select highest-scoring sentences
#     ranked_sentences = sorted(
#         sentence_scores,
#         key=sentence_scores.get,
#         reverse=True
#     )
#     summary = ranked_sentences[:num_sentences]
#     # Return summary in original order
#     summary = [sentence for sentence in sentences if sentence in summary]
#     return " ".join(summary)
# # Take text input from user
# text = input("Enter a paragraph or long text: ")
# # Take number of sentences for summary
# n = int(input("Enter number of sentences for summary: "))
# # Generate summary
# summary = summarize_text(text, n)
# # Display result
# print("\n----- SUMMARY -----")
# print(summary)


# 26
# import re

# # Dictionary of common contractions
# contractions = {
#     "don't": "do not",
#     "doesn't": "does not",
#     "didn't": "did not",
#     "can't": "cannot",
#     "couldn't": "could not",
#     "won't": "will not",
#     "wouldn't": "would not",
#     "isn't": "is not",
#     "aren't": "are not",
#     "wasn't": "was not",
#     "weren't": "were not",
#     "haven't": "have not",
#     "hasn't": "has not",
#     "hadn't": "had not",
#     "I'm": "I am",
#     "you're": "you are",
#     "he's": "he is",
#     "she's": "she is",
#     "it's": "it is",
#     "we're": "we are",
#     "they're": "they are"
# }
# # Function to normalize text
# def normalize_text(text):
#     # Convert text to lowercase
#     text = text.lower()
#     # Expand contractions
#     for contraction, expansion in contractions.items():
#         text = text.replace(contraction.lower(), expansion.lower())
#     # Remove numbers
#     text = re.sub(r'\d+', '', text)
#     # Remove punctuation and special characters
#     text = re.sub(r'[^a-zA-Z\s]', '', text)
#     # Remove extra spaces
#     text = re.sub(r'\s+', ' ', text).strip()
#     return text
# # Take input from user
# text = input("Enter a block of text: ")
# # Clean the text
# cleaned_text = normalize_text(text)
# # Display result
# print("\nOriginal Text:")
# print(text)
# print("\nCleaned Text:")
# print(cleaned_text)


# 27
# import re

# # Function to check palindrome
# def is_palindrome(text):
#     # Convert to lowercase and remove spaces/punctuation
#     normalized_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
#     # Check forward and backward
#     if normalized_text == normalized_text[::-1]:
#         return True
#     else:
#         return False
# # Take input from user
# text = input("Enter a word or phrase: ")
# # Check palindrome
# result = is_palindrome(text)
# # Display result
# print("Is palindrome:", result)


# 28
# import re
# from collections import Counter
# # Function to extract keywords
# def extract_keywords(text):
#     # Convert text to lowercase
#     text = text.lower()
#     # Extract words
#     words = re.findall(r'\b[a-zA-Z]+\b', text)
#     # Predefined stopwords
#     stopwords = {
#         "the", "is", "a", "an", "and", "or", "of", "to",
#         "in", "on", "for", "with", "this", "that", "it",
#         "are", "was", "were", "be", "by", "as", "from",
#         "at", "can", "has", "have", "had", "which", "their",
#         "they", "we", "our", "also", "using", "used"
#     }
#     # Remove stopwords
#     important_words = []
#     for word in words:
#         if word not in stopwords:
#             important_words.append(word)
#     # Count word frequency
#     frequency = Counter(important_words)
#     # Get top 5 keywords
#     top_keywords = frequency.most_common(5)
#     return top_keywords
# # Take input from user
# text = input("Enter research paper text: ")
# # Extract keywords
# keywords = extract_keywords(text)
# # Display result
# print("\nTop 5 Keywords:")
# for word, count in keywords:
#     print(word, ":", count)


# 29
# import re
# # Predefined dictionary of correctly spelled words
# dictionary = {
#     "this", "is", "a", "simple", "python", "program",
#     "to", "check", "spelling", "in", "the", "text",
#     "hello", "world", "computer", "science", "student",
#     "learning", "programming", "language", "good", "morning"
# }
# # Function to find misspelled words
# def spell_checker(text):
#     # Extract words from text
#     words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
#     misspelled = []
#     for word in words:
#         if word not in dictionary and word not in misspelled:
#             misspelled.append(word)
#     return misspelled
# # Take input from user
# text = input("Enter a block of text: ")
# # Check spelling
# result = spell_checker(text)
# # Display result
# print("\nMisspelled words:")
# if result:
#     print(result)
# else:
#     print("No misspelled words found.")

# 30
# Bank Account Program

# class BankAccount:

#     # Class-level counter for unique account numbers
#     account_counter = 1000

#     # Constructor
#     def __init__(self, account_holder):
#         self.account_holder = account_holder
#         self.balance = 0
#         BankAccount.account_counter += 1
#         self.account_number = BankAccount.account_counter

#     # Deposit money
#     def deposit(self, amount):
#         self.balance += amount
#         print(amount, "deposited successfully.")

#     # Withdraw money
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(amount, "withdrawn successfully.")
#         else:
#             print("Error: Insufficient balance.")

#     # Display balance
#     def display_balance(self):
#         print("Account Holder:", self.account_holder)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)

#     # Transfer money
#     def transfer(self, amount, other_account):
#         if amount <= self.balance:
#             self.balance -= amount
#             other_account.balance += amount
#             print(amount, "transferred successfully to",
#                   other_account.account_holder)
#         else:
#             print("Error: Insufficient balance for transfer.")


# # Create two BankAccount objects
# account1 = BankAccount("Rahul")
# account2 = BankAccount("Priya")


# # Display initial details
# print("\n--- Initial Accounts ---")
# account1.display_balance()
# print()
# account2.display_balance()


# # Deposit money
# print("\n--- Deposits ---")
# account1.deposit(5000)
# account2.deposit(3000)


# # Display balances
# print("\n--- After Deposits ---")
# account1.display_balance()
# print()
# account2.display_balance()


# # Withdraw money
# print("\n--- Withdrawal ---")
# account1.withdraw(1000)


# # Transfer money
# print("\n--- Transfer ---")
# account1.transfer(1500, account2)


# # Final balances
# print("\n--- Final Balances ---")
# account1.display_balance()
# print()
# account2.display_balance()


# 31
# Person class
# class Person:
#     # Constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # Display person information
#     def display_person_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# # Employee class inherits Person
# class Employee(Person):
#     # Constructor
#     def __init__(self, name, age, employee_id, salary):
#         # Initialize inherited attributes
#         super().__init__(name, age)
#         # Initialize employee attributes
#         self.employee_id = employee_id
#         self.salary = salary
#     # Display employee information
#     def display_employee_info(self):
#         print("\n----- Employee Details -----")
#         # Call parent class method
#         self.display_person_info()
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)
# # Take input from user
# name = input("Enter employee name: ")
# age = int(input("Enter employee age: "))
# employee_id = input("Enter employee ID: ")
# salary = float(input("Enter employee salary: "))
# # Create Employee object
# employee = Employee(name, age, employee_id, salary)
# # Display employee details
# employee.display_employee_info()

# 32
# Person class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_person_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# # Employee inherits from Person
# class Employee(Person):
#     def __init__(self, name, age, employee_id, salary):
#         super().__init__(name, age)
#         self.employee_id = employee_id
#         self.salary = salary
#     def display_employee_info(self):
#         # Call Person class method
#         self.display_person_info()
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)
# # Manager inherits from Employee
# class Manager(Employee):
#     def __init__(self, name, age, employee_id, salary, department, team_size):
#         super().__init__(name, age, employee_id, salary)
#         self.department = department
#         self.team_size = team_size
#     def display_manager_info(self):
#         print("\n----- Manager Details -----")
#         # Display Person and Employee information
#         self.display_employee_info()
#         # Display Manager information
#         print("Department:", self.department)
#         print("Team Size:", self.team_size)
# # Take input from user
# name = input("Enter manager name: ")
# age = int(input("Enter manager age: "))
# employee_id = input("Enter employee ID: ")
# salary = float(input("Enter salary: "))
# department = input("Enter department: ")
# team_size = int(input("Enter team size: "))
# # Create Manager object
# manager = Manager(
#     name,
#     age,
#     employee_id,
#     salary,
#     department,
#     team_size
# )
# # Display all information
# manager.display_manager_info()


# 33
# Calculator class
# class Calculator:
#     # add method using default arguments
#     def add(self, a, b, c=0, d=0):
#         return a + b + c + d
# # Create Calculator object
# calculator = Calculator()
# # Take input from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print("\nAddition of two numbers:", calculator.add(num1, num2))
# num3 = float(input("Enter third number: "))
# print("Addition of three numbers:", calculator.add(num1, num2, num3))
# num4 = float(input("Enter fourth number: "))
# print("Addition of four numbers:", calculator.add(num1, num2, num3, num4))