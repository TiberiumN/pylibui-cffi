"""
 Pylibui test suite.

"""

from pylibui.controls import Checkbox
from tests.utils import WindowTestCase


class CheckboxTest(WindowTestCase):
    def setUp(self):
        super().setUp()
        self.checkbox = Checkbox('my checkbox')

    def test_text_initial_value(self):
        """Tests the checkbox's `text` initial value is the one passed to
        constructor."""
        self.assertEqual(self.checkbox.text, 'my checkbox')

    def test_text_can_be_changed(self):
        """Tests the checkbox's `text` attribute can be changed."""
        text = 'My new checkbox'
        self.checkbox.text = text
        self.assertEqual(self.checkbox.text, text)

    def test_checked_initial_value(self):
        """Tests the checkbox's `checked` initial value is False."""
        self.assertEqual(self.checkbox.checked, False)

    def test_checked_can_be_set_to_true(self):
        """Tests the checkbox's `checked` attribute can be set to True."""
        self.checkbox.checked = True
        self.assertEqual(self.checkbox.checked, True)

    def test_checked_can_be_set_to_false(self):
        """Tests the checkbox's `checked` attribute can be set to False."""
        self.checkbox.checked = False
        self.assertEqual(self.checkbox.checked, False)
