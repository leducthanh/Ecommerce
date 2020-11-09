from django.test import TestCase
def add(a,b):
    return a+b

class CalcTests(TestCase):
    def TestSum(self):
        """This is test summation"""
        self.assertSetEqual(add(3, 4), 7)

