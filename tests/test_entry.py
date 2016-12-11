"""
 Pylibui test suite.

"""

from pylibui.controls import Entry, PasswordEntry, SearchEntry
from tests.utils import WindowTestCase


class EntryTest(WindowTestCase):
    def setUp(self):
        super().setUp()
        self.entry = Entry()

    def test_text_initial_value(self):
        """Tests the entry's `text` initial value is empty."""
        self.assertEqual(self.entry.text, '')

    def test_text_can_be_changed(self):
        """Tests the entry's `text` attribute can be changed."""
        text = 'My entry'
        self.entry.text = text
        self.assertEqual(self.entry.text, text)

    def test_read_only_initial_value(self):
        """Tests the entry's `read_only` initial value is False."""
        self.assertEqual(self.entry.read_only, False)

    def test_read_only_can_be_set_to_true(self):
        """Tests the entry's `read_only` attribute can be set to True."""
        self.entry.read_only = True
        self.assertEqual(self.entry.read_only, True)

    def test_read_only_can_be_set_to_false(self):
        """Tests the entry's `read_only` attribute can be set to False."""
        self.entry.read_only = False
        self.assertEqual(self.entry.read_only, False)
