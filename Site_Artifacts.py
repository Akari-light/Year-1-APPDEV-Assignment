#### ACCOUNT CLASSES ####
# Shelve -> Accounts || {UUID: Account}
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

#### USER CLASSES ####
# Shelve -> Account_particulas || {UUID: User_Information}
class Users:
    def __init__(self, nric, address, postal_code, date_of_birth, contact_no, gender, race, nationality, medication = 'No Records', appointment_id = None):
        self.__nric = nric
        self.__address = address
        self.__postal_code = postal_code
        self.__date_of_birth = date_of_birth
        self.__contact_no = contact_no
        self.__gender = gender
        self.__race = race
        self.__nationality = nationality
        self.__medication = medication
        self.__appointment_id

    #Accesser & Mutator
    def set_nric (self, nric):
        self.__nric = nric

    def get_nric (self):
        return self.__nric
    
    def set_address (self, address):
        self.__address = address

    def get_address (self):
        return self.__address

    def set_postal_code (self, postal_code):
        self.__postal_code = postal_code

    def get_postal_code (self):
        return self.__postal_code

    def set_date_of_birth (self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_date_of_birth (self):
        return self.__date_of_birth

    def set_contact_no (self, contact_no):
        self.__contact_no = contact_no

    def get_contact_no (self):
        return self.__contact_no

    def set_gender (self, gender):
        self.__gender = gender

    def get_gender (self):
        return self.__gender

    def set_race (self, race):
        self.__race = race

    def get_race (self):
        return self.__race

    def set_nationality (self, nationality):
        self.__nationality = nationality

    def get_nationality (self):
        return self.__nationality

    def set_medication (self, medication):
        self.__medication = medication

    def get_medication (self):
        return self.__medication

    def set_appointment_id (self, appointment_id):
        self.__appointment_id = appointment_id

    def get_appointment_id (self):
        return self.__appointment_id

#### INVENTORY CLASSES ####
# Shelve -> Inventories || { Med_ID: Medicine_Information}
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

#### APPOINTMENT CLASSES ####
# Shelve -> Appointments || { Appointment_ID: Appointment_Information}
class Appointment():
    def __init__(self, doctor, appointment_type, date, time):
        self.__doctor = doctor
        self.__appointment_type = appointment_type
        self.__date = date
        self.__time = time

    #Accesser & Mutator
    def set_doctor (self, doctor):
        self.__doctor = doctor

    def get_doctor (self):
        return self.__doctor

    def set_appointment_type (self, appointment_type):
        self.__appointment_type = appointment_type

    def get_appointment_type (self):
        return self.__appointment_type

    def set_date (self, date):
        self.__date = date

    def get_date (self):
        return self.__date

    def set___time (self, __time):
        self.____time = __time

    def get___time (self):
        return self.____time