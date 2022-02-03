# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(n):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
      
#    return n>=1
   
# pascal_triangle(2)


# for i in zip("abc","123"):
#     print(i)
trow = [1]
y = [0]
for x in range(2):
    print(trow)
    print(type(trow+y))
    for l,r in zip(trow+y,y+trow):
        print(l+r)
        trow=[l+r]

