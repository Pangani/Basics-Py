# This is a simple shopping cart program that uses dictionaries to represent different shops and their inventory.
freelancers = {'name':'freelancing Shop',
               'brian': 70, 
               'black knight':20, 
               'biccus diccus':700, 
               'grim reaper':500,
                'minstrel':-15}
antiques = {'name':'Antique Shop',
            'french castle':400, 
            'wooden grail':3, 
            'scythe':150, 
            'catapult':75, 
            'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

def combine_stores(*stores):
    """This function takes in multiple stores and combines them into one store."""
    combined = {}
    for d in stores:
        combined.update(d)
        combined.pop('name', None)
    return combined

def print_inventory(store):
    """This function takes in a store and prints its inventory."""
    for item, price in store.items():
        if item != 'name':
            print(f"{item}: {price} gold pieces")

def adjust_total_cost(total_cost, purse, cart):
    """This function checks if the total cost of the items in the cart exceeds the amount of gold pieces in the purse."""
    print(f"\nYou don't have enough gold pieces to buy these items. You need {total_cost - purse} more gold pieces.")
    print(f'You have exceeded your budget of {purse} gold pieces. You need to remove some items from your cart.')
    while total_cost > purse:
        print(f'\nYour current total cost is {total_cost} gold pieces. Please remove an item from your cart.')
        print_inventory(cart)
        remove_item = input('Type the name of the item you want to remove: ').lower()
        # TODO: remove items based on numbering the items in the cart 
        # and allowing the user to input the number of the item they want to remove instead of typing the name of the item.
        if remove_item in cart:
            total_cost -= cart[remove_item]
            cart.pop(remove_item)
            print(f'{remove_item} has been removed from your cart.')
        else:
            print(f'{remove_item} is not in your cart. Please try again.')

    print("\nYour total cost is now within your budget. You can proceed to checkout.")
    # TODO: add a function that allows the user to add items back to the cart 
    # if they have removed too many items and want to add some back.
    return total_cost, cart
def check_budget(total_cost, purse):
    """This function checks if the total cost of the items in the cart exceeds the amount of gold pieces in the purse."""
    if total_cost > purse:
        return False
    else:
        return True

# -------- MAIN PROGRAM --------
print("Welcome to the shopping mall! You have 1000 gold pieces to spend. Let's start shopping!")

#create an empty shopping cart
cart = {}
purse = 1000
#loop through stores/dicts
for SHOPNAME in [freelancers, antiques, pet_shop]:
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    print(f'\nWelcome to {SHOPNAME["name"]}! Here is what we have for sale:')
    print_inventory(SHOPNAME)

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
    exit()

total_cost = sum(cart.values())

#TODO: create a function that checks if the total cost of the items in the cart exceeds the amount of gold pieces in the purse. If it does, prompt the user to remove items from the cart until the total cost is less than or equal to the amount of gold pieces in the purse.
if not check_budget(total_cost,purse):
    total_cost, cart = adjust_total_cost(total_cost, purse, cart)

print(f'\nYour total cost is {total_cost} gold pieces. You have {purse - total_cost} gold pieces left in your purse.')
print(f'\nYou Purchased {len(cart)} Items Today and they are: ')
print_inventory(cart)
print('Thank you for shopping with us! Have a great day!')

print(f"\n(After Buying): Inventory in all stores: ")
# print the inventory of all stores after shopping
print_inventory(combine_stores(freelancers, antiques, pet_shop))