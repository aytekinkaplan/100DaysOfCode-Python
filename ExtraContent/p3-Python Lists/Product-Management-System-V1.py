products = {}


def add_product():
    id = input('Product ID: ')
    name = input('Product Name: ')
    price = input('Product Price: ')
    products[id] = {"name": name, "price": price}


def view_product():
    id = input('Enter the product ID you want to view: ')
    if id in products:
        product = products[id]
        print(f'ID: {id}, Product Name: {product["name"]}, Product Price: {product["price"]}')
    else:
        print("Product not found.")


while True:
    print("1. Add Product")
    print("2. View Product")
    print("3. Exit")
    choice = input("Make your choice: ")
    if choice == '1':
        add_product()
    elif choice == '2':
        view_product()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
