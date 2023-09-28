"""This is the inventory screen. It will show all the items the player has collected so far."""

init python:
    # All Items and their description
    item_book = {
        # Items
        "Popcorn": "Crunchy snack that restores +10 health.",
        "Churros" : "Sweet treat that restores +20 health"
    }
    
    class Inventory:
        def __init__(self):
            self.itemList = []
        
        def addItem(self, item_name, amount=1):
            if len(self.itemList) > 0:
                for item in self.itemList:
                    if item['name'] == item_name:
                        item['amount'] += amount
                        return
            self.itemList.append({'name': item_name, 'amount': amount})

        def deleteItem(self, item_name, amount=1):
            if self.isItem(item_name):
                for item in self.itemList:
                    if item['name'] == item_name:
                        if item['amount'] == amount:
                            self.itemList.remove(item)
                        elif item['amount'] > amount:
                            item['amount'] -= amount
                        else:
                            narrator("You don't have enough of this item!")
                        return
        
        def isItem(self, item_name):
            for item in self.itemList:
                if item['name'] == item_name:
                    return True
            return False
    
    def get_item_description(item_name):
        if item_name in item_book.keys():
            return item_book[item_name]
        return "No description available."