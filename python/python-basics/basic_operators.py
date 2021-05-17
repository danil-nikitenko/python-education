"""Basic operators"""

x = object()
y = object()

# change this code
x_list = []
y_list = []
for i in range(10):
    x_list.append(x)
    y_list.append(y)
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
