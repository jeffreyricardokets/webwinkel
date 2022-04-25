from models import *
from rich.console import Console
from rich.table import Table

console = Console()

#create a user
def create_user(name,address,billing_information):
    query = Users.select().where(Users.username == name)
    if query.exists():
        return console.print('Error : there is already a user with that name', style='Bold red')
    else:
        user = Users.create(username = name, address = address, billing_information= billing_information)
        console.print(f"We create the user '{user.username}' in our database", style='Bold green')

#list the users that we have in our database
def user_list():
    table = Table(title='User List')
    table.add_column('name')
    table.add_column('addres')
    table.add_column('billing information')
    for user in Users:
        table.add_row(user.username, user.address, user.billing_information)
    console.print(table)

#list the users orders in a table
def list_user_orders(user_id):
    user = (Users.select().where(Users.user_id == user_id))
    if user.exists():
        orders = (Products.select(Orders.order_id,
        Orders.product_ammount,
        Orders.order_date,
        Orders.total_ammount ,
        Products)
        .join(Orders, attr='orders')
        .where(Orders.user_id == user_id))
        if orders.exists():
            user =  Users.get(Users.user_id == user_id)
            print_list_user_orders_table(user, orders)
        else:
            return console.print('could find any product attached to this user' , style='Bold red')
    else:
        return console.print('Could not find the user', style='Bold red')
        
#print the the table for the product list for the orders
def print_list_user_orders_table(user, orders):
    table = Table(title=f'The products of : {user.username}')
    table.add_column('Order ID')
    table.add_column('Name')
    table.add_column('Description')
    table.add_column('Product price')
    table.add_column('Quantity')
    table.add_column('Total price')
    table.add_column('Date orderd')
    for order in orders:
        table.add_row(str(order.orders.order_id),
        order.product_name,
        order.product_description,
        str(order.product_price_per_unit),
        str(order.orders.product_ammount),
        str(order.orders.total_ammount),
        str(order.orders.order_date))
    console.print(table)