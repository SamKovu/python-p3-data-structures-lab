spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [x.get("name") for x in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [x for x in spicy_foods if x.get("heat_level")>5]

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(f"{x['name']} ({x['cuisine']}) | Heat Level: {x['heat_level']*'🌶'}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
      for x in spicy_foods:
          if x.get("cuisine")==cuisine:
              return x

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    average=0
    for x in spicy_foods:
        average+=x.get("heat_level")
    return int(average/len(spicy_foods))
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    

#print(get_names(spicy_foods))
#print(get_spiciest_foods(spicy_foods))
#print_spicy_foods(spicy_foods)
#print(get_spicy_food_by_cuisine(spicy_foods, "American"))
#print_spiciest_foods(spicy_foods)
print(get_average_heat_level(spicy_foods))



