cook_book = {}
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    for f in file:
        dish = f.strip()
        ingredient = []
        ingredient_count = file.readline()
        for i in range(int(ingredient_count)):
            y = file.readline()
            ingredient_name, quantity, measure = y.strip().split(' | ')
            ingredient.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        w = file.readline()
        cook_book.update({dish: ingredient})
     
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                dict_ = {}
                if ingredient['ingredient_name'] not in shop_list:
                    count = int(ingredient['quantity']) * person_count
                    dict_ = {ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': count}}
                    shop_list.update(dict_)  
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] = shop_list[ingredient['ingredient_name']]['quantity'] + int(ingredient['quantity']) * person_count
        else:
            print('Такого блюда нет!')
    print(shop_list)
    return shop_list

# get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5)

def number_of_line(*files):
    all_text = {}
    for file in files:
        with open(file, 'rt', encoding='utf-8') as f:
            y = f.readlines()
            all_text[file] = y
    all_text1 = {k: all_text[k] for k in sorted(all_text, key=all_text.get, reverse=True)}
    for key, value in all_text1.items():
        with open('new_file.txt', 'a', encoding='utf-8') as f:
            r = len(value)
            f.writelines(f'{key}')
            f.writelines(f'\n{r}\n')
            f.writelines(value)
            f.writelines('\n')
    
number_of_line('1.txt','2.txt', '3.txt')


