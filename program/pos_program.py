import csv

food_menu = []
with open('menu.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        food_menu.append(row)

print("FOOD MENU:")
for i in range(1, len(food_menu)):
    menu_display = str(food_menu[i]).replace("'","").replace(",", "-").replace("[", "").replace("]", "").replace("- - -", "-").replace("- -", "-")
    print(str(i) + ": " + menu_display)

input_num = input("\nWhat item number do you want to select?\n")
try:
    selected_item = food_menu[int(input_num) + 1][0]
except:
    print("sorry, but you need to select a number that is within the range of the menu.")



