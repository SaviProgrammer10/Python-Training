# School Club Member Badge

# Collect member details
member_name = input("Enter Member Name: ")
club_name = input("Enter Club Name: ")
age = int(input("Enter Age: "))
member_id = int(input("Enter Member ID: "))

# Convert values into text
age_text = str(age)
id_text = str(member_id)

# Create badge code using string slicing
badge_code = member_name[:3].upper() + club_name[:3].upper()

# Print the badge
print("\n===== SCHOOL CLUB MEMBER BADGE =====")
print("Member Name :", member_name)
print("Club Name   :", club_name)
print("Age         :", age_text)
print("Member ID   :", id_text)
print("Badge Code  :", badge_code)
print("Welcome to the", club_name + " Club!")