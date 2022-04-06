import csv

# opens the food_menu and turns it into a 2d list
import os

food_menu = []
with open('menu.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        food_menu.append(row)
# prints menu
for i in range(0, len(food_menu)):
    print(str(i) + str(food_menu[i]))
# this 'orders' list will store all the infomation from all the customers
orders = []
# cost is kept track of and will be appended to order list


def customer_orders():
    # every order is created individually then transferred to orders list, which wil store all information
    order = ['', '', '', '', '', '', '']
    # asks for name of customer and appends it to order list
    cost = 0
    name = input("Customer Name:")
    order[0] = name
    # asks for the number corresponding with the item on the food menu
    selected_item = food_menu[int(input("Meal #:"))]
    try:
        # adds item to order
        order[1] = selected_item[0]
        print(order)
    except:
        print("you need to select a positive integer within the range of the menu")
    dietary_requirements(selected_item, order)
    simple_options(selected_item, order, cost)
    steak_options(selected_item, order, cost)
    food_costs(selected_item, order, cost)


def dietary_requirements(selected_item, order):
    if_gluten(selected_item, order)
    if_vegan(selected_item, order)
    print(order)


def if_gluten(selected_item, order):
    if 'gf' in selected_item[3]:
        dietary_gluten = input("Gluten Free? y/n")
        if dietary_gluten == 'y':
            dietary_gluten = 'Gluten Free, '
        elif dietary_gluten == "n":
            dietary_gluten = "Non Gluten Free, "
        else:
            if_gluten(selected_item, order)
            print("you need to print a valid value!")
    else:
        dietary_gluten = "Non Gluten Free, "
    order[3] = dietary_gluten


def if_vegan(selected_item, order):
    if 'v' in selected_item[3]:
        dietary_vegan = input("Vegan? y/n")
        if dietary_vegan == 'y':
            dietary_vegan = 'Vegan.'
        elif dietary_vegan == 'n':
            dietary_vegan = "Non Vegan."
        else:
            print("you did not enter a valid value. Please try again")
            if_vegan(selected_item, order)
    else:
        dietary_vegan = "Non Vegan."
    order[3] = order[3] + dietary_vegan


def simple_options(selected_item, order, cost):
    if '-Add' in selected_item[2]:
        add_option = input(selected_item[2])
        if add_option == 'y':
            print(cost)
            cost += abs(float(selected_item[2][len(selected_item[2]) - 4:len(selected_item[2])-1]))
            print(cost)
            print(order)
            order[2] = selected_item[2]
            print(order)
        elif add_option == 'n':
            order[3] = "None"
        else:
            print("you did not enter a valid value. Please try again")
            simple_options(selected_item, order, cost)


def steak_options(selected_item, order, cost):
    if selected_item[0] == "Rib Eye Steak":
        sauce_options(selected_item, order, cost)
        egg_option(order, cost)


def sauce_options(selected_item, order, cost):
    sauce = input("Add Mushroom Sauce, Garlic Butter OR Peppercorn Sauce $3.00. m/g/p or n for none")
    if sauce == "m":
        order[2] = "Mushroom Sauce $3.00."
        cost += 3
    elif sauce == "g":
        order[2] = "Garlic Butter Sauce $3.00."
        cost += 3
    elif sauce == "p":
        order[2] = "Peppercorn Sauce $3.00."
        cost += 3
    elif sauce == "n":
        order[2] = "No Sauce."
    else:
        print("Sorry, you did not input a valid value. Please try again.")
        sauce_options(selected_item, order, cost)


def egg_option(order, cost):
    eggs = input("Add Eggs(each) $3.00(Max 4), Input amount: (0 for none)")
    if 0 <= int(eggs) <= 4:
        order[2] = order[2] + "-Add " + eggs + " Eggs $" + str(int(eggs)*3) + ".00"
        print(order)
        cost += int(eggs) * 3
    else:
        print("you need to input a positive integer that is less than 5")
        egg_option(order, cost)


def food_costs(selected_item, order, cost):
    pass





customer_orders()

