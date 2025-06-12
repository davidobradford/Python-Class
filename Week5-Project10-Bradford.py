purchaseprice = 0
month = 0

while purchaseprice <= 0:
    purchaseprice = int(input("Enter The Purchase Price: "))
    if purchaseprice <= 0:
        print("Purchase Price Cannot Be Zero or Less, Try again...")

print(" ")

downpayment = purchaseprice * .10
balance = purchaseprice - downpayment
payment = balance * .05

print("Month","%12s" % "Balance","%12s" % "Interest","%12s" % "Principal","%12s" % "Payment","%12s" % "Balance After Pmt")
while balance != 0:
    month += 1
    if balance < payment:
        payment = balance
        interest = 0
    else:
        interest = balance * .12 / 12
    principal = payment - interest
    print("%5d" % month, "%12.2f" % balance, "%12.2f" % interest, "%12.2f" % principal, "%12.2f" % payment, "%12.2f" % (balance - principal))
    balance = balance - principal
    





