#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
class Pizza:
    def __init__(self, size: str, crust_type: str, toppings=None):
        if toppings is None:
            toppings = []
        self._size = size          # protected attribute
        self._crust_type = crust_type
        self._toppings = toppings[:]
  
# 2. Add a method to add a new topping
    def add_topping(self, new_topping: str) -> None:
        if new_topping and new_topping not in self._toppings:
            self._toppings.append(new_topping)
        
# 3. Add a method to remove a topping if it exists
    def remove_topping(self, topping: str) -> bool:
        if topping in self._toppings:
            self._toppings.remove(topping)
            return True
        return False
# 4. Add a method to print pizza details:
    def __str__(self) -> str:
        """Return a human-readable description of the pizza."""
        toppings_str = ", ".join(self._toppings) if self._toppings else "No toppings yet!"
        return f"Size: {self._size}\nCrust: {self._crust_type}\nToppings: {toppings_str}"
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

if __name__ == "__main__":
    pizza = Pizza("medium", "regular", ["cheese", "tomato"])
    pizza.add_topping("olives")
    pizza.remove_topping("tomato")   # remove one topping
    print(pizza)