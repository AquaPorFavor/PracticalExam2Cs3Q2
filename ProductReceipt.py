
def display_receipt():
    print("\n========== RECEIPT ==========")

    total_amount = 0

    for item in cart:
        subtotal = item["quantity"] * item["price"]
        total_amount += subtotal

        print(
            f"{item['name']} "
            f"x {item['quantity']} "
            f"@ P{item['price']:.2f} "
            f"| Subtotal: P{subtotal:.2f}"
        )

    print("==============================")
    print(f"TOTAL AMOUNT: P{total_amount:.2f}")
    print("==============================")
