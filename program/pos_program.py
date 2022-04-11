import csv

# opens the food_menu and turns it into a 2d list
food_menu = []
with open('menu.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        food_menu.append(row)
# prints menu
for i in range(0, len(food_menu)):
    print(str(i) + str(food_menu[i]))
# cost will keep track of the cost of the food, and is used globally throughout the program
cost = 0
# this 'orders' list will store all the infomation from all the customers
orders = []


def customer_orders():
    # every order is created individually then transferred to orders list, which wil store all information
    order = ['', '', '', '', '', '', '']
    # cost(global) is to keep track of the total cost of the food
    global cost
    # resets cost to 0
    cost = 0
    # asks for name of customer and appends it to order list
    name = input("Customer Name:")
    order[0] = name
    # the parts of the program are individual methods to provide convienience for users
    # the selected item is the item that the customer has selected, as a sublist of the food_menu list
    selected_item = select_food(order)
    order[1] = selected_item
    dietary_requirements(selected_item, order)
    simple_options(selected_item, order)
    steak_options(selected_item, order)
    food_costs(selected_item, order)


'''
In the select_food method, the program asks for an integer value that will correspond to an item
in the food_menu list. this will be returned to the method declaration, and the selected_item variable
is essential to the rest of the code. The name of the selected_item will also be implemented into the orders
list. I also made the design decision to allow for the user to restart the method if any errors arise.
This is seen in all the methods.
'''


def select_food(order):
    try:
        selected_item = int(input("Meal #:"))
        if 0 < int(selected_item) < len(food_menu):
            selected_item = food_menu[int(selected_item)]
            return selected_item
        else:
            print("You need to input an integer value within the confines of the menu. Please try again")
            select_food(order)
    except:
        print("You need to input an integer value. Please Try Again")
        select_food(order)


'''
The dietary_requirements method allows the user to add any dietary requirements for those orders that do 
include those options. The method contains another two methods for gluten free or vegan options.
'''


def dietary_requirements(selected_item, order):
    if_gluten(selected_item, order)
    if_vegan(selected_item, order)


# this method asks for either a 'y' or a 'n', sometjing seen with many options throughout the code
def if_gluten(selected_item, order):
    if 'gf' in selected_item[3]:
        dietary_gluten = input("Gluten Free? y/n")
        # depending on the value given, dietary_gluten will be one of two values
        if dietary_gluten == 'y':
            dietary_gluten = 'Gluten Free, '
        elif dietary_gluten == "n":
            dietary_gluten = "Non Gluten Free, "
        else:
            # used to repeat the method if an incorrect value is inputted
            if_gluten(selected_item, order)
            print("you need to print a valid value!")
    else:
        dietary_gluten = "Non Gluten Free, "
        # The dietary_gluten is then appended to the orders list
    order[3] = dietary_gluten


# same as if_gluten method
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
        # order[3] will now equal dietary_gluten + dietary_vegan
    order[3] = order[3] + dietary_vegan


'''
simple_options checks if an index in selected_item contains a a chain of certain characters, and then,
if so, will ask the user if they want to add this option to their order. This will also add to the cost, too
'''


def simple_options(selected_item, order):
    # accesses cost variable
    global cost
    # checks for '-Add' in index
    if '-Add' in selected_item[2]:
        add_option = input(selected_item[2])
        if add_option == 'y':
            print(cost)
            # adds the absolute value of the float between certain indexes in the selected_item[2] variable
            cost += abs(float(selected_item[2][len(selected_item[2]) - 4:len(selected_item[2])-1]))
            # adds option to order
            order[2] = selected_item[2]
        elif add_option == 'n':
            order[3] = "None"
        else:
            print("you did not enter a valid value. Please try again")
            simple_options(selected_item, order)


def steak_options(selected_item, order):
    if selected_item[0] == "Rib Eye Steak":
        sauce_options(selected_item, order)
        egg_option(order)


def sauce_options(selected_item, order):
    global cost
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
        sauce_options(selected_item, order)


def egg_option(order):
    global cost
    eggs = input("Add Eggs(each) $3.00(Max 4), Input amount: (0 for none)")
    if 0 <= int(eggs) <= 4:
        order[2] = order[2] + "-Add " + eggs + " Eggs $" + str(int(eggs)*3) + ".00"
        print(order)
        cost += int(eggs) * 3
    else:
        print("you need to input a positive integer that is less than 5")
        egg_option(order)


def food_costs(selected_item, order):
    global cost
    if '/' in selected_item[4]:
        food_size_options = selected_item[4].split('/')
        food_size = input("1: " + food_size_options[0] + " 2: " + food_size_options[1] + "select integer")
        if 0 < int(food_size) < 3:
            food_size = food_size_options[int(food_size) - 1]
            food_cost = food_size[len(food_size) - 5:len(food_size) ]
            cost = cost + abs(float(food_cost))
            order[4] = food_menu
            print(cost)
        else:
            print("sorry, you need to select either 1 or 2")
            food_costs(selected_item, order)
    else:
        cost += abs(float(selected_item[4][len(selected_item[2]) - 5:len(selected_item[2]) - 1]))
        order[4] = selected_item[4]
        print(order)
        print(cost)


customer_orders()

