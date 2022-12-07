import re
import pyodbc

from DB.Database import Database


class PlanesPruebaModel:
    def __init__(self):
        self.email = "a@b.cd"

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

    def temp(self):
        db = Database()
        db.cursor.execute("SELECT @@VERSION as version")
        
        while 1:
            row = db.cursor.fetchone()
            if not row:
                break
            print(row.version)
        
        db.cursor.close()
        db.connection.close()