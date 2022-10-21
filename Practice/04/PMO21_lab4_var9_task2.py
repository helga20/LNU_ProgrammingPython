recipes = {
    "Грецький салат": {"Помідори": 250, "Огірки": 200, "Перець": 200,\
            "Цибуля": 50,  "Фета": 200,  "Оливки": 50, "Оливкова олія": 150},\
    "Капрезе": {"Помідори": 200, "Моцарелла": 150, "Зелений базилік": 30,\
            "Оливкова олія": 100},\
    "Яблучний крамбл": {"Вершкове масло": 180, "Пшеничне борошно": 140,\
            "Яблука": 300, "Цукор": 190,  "Імбир": 10, "Кориця": 10},\
    "Крем-суп із броколі": {"Броколі": 400, "Морква": 100,"Цибуля": 100,\
            "Сир вершковий": 100,  "Масло": 70, "Вершки": 100, "Спеції": 15}
    }

for dish, component in recipes.items():
    print(f"--- {dish.upper()} ---")
    for ingredient, weight in component.items():
        print(f"{ingredient} - {weight} г")

print("\nВведіть інгредієнт:")
ingredient_list = []
input_ingredient = input().capitalize()
count = 0
for dish, component in recipes.items():
    for ingredient, weight in component.items():
        if ingredient in input_ingredient and weight <= 200:
            ingredient_list.append(input_ingredient)
            count += 1
print(f"Можна приготувати {count} страв,\
маючи інгредієнт {input_ingredient.lower()}")

dict_ = {}
for dish, component in recipes.items():
    for ingredient, weight in component.items():
        if ingredient not in dict_:
            dict_[ingredient] = 1
        else:
            dict_[ingredient] +=1
print("\nІнгредієнт та у скількох стравах його використовують: \n", dict_)

max_w = {dish: max(component.values()) for dish, component in recipes.items()}
print("\nВага інгредієнтів, яких потрібно для страв найбільше: \n", max_w)