# inputvar1 = int(input("TYPE A NUM: "))
# var1 = 5

# if  :
#     print("your input was ether less than 5 or a positive number")
# else:
#     print("Your input was either greater than 5 or negative")

# inputvar1 = input("Type the name")
# uppervar1 = inputvar1.upper()
# listvar1 = ["TODD MALONE",    "Len Trujillo",    
# "Dana Stanton",    "Cornell Mcguire",    "Earnestine Cherry"]

# if uppervar1 in listvar1:
#     print("Len is in the list")
# else:
#     print("Len is not in the list")

inputvar1 = input("Type a letter in the alphabet: ")
vowl = "aeiou"
constonant = "bcdfghjklmnpqrstvwxyz"

if inputvar1 in vowl:
    print("It was a vowl")
elif inputvar1 in constonant:
    print("it was a consonant")
else:
    print("You didn't type an alphabet letter")