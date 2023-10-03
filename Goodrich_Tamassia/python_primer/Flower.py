class Flower:
    """"A class representing a flower for a store"""

    def __init__(self, name, petals, price):
        if not isinstance(name, str):
            raise ValueError('name parameter must be of string type')
        if not isinstance(petals, int):
            raise ValueError('petals parameter must be of type integer')
        if not isinstance(price, (float, int)):
            raise ValueError('price parameter must be of a numeric type')

        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError('parameter must be of string type')
        self._name = new_name

    def set_petals(self, new_petals):
        if not isinstance(new_petals, int):
            raise ValueError('parameter must be of type integer')
        self._petals = new_petals

    def set_price(self, new_price):
        if not isinstance(new_price, (float, int)):
            raise ValueError('parameter must be of a numeric type')
        self._price = new_price

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    def get_petal_number(self):
        return self._petals




