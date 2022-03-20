def get_recipe_price(prices, optionals=[], **ingredients):
    total = 0
    for ing in ingredients:
        if ing not in optionals:
            total += ingredients.get(ing)*prices.get(ing)
    return total//100

