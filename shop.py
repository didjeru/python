# напишите здесь функцию print_shopping_list(),
# подобрав уникальные названия продуктов и сложив значения

def print_shopping_list(a, b):
    product_a=set(a)
    spisok = product_a.union(b)
    d = {}
    for key in spisok:       
        if key in a:
            if key in b:
                c=a[key]+b[key]
                d[key]=c
            else: d[key]=a[key]
        elif key in b:
            d[key]=b[key]
    for key in d:
        print(str(key)+': '+str(d[key]))


pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)
