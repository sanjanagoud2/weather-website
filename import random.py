import random

# Define the ingredients and quantities for 5 people
chicken_quantity = 750  # grams
yogurt_quantity = 1.5  # cups
ginger_garlic_paste_quantity = 1.5  # tablespoons
red_chili_powder_quantity = 1.5  # teaspoons
turmeric_powder_quantity = 0.75  # teaspoons
garam_masala_quantity = 1.5  # teaspoons
salt_quantity = "to taste"

rice_quantity = 3  # cups
water_quantity = "as needed"
cardamom_quantity = 5
cloves_quantity = 5
cinnamon_stick_quantity = 1
onion_quantity = 2  # large onions
tomato_quantity = 2  # large tomatoes
green_chilies_quantity = 4  # or 5 as per preference
coriander_leaves_quantity = 0.5  # cup
mint_leaves_quantity = 0.5  # cup
ghee_or_oil_quantity = "3 tablespoons"
milk_quantity = 0.5  # cup
saffron_quantity = "a pinch (optional)"
fried_onions_quantity = "3 tablespoons"

# Function to print ingredient and quantity
def print_ingredient(ingredient, quantity):
    print(f"- {quantity} {ingredient}")

# Print the ingredients and quantities
print("Ingredients for Chicken Biryani (for 5 people):")
print("\nFor Marinating Chicken:")
print_ingredient("chicken", f"{chicken_quantity} grams")
print_ingredient("yogurt", f"{yogurt_quantity} cups")
print_ingredient("ginger-garlic paste", f"{ginger_garlic_paste_quantity} tablespoons")
print_ingredient("red chili powder", f"{red_chili_powder_quantity} teaspoons")
print_ingredient("turmeric powder", f"{turmeric_powder_quantity} teaspoons")
print_ingredient("garam masala", f"{garam_masala_quantity} teaspoons")
print_ingredient("salt", salt_quantity)

print("\nFor Rice:")
print_ingredient("Basmati rice", f"{rice_quantity} cups")
print_ingredient("water", water_quantity)
print_ingredient("green cardamom pods", cardamom_quantity)
print_ingredient("cloves", cloves_quantity)
print_ingredient("cinnamon stick", cinnamon_stick_quantity)
print_ingredient("salt", salt_quantity)

print("\nFor Biryani:")
print_ingredient("onions", f"{onion_quantity} large, thinly sliced")
print_ingredient("tomatoes", f"{tomato_quantity} large, chopped")
print_ingredient("green chilies", f"{green_chilies_quantity} (slit)")
print_ingredient("fresh coriander leaves", f"{coriander_leaves_quantity} cup, chopped")
print_ingredient("fresh mint leaves", f"{mint_leaves_quantity} cup, chopped")
print_ingredient("ghee or vegetable oil", ghee_or_oil_quantity)
print_ingredient("warm milk", f"{milk_quantity} cup")
print_ingredient("saffron strands", saffron_quantity)
print_ingredient("fried onions", fried_onions_quantity)

# Additional cooking instructions can be added here.
