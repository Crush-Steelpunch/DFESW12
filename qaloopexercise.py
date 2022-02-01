# Write a while loop 
# which asks for the names of 5 people,   DONE
# and for each person prints their name   DONE
# followed by the text 
# "is awesome!" DONE

# Attempt 1: print after each name is input

# countvar = 5
# while countvar > 0:
#     namevar1 = input("Type NAME: ")
#     print(f"{namevar1} is awesome!")
#     countvar = countvar -1

# take in 5 names, then print at end
# Use a list

countvar = 5
listvar = []
while countvar > 0:
    listvar.append(input("Type Name: "))
    countvar = countvar -1

for i in listvar:
    print(f"{i} is awesome!")