import csv

def get_csv_path(sys_argv):
    if len(sys_argv) < 2:
        raise RuntimeError("Please provide a valid file path for the CSV data.")
    return sys_argv[1]


def get_csv_data(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader_ = csv.reader(csvfile, delimiter=',')

        try:
            row1 = next(reader_)
        except StopIteration:
            raise RuntimeError("Provided CSV is empty.")
        if row1[0].lower() != 'target price':
            raise RuntimeError("CSV data does not match required format.")
        try:
            target_price = float(row1[1].replace('$', ''))
        except ValueError:
            raise ValueError('Invalid target price in CSV file.')
        if target_price < 0:
            raise RuntimeError("Provided target price less than zero.")

        dishes = []
        row_counter = 1
        for row in reader_:
            row_counter += 1
            try:
                dish_price = float(row[1].replace('$', ''))
            except:
                raise RuntimeError("Invalid format for dish on row " + str(row_counter))

            if dish_price <= 0:
                raise RuntimeError("Non-positive value provided for dish price row " + str(row_counter))
            dish = {'name':row[0], 'price':dish_price}
            dishes.append(dish)

    return target_price, dishes


def print_dish_combination(dish_combination):
    if len(dish_combination) == 0:
        print("There is no combination of dishes that is equal to the target price.")
    else:
        print("Dish combination for target price:")
        print(' * ' + '\n * '.join(dish_combination))
