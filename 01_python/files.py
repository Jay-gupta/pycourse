# with open("data\\test.csv", "w") as f:
#     f.write("hello 123")
# # implied f.close()

# #with open("data\\test.csv", "r") as myfile:
# #    pass

# f = open("data//test.csv", "w")
# f.write("hello")
# #f.close()


with open("data/test.csv", "r") as f:
    #for l in f:
    #    a.append(l)
    #a = f.readlines()
    a = f.read()

b = a.split()
#a.sort()

print(b)

