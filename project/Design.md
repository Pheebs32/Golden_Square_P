#User Stories
>As a customer
>So that I can check if I want to order something
>I would like to see a list of dishes with prices.

>As a customer
>So that I can order the meal I want
>I would like to be able to select some number of several available dishes.

>As a customer
>So that I can verify that my order is correct
>I would like to see an itemised receipt with a grand total.

Use the 'twilio-python' package to implement this next one. You will need to use mocks too.

>As a customer
>So that I am reassured that my order will be delivered on time
>I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

#Boiler Code
```python
class Menu():
    # public properties: 
    # menu: a string representing the menu in a list
    # price: a string repressenting the price in a list
    def __init__(self, menu):
        # _menu: a list representing the menu
        # side_effect: sets the above properties
        pass

    def menu(self):
        # menu_entry: a namedtuple which keeps the format of the menu as a list
        #_menu: a list of instances in menu_entry
        # index: attributes of 'index' in menu_entry
        # descr: attributes of 'description' in menu_entry
        # price: attributes of 'price' in menu_entry
        pass

    def all_menu(self):
        # returns: a list of the _menu
        pass

class ShoppingList():
    def __init__(self, shopping):
        # _shopping: a list representing shopping
        # total: integer
        # side_effect: sets the above properties
        pass

    def add(self):
        # shopping: an instance of menu
        # returns: nothing
        # side_effects: add to list of _shopping
        pass

    def all_shopping(self):
        # returns: a list of the _shopping
        pass

    def total(self):
        # total: an instance of _total
        # returns: grand total of _shopping
        # side_effects: returns total
        pass
```
# Create example intergration tests
```python
# Menu
''' Menu is populated with objects'''

menu = Menu()
menu.all() # => ['number', 'food', 'price', 'number', 'food', 'price']

# ShoppingList
''' Initially ShoppingList is empty'''

shopping = Shoppinglist()
shopping.all() # => []

# ShoppingList
''' Multiple entries have been added
all() lists them out in the order they where added'''

shopping = Shoppinglist()
shopping.add(['1'])
shopping.add(['2'])
shopping.add(['3'])
shopping.all() # => ['1', 'food', 'price', '2', 'food', 'price', '3', 'food', 'price']

