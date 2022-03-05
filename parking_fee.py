hour = int(input('hour: '))
min = int(input('min: '))
if hour < 0 or min < 0:
    print("Invalid value")

elif hour == 0 and min <= 30:
    print("Free")
else:
    fee = hour * 20
    if min > 0:
        fee += 20 # fee = fee + 20
    print(fee)