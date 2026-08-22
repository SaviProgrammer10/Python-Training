print("=== Simple ATM ===")

customers = 0
total = 0

while True:
    name = input("Enter customer name: ")
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount!")
        continue

    print("\nNotes given:")

    n100 = amount // 100
    amount = amount % 100

    n50 = amount // 50
    amount = amount % 50

    n20 = amount // 20
    amount = amount % 20

    n10 = amount // 10
    amount = amount % 10

    n5 = amount // 5
    amount = amount % 5

    n1 = amount

    if n100 > 0:
        print("100-unit notes:", n100)
    if n50 > 0:
        print("50-unit notes:", n50)
    if n20 > 0:
        print("20-unit notes:", n20)
    if n10 > 0:
        print("10-unit notes:", n10)
    if n5 > 0:
        print("5-unit notes:", n5)
    if n1 > 0:
        print("1-unit notes:", n1)

    customers += 1
    total += n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 + n5 * 5 + n1

    again = input("\nNext customer? (yes/no): ")

    if again.lower() != "yes":
        break

print("\n=== ATM Report ===")
print("Customers served:", customers)
print("Total money dispensed:", total)
print("ATM closed. Goodbye!")