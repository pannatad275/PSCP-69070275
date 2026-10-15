'''Pad Thai'''
required_ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

required_tastes = {"Sweet", "Sour", "Salty"}

ingredients_used = set()
has_unknown_ingredient = False

while True:
    line = input().strip()
    if line == "Cook":
        break
    if line not in required_ingredients:
        has_unknown_ingredient = True
    ingredients_used.add(line)

tastes_present = set()
while True:
    line = input().strip()
    if line == "End":
        break
    tastes_present.add(line)
if has_unknown_ingredient:
    print("This is not Pad Thai!!!")
elif len(ingredients_used) < 11:
    print("This is bad!")
elif tastes_present == required_tastes:
    print("Delicious!")
else:
    print("Not Bad...")
