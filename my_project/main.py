from restaurant import chef

menu = {}
chef.add_dish(menu, "Pizza", 10)
chef.add_dish(menu, "Burger", 8)
chef.display_menu(menu)

chef.update_price(menu, "Burger", 9)
chef.place_order(menu, "Pizza")
chef.remove_dish(menu, "Burger")

chef.display_menu(menu)
