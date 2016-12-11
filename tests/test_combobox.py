"""
 Pylibui test suite.

"""

from pylibui.controls import Combobox
from tests.utils import WindowTestCase


class ComboboxTest(WindowTestCase):
    def setUp(self):
        super().setUp()
        self.combobox = Combobox()

    def test_set_selected(self):
        """Tests the set_selected method of the combobox."""
        self.combobox.append("option1")
        value = 0
        self.combobox.selected = value
        self.assertEqual(self.combobox.selected, value)
