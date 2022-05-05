
import csv
import sys

class InventoryFileException (Exception):
    pass

class InventoryNoKeyFoundException (Exception):
    pass

class Inventory:
    def __init__(self,filepath):
        self.file = filepath
        self.inventory_dictionary = {}
        self.readfile()


    def readfile(self):
        line_count = 0
        try:
            self.fhandle = open(self.file)
            reader = csv.reader(self.fhandle)
            for row in reader:
                if line_count == 0:
                    self.headers = row
                    line_count += 1
                    continue
                line_count += 1
                self.inventory_dictionary[row[0]] = row[1:]
            return True
        except FileNotFoundError:
            raise InventoryFileException("Error:  File not found")
        finally:
            self.fhandle.close()
        return True

    def returnHeaders(self):
        return self.headers

    def getCostOfInventoryData(self):

       return self.inventory_dictionary

    def set_itemname(self,SKU,new_name):
        try:
            self.inventory_dictionary[SKU] = new_name
            return True
        except KeyError:
            raise InventoryNoKeyFoundException("Error:  Invalid SKU")

    def set_itemunitcost(self,SKU,new_unit_cost):
        try:
            self.inventory_dictionary[SKU] = new_unit_cost
            return True
        except KeyError:
            raise InventoryNoKeyFoundException("Error:  Invalid SKU")
            return False

def cost_of_inventory_report(data):

    cost_of_inv_data = {}
    total = 0
    count = 0
    print("SKU\t\tItem Name\t\tCost Of Inventory")
    for (key,value) in data.items():
        count += 1
        cost_of_inventory = float(value[1].lstrip('$')) * int(value[2])
        total += cost_of_inventory
        print (f"{key} {value[0]}  ${cost_of_inventory}")

    print (f"Number of items processed: {count}")
    print (f"Total Cost of Inventory: ${total}")
    return



def main():
    filepath = r"C:\Users\User\basicpython\labs\lab5\data\inventory.csv"
    filepath = r"C:\Users\User\basicpython\labs\lab5\data\inventory.csv"
    inventory = Inventory(filepath)
    cost_of_inventory_report(inventory.getCostOfInventoryData())

main()


