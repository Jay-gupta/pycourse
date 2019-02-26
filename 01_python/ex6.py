marks=[75, 70, 60, 50]
slab=['a', 'a-', 'b', 'b-']

c = 0
while c<len(marks):
    if g >= marks[c]:
        break
    c = c + 1

slab[c]
g = 30

if g >= 75:
    print("first")
elif g >= 70:
    print("u s")
elif g >= 60:
    print("s")
elif g >= 50:
    print("th")
elif g >= 45:
    print("f1 s")
elif g >= 40:
    print("f2")
else:
    print("f3")