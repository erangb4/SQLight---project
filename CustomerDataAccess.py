import sqlite3
from Customer import Customer


class CustomerDataAccess:

    def __init__(self, file_path):
        self.con = sqlite3.connect(file_path)
        self.cur = self.con.cursor()

    def print_all_costumers(self):
        self.cur.execute("SELECT * FROM customer")
        for row in self.cur:  # print all the rows from the sql table
            print(row)

    def insert_customer(self, customer):
        self.cur.execute(f'INSERT INTO customer VALUES ({customer.id}, "{customer.f_name}",' + \
                         f' "{customer.l_name}", "{customer.address}", "{customer.mobile}") ')
        self.con.commit()

    def delete_customer(self, id):
        self.cur.execute(f'DELETE FROM customer WHERE id = {id}')
        self.con.commit()

    def get_all_customers(self):  # the function enter all the customers to one list and return it
        self.cur.execute(f'SELECT * FROM customer')
        _customers = []
        for person in self.cur:
            _customers.append(person)
        return _customers

    def update_customer(self, id, customer):
        self.cur.execute(f'UPDATE customer SET id = {customer.id}, f_name = "{customer.f_name}",' + \
                         f' l_name = "{customer.l_name}", address = "{customer.address}",' + \
                         f' mobile = "{customer.mobile}" WHERE id = {id}')
        self.con.commit()

    def get_customer_by_id(self, id):
        self.cur.execute(f'SELECT * FROM customer WHERE id = {id}')
        customer = None
        for row in self.cur:  # the function take all the details from the sql (by id) table
            customer = Customer(row[0], row[1], row[2], row[3], row[4])  # and return it by Customer file
        return customer

    def get_customer_by_f_name_and_l_name(self, f_name, l_name):
        self.cur.execute(f'SELECT * FROM customer WHERE f_name = "{f_name}" AND l_name = "{l_name}"')
        customer = None
        for row in self.cur:  # the function take all the details from the sql (by first name and last name) table
            customer = Customer(row[0], row[1], row[2], row[3], row[4])  # and return it by Customer file
        return customer
