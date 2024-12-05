import sqlite3
import time

class Market():
    def __init__(self,name,producer,price,production_date,consumption_date,size):
        self.name = name
        self.producer = producer
        self.price = price
        self.production_date = production_date
        self.consumption_date = consumption_date
        self.size = size

    def __str__(self):
        return "Name: {}\nProducer: {}\nPrice: {}\nProduction Date {}\nConsumption Date: {}\nSize: {}\n".format(self.name,self.producer,self.price,self.production_date,self.consumption_date,self.size)









class MarketLibrary():
    def __init__(self):
        self.create_connection()

    def create_connection(self):

        self.connection = sqlite3.connect("MarketLibrary.db")
        self.cursor = self.connection.cursor()

        questioning = "Create Table If not exists products(name TEXT,producer TEXT,Price INT,production date INT,consumption_date INT,size TEXT)"
        self.cursor.execute(questioning)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()


    def show_products(self):
        questioning = "Select * From products"
        self.cursor.execute(questioning)
        products = self.cursor.fetchall()

        if len(products) == 0:
            print("No products!")
        else:
            for i in products:
                product = Market(i[0],i[1],i[2],i[3],i[4],i[5])
                print(product)


    def question_products(self,name):
        questioning = "Select * From products where name = ?"
        self.cursor.execute(questioning,(name,))
        products = self.cursor.fetchall()

        if len(products) == 0:
            print("No products!")
        else:
            product = Market(products[0][0],products[0][1],products[0][2],products[0][3],products[0][4],products[0][5])
            print(product)

    def add_product(self,Market):
        questioning = "Insert into products Values(?,?,?,?,?,?)"
        self.cursor.execute(questioning,(Market.name,Market.producer,Market.price,Market.production_date,Market.consumption_date,Market.size))
        self.connection.commit()

    def delete_product(self,name):
        questioning = "Delete from products where name = ?"
        self.cursor.execute(questioning,(name,))
        self.connection.commit()

    def upgrade_year(self, name):
        querying = "Select * From products where name = ?"
        self.cursor.execute(querying, (name,))
        product = self.cursor.fetchone()

        if not product:
            print("No product!")
        else:
            try:
                consumption_date = int(product[4])  # Tablonuzda `consumption_date` bir yıl olarak saklanıyorsa.
                consumption_date +=1
                querying_update = "Update products set consumption_date = ? where name = ?"
                self.cursor.execute(querying_update, (name,consumption_date ))
                self.connection.commit()
                print("Consumption date updated.")
            except ValueError:
                print("Error: consumption_date is not a valid year.")

    def upgrade_size(self, name, new_size):
        querying = "Select * From products where name = ?"
        self.cursor.execute(querying, (name,))
        product = self.cursor.fetchone()

        if not product:
            print("No product!")
        else:
            current_size = product[5]
            if current_size == new_size:
                print(f"The size of the product is already {new_size}.")
            else:
                querying_update = "Update products set size = ? where name = ?"
                self.cursor.execute(querying_update, (new_size, name))
                self.connection.commit()
                print(f"Size updated to {new_size}.")
