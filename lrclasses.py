def isavowel(letterin):
    if letterin in "aeiou":
        return True
    else:
        return False

def isaconsonant(letterin):
    if letterin in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False

def isletterwithonlystraightlines(letterin):
    if letterin.upper() in "AEFHIKLMNTVWXYZ":
        return True
    else:
        return False
        

testletter = "f"
vowelresult = isavowel(testletter)
consonantresult = isaconsonant(testletter)
print(testletter,"tested as a vowel: ", vowelresult)
print(testletter,"tested as a consonant: ", consonantresult)