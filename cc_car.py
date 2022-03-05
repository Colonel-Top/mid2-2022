cc = int(input("Enter cc:"))
tax = 0
if cc <= 600:
    tax = cc * 0.5
elif cc > 600 and cc <= 1800:
    cc_ext = cc - 600
    cc_ext *= 1.5
    tax = cc_ext + 300
elif cc > 1800:
    cc -= 1800
    cc *= 4
    tax = cc + 300 + 1800

print("Tax =",tax)