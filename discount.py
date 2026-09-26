def discount(amount):

    if amount > 50000:

        print("20% is the discount", amount*0.20)

    elif amount <50000 and amount >=20000:
        print("10% is the discount",amount*0.10)

    else:
        print("no discount")

discount(65000)

discount(20000)
