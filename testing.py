import unittest
from find_combination import find_dish_combination3 as find_dish_combination

class TestCombo(unittest.TestCase):

    def prepare_items(self, item_names, item_prices):
        return [{'name': item_names[i], 'price': item_prices[i]} for i in range(len(item_names))]

    def test1(self):
        prepared_items = self.prepare_items(['a', 'b', 'c'], [2, 7, 3])
        possible_solutions = [
            ['a'] * 10,
            ['a'] * 7 + ['c'] * 2,
            ['a'] * 5 + ['b'] + ['c'],
            ['a'] * 4 + ['c'] * 4,
            ['a'] * 3 + ['b'] * 2,
            ['a'] * 2 + ['b'] + ['c'] * 3,
            ['a'] + ['c'] * 6,
            ['b'] * 2 + ['c'] * 2
        ]
        tested_solution = find_dish_combination(20, prepared_items)
        assert tested_solution in possible_solutions

    def test_empty_items(self):
        prepared_items = self.prepare_items([], [])
        self.assertEqual(find_dish_combination(20, prepared_items), [])

    def test_no_solution(self):
        prepared_items = self.prepare_items(['a','b'], [10,9])
        self.assertEqual(find_dish_combination(17, prepared_items), [])

    def test_exactly_one_item(self):
        prepared_items = self.prepare_items(['a','b','c'],[9,10,11])
        self.assertEqual(find_dish_combination(10, prepared_items), ['b'])


if __name__ == '__main__':
    unittest.main()