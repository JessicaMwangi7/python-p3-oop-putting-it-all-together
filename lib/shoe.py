class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Private attribute for size
        self.condition = "New"  # Default condition of the shoe

        # Set the size using the setter
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # Check if size is an integer
            print("size must be an integer")
            self._size = 0  # Default to size 0 if invalid
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")  # Only print this message
        self.condition = "New"  # Reset condition to "New" (moved inside the method)
