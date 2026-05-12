grand_total = 0
products = []
for i in range(1, 6):
    print(f"\nProduct {i}:")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append((name, price))
    grand_total += price
gst_percent = float(input("\nEnter GST percentage for all products: "))
gst_amount = grand_total * gst_percent / 100
sgst = gst_amount / 2
cgst = gst_amount / 2
final_total = grand_total + gst_amount
print("\nProducts entered:")
for name, price in products:
    print(f"- {name}: {price:.2f}")
print(f"\nTotal Base Price: {grand_total:.2f}")
print(f"SGST: {sgst:.2f}")
print(f"CGST: {cgst:.2f}")
print(f"Grand Total (with GST): {final_total:.2f}")
