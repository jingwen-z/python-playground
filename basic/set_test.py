#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


class TestSet(unittest.TestCase):
    def test_creation(self):
        set_a = set([2, 2, 2, 1, 3, 3])
        set_b = {2, 2, 2, 1, 3, 3}
        set_c = set_b.copy()
        self.assertEqual({1, 2, 3}, set_a)
        self.assertEqual({1, 2, 3}, set_b)
        self.assertEqual({1, 2, 3}, set_c)

    def test_union(self):
        a = {1, 2, 3, 4, 5}
        b = {3, 4, 5, 6, 7, 8}
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, a.union(b))
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, a | b)

        a.update(b)
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, a)
        self.assertEqual({3, 4, 5, 6, 7, 8}, b)

        b |= a
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, a)
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, b)

    def test_intersection(self):
        a = {1, 2, 3, 4, 5}
        b = {3, 4, 5, 6, 7, 8}
        self.assertEqual({3, 4, 5}, a.intersection(b))
        self.assertEqual({3, 4, 5}, a & b)

        a.intersection_update(b)
        self.assertEqual({3, 4, 5}, a)
        self.assertEqual({3, 4, 5, 6, 7, 8}, b)

        b &= a
        self.assertEqual({3, 4, 5}, a)
        self.assertEqual({3, 4, 5}, b)

    def test_add(self):
        a = {1, 2}
        a.add(3)
        self.assertEqual({1, 2, 3}, a)
        a.add(2)
        self.assertEqual({1, 2, 3}, a)

    def test_clear(self):
        a = {1, 2}
        a.clear()
        self.assertEqual(set(), a)

    def test_remove(self):
        a = {1, 2, 3, 4, 5}
        a.remove(4)
        self.assertEqual({1, 2, 3, 5}, a)

    def test_diff(self):
        a = {1, 2, 3, 4, 5}
        b = {3, 4, 5, 6, 7, 8}
        self.assertEqual({1, 2}, a.difference(b))
        self.assertEqual({1, 2}, a - b)
        self.assertEqual({6, 7, 8}, b.difference(a))
        self.assertEqual({6, 7, 8}, b - a)

        a.difference_update(b)
        self.assertEqual({1, 2}, a)
        self.assertEqual({3, 4, 5, 6, 7, 8}, b)

        a.add(3)
        b -= a
        self.assertEqual({1, 2, 3}, a)
        self.assertEqual({4, 5, 6, 7, 8}, b)

    def test_sym_diff(self):
        a = {1, 2, 3, 4, 5}
        b = {3, 4, 5, 6, 7, 8}
        self.assertEqual({1, 2, 6, 7, 8}, a.symmetric_difference(b))
        self.assertEqual({1, 2, 6, 7, 8}, a ^ b)

        a.symmetric_difference_update(b)
        self.assertEqual({1, 2, 6, 7, 8}, a)
        self.assertEqual({3, 4, 5, 6, 7, 8}, b)

        b ^= a
        self.assertEqual({1, 2, 6, 7, 8}, a)
        self.assertEqual({1, 2, 3, 4, 5}, b)

    def test_subset(self):
        a = {1, 2, 3}
        b = {1, 2, 3, 4, 5}
        c = {3, 4, 5, 6, 7}
        d = {6, 7}

        self.assertEqual(True, a.issubset(b))
        self.assertEqual(True, c.issuperset(d))
        self.assertEqual(True, a.isdisjoint(d))
        self.assertEqual(True, {1, 2, 3} == {3, 2, 1})

    def test_set_element(self):
        my_list = [1, 2, 3, 4]
        my_set = {tuple(my_list)}
        self.assertEqual({(1, 2, 3, 4)}, my_set)


if __name__ == '__main__':
    unittest.main()
