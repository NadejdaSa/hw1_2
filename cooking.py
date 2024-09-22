def create_cb(file):
    cook_book = {}
    strings_list = [line.strip() for line in file.readlines()]
    while strings_list != []:
        if strings_list[0] == '':
            strings_list.pop(0)
        dish = strings_list[0]
        number_of_ingredients = int(strings_list[1])
        cook_book[dish] = []
        for ingredient in strings_list[2:2 + number_of_ingredients]:
            ingredient_name, quantity, measure = ingredient.split(' | ')
            vocabulary = {'ingredient name': ingredient_name, 'quantity': quantity, 'measure': measure}
            cook_book[dish].append(vocabulary)
        strings_list[:2 + number_of_ingredients] = []
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in our_cook_book[dish]:
            if ingredient['ingredient name'] not in shop_list:
                shop_list[ingredient['ingredient name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
            else:
                shop_list[ingredient['ingredient name']]['quantity'] += int(ingredient['quantity']) * person_count
  
    return shop_list

with open('recipes.txt', encoding='utf-8') as our_file:
    our_cook_book = create_cb(our_file)

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))