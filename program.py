import sqlite3
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess


def print_menu():  # return the menu by rows
    return f'1. Get all customers \n2. Get customer by id \n3. Insert customer' +\
           f' \n4. Delete customer \n5. Update customer \n6. Exit \nPlease enter your choose: '


def get_customer():
    id = int(input('Enter id: '))
    customer = dao.get_customer_by_id(id)
    if customer is not None:  # chek if the customer are exist
        print(customer)       # if yes print customer else print massage
    else:
        print(f'Customer with id: {id} does not exist\n ')


def insert():
    _id = int(input('Enter id: '))
    if dao.get_customer_by_id(_id) is not None:  # chek if the id already exist
        print('customer with the same id already exist')
        return
    _f_name = str(input('Enter first name: '))
    _l_name = str(input('Enter last name: '))
    if chek(_f_name, _l_name) != 'yes':          # chek if the first name and last name already exist
        return
    _address = str(input('Enter address: '))
    _mobile = str(input('Enter mobile: '))
    customer = Customer(_id, _f_name, _l_name, _address, _mobile)
    dao.insert_customer(customer)
    print('Records updated successfully')


def delete():
    id = int(input('Enter id: '))
    if dao.get_customer_by_id(id) is not None:  # chek if the customer are exist
        dao.delete_customer(id)
        print('Records updated successfully')
    else:
        print(f'Customer with id: {id} does not exist')


def chek(_f_name, _l_name):  # this function chek if the first name and the last name already exist
    if dao.get_customer_by_f_name_and_l_name(_f_name, _l_name) is not None:
        return str(input('are you sure? '))
    return 'yes'


def update():
    id = int(input('Enter the current id: '))  # the current id
    if dao.get_customer_by_id(id) is None:     # chek if the id exist
        print('customer with the specified id does not exist')
        return
    _id = int(input('Enter the new id:'))      # chek that the new id not exist except the current id
    if dao.get_customer_by_id(_id) is not None and _id != id:
        print('customer with the same id already exist')
        return
    _f_name = str(input('Enter first name: '))
    _l_name = str(input('Enter last name: '))
    _address = str(input('Enter address: '))
    _mobile = str(input('Enter mobile: '))
    customer = Customer(_id, _f_name, _l_name, _address, _mobile)  # connecting all the inputs to one customer
    dao.update_customer(id, customer)
    print('Records updated successfully')


def action_selector(num_choose):  # the action selector convert the number to action
    if num_choose == 1:
        dao.print_all_costumers()
    elif num_choose == 2:
        get_customer()
    elif num_choose == 3:
        insert()
    elif num_choose == 4:
        delete()
    elif num_choose == 5:
        update()


def main():
    num_choose = int(input(f'\n{print_menu()}'))  # print the menu and get the input from the user
    while num_choose != 6:                        # if the input is 6 exit the loop
        if 6 < num_choose or num_choose < 1:      # if the input is not 1-5 get a new input and start over
            num_choose = int(input(f'\nYour input is not correct \n{print_menu()}'))
            continue
        else:                                     # else it's mean that the input is 1-5
            action_selector(num_choose)           # take the input to the action selector
        num_choose = int(input(f'\n{print_menu()}'))  # when he finished the action take another number
    print('Good bye!')


dao = CustomerDataAccess(r'C:\Users\erang\DataGripProjects\project_3\identifier.sqlite')
main()
sqlite3.connect(r'C:\Users\erang\DataGripProjects\project_3\identifier.sqlite').close()
