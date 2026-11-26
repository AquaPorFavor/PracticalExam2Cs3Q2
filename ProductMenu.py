products = []
cart = []


def add_products():
    print("===== ADD PRODUCTS =====")

    while True:
        try:
            item_count = int(input("How many products would you like to add? "))
            if item_count <= 0:
                print("Enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    for number in range(1, item_count + 1):
        name = input(f"Enter name of product {number}: ").strip()

        while True:
            try:
                price = float(input(f"Enter price of {name}: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid price.")

        products.append({
            "name": name,
            "price": price
        })


def display_menu():
    print("\n===== PRODUCT MENU =====")

    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['name']} - P{product['price']:.2f}")

    print("0. Finish ordering")


def take_order():
    while True:
        display_menu()

        try:
            choice = int(input("Select a product: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break

        if choice < 1 or choice > len(products):
            print("Invalid selection.")
            continue

        selected_product = products[choice - 1]

        while True:
            try:
                quantity = int(input(
                    f"Enter quantity for {selected_product['name']}: "
                ))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Please enter a valid quantity.")

        cart.append({
            "name": selected_product["name"],
            "quantity": quantity,
            "price": selected_product["price"]
        })

        print(f"{selected_product['name']} was added to the order.")

add_products()
take_order()
