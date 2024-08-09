import random

products = {}
next_id = 1000


def generate_id():
    global next_id
    product_id = next_id
    next_id += 1
    return product_id


def add_products():
    product_name = input("Enter the product name: ")
    while True:
        try:
            product_price = float(input("Enter the product price: "))
            break
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
    product_id = generate_id()
    products[product_id] = [product_name, product_price]
    print("Product added successfully!")
    print(f"Product ID: {product_id} | Product Name: {product_name} | Product Price: {product_price}")


def view_products():
    print("All products:")
    for product_id, product_details in products.items():
        print(f"Product ID: {product_id} | Product Name: {product_details[0]} | Product Price: {product_details[1]}")


def update_product_price():
    try:
        product_id = int(input("Enter the product ID: "))
        if product_id in products:
            while True:
                try:
                    new_price = float(input("Enter the new price: "))
                    break
                except ValueError:
                    print("Invalid price. Please enter a numeric value.")
            products[product_id][1] = new_price
            print("Product price updated successfully!")
        else:
            print("Product not found!")
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")


def delete_product():
    try:
        product_id = int(input("Enter the product ID: "))
        if product_id in products:
            del products[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found!")
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")


def sort_products():
    sorted_products = sorted(products.items(), key=lambda x: x[1][0])
    print("All products sorted alphabetically:")
    for product_id, product_details in sorted_products:
        print(f"Product ID: {product_id} | Product Name: {product_details[0]} | Product Price: {product_details[1]}")


while True:
    print("\nProduct Management System")
    print("1. Add product")
    print("2. View products")
    print("3. Update product price")
    print("4. Delete product")
    print("5. Sort products")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        add_products()
    elif choice == 2:
        view_products()
    elif choice == 3:
        update_product_price()
    elif choice == 4:
        delete_product()
    elif choice == 5:
        sort_products()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")

    print()

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        break

print("Thank you for using the Product Management System!")
