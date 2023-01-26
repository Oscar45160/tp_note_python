
#  Imports
import pandas as pd
from datetime import datetime
import os

#  Class
class Contact:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.creation_time = datetime.today().date()
        self.contacts = []
        self.updated_phone = None

        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "creation_time": self.creation_time,
            "updated_phone": self.updated_phone
        }
        df = pd.DataFrame(data, index=[0])

        # if the file doesn't exist, create it and add the header
        if not os.path.isfile("data/contact.csv"):
            df.to_csv("data/contact.csv", header=True)
        else:  # else it exists so append without writing the header
            df.to_csv("data/contact.csv", index=False)


#  Update
    def update_phone(self, new_phone):
        self.updated_phone = datetime.today().date()
        self.phone = new_phone

        # convert the object to a DataFrame
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "creation_time": self.creation_time,
            "updated_phone": self.updated_phone
        }
        df = pd.DataFrame(data, index=[0])

        df.to_csv("data/contact.csv", mode='a', header=False, index=False)


#  Showing informations of object on screen
    def show_contact(self):
        print(self.first_name)
        print(self.last_name)
        print(self.phone)
        print(self.contacts)
        print(self.creation_time)

#  Create --> add a contact to object's contact list
    def create_contact(self, contact):
        self.contacts.append(contact)
        data_contact = {
            'Contact': self.contacts
        }
        df_contact = pd.DataFrame(data_contact)
        if not os.path.isfile(f'data/user/{self.first_name}.csv'):
            df_contact.to_csv(f'data/user/{self.first_name}.csv', header=True, index=False)
        else:
            df_contact.to_csv(f'data/user/{self.first_name}.csv', mode='a', header=False, index=False)

#  Delete --> remove contact from list
    def delete_contact(self, contact):
        self.contacts.remove(contact)

        data_contact = {
            'Contact': self.contacts
        }
        df_contact = pd.DataFrame(data_contact)
        if not os.path.isfile(f'data/user/{self.first_name}.csv'):
            pass
        else:
            df_contact = df_contact.query('Contact != "contact"')
        df_contact = pd.DataFrame(data_contact)


Oscar = Contact("Oscar", "Pimpaud", "0647246556")
Oscar.show_contact()
Oscar.create_contact("Victor")
Oscar.show_contact()
Oscar.delete_contact("Victor")
Oscar.show_contact()
