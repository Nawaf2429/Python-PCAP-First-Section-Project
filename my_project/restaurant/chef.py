def add_dish(menu, name, price):
    if name in menu:
        print("Dish already exists.")
    else:
        menu[name] = {'price': price, 'available': True}

def remove_dish(menu, name):
    if name in menu:
        del menu[name]
    else:
        print("Dish not found.")

def update_price(menu, name, new_price):
    if name in menu:
        menu[name]['price'] = new_price
    else:
        print("Dish not found.")

def place_order(menu, name):
    if name not in menu:
        print("Dish not found.")
    elif not menu[name]['available']:
        print("Dish not available.")
    else:
        menu[name]['available'] = False
        print("Order placed.")

def display_menu(menu):
    for name, info in menu.items():
        status = "Yes" if info['available'] else "No"
        print(f"{name} - ${info['price']} - Available: {status}")
