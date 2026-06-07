# This is a simple shopping cart program that uses dictionaries to represent different shops and their inventory.
freelancers = {'name':'freelancing Shop',
               'brian': 70, 
               'black knight':20, 
               'biccus diccus':100, 
               'grim reaper':500,
                'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

def combine_stores(*stores):
    """This function takes in multiple stores and combines them into one store."""
    combined = {}
    for d in stores:
        combined.update(d)
        combined.pop('name', None)
    return combined

def calculate_total_cost(cart):
    """This function takes in a shopping cart and calculates the total cost."""
    total_cost = 0
    for item, price in cart.items():
        total_cost += price
    return total_cost

def print_store_inventory(store):
    """This function takes in a store and prints its inventory."""
    for item, price in store.items():
        if item != 'name':
            print(f"{item}: {price} gold pieces")

# -------- MAIN PROGRAM --------

print("Welcome to the shopping mall! You have 1000 gold pieces to spend. Let's start shopping!")

#create an empty shopping cart
cart = {}
#loop through stores/dicts
for SHOPNAME in [freelancers, antiques, pet_shop]:
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    print(f'\nWelcome to {SHOPNAME["name"]}! Here is what we have for sale:')
    print_store_inventory(SHOPNAME)

    buy_item = input('\nType what do you want to buy or "exit" to leave shop:').lower()
    #update the cart
    if buy_item in SHOPNAME:
        cart.update({buy_item: SHOPNAME.pop(buy_item)})
    elif buy_item == 'exit':
        print(f'You have exited {SHOPNAME["name"]} without buying anything. Moving on to the next store...')
    else:
        print(f'You have entered an invalid item. Exiting {SHOPNAME["name"]} and moving on to the next store...')

# print the shopping cart and the total cost of the items in the cart
if not cart:
    print("\nYou didn't buy anything today. Better luck next time!")
else:
    print(f'\nYou Purchased {len(cart)} Items Today and they are: ')
    for item in cart:
        print(f' - {item}')
    print(f'You used {calculate_total_cost(cart)} gold pieces today, you have {1000 - calculate_total_cost(cart)} gold pieces left in your purse.')

    print(f"\n(After Buying): Inventory in all stores: ")
    # print the inventory of all stores after shopping
    print_store_inventory(combine_stores(freelancers, antiques, pet_shop))