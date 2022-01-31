#shoppinglist = ["meat", "veg", "cake", "beer for the weekend"]
#                 0       1      2            3
#                 -4     -3     -2           -1
#print(shoppinglist[-1])



#shoppinglist = ["meat", "veg", "cake",["christmas cake","Birthday cake","Oat cake"], "beer for the weekend"]
#print(shoppinglist[3])

# Lists

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]
cool_animals = [cool_cows, cool_sheep, cool_pigs]
print(cool_animals[2][1])
cool_pigs.append("Babe")
print(cool_pigs)
cool_pigs.insert(0, "Piglet")
print(cool_pigs)

print(cool_pigs)
print(len(cool_pigs))

# Tuple

shoppingList = ("meat", "veg", "cake", "beer for the weekend")
print(shoppingList[3])




dictionary1 = {  "name":"Leon" , "Coolness":100   , "fan":True  , "device":"laptop"}
print(dictionary1["fan"])
print(dictionary1.keys())
print(dictionary1.values())

dictionary1["rpm"] = 420

print(dictionary1)

popcap = dictionary1.pop("Coolness")
print(dictionary1)


lucky_numbers = [5, 55, 4, 3, 101, 42]
print(min(lucky_numbers))
