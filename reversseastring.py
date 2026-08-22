s1 = input("Please enter your own String : ")

string2 = ('')
#loop for printing in reverse 
for i in s1:
    string2 = i + string2
    
print("\nThe Original String = ", s1)
print("The Reversed String = ", string2)
