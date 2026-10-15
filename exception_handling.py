# Student Information Program using Exception Handling

# Function to take name
while True:
    try:
        name = input("Enter student name: ")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Give name in character format.")

        break

    except ValueError as e:
        print("Invalid Input:", e)


# Function to take roll number
while True:
    try:
        roll_no = input("Enter roll number: ")

        if not roll_no.isdigit():
            raise ValueError("Give roll number in numerical format.")

        roll_no = int(roll_no)
        break

    except ValueError as e:
        print("Invalid Input:", e)

                                                                                                                                                   
# Function to take division
while True:
    try:
        division = input("Enter division: ")

        if not division.isalpha():
            raise ValueError("Give division in character format.")

        break

    except ValueError as e:
        print("Invalid Input:", e)


# Function to take Cloud Computing marks
while True:
    try:
        cloud = float(input("Enter marks in Cloud Computing: "))

        if cloud < 0 or cloud > 100:
            raise ValueError("Marks should be between 0 and 100.")

        break

    except ValueError as e:
        print("Invalid Input:", e)


# Function to take APC marks
while True:
    try:
        apc = float(input("Enter marks in APC: "))

        if apc < 0 or apc > 100:
            raise ValueError("Marks should be between 0 and 100.")

        break

    except ValueError as e:
        print("Invalid Input:", e)


# Function to take Java marks
while True:
    try:
        java = float(input("Enter marks in Java: "))

        if java < 0 or java > 100:
            raise ValueError("Marks should be between 0 and 100.")

        break

    except ValueError as e:
        print("Invalid Input:", e)


# Display student information
print("\n----- STUDENT INFORMATION -----")
print("Name              :", name)
print("Roll No.          :", roll_no)
print("Division          :", division)
print("Cloud Computing   :", cloud)
print("APC               :", apc)
print("Java              :", java)