
def lunch_menu(day, one, two, three, four):
    week_menu = []

    index = 0
    while index < len(day):
        this_week = day[index] + "'s menu: " + protein[index] + " & " + grains[index] + " & " + veggies[index] + " & " + dessert[index] 
        week_menu.append(this_week)
        index += 1
    return week_menu

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
protein = ['beans', 'tempeh', 'tofu', 'mushrooms', 'v-burger']
grains = ['rice', 'quinoa', 'buckwheat', 'polenta', 'bun']
veggies = ['poblano peppers', 'broccoli', 'zuchini', 'eggplant', 'lettuce, pickles, tomato']
dessert = ['mango', 'vanilla pudding', 'pineapple', 'brownie', 'ice cream']

lunch = lunch_menu(day, protein, grains, veggies, dessert)
print(lunch)