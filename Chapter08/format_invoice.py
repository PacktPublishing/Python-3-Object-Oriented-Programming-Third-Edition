# This won't render right
subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print(f"Sub: ${subtotal} Tax: ${tax} Total: ${total}")

print(f"Sub: ${subtotal:0.2f} Tax: ${tax:0.2f} Total: ${total:0.2f}")

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]

print("PRODUCT    QUANTITY    PRICE    SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity: ^9d}    "
        f"${price: <8.2f}${subtotal: >7.2f}"
    )
