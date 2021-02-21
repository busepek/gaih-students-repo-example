import random
import time
import sys

class Recipe:
    def __init__(self,name):
        self.name = name
    def cook(self):
        print("Cooking... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Cooked!")
    def boil(self):
        print("Boiling... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Boiled!")
    def grill(self):
        print("Grilling... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Grilled!")
    def chop(self):
        print("Chopping... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Chopped!")
    def mix(self):
        print("Mixing ingredients... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Mixed!")
    def grate(self):
        print("Grating ingredients... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Grated!")
    def salt(self):
        print("Adding salt... Please wait...")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Salt added!")
    def spicy(self):
        while True:
            add_spicy = input("Would you like to add some spicies? Please write 'yes' to add, 'no' to not add: ").lower()
            if add_spicy == "yes":
                print("Adding spicies... Please wait...")
                for i in range(30):
                    time.sleep(.1)
                    print(".", end = " ")
                print("Spicies added!")
                break
            elif add_spicy == "no":
                print("Spicies not added!")
                break
            else:
                print("Please write YES or NO !!!", "Try again: ", sep = "\n")
                continue
    def ready(self):
        print("Your meal is ready!", "Afiyet Olsun!", sep = "\n")
    def rate(self):
        print("Did you like the recipe? Rate us!")
        print("""Rates:
        1: Very Bad!
        2: Bad!
        3: Unstable!
        4: Good!
        5: Very Good!""")
        rate = input("Your rate: ")
        print("Your rate is {}! Thank you!".format(rate))
        sys.exit("Good bye!!(:")

class ChickenSalad(Recipe):
    def __init__(self, name):
        super().__init__(name)
    def main(self):
        self.ingredients()
        self.prep_time()
        self.boil()
        self.grill()
        self.chop()
        self.mix()
        self.salt()
        self.spicy()
        self.ready()
        self.rate()
    def ingredients(self):
        ingredients_list = ["chicken", "lettuce", "cucumber", "red onion", "cherry tomatoes", "olive oil", "lemon"]
        ingredients_amount = ["250 gr", "1", "1", "1", "7", "3 spoon", "1"]
        ingredients = dict(zip(ingredients_list, ingredients_amount))
        print("Chicken Salad has {} ingredients in it. These are:".format(len(ingredients_amount)))
        for i in ingredients:
            print(i, ":", ingredients[i])
    def prep_time(self):
        prep_time = "30 mins"
        print("Preparation Time: ", prep_time)
    def boil(self):
        boiled_items = "chicken"
        boiled_time = "20 mins"
        print("You need to boil {} for {}".format(boiled_items,boiled_time))
        super().boil()
    def grill(self):
        grilled_items = "chicken"
        grilled_time = "7 mins"
        print("You need to grill {} for {}".format(grilled_items,grilled_time))
        super().grill()
    def chop(self):
        chopped_items = ["lettuce", "cucumber", "red onion", "cherry tomatoes", "chicken"]
        for i in range(5):
            print("You need to chop {}".format(chopped_items[i]))
        super().chop()
    def mix(self):
        mixed_items = "all ingredients"
        print("You need to mix {}!".format(mixed_items))
        super().mix()
    def salt(self):
        super().salt()
    def spicy(self):
        super().spicy()
    def ready(self):
        super().ready()
    def rate(self):
        super().rate()

class Meatball(Recipe):
    def __init__(self, name):
        super().__init__(name)
    def main(self):
        self.ingredients()
        self.prep_time()
        self.grate()
        self.salt()
        self.spicy()
        self.mix()
        self.cook()
        self.ready()
        self.rate()
    def ingredients(self):
        ingredients_list = ["mince", "bread crumb", "parsley", "tomato sauce", "onion", "potato", "olive oil"]
        ingredients_amount = ["500 gr", "50 gr", "1 bunch", "3 spoon", "1", "2", "3 spoon"]
        ingredients = dict(zip(ingredients_list, ingredients_amount))
        print("Meatball has {} ingredients in it. These are:".format(len(ingredients_amount)))
        for i in ingredients:
            print(i, ":", ingredients[i])
    def prep_time(self):
        prep_time = "45 mins"
        print("Preparation Time: ", prep_time)
    def grate(self):
        grated_items = ["onion", "potato", "parsley"]
        for i in range(2):
            print("You need to grate {}".format(grated_items[i]))
        super().grate()
    def salt(self):
        super().salt()
    def spicy(self):
        super().spicy()
    def mix(self):
        mixed_items = "all ingredients"
        print("You need to mix {}!".format(mixed_items))
        super().mix()
    def cook(self):
        cook_time = "30 mins"
        cook_heat = "200 degrees"
        print("You need to cook your meal in the {} owen for {}".format(cook_heat,cook_time))
        super().cook()
    def ready(self):
        super().ready()
    def rate(self):
        super().rate()

class Pasta(Recipe):
    def __init__(self, name):
        super().__init__(name)
    def main(self):
        self.ingredients()
        self.prep_time()
        self.boil()
        self.chop()
        self.grill()
        self.grate()
        self.mix()
        self.salt()
        self.spicy()
        self.cook()
        self.ready()
        self.rate()
    def ingredients(self):
        ingredients_list = ["pasta", "chicken", "mushrooms", "garlic", "olive oil", "cream", "cheese", "butter"]
        ingredients_amount = ["500 gr", "250 gr", "150 gr", "3 cloves", "1 spoon", "2 pack", "100 gr", "3 spoon"]
        ingredients = dict(zip(ingredients_list, ingredients_amount))
        print("Pasta has {} ingredients in it. These are:".format(len(ingredients_amount)))
        for i in ingredients:
            print(i, ":", ingredients[i])
    def prep_time(self):
        prep_time = "45 mins"
        print("Preparation Time: ", prep_time)
    def boil(self):
        boiled_items = ["pasta", "chicken"]
        boied_time = "20 mins"
        for i in range(2):
            print("You need to boil {} for {}".format(boiled_items[i],boied_time))
        super().boil()
    def chop(self):
        chopped_items = ["chicken", "garlic", "mushroom"]
        for i in range(3):
            print("You need to chop {}.".format(chopped_items[i]))
        super().chop()
    def grill(self):
        grilled_items = ["chicken", "mushrooms", "garlic"]
        grilled_time = "10 mins"
        for i in range(3):
            print("You need to grill {} for {}.".format(grilled_items[i],grilled_time))
        super().grill()
    def grate(self):
        grated_items = "cheese"
        print("You need to grate {}".format(grated_items))
        super().grate()
    def mix(self):
        mixed_items = "all ingredients"
        print("You need to mix {}!".format(mixed_items))
        super().mix()
    def salt(self):
        super().salt()
    def spicy(self):
        super().spicy()
    def cook(self):
        cook_time = "5 mins"
        print("You need to cook your meal for {}".format(cook_time))
        super().cook()
    def ready(self):
        super().ready()
    def rate(self):
        super().rate()

user_name = input("Please write your name: ")
print("Welcome {}! Hungry, huh?".format(user_name))
print("""We prepared 3 meals for you:
 1- Chicken Salad
 2- Meatball
 3- Pasta
 What would you like to cook?""")

while True:
    meal_select = input("Please write 1 for Chicken Salad, 2 for Meatball and 3 for Pasta. Your choice: ")
    if meal_select == "1":
        print("Purrrfect! You choose Chicken Salad!", "Your recipe is preparing... Please wait...", sep = "\n")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Let's start!!!")
        recipe_opt = ChickenSalad("{}".format(user_name))
        recipe_opt.main()
        break
    elif meal_select == "2":
        print("Deliciouss! You choose Meatball!", "Your recipe is preparing... Please wait...", sep = "\n")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Let's start!!!")
        recipe_opt = Meatball("{}".format(user_name))
        recipe_opt.main()
        break
    elif meal_select == "3":
        print("Tasssty! You choose Pasta!", "Your recipe is preparing... Please wait...", sep = "\n")
        for i in range(30):
            time.sleep(.1)
            print(".", end = " ")
        print("Let's start!!!")
        recipe_opt = Pasta("{}".format(user_name))
        recipe_opt.main()
        break
    else:
        print("We have 3 options for you. Please select 1,2 or 3!")
        continue


