# Percentage Calculation Program

marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))
marks4 = float(input("Enter marks of Subject 4: "))
marks5 = float(input("Enter marks of Subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total / 500) * 100

print("\nTotal Marks =", total)
print("Percentage =", percentage, "%")