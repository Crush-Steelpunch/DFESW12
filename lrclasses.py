class Lettertest:

    stringofletters = "AEIOU"

    def testaletter(self,letterin):
        if letterin.upper() in self.stringofletters:
            return True
        else:
            return False




testletter = "f"
isavowel = Lettertest()
isaconsonant = Lettertest()
isaletterwithoneendpoint = Lettertest()
isaconsonant.stringofletters = "BCDFGHJKLMNPQRSTVWXYZ"
isaletterwithoneendpoint.stringofletters = "P"
vowelresult = isavowel.testaletter(testletter)
print(isavowel.stringofletters)
print(isaconsonant.stringofletters)
print(isaletterwithoneendpoint.stringofletters)

#vowelresult = isavowel(testletter)
#consonantresult = isaconsonant(testletter)
print(testletter,"tested as a vowel: ", vowelresult)
#print(testletter,"tested as a consonant: ", consonantresult)