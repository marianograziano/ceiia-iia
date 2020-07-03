from unittest import TestCase
import math

import numpy as np

from ej_1 import vector_norm_l0, vector_norm_l1, vector_norm_inf, vector_norm_l2
from ej_2 import orden_segun_l2


class NormTestCase(TestCase):

    def test_norm_l0(self):
        a = np.array([[1,2,3,4],[5,6,7,8]])
        expected = np.array([4, 4])
        result = vector_norm_l0(a)
        np.testing.assert_equal(expected, result)

        a = np.array([[1,0,0,4],[5,6,0,8]])
        expected = np.array([2,3])
        result = vector_norm_l0(a)
        np.testing.assert_equal(expected, result)

    def test_norm_l1(self):
        a = np.array([[1,2,3,4],[5,6,7,8]])
        expected = np.array([10, 26])
        result = vector_norm_l1(a)
        np.testing.assert_equal(expected, result)

        a = np.array([[-1,-2,-3,-4],[-5,-6,-7,-8]])
        expected = np.array([10, 26])
        result = vector_norm_l1(a)
        np.testing.assert_equal(expected, result)

    def test_norm_l2(self):
        a = np.array([[1,2],[3,4]])
        expected = np.array([math.sqrt(5), math.sqrt(25)])
        result = vector_norm_l2(a)
        np.testing.assert_allclose(expected, result)

    def test_sorting_by_norm_l2(self):
        a = np.array([[1,2,3,4],[5,6,7,8]])
        sorted_a = orden_segun_l2(a)
        np.testing.assert_equal(np.array([[5,6,7,8],[1,2,3,4]]), sorted_a)

        a = np.array([[1,2,3,4],[10,11,12,13],[5,6,7,8]])
        sorted_a = orden_segun_l2(a)
        np.testing.assert_equal(np.array([[10,11,12,13],[5,6,7,8],[1,2,3,4]]), sorted_a)