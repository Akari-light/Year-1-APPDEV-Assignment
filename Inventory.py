class Inventory:
    count_id = 0

    def __init__(self, med_name, quantity, med_type):
        Inventory.count_id += 1
        self.__med_id = Inventory.count_id
        self.__med_name = med_name
        self.__quantity = quantity
        self.__med_type = med_type

    def get_med_id(self):
        return self.__med_id

    def get_med_name(self):
        return self.__med_name

    def get_quantity(self):
        return self.__quantity

    def get_med_type(self):
        return self.__med_type

    def set_med_id(self, med_id):
        self.__med_id = med_id

    def set_med_name(self, med_name):
        self.__med_name = med_name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_med_type(self, med_type):
        self.__med_type = med_type
