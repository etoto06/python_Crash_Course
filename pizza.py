def make_pizza(size, *toppings):
    """주문 요약"""
    print(f" make {size} -inch")
    for topping in toppings:
        print(f"- {topping}")