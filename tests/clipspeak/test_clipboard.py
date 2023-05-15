import unittest
from unittest import mock
from clipspeak import clipboard

class TestClipboard(unittest.TestCase):
    """A test case class for testing the clipboard module."""

    @mock.patch("pyperclip.paste")
    def test_get_clipboard(self, mock_paste):
        """Test if get_clipboard returns the correct clipboard contents."""
        # Set up different clipboard contents
        mock_paste.side_effect = ["Hello", "123", "", "ClipSpeak"]
        # Test if get_clipboard returns the same contents
        self.assertEqual(clipboard.get_clipboard(), "Hello")
        self.assertEqual(clipboard.get_clipboard(), "123")
        self.assertEqual(clipboard.get_clipboard(), "")
        self.assertEqual(clipboard.get_clipboard(), "ClipSpeak")

if __name__ == "__main__":
    unittest.main()
