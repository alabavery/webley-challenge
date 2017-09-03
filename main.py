import sys
import find_combination
import input_output

csv_file_path = input_output.get_csv_path(sys.argv)
target_price, dishes = input_output.get_csv_data(csv_file_path)

if target_price == 0:
    sys.exit('Target price is zero -- solution is an order of zero dishes.')

dish_combination = find_combination.find_dish_combination1(target_price, dishes)
# dish_combination = find_combination.find_dish_combination2(target_price, dishes) # different algorithm
input_output.print_dish_combination(dish_combination)