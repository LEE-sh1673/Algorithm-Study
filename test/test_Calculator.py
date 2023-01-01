from unittest import TestCase

from test.Calculator import add


class Test(TestCase):
    def test_add(self):
        self.assertEqual(30, add(10, 20))
