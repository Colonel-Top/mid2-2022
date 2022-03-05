item_price = int(input("Please enter item price "))
cash_price = int(input("Please enter cash "))

change = cash_price - item_price
print("Your change is ",change,"Baht of:")


sub = 500
bank  = change // sub
if bank:
    print(bank,sub,"-Baht bill (s)",end=" ")
    change = change - (bank*sub)

sub = 100
bank  = change // sub
if bank:
    print(bank%sub,sub,"-Baht bill (s)",end=" ")
    change = change - (bank*sub)

sub = 50
bank  = change // sub
if bank:
    print(bank%sub,sub,"-Baht bill (s)",end=" ")
    change = change - (bank*sub)

sub = 20
bank  = change // sub
if bank:
    print(bank%sub,sub,"-Baht bill (s)",end=" ")
    change = change - (bank*sub)

sub = 10
bank  = change // sub
if bank:
    print(bank%sub,sub,"-Baht coin (s)",end=" ")
    change = change - (bank*sub)

sub = 5
bank  = change // sub
if bank:
    print(bank%sub,sub,"-Baht coin (s)",end=" ")
    change = change - (bank*sub)

if bank:
    print(change,"1-Baht coin (s)")