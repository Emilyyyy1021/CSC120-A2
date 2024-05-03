from computer import Computer
"""
File: oo_resale_shop.py
Author: Emily Wang
Date: Feb 7, 2023
Description: Holds the functions of a resale shop, such as buying a computer (add to inventory), 
selling a computer (remove from inventory), and storing the inventory for the store
"""
class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        self.itemID = 0

    # What methods will you need?
        
    # Buying(add) a computer 
    def buy(self, computer: Computer):
        """
        Takes in a Dict containing all the information about a computer,
        adds it to the inventory, returns the assigned item_id
        """
        self.itemID += 1
        self.inventory.append((self.itemID, computer))
        return self.itemID
    
    # Sell(remove) a computer
    def sell(self, item_id: int):
        """
        Takes in an item_id, removes the associated computer if it is the inventory, 
        prints error message otherwise
        """
        found = False
        for id_, _ in self.inventory:
            if id_ == item_id:
                self.inventory.remove((id_, _))
                print("Item", item_id, "sold!")
                found = True
                break
        
        # If the item_id is not found in the inventory
        if not found:
            print("Item", item_id, "not found. Please select another item to sell.")

    # Print the inventory 
    def print_inventory(self):
        """
        Prints all the items in the inventory (if it isn't empty).
        """
        # If the inventory is not empty
        if self.inventory:
            # For each computer in the inventory
            for itemID, computer in self.inventory:
                # Print its details
                print(f'Item ID: {itemID} : {computer.description, computer.processor_type, computer.hard_drive_capacity, computer.memory, computer.operating_system, computer.year_made, computer.price}')
        else:
            print("No inventory to display.")


def main():
    shop = ResaleShop()
    # shop.buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, 
    # "operating_system":"High Sierra", "year_made":2019, "price":1000})
    newComputer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    print(shop.buy(newComputer))
    shop.print_inventory()
    shop.sell(1)

if __name__ == "__main__": 
    main()