
def run():
    cart = ShoppingCart()

    # TODO: Implement CartItem and ShoppingCart to allow the usage just below:
    raise NotImplementedError("Shopping cart and cart item not done!")
    cart.add(CartItem("Tesla P85 - Yellow", 120000))
    cart.add(CartItem("Tesla - White", 69000))
    cart.add(CartItem("Lotus Evora", 79890))

    print_cart_summary(cart)


def print_cart_summary(cart):
    print()
    print("Shopping cart details:")
    print()
    subtotal = 0

    # TODO: Make sure cart is iterable.
    for item in cart:
        print("{0} ${1:,}".format(
            (item.name + " ").ljust(50, '.'),
            item.price))
        subtotal += item.price

    print("".ljust(60, '_'))
    print("{0} ${1:,}".format("Subtotal".ljust(50), subtotal))
    print("{0} ${1:,}".format("Tax".ljust(50), int(subtotal*.15)))
    print("{0} ${1:,}".format("Total".ljust(50), int(subtotal*1.15)))



class ShoppingCart:

    def __init__(self):
        pass

    # TODO: implement add and __iter__


class CartItem:
    pass
    # TODO: add constructor, store name and price
