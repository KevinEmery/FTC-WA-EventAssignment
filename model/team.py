class Team(object):

    def __init__(self, number: str, zip_code: str, name: str = ""):
        self.number = number
        self.zip_code = zip_code
        self.name = name
