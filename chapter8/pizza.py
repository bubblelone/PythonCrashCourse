
def make_pizza(size, *toppings):
    print("\nmaking a " + str(size) + "-inch pizza with the following toppings:")
    for toppoing in toppings:
        print("- " + toppoing)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')
