import unittest
from classes.bar_tab import BarTab

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar_tab = BarTab(1, "Callum", 0)

    def test_room_has_tab_start_at_0(self):
        self.assertEqual(0, self.bar_tab.amount_spent)