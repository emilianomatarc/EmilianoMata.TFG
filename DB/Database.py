import pyodbc

class Database(object):

    connection = None
    cursor = None

    def __init__(self):
        if Database.connection is None:
            try:
                Database.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(LocalDB)\MSSQLLocalDB;DATABASE=GlobaLIS_DB;Trusted_Connection=yes;')
                Database.cursor = Database.connection.cursor()
            except Exception as error:
                print("Error: Connection not established {}".format(error))
            else:
                print("Connection established")

        self.connection = Database.connection
        self.cursor = Database.cursor