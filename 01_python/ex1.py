
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# () {}

d = 0

while True:
    try:
        x = input()
        d = int(x)
        break
    except:
        print("please enter a number between 0 and 6")

print(d)
#d = int(x)
# guard
if d>=0 and d <= len(days):
    print(days[d])
