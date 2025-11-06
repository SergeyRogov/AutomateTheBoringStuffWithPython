def display_inventory(inventory):
    total_items = 0

    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
        total_items += value

    print("Total items:", total_items)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

def main():
    items = {
        "rope": 1,
        "torch": 6,
        "gold coin": 42,
        "dagger": 1,
        "arrow": 12
    }
    print("___BEFORE___")
    display_inventory(items)

    dragon_loot = [
        "gold coin",
        "dagger",
        "gold coin",
        "gold coin",
        "ruby"
    ]
    add_to_inventory(items, dragon_loot)

    print("\n___AFTER___")
    display_inventory(items)