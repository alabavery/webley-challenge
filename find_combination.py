def find_dish_combination3(target_price, dishes, total_price=0, combo_so_far=[]):
    if total_price > target_price:
        return []

    for i,dish in enumerate(dishes):
        if (target_price - total_price) % dish['price'] == 0:
            quantity_of_dish = int((target_price - total_price) / dish['price'])
            return combo_so_far + [dish['name']] * quantity_of_dish
        returned_combo = find_dish_combination3(target_price, dishes[i:], total_price + dish['price'],
                                               combo_so_far + [dish['name']])
        if len(returned_combo) > 0:
            return returned_combo
    return []

"""
Just for fun... an iterative solution.  It's very slow when
the ratio between target price and dish prices is very high.
"""
def find_dish_combination1(target_price, dishes):
    """
    :param target_price: float
    :param dishes: List({'name':str,'price':float})
    :return: List(str) (if no solution, then list is empty)
    """
    for start_dish_index,_ in enumerate(dishes):
        queue = [[0, start_dish_index, []]] # queue: List(List(current total, dishes included))

        while queue:
            total, last_dish_index, combo_solution = queue.pop()

            for i,dish in enumerate(dishes[last_dish_index:]):
                i += last_dish_index
                new_total = total + dish['price']
                new_combo_solution = combo_solution + [dish['name']]

                if new_total == target_price:
                    return new_combo_solution
                if new_total > target_price:
                    continue
                queue.append([new_total, i, new_combo_solution])
    return []


def find_dish_combination2(target_price, dishes, total_price=0, combo_so_far=[]):
    if total_price > target_price:
        return []
    if total_price == target_price:
        return combo_so_far

    for i,dish in enumerate(dishes):
        returned_combo = find_dish_combination2(target_price, dishes[i:], total_price + dish['price'],
                                               combo_so_far + [dish['name']])
        if len(returned_combo) > 0:
            return returned_combo
    return []