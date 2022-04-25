from models import *
from rich.console import Console
from rich.table import Table

console = Console()

def create_tag(name):
    query = Tags.select().where(Tags.tag_name == name)
    if query.exists():
        console.print('tag already exist use one with a different name', style='Bold red')
    else:
        tag = Tags.create(tag_name = name) 
        console.print(f'Created a tag with name : {tag.tag_name}', style='Bold green')

def product_add_tag(product_id, tag_id):
    product_query = Products.select().where(Products.product_id == product_id)
    tag_query = Tags.select().where(Tags.id == tag_id)
    Tag_for_products.select()
    
    if tag_query.exists() and product_query.exists():
        product = Products.get(Products.product_id == product_id)
        tag = Tags.get(Tags.id == tag_id)
        test_query = Tag_for_products.select().where(Tag_for_products.product_id == product.product_id ,Tag_for_products.product_tag_id == tag.id)
        if test_query.exists():
            return console.print('tag already added to this product' , style='bold red')
        else:
            Tag_for_products.create(product_id = product , product_tag_id = tag)
            return console.print('tag has been paired with the product', style='bold green')
    else:
        console.print('Error: something went wrong', style='bold red')

def list_products_per_tag_id(tag_id):
    query = Products.select().join(Tag_for_products).where(Tag_for_products.product_tag_id == tag_id)
    if query.exists():
        print_list_tag_query(query)
    else:
        console.print('Could not find the tag', style='Bold red')

def list_products_per_tag_name(tag_name):
    find_tag_query = Tags.select().where(Tags.tag_name == tag_name)
    if find_tag_query.exists():
        for item in find_tag_query:
            query = Products.select().join(Tag_for_products).where(Tag_for_products.product_tag_id == item.id)
            print_list_tag_query(query)
            return
    else:
        console.print('Could not find the tag', style='Bold red')

#list all the tags
def list_all_tag():
    table = Table(title='All the tags')
    table.add_column('tag id')
    table.add_column('tag name')
    for tag in Tags:
        table.add_row(str(tag.id), tag.tag_name)
    console.print(table)

#print products connected to this tag 
def print_list_tag_query(query):
        table = Table(title='Product list that is connect to the tag')
        table.add_column('Product id')
        table.add_column('Product name')
        table.add_column('Product stock')
        for item in query:
            table.add_row(str(item.product_id),item.product_name,str(item.product_stock))
        console.print(table)