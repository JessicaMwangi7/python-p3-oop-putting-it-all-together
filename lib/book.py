class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize the internal page_count to None

        # Validate page_count is an integer, if not, print an error
        self.page_count = page_count
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):  # Check if value is an integer
            print("page_count must be an integer")
            self._page_count = 0  # If not an integer, set page_count to 0
        else:
            self._page_count = value  # Otherwise, set it to the given value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  # Print when turning the page
