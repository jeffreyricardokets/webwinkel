from os import remove
from models import *
import datetime
from rich.console import Console

console = Console()

#purchase a product for the user
def purchase_product(product_id, buyer_id, quantity):
    buyer = Users.get(Users.user_id == buyer_id)
    product = Products.get(Products.product_id == product_id)
    
    if product.product_stock >= quantity:
        give_user_product_tool(buyer,product, quantity)
    else:
        print('not enough in stock')

#add a product for the user
def add_product(product_id, buyer_id, quantity):
    buyer = Users.get(Users.user_id == buyer_id)
    product = Products.get(Products.product_id == product_id)
    
    if product.product_stock >= quantity:
        give_user_product_tool(buyer,product, quantity, True)
    else:
        console.print('not enough in stock', style='Bold red')

#give user the product he bought
def give_user_product_tool(buyer, product, quantity , free = False):
    product.product_stock = product.product_stock - quantity
    product.save()       
    if not free:
        price =  product.product_price_per_unit
    else:
        price = 0
    order_made = Orders.create(order_product = product, product_ammount = quantity,
    product_price = price,
    total_ammount = price * quantity,
    order_date = datetime.datetime.now(),
    user = buyer)
    console.print(f'{product.product_name} added to the user', style='Bold green')


def delete_order(order_id):
    item_to_delete = Orders.get(Orders.order_id == order_id)
    item_to_delete.delete_instance()
    return console.print('Order has removed from our database', style='Bold green')

#remove order from user
def remove_product(product_id,user_id, remove_row = False):
    find_if_order_exist = Orders.select().where((Orders.order_product_id == product_id) & (Orders.product_ammount >= 1))
    if find_if_order_exist.exists():
        query = Orders.select().where((Orders.order_product_id == product_id) & (Orders.user_id == int(user_id)) & (Orders.product_ammount >= 1))
        if query.exists():
            for item in query:
                object = Orders.get(Orders.order_id == item.order_id)
                if object.product_ammount > 1:
                    object.product_ammount = item.product_ammount - 1
                    object.save()
                    return console.print('Removed one item from the user', style='Bold green')
                else:
                    delete_order(item.order_id)
                    return
        else:
            console.print('User id does not match the one we have in our database', style='Bold red')
    else:
        console.print('Order has not been found in our database' , style='Bold red')

