# 11
# import re
# def vaild_email(email):
#     pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
# email=input("Enter Email id: ")
# if vaild_email(email):
#     print("valid email")
# else:
#     print("invalid email")

# 14
# import re
# password = input("Enter your password: ")
# def check_password(password):   
#     if len(password) < 8:
#         return "Weak"   
#     if not re.search(r'[A-Z]', password):
#         return "Weak"    
#     if not re.search(r'[a-z]', password):
#         return "Weak"   
#     if not re.search(r'[0-9]', password):
#         return "Weak" 
#     if not re.search(r'[!@#$%^&*()_\-]', password):
#         return "Weak"
#     return "Strong "

# print(check_password(password))


# 17
# import re
# def extract_hashtags(text):
#     pattern = r'#[A-Za-z0-9_]+'
#     hashtags = re.findall(pattern, text)
#     return hashtags
# text = input("Enter a social media post: ")
# print(extract_hashtags(text))

# 19
# import re
# ip = input("Enter an IP address: ")
# def validate_ip(ip):  
#     ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
#     if re.match(ipv4_pattern, ip):
#         return "Vaild IPV 4 IP address"
#     else:
#         return "Invalid IPV 4 IP address"
# print(validate_ip(ip))



