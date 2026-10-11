total_bill = float(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people: "))

if number_of_people <= 0:
    print("The number of people must be at least 1.")
else:
    bill_with_tip = total_bill * 1.10
    amount_per_person = bill_with_tip / number_of_people

print(f"Bill total: {total_bill:.2f}")
print(f"People: {number_of_people}")
print(f"Total with tip: {bill_with_tip:.2f}")
print(f"Each person pays: {amount_per_person:.2f}")

