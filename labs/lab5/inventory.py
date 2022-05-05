
import csv

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
        try:
            self.fhandle = open(self.file)
            reader = csv_reader(self.fhandle)
            self.headers = reader.readline()
            for row in reader:
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

        compiled_report_list = []
        for (key,value) in self.inventory_dictionary:
            report_row =[]
            report_row[0] = key
            report_row[1] = value[1]
            report_row[2] = value[3] * value[4]
            compiled_report_list.append(report_row)

        return compiled_report_list

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

def cost_of_inventory_report(compiled_data):
    total = 0
    print("SKU\t\tItem Name\t\tCost Of Inventory")
    for row in compiled_data:
        print (row)
        total += row[2]
    print (f"Number of items processed: {len(compiled_data)}")
    print (f"Total Cost of Inventory: {total}")
    return



def main():
    filepath = r"C:\Users\User\basicpython\labs\lab5\data\inventory.dat"
    inventory = Inventory(filepath)
    cost_of_inventory_report(inventory.getCostOfInventoryData())

main()


