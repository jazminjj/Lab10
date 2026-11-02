class MenuBoard:
    """A tool that knows about the menu. It knows nothing about chatting."""

    def __init__(self, menu):
        """Store the menu this tool can look up."""
        self.menu = menu

    def find_item(self, text):
        """Return the first known menu item mentioned in text, or None."""
        for item in self.menu:
            if item in text.lower():
                return item
        return None

    def price_for(self, item):
        """Return the price of one menu item, or None if unknown."""
        if item in self.menu:
            return self.menu[item]
        return None

    def list_items(self):
        """Return a list of all menu items as one comma-separated string."""
        return ", ".join(self.menu)
