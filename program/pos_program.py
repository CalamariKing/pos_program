import csv

food_menu = []
with open('menu.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        food_menu.append(row)
for i in range(len(food_menu)):
    menu_display = str(food_menu[i]).replace("'","").replace(",", "-").replace("[", "").replace("]", "")
    print(str(i) + ": " + menu_display)