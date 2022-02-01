
#     Asks for an input from the user as a mark. DONE
#     If the mark is greater that 85 print "Distinction" DONE
#     If the mark is between 65 and 85 print "Pass" DONE
#     Anything else print "Fail"   DONE

# Try to do this both with and without elif statements.

inputvar1 = int(input("MARK: "))

if inputvar1 > 85:
    print("Distiction")
elif inputvar1 > 64:
    print("Pass")
else:
    print("Fail")

if inputvar1 >= 65:
    if inputvar1 > 85:
        print("Distiction")
    else:
        print("Pass")
else:
    print("Fail")
70