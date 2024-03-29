class Record:
    def __init__(self, name, surname, number="", email=""):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

    @staticmethod
    def jdefault(o):
        return o.__dict__

    def is_incomplete_records(self):
        return self.number == "" or self.email == ""

    def __eq__(self, other):
        return self.name.__eq__(other.name) and self.surname.__eq__(other.surname) and self.number.__eq__(
            other.number) and self.email.__eq__(other.email)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name + '\t' + self.surname + '\t' + self.number + '\t' + self.email
