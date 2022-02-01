var1 = '* '

for i in range(1,6):
    j = i
    var2 = ''
    while j > 0:
        var2 = var2 + var1
        j = j - 1
    print(var2)

for i in range(4,0,-1):
    j = i
    var2 = ''
    while j > 0:
        var2 = var2 + var1
        j = j - 1
    print(var2)
