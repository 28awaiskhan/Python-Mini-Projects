menu = {
    "Burger": 120,
    "Pasta": 150,
    "Pizza": 180,
    "Salad": 100,
    "Biryani": 250,
    "Coldrink": 100
}

print("Welcome to our Resturant")
print(f'''
Pizza: Rs.180
Burger: Rs.120
Pasta: Rs.150
Biryani: Rs.250
Salad: Rs.100
Coldrink: 100'''
)    

orderRs = 0

item_1 = input('Enter You order')

if item_1 in menu:
    orderRs += menu[item_1]
    print(f'your 1st item {item_1} has been add your order')
else:
    print('item not available')

# item 2
another_msg1 = input("Do you want to order anything else?(Yes/No)")

print(f'''
Pizza: Rs.180
Burger: Rs.120
Pasta: Rs.150
Biryani: Rs.250
Salad: Rs.100
Coldrink: 100'''
)



if another_msg1 == "Yes" or 'yes' or 'YES':
    item_2 = input('Enter You 2nd order')
    if item_2 in menu:
        orderRs += menu[item_2]
    print(f'Your 2nd item {item_2} has been add your order')
else:
    print('its not available')

# item 3
another_msg2 = input("Do you want to order anything else?(Yes/No)")


if another_msg2 == "Yes" or 'yes' or 'YES':
    item_3 = input('Enter You 3rd order')
    if item_3 in menu:
        orderRs += menu[item_3]
    print(f'Your 3rd item {item_3} has been add your order')
else:
    print('its not available')

print(
f'''
1. {item_1} Rs.{menu[item_1]}
2. {item_2} Rs.{menu[item_2]}
3. {item_3} Rs.{menu[item_3]}
Your total Bill Amount {orderRs}''')





# menu = {
#     "Burger": 120,
#     "Pasta": 150,
#     "Pizza": 180,
#     "Salad": 100,
#     "Biryani": 250,
#     "Coldrink": 100
# }

# def print_menu(menu):
#     print("Available Menu Items:")
#     for item, price in menu.items():
#         print(f"{item}: Rs.{price}")

# print("Welcome to our Restaurant")

# orderRs = 0

# # Print the menu and take the first order
# print_menu(menu)
# item_1 = input('Enter your order: ')

# if item_1 in menu:
#     orderRs += menu[item_1]
#     print(f'Your 1st item "{item_1}" has been added to your order.')
#     del menu[item_1]  # Remove the ordered item from the menu
# else:
#     print('Item not available')

# # Check if the user wants to order more items
# another_msg1 = input("Do you want to order anything else? (Yes/No): ")

# if another_msg1.lower() == "yes":
#     print_menu(menu)
#     item_2 = input('Enter your 2nd order: ')
#     if item_2 in menu:
#         orderRs += menu[item_2]
#         print(f'Your 2nd item "{item_2}" has been added to your order.')
#         del menu[item_2]  # Remove the ordered item from the menu
#     else:
#         print('Item not available')

# # Check if the user wants to order another item
# another_msg2 = input("Do you want to order anything else? (Yes/No): ")

# if another_msg2.lower() == "yes":
#     print_menu(menu)
#     item_3 = input('Enter your 3rd order: ')
#     if item_3 in menu:
#         orderRs += menu[item_3]
#         print(f'Your 3rd item "{item_3}" has been added to your order.')
#         del menu[item_3]  # Remove the ordered item from the menu
#     else:
#         print('Item not available')

# # Print the final bill
# print(f'''
# Your Order:
# 1. {item_1} - Rs.{menu.get(item_1)}
# 2. {item_2} - Rs.{menu.get(item_2)}
# 3. {item_3} - Rs.{menu.get(item_3)}

# Your total Bill Amount: Rs.{orderRs}
# ''')
