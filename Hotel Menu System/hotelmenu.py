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





