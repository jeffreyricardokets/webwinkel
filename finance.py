from models import *
from rich.console import Console

console = Console()

#earning filter
def show_revenue(first_date,second_date):
    orders = Orders.select().where(Orders.order_date.between(first_date,second_date))
    if orders.exists():
        revenue_counter = 0
        for order in orders:
            revenue_counter = revenue_counter + order.total_ammount
        return console.print(f"the revenenue from the selected date's is : {round(revenue_counter,2)} euro's", style='Bold green')
    else:
        return console.print('no record found', style='Bold red')