no_of_member = int(input("Enter number of members: "))

xs = 0
s = 0
m = 0
l = 0
xl = 0

for i in range(0,no_of_member):
    custom_size = int(input("Enter polo size: "))
    if custom_size < 36:
        xs += 1
    elif custom_size >= 36 and custom_size < 38:
        s += 1
    elif custom_size >= 38 and custom_size < 40:
        m += 1
    elif custom_size >= 40 and custom_size < 42:
        l += 1
    elif custom_size >= 42:
        xl += 1
        
print("Polo size XS =",xs)
print("Polo size S =",s)
print("Polo size M =",m)
print("Polo size L =",l)
print("Polo size XL =",xl)