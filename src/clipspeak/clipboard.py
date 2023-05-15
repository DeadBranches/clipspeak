import pyperclip

def get_clipboard():
    """Return the clipboard contents as a string."""
    return pyperclip.paste()
