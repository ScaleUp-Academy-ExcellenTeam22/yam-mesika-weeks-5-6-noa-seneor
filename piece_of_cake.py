def get_recipe_price(prices, optionals=[], **ingredients):
    """
    :param prices: dictionary of ingredient key price value (100gr)
    :param optionals: list of optional ingredients
    :param ingredients: ingredient quantity
    :return: total price without optionals
    """
    total_lst = [ingredients.get(ing) * prices.get(ing) for ing in ingredients if ing not in optionals]
    return sum(total_lst)//100
