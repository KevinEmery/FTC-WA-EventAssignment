class League(object):
    
    def __init__(self, name: str, zip_code: str, capacity: int = 0):
        self.name = name
        self.zip_code = zip_code
        self.capacity = capacity
