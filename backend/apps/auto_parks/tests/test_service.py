from unittest import TestCase

from ..services import calc


class ServicesTestCase(TestCase):
    def test_plus(self):
        res = calc(1, 2, '+')
        self.assertEquals(res, 3)

    def test_minus(self):
        res = calc(2, 5, '-')
        self.assertEquals(res, -3)

    def test_multi(self):
        res = calc(3, 3, '*')
        self.assertEquals(res, 9)
