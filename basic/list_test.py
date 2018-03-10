#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
import unittest


class TestList(unittest.TestCase):
    def test_square_brackets(self):
        a_list = [2, 3, 7, None]
        self.assertEqual(list, type(a_list))
        self.assertEqual([2, 3, 7, None], a_list)

    def test_list_fct(self):
        tup = ('foo', 'bar', 'baz')
        b_list = list(tup)
        self.assertEqual(list, type(b_list))
        self.assertEqual(['foo', 'bar', 'baz'], b_list)

    def test_modify_inplace(self):
        b_list = ['foo', 'bar', 'baz']
        b_list[1] = 'peekaboo'
        self.assertEqual(['foo', 'peekaboo', 'baz'], b_list)

    def test_materialise(self):
        gen = range(10)
        gen_list = list(gen)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], gen_list)


class TestAddRemove(unittest.TestCase):
    def test_list_append(self):
        b_list = ['foo', 'peekaboo', 'baz']
        b_list.append('dwarf')
        self.assertEqual(['foo', 'peekaboo', 'baz', 'dwarf'], b_list)

    def test_list_insert(self):
        b_list = ['foo', 'peekaboo', 'baz', 'dwarf']
        b_list.insert(1, 'red')
        self.assertEqual(['foo', 'red', 'peekaboo', 'baz', 'dwarf'], b_list)

    def test_list_pop(self):
        b_list = ['foo', 'red', 'peekaboo', 'baz', 'dwarf']
        self.assertEqual('peekaboo', b_list.pop(2))
        self.assertEqual(['foo', 'red', 'baz', 'dwarf'], b_list)

    def test_list_remove(self):
        b_list = ['foo', 'red', 'baz', 'dwarf']

        b_list.append('foo')
        self.assertEqual(['foo', 'red', 'baz', 'dwarf', 'foo'], b_list)

        b_list.remove('foo')
        self.assertEqual(['red', 'baz', 'dwarf', 'foo'], b_list)

    def test_list_contain(self):
        b_list = ['red', 'baz', 'dwarf', 'foo']
        self.assertEqual(True, 'dwarf' in b_list)
        self.assertEqual(False, 'dwarf' not in b_list)


class TestConcatenating(unittest.TestCase):
    def test_list_addition(self):
        self.assertEqual([4, None, 'foo', 7, 8, (2, 3)], [4, None, 'foo'] + [7, 8, (2, 3)])

    def test_list_extend(self):
        x = [4, None, 'foo']
        x.extend([7, 8, (2, 3)])
        self.assertEqual([4, None, 'foo', 7, 8, (2, 3)], x)


class TestSorting(unittest.TestCase):
    def test_list_sort(self):
        a = [7, 2, 5, 1, 3]
        a.sort()
        self.assertEqual([1, 2, 3, 5, 7], a)

    def test_sort_key(self):
        b = ['saw', 'small', 'He', 'foxes', 'six']
        b.sort(key=len)
        self.assertEqual(['He', 'saw', 'six', 'small', 'foxes'], b)


class TestBisect(unittest.TestCase):
    def test_list_bisect(self):
        c = [1, 2, 2, 2, 3, 4, 7]
        self.assertEqual(4, bisect.bisect(c, 2))
        self.assertEqual(6, bisect.bisect(c, 5))

    def test_list_insort(self):
        c = [1, 2, 2, 2, 3, 4, 7]
        bisect.insort(c, 6)
        self.assertEqual([1, 2, 2, 2, 3, 4, 6, 7], c)


class TestSlicing(unittest.TestCase):
    def test_basic_form(self):
        seq = [7, 2, 3, 7, 5, 6, 0, 1]
        self.assertEqual([2, 3, 7, 5], seq[1:5])

        seq[3:4] = [6, 3]
        self.assertEqual([7, 2, 3, 6, 3, 5, 6, 0, 1], seq)

    def test_oneside_omitted(self):
        seq = [7, 2, 3, 7, 5, 6, 0, 1]
        self.assertEqual([7, 2, 3, 7, 5], seq[:5])
        self.assertEqual([7, 5, 6, 0, 1], seq[3:])

    def test_neg_indice(self):
        seq = [7, 2, 3, 6, 3, 5, 6, 0, 1]
        self.assertEqual([5, 6, 0, 1], seq[-4:])
        self.assertEqual([6, 3, 5, 6], seq[-6:-2])

    def test_step(self):
        seq = [7, 2, 3, 6, 3, 5, 6, 0, 1]
        self.assertEqual([7, 3, 3, 6, 1], seq[::2])
        self.assertEqual([1, 0, 6, 5, 3, 6, 3, 2, 7], seq[::-1])
