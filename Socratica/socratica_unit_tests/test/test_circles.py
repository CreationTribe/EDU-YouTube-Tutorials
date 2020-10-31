import unittest

from math import pi

from Socratica.socratica_unit_tests import circle_area


class TestCircleArea(unittest.TestCase):
	def test_area(self):
		# Test areas when radius >= 0
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

