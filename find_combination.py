
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


"""
Just for fun... the recursive solution I found.  It's faster, but hits recursion limit when
the ratio between target price and dish prices is too high.
"""
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
