first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number == 0:
    print("The second number cannot be 0.")
else:
    remainder = first_number % second_number
    if remainder == 0:
        print(f"{first_number} is a multiple of {second_number}")
    else:
        print(f"{first_number} is not a multiple of {second_number}")
   
 