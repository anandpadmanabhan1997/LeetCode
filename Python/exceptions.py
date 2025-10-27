class InventoryError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        if self.code:
            return f"[Error {self.code}] {self.message}"
        return self.message

try:
    raise InventoryError("Stock too low", code=404)
except InventoryError as e:
    print(e)  # Output: [Error 404] Stock too low
