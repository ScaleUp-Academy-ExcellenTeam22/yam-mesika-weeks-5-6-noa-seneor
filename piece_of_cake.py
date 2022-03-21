def get_recipe_price(prices, optionals=[], **ingredients):
    """
    receives as parameter a dictionary of ingredients : price for 100gr ,
    optional ingredients that we ignore and quantity for all ingredients
    :return: total price
    """
    total_lst = [ingredients.get(ing)*prices.get(ing) for ing in ingredients if ing not in optionals]
    return sum(total_lst)//100
