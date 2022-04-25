from models import *
from rich.console import Console
from rich.table import Table

console = Console()

#def add_product_to_catalog(user_id, product):
def add_product_to_catalog(product_name, description, price_per_unit, stock):
    product = Products.select().where(Products.product_name == product_name)
    if product.exists():
        if not create_product_with_same_name():
            return
    item = Products.create(product_name = product_name, product_description = description, product_price_per_unit= price_per_unit, product_stock = stock)
    console.print(f"We created the following product in our database '{item.product_name}'", style='Bold green')

#product already exist ask if we want to continue
def create_product_with_same_name():
    console.print('That productname already exist do you want to put this record in the database?' , style='Bold red')
    input_user = input('Write Y to continue and N to exit ')
    if input_user == 'n' or input_user == 'N':
        print('You chose the option not to make another product with the same name')
        return False
    elif input_user == 'y' or input_user == 'Y':
        print('You chose the option to make another product with the same name')
        return True
    else:
        print('you pressed the wrong key')
        return False

#remove product from catalog search by id
def remove_product_from_catalog_by_id(product_id):
    remove_products = (Products.select().where(Products.product_id == product_id))
    if remove_products.exists():
        delete_products(remove_products)
    else:
        print('product not found')

#def remove product from catalog search by name mostly usefull to delete multiple objects
def remove_product_from_catalog_by_name(product_name):
    remove_products = (Products.select().where(Products.product_name ** product_name))
    if remove_products.exists():
        delete_products(remove_products)
    else:
        print('Product is not found')
        return

def delete_products(remove_products):
    for product in remove_products:
        remove_tags_from_product = Tag_for_products.select().where(Tag_for_products.product_id == product.product_id)
        if remove_tags_from_product.exists():
            for tag in remove_tags_from_product:
                tag.delete_instance()
        product.delete_instance()
        print('deleted this product')
#get a list of id and turn them into a table
def product_list_to_table(my_list):
    table = Table(title = 'Product list')
    table.add_column('product id')
    table.add_column('product name')
    table.add_column('product description')
    table.add_column('product price')
    for id in my_list:
        item = Products.get(Products.product_id == id)
        table.add_row(str(item.product_id), item.product_name, item.product_description, str(item.product_price_per_unit))
    console.print(table)    


def update_stock(product_id, new_quantity):
    query  = Products.select().where(Products.product_id == product_id)
    if query.exists():
        try:
            product  = Products.get(Products.product_id == product_id)
            old_stock = product.product_stock
            if old_stock == int(new_quantity):
                console.print('the current stock is same stock quantity as you provided', style='Bold red')
                return
            product.product_stock = new_quantity
            product.save()
            console.print(f'Changed the stock of product {old_stock} from to {product.product_stock}', style='Bold green')
        except:
            print('Error there is something wrong')
    else:
        print('could not find the product')


#list all the products we have in our database
def products_list():
    my_list =[]
    query = Products.select()
    for product in Products:
        my_list.append(product.product_id)
    product_list_to_table(my_list)
    