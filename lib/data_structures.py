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


def get_spiciest_foods(spicy_foods):
    food_spicy_above_5 = []
    i = 0
    for i in range(len(spicy_foods)):
        if spicy_foods[i]["heat_level"] > 5:
            food_spicy_above_5.append(spicy_foods[i])
    return food_spicy_above_5


def print_spicy_foods(spicy_foods):
    i = 0
    for i in range(len(spicy_foods)):
        name = spicy_foods[i]["name"]
        level = "🌶" * spicy_foods[i]["heat_level"]
        cuisine = spicy_foods[i]["cuisine"]
        print(f"{name} ({cuisine}) | Heat Level: {level}")


def print_spiciest_foods(spicy_foods):
    foods_above_5 = get_spiciest_foods(spicy_foods)
    print_spicy_foods(foods_above_5)


def get_average_heat_level(spicy_foods):
    average = 0
    i = 0
    for i in range(len(spicy_foods)):
        average = average + spicy_foods[i]["heat_level"]
    return average / len(spicy_foods)


def get_names(spicy_foods):
    foods = []
    i = 0
    for i in range(len(spicy_foods)):
        foods.append(spicy_foods[i]["name"])
    return foods


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    i = 0
    for i in range(len(spicy_foods)):
        if spicy_foods[i]["cuisine"] == cuisine:
            return spicy_foods[i]


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
