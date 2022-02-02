def letterType(inputvar1):
    vowl = "aeiou"
    constonant = "bcdfghjklmnpqrstvwxyz"

    if inputvar1 in vowl:
        print("It was a vowl")
    elif inputvar1 in constonant:
        print("it was a consonant")
    else:
        print("You didn't type an alphabet letter")


lettertest = input("Type a letter: ")
letterType(lettertest)
letterType("v")

anotherlettertest = input("Type a letter: ")
letterType(anotherlettertest)