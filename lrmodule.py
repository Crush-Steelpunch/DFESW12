import lrfunctions
import pdb
pdb.set_trace()

testword = "racecar"
palvar = lrfunctions.testispalindrome(testword)
print(testword, "palindrome test result:", palvar)
pasq = lrfunctions.pascalstriangle(5)
print(pasq)
list1 = ["k","^","(","1"]
countvar = len(list1)
for i in range(countvar + 1):
    print(list1[i])
