#!/usr/bin/env python
# -*- coding: utf-8 -*-

import list2 as impl
import unittest


class TestList2(unittest.TestCase):

    def test_remove_adjacent(self):
        self.assertEqual(impl.remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(impl.remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(impl.remove_adjacent([]), [])

    def test_linear_merge(self):
        self.assertEqual(impl.linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
                         ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(impl.linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
                         ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(impl.linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
                         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    unittest.main()