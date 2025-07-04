# Problem 4: Set Character
# In the previous exercise, we accessed and modified a players catchphrase attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

# Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

# If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
# Otherwise, it should print out "Invalid catchphrase".
# Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
    def set_catchphrase(self, new_catchphrase):
        # check if the catchphrase is valid (less than 20 chars, all contain only alphebetic, and whitespace characters)
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            # if its valid update catchphrase
            self.catchphrase = new_catchphrase
            # if its not valid print out "Invalid catchphrase".
        else:
            print("Invalid catchphrase")

# Example Usage:

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

# Example Output:

# Example 1:
# Catchphrase Updated!
# sweet dreams
# Invalid catchphrase
# sweet dreams


# Problem 5: Add Furniture
# Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

# Update the Villager class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.

# If the item is valid, add item_name to the player’s furniture attribute.
# The method does not need to return any values.
# item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".

class Villager:
    # ... methods from previous problems
	
    # New method
    def add_item(self, item_name):
        pass

# Example Usage:

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

# Example Output:

# []
# ["acoustic guitar"]
# ["acoustic guitar", "cacao tree"]
# ["acoustic guitar", "cacao tree"]