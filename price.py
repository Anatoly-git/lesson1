def format_price(price):
    price = int(price)
    return(f'Цена: {price} руб.')
over_price = format_price(56.24)
print(over_price)