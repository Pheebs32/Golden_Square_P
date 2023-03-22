from collections import namedtuple
def menu():
    menu_entry = namedtuple('menu_entry', ['index','description','price'])
    _menu = []
    _menu.append(menu_entry(1, 'Hawaiian', '£6.50'))
    _menu.append(menu_entry(2, 'Ham & Cheese', '£5.50'))
    _menu.append(menu_entry(3, 'Beef & Onion', '£7.00'))
    _menu.append(menu_entry(4, 'Pepperoni', '£6.50'))
    _menu.append(menu_entry(5, 'Simply cheese', '£5.00'))

    for entry in _menu:
        index = str(getattr(entry, 'index')).ljust(5)
        descr = getattr(entry, 'description').ljust(25)
        price = getattr(entry, 'price').ljust(7)
        print ("{0}{1}{2}".format(index,descr,price))

menu()