r = float(input("Please enter R: "))
amount = 0
if r > 0:

    #Loop through x and y inside R
    for x in range(1,int(r)+1):
        for y in range (1,int(r)+1):
            #print(x,y)
            if ((x**2+y**2)**0.5) <= r:
                amount += 1
    print("Point within the area =",amount)
else:
    print("Invalid Input.")