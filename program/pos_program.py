import csv

# opens the food_menu and turns it into a 2d list
food_menu = []
with open('menu.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        food_menu.append(row)
file.close()
drinks_menu = []
with open('drinks_menu.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        drinks_menu.append(row)

'''
In this part of the code, It prints out both the food and the drinks menu to a csv file, res

'''




# cost will keep track of the cost of the food, and is used globally throughout the program
cost = 0
# this 'orders' list will store all the infomation from all the customers
orders = []
selected_item = []
selected_drink = []


def food_order():
    global selected_item
    # prints menu
    for k in range(0, len(food_menu)):
        print(str(k) + str(food_menu[k]))
    # every order is created individually then transferred to orders list, which wil store all information
    order = ['', '', '', '', '', '', '', '']
    # cost(global) is to keep track of the total cost of the food
    global cost
    # resets cost to 0
    cost = 0
    # asks for name of customer and appends it to order list
    name = input("Customer Name:")
    order[0] = name
    drink_order(order)
    # the parts of the program are individual methods to provide convenience for users
    # the selected item is the item that the customer has selected, as a sublist of the food_menu list
    selected_item = select_food(order)
    order[1] = selected_item[0]
    dietary_requirements(selected_item, order)
    simple_options(order)
    steak_options(order)
    food_costs(order)
    orders.append(order)


'''
In the select_food method, the program asks for an integer value that will correspond to an item
in the food_menu list. this will be returned to the method declaration, and the selected_item variable
is essential to the rest of the code. The name of the selected_item will also be implemented into the orders
list. I also made the design decision to allow for the user to restart the method if any errors arise.
This is seen in all the methods.
'''


def select_food(order):
    global selected_item
    try:
        selected_number = int(input("Meal #:"))
        if 0 < int(selected_number) < len(food_menu):
            selected_item = food_menu[int(selected_number)]
            return selected_item
        else:
            print("You need to input an integer value within the confines of the menu. Please try again")
            select_food(order)
    except ValueError:
        print("You need to input an integer value. Please Try Again")
        selected_item = select_food(order)
        return selected_item


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


def simple_options(order):
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
            order_cancellation()
        elif add_option == 'n':
            order[2] = "None"
            order_cancellation()
        else:
            print("you did not enter a valid value. Please try again")
            simple_options(order)
    else:
        order[2] = "None"

'''
As the steak in the food_menu is more complex than simple_options, I added a seperate method for
it that allows for sauce options and an option to add multiple eggs(max 4)
'''


def steak_options(order):
    # checks to see if the option includes the string "Rib Eye Steak"
    if selected_item[0] == "Rib Eye Steak":
        sauce_options(order)
        egg_option(order)
        order_cancellation()


def sauce_options(order):
    global cost
    # asks for the sauce wanted, or n for none
    sauce = input("Add Mushroom Sauce, Garlic Butter OR Peppercorn Sauce $3.00. m/g/p or n for none")
    if sauce == "m":
        # if a sauce is selected, it adds that sauce to the order list then adds a cost
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
        sauce_options(order)


def egg_option(order):
    global cost
    # asks for aount of eggs wanted
    eggs = input("Add Eggs(each) $3.00(Max 4), Input amount: (0 for none)")
    if 0 <= int(eggs) <= 4:
        order[2] = order[2] + "-Add " + eggs + " Eggs $" + str(int(eggs)*3) + ".00"
        print(order)
        cost += int(eggs) * 3
    else:
        print("you need to input a positive integer that is less than 5")
        egg_option(order)


'''
food_costs is needed to get the final cost of the food, as well as give options
if more than one size is available
'''


def food_costs(order):
    global cost
    # checks for a '/' in selected_item
    if '/' in selected_item[4]:
        # splits the string at the '/'
        food_size_options = selected_item[4].split('/')
        # asks which size the customer wants
        food_size = input("1: " + food_size_options[0] + " 2: " + food_size_options[1] + "select integer")
        if 0 < int(food_size) < 3:
            food_size = food_size_options[int(food_size) - 1]
            food_cost = food_size[len(food_size) - 5:len(food_size)]
            cost = cost + abs(float(food_cost))
            order[4] = food_cost
            print(cost)
        else:
            print("sorry, you need to select either 1 or 2")
            food_costs(order)
    else:
        cost += abs(float(selected_item[4][len(selected_item[2]) - 5:len(selected_item[2]) - 1]))
        order[4] = selected_item[4]
        print(order)
        print(cost)


def order_cancellation():
    cancel_order = input("press enter to continue order or 'x' to exit program ''")
    if cancel_order == "x":
        quit()


def meals_amount():
    try:
        while True:
            amount = int(input("Meals Amount:"))
            if 0 < amount < 5:
                return amount
            else:
                print("You need to input a positive integer less than 5")
                continue

    except:
        print("you need to input an integer value")
        meals_amount()


def drink_order(order):
    global selected_drink
    for k in range(0, len(drinks_menu)):
        print(str(k) + str(drinks_menu[k]))
    # drink selection
    selected_drink = select_drink(order)
    order[5] = selected_drink[0]
    # options if selected_drink was a range of drinks
    drink_options(order)
    # costs for the drinks
    drink_costs(order)


def select_drink(order):
    global selected_drink
    try:
        selected_drink = int(input("Drink #:"))
        if 0 < int(selected_drink) < len(food_menu):
            selected_drink = drinks_menu[int(selected_drink)]
            print(selected_drink)
            return selected_drink
        else:
            print("You need to input an integer value within the confines of the menu. Please try again")
            select_drink(order)
    except ValueError:
        print("You need to input an integer value. Please Try Again")
        selected_drink = select_drink(order)
        return selected_drink


'''
drink_options asks for the integer corresponding with the list of drinks that is under the drink 
range selected. It then adds this to the order list.
'''


def drink_options(order):
    try:
        if '/' in selected_drink[2]:
            # splits the range of options up at the '/'
            options = selected_drink[2].split('/')
            print("Drink Options:")
            for x in range(0, len(options)):
                print(str(x + 1) + ": " + str(options[x]))
            drink_select = input("Select Integer ")
            if 0 < int(drink_select) <= len(options):
                order[6] = options[int(drink_select) - 1]
                print('Selected Item: ' + options[int(drink_select) - 1])
            else:
                print("Sorry, you need to input a positive integer within the range of the options")
                drink_options(order)
    except ValueError:
        print("Sorry, you need to enter a integer value")
        drink_options(order)


def drink_costs(order):
    global cost
    # gets cost from a specific index in the cost string
    cost += abs(float(selected_drink[3][1:len(selected_drink[3])]))
    order[7] = selected_drink[3]


meals_amount = meals_amount()
for i in range(0, meals_amount):
    print("Customer " + str(i + 1))

    food_order()
    print(orders)

