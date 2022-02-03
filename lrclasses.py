class Lettertest:


    def __init__(self,stringin):
        self.stringofletters = stringin



    def testaletter(self,letterin):
        if letterin.upper() in self.stringofletters:
            return True
        else:
            return False




testletter = "f"
isavowel = Lettertest("AEIOU")
isaconsonant = Lettertest("BCDFGHJKLMNPQRSTVWXYZ")
isaletterwithoneendpoint = Lettertest("P")
#isaconsonant.stringofletters = "BCDFGHJKLMNPQRSTVWXYZ"
#isaletterwithoneendpoint.stringofletters = "P"
vowelresult1 = isavowel.testaletter("b")
vowelresult2 = isavowel.testaletter("i")
vowelresult3 = isavowel.testaletter("j")
vowelresult4 = isavowel.testaletter("o")
print(isavowel.stringofletters)
print(isaconsonant.stringofletters)
print(isaletterwithoneendpoint.stringofletters)

#vowelresult = isavowel(testletter)
#consonantresult = isaconsonant(testletter)
print(testletter,"tested as a vowel: ", vowelresult)
#print(testletter,"tested as a consonant: ", consonantresult)