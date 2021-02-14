class Patient:
    def __init__(self, birth_cert, home_addr, telephone, medication):
        self.__birth_cert = birth_cert
        self.__home_addr = home_addr
        self.__telephone = telephone
        self.__medication = medication

    # accessor
    def get_birth_cert(self):
        return self.__birth_cert

    def get_home_addr(self):
        return self.__home_addr

    def get_telephone(self):
        return self.__telephone

    def get_medication(self):
        return self.__medication

    # mutator
    def set_birth_cert(self, birth_cert):
        self.__birth_cert = birth_cert

    def set_home(self, home_addr):
        self.__home_addr = home_addr

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def set_medication(self, medication):
        self.__medication = medication