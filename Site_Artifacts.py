class Account():
    def __init__(self, first_name, last_name, email, password, account_type = "P"):
        self.__account_type = account_type
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    #Accesser & Mutator
    def set_account_type (self, account_type):
        self.__account_type = account_type

    def get_account_type (self):
        return self.__account_type

    def set_first_name (self, first_name):
        self.__first_name = first_name

    def get_first_name (self):
        return self.__first_name
    
    def set_last_name (self, last_name):
        self.__last_name = last_name

    def get_last_name (self):
        return self.__last_name

    def set_email (self, email):
        self.__email = email

    def get_email (self):
        return self.__email

    def set_password (self, password):
        self.__password = password

    def get_password (self):
        return self.__password

    #Methods
    def get_full_name(self):
        full_name = "{} {}".format(self.get_first_name(), self.get_last_name())
        return(full_name)

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

