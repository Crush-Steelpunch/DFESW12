def reverseaword(inword):
    lenword = len(inword)-1
    revword = ""
    for letter in range(lenword,-1,-1):
        revword = revword + inword[letter]
    return revword

def palindrometest(typedword,reversedword):
    if userinputvar == capturedword:
        return True
    else:
        return False


# Palimdrome Finder
# User types in a word#
# I find out if it is a palindrom
userinputvar = input("Type a word")
capturedword = reverseaword(userinputvar)
ispalindrome = palindrometest(userinputvar,capturedword)
print(f"{userinputvar} tested: {ispalindrome}")


#otto
#racecar



