# 1- Store information for 3 products (id, name, price) in a dictionary with user-provided information.
# 2- Retrieve and display the product information based on the product ID provided by the user.



products = {
            '100': {'name': 'IPhone 8', 'price': '5000'},
            '101': {'name': 'IPhone X', 'price': '6000'},
            '102': {'name': 'IPhone XR', 'price': '7000'}
        }

# id = input('id: ')
# name = input('ad: ')
# price = input('price: ')

# products[id] = {
#     "name": name,
#     "price": price
# }

# id = input('id: ')
# name = input('name: ')
# price = input('price: ')# 1- Store 3 product details (id, name, price) in a dictionary with user-provided information.
# # 2- Retrieve a product's information by asking the user for the product id.
#
# products = {
#     '100': {'name': 'IPhone 8', 'price': '5000'},
#     '101': {'name': 'IPhone X', 'price': '6000'},
#     '102': {'name': 'IPhone XR', 'price': '7000'}
# }
#
# # id = input('Enter product id: ')
# # name = input('Enter product name: ')
# # price = input('Enter product price: ')
#
# # products[id] = {
# #     "name": name,
# #     "price": price
# # }
#
# # id = input('Enter product id: ')
# # name = input('Enter product name: ')
# # price = input('Enter product price: ')
#
# # products[id] = {
# #     "name": name,
# #     "price": price
# # }
#
# # id = input('Enter product id: ')
# # name = input('Enter product name: ')
# # price = input('Enter product price: ')
#
# # products[id] = {
# #     "name": name,
# #     "price": price
# # }
#
# id = input('Enter the product id you want to search for: ')
# product = products[id]
#
# print(f'id: {id}, product name: {product["name"]}, product price: {product["price"]}')
# # print(products)

# products[id] = {
#     "name": name,
#     "price": price
# }


# id = input('id: ')
# name = input('name: ')
# price = input('price: ')

# products[id] = {
#     "name": name,
#     "price": price
# }

id = input('Enter the product id you want to search for: ')
product = products[id]

print(f'id: {id} product name: {product["name"]} product price: {product["price"]}')
# print(products)

