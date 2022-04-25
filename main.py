__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import products
import users
import tags
import orders
import search
import finance
import argparse


def main():
    request_input_parser()

if __name__ == "__main__":
    #to create the tables
    db.create_tables([Users,Products,Orders,Tags,Tag_for_products])

    def request_input_parser():
        #create the top-level parser
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest = 'command')

        #create the parser for creating users
        parser_c_user = subparser.add_parser('add-user', help='Users')
        parser_c_user.add_argument('--username')
        parser_c_user.add_argument('--address')
        parser_c_user.add_argument('--payment')

        #create the parser for showing the users
        subparser.add_parser('user-list', help='create a list of all users')

        #create the parser for showing the products
        subparser.add_parser('product-list', help='create a list of all product')

        #create the parser for showing the tags
        subparser.add_parser('tag-list', help='create a list of all tags')

        #create the parser for showing products that the user have
        parser_show_user_products = subparser.add_parser('show-products-user', help='create a list of all user product')
        parser_show_user_products.add_argument('--user-id')

        #create the parser to add product to catalog
        parser_create_catalog_product = subparser.add_parser('create-catalog-product' , help='add product to the catalog')
        parser_create_catalog_product.add_argument('--product-name')
        parser_create_catalog_product.add_argument('--description')
        parser_create_catalog_product.add_argument('--price')
        parser_create_catalog_product.add_argument('--stock')

        #create the parser to update product stock
        parser_update_stock = subparser.add_parser('update-stock', help='change stock of product')
        parser_update_stock.add_argument('--product-id')
        parser_update_stock.add_argument('--ammount-stock')

        #create the parser to remove a product
        parser_remove_catalog_product = subparser.add_parser('remove-catalog-product', help='remove a product from the catalog')
        parser_remove_catalog_product.add_argument('--id')
        parser_remove_catalog_product.add_argument('--product-name')

        #create a parser to create a tag
        parser_create_tag = subparser.add_parser('create-tag' , help='Create a tag')
        parser_create_tag.add_argument('--tag-name')

        #create a parser to pair a tag to a product
        parser_pair_product_tag = subparser.add_parser('pair-product-tag', help="pair a product to a tag")
        parser_pair_product_tag.add_argument('--product-id')
        parser_pair_product_tag.add_argument('--tag-id')

        #create a parser to list products that are connected to a tag
        parser_list_products_tag = subparser.add_parser('list-products-on-tag' , help='display all the items that is paired with this tag')
        parser_list_products_tag.add_argument('--tag-id')
        parser_list_products_tag.add_argument('--tag-name')

        #create a parser to search for a product
        parser_search = subparser.add_parser('search', help='search')
        parser_search.add_argument('--product')

        #create a parser to buy a product for a user
        parser_buy_product = subparser.add_parser('buy', help='buy a product for the user')
        parser_buy_product.add_argument('--product-id')
        parser_buy_product.add_argument('--buyer-id')
        parser_buy_product.add_argument('--quantity')

        #give a user a product
        parser_give_product = subparser.add_parser('give-product', help='give a product for the user')
        parser_give_product.add_argument('--product-id')
        parser_give_product.add_argument('--buyer-id')
        parser_give_product.add_argument('--quantity')

        #remove product from user
        parser_remove_product = subparser.add_parser('remove-product', help='remove a product/order')
        parser_remove_product.add_argument('--product-id')
        parser_remove_product.add_argument('--user-id')

        #create a parser to print the revenue
        parser_revenue = subparser.add_parser('revenue', help='print revenue need --startdate en --enddate')
        parser_revenue.add_argument('--startdate')
        parser_revenue.add_argument('--enddate')

        args = parser.parse_args()

        if args.command == 'add-user':
            users.create_user(args.username, args.address, args.payment)

        if args.command == 'user-list':
            users.user_list()

        if args.command == 'product-list':
            products.products_list()
        
        if args.command =='tag-list':
            tags.list_all_tag()

        if args.command == 'show-products-user':
            users.list_user_orders(args.user_id)

        if args.command == 'create-catalog-product':
            products.add_product_to_catalog(args.product_name, args.description, args.price, args.stock)

        if args.command == 'update-stock':
            products.update_stock(args.product_id,args.ammount_stock)

        if args.command == 'remove-catalog-product':
            if args.id:
                products.remove_product_from_catalog_by_id(args.id)
            elif args.product_name:
                products.remove_product_from_catalog_by_name(args.product_name)

        if args.command == 'create-tag':
            tags.create_tag(args.tag_name)
        
        if args.command == 'pair-product-tag':
            tags.product_add_tag(args.product_id, args.tag_id)


        if args.command == 'list-products-on-tag':
            if args.tag_id:
                tags.list_products_per_tag_id(args.tag_id)
            elif args.tag_name:
                tags.list_products_per_tag_name(args.tag_name)

        if args.command == 'search':
            search.search(args.product)

        if args.command == 'buy':
            orders.purchase_product(args.product_id, args.buyer_id, int(args.quantity))

        if args.command == 'give-product':
            orders.add_product(args.product_id, args.buyer_id, int(args.quantity))

        if args.command == 'remove-product':
            orders.remove_product(args.product_id, args.user_id)
        if args.command == 'revenue':
            finance.show_revenue(args.startdate,args.enddate)

    main()