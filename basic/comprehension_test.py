#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


class TestComprehensio(unittest.TestCase):
    def test_list_comp(self):
        strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
        self.assertEqual(['BAT', 'CAR', 'DOVE', 'PYTHON'], [x.upper() for x in strings if len(x) > 2])

    def test_set_comp(self):
        strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
        unique_lengths = {len(x) for x in strings}
        self.assertEqual({1, 2, 3, 4, 6}, unique_lengths)
        self.assertEqual({1, 2, 3, 4, 6}, set(map(len, strings)))

    def test_dict_comp(self):
        strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
        loc_mapping = {val: index for index, val in enumerate(strings)}
        self.assertEqual({'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}, loc_mapping)

        words = ['apple', 'banana', 'candy']
        mapping = {word[0]: word for index, word in enumerate(words)}
        self.assertEqual({'a': 'apple', 'b': 'banana', 'c': 'candy'}, mapping)

        mapping = {word[0]: word for _, word in enumerate(words)}
        self.assertEqual({'a': 'apple', 'b': 'banana', 'c': 'candy'}, mapping)

        mapping = {word[0]: word for word in words}
        self.assertEqual({'a': 'apple', 'b': 'banana', 'c': 'candy'}, mapping)

    def test_single_nested_list_comp(self):
        all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Matalia', 'Pilar']]
        result = [name for names in all_data for name in names if name.count('e') >= 2]
        self.assertEqual(['Steven'], result)

    def test_nested_list_comp(self):
        some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        flattened = [x for tup in some_tuples for x in tup]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], flattened)

        list_of_lists = [[x for x in tup] for tup in some_tuples]
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], list_of_lists)


if __name__ == '__main__':
    unittest.main()
