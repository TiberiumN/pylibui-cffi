"""
 Pylibui test suite.

"""

from pylibui import libui
from pylibui.controls import Control
from tests.utils import WindowTestCase


class ControlTest(WindowTestCase):
    def setUp(self):
        super().setUp()
        self.control = Control(libui.uiNewButton(''))

    def test_visible_initial_value(self):
        """Tests the control's `visible` initial value is True."""
        self.assertEqual(self.control.visible(), False)

    def test_show(self):
        """Tests the control can be shown."""
        self.control.show()
        self.assertEqual(self.control.visible(), True)

    def test_hide(self):
        """Tests the control can be hidden."""
        self.control.hide()
        self.assertEqual(self.control.visible(), False)

    def test_enabled_initial_value(self):
        """A control's `enabled` initial value should be True."""
        self.assertEqual(self.control.enabled, True)

    def test_can_enable_control(self):
        """Tests a control can be enabled."""
        self.control.enabled = True
        self.assertEqual(self.control.enabled, True)

    def test_can_disable_control(self):
        """Tests a control can be disabled."""
        self.control.enabled = False
        self.assertEqual(self.control.enabled, False)
