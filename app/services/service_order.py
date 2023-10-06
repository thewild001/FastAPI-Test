def process_orders(orders, criterion):
    total_price = 0 
    for order in orders:
        if criterion == "all" or order.status == criterion:
            total_price += order.quantity * order.price
    
    return round(total_price, 2)
