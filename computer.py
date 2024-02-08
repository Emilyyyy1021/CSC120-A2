"""
File: computer.py
Author: Emily Wang
Date: Feb 7, 2023
Description: Holds the functions of a computer, such as updating a computer's price, updating a computer's OS, and refurbishing a computer
"""
class Computer:
    # from typing import Optional

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str 
    year_made: int
    price: int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # set up the constructor
    def __init__(self, description, processor_type , hard_drive_capacity, memory, operating_system,
                 year_made, price ):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
        
    # update the price
    def update_price(self, new_price: int):
        """
        Takes in a new price, updates the price of the associated computer 
        """
        # if item_id in shop.inventory:
        #     shop.inventory[item_id]["price"] = new_price
        #     print(shop.inventory[item_id].price)
        # else:
        #     print("Item", item_id, "not found. Cannot update price.")

        self.price = new_price
        return self.price
    
    # update the operating system
    def update_os(self, new_os):
        """
        Takes in a new operating system, updates the system of the associated computer
        """
        self.operating_system = new_os # update details after installing new OS
        return self.operating_system
    
    # refurbish the computer & update system
    def refurbish(self, new_os: str):
        """
        Takes in a new operating system, updates the system of the associated computer, 
        and update the price of the computer according to its year made
        """
        # if item_id in shop.inventory:
        # computer = shop.inventory[item_id] # locate the computer
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        if new_os is not None: 
            self.operating_system = new_os # update details after installing new OS
            return self.operating_system



def main():
    newcomputer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    

    
    



if __name__ == "__main__":
    main()
    