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


def customer_orders():
    # every order is created individually then transferred to orders list, which wil store all information
    order = ['', '', '', '', '', '', '']
    # cost is kept track of and will be appended to order list
    cost = 0
    # asks for name of customer and appends it to order list
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
    dietery_requirements(selected_item, order, cost)

def dietery_requirements(selected_item, order, cost):

    dietary_gluten = ''
    dietary_vegan = ''
    if 'gf' in selected_item[3]:
        dietary_gluten = input("Gluten Free? y/n")
        if dietary_gluten == 'y':
            dietary_gluten = 'Gluten Free, '
    if 'v' in selected_item[3]:
        dietary_vegan = input("Vegan? y/n")
        if dietary_vegan == 'y':
            dietary_vegan = 'Vegan.'
    order[3] = dietary_gluten + dietary_vegan
    print(order)








customer_orders()
