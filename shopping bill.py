def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst
print(calculateElectronicsGST(100, 100))

def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst
print(calculateFashionGST(100, 100))

def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst
print(calculateFoodGST(100))

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total
print(totalBill(100, 100, 100, 100, 100))

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount
    return final_amount
print(calculateDiscountedBill(100, 100, 100, 100, 100))

a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Total after GST =", format(total, ".2f"))
print("Discount =", format(discount, ".2f"))
print("Final payable amount =", format(final_amount, ".2f"))