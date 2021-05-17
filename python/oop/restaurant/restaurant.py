"""
Restaurant module.

Simulates the work of a restaurant.
"""

from abc import ABC, abstractmethod
from itertools import count

menu = {
    'Boneless Wings': 100,
    'Seared Steak': 80,
    'Chicken Dip': 80,
    'Fish & Chips': 75,
    'House Salad': 60,
    'Caesar Salad': 80,
    'Chicken Salad': 55,
    'Juice': 20,
    'Coca-Cola': 30,
    'Fudge Cake': 50,
    'Truffle Pie': 45
}


class Employee(ABC):
    """
    Employee class.

    Abstract class. Represents a restaurant employee.
    """
    def __init__(self, employee_id, employee_name, employee_position, employee_experience):
        self.employee_id = employee_id
        self._employee_name = employee_name
        self._employee_position = employee_position
        self._employee_experience = employee_experience

    @staticmethod
    def request_payment(order):
        """
        request_payment(order: Order)

        Requests an order payment.
        """
        order.customer.pay(order)


class Waiter(Employee):
    """
    Waiter class.

    Represents the restaurant waiter.
    """
    def __init__(self, employee_id, employee_name, employee_experience):
        super().__init__(employee_id, employee_name, 'waiter', employee_experience)
        self.orders_by_table = {}

    def take_order(self, customer, table_id, menu_items):
        """
        take_order(customer: CustomerIn, table_id: int, menu_items: str[])

        Allows waiter to take orders from customers.
        """
        order_in = InRestaurantOrder(customer, table_id, menu_items)
        if table_id in self.orders_by_table:
            self.orders_by_table[table_id].append(order_in)
        else:
            self.orders_by_table[table_id] = [order_in]
        order_in.order_status = 'taken'

    def give_orders(self, cook):
        """
        give_orders(cook: Cook)

        Transfers orders from waiter to the cook.
        """
        orders = []
        for order_list in self.orders_by_table.values():
            for order in order_list:
                if order.order_status == 'taken':
                    orders.append(order)
        cook.take_order(orders)

    @staticmethod
    def deliver_order(order):
        """
        deliver_order(order: Order)

        Allows waiter to deliver orders.
        """
        if order.order_status == 'prepared':
            print(f'Delivering order № {order.order_id}...')
            print(f'Order № {order.order_id} was delivered to table № {order.table_id}.')
            order.order_status = 'delivered'


class Deliveryman(Employee):
    """
    Deliveryman class.

    Represents the restaurant deliveryman.
    """
    def __init__(self, employee_id, employee_name, employee_experience):
        super().__init__(employee_id, employee_name, 'deliveryman', employee_experience)
        self.order_by_address = {}

    def take_order(self, customer, address, distance, menu_items):
        """
        take_order(customer: CustomerOut, address: str, distance: float, menu_items: str[])

        Allows deliveryman to take orders from customers.
        """
        order_out = DeliveryOrder(customer, address, distance, menu_items)
        if address in self.order_by_address:
            self.order_by_address[address].append(order_out)
        else:
            self.order_by_address[address] = [order_out]
        order_out.order_status = 'taken'

    def give_orders(self, cook):
        """
        give_orders(cook: Cook)

        Transfers orders from deliveryman to the cook.
        """
        orders = []
        for order_list in self.order_by_address.values():
            for order in order_list:
                if order.order_status == 'taken':
                    orders.append(j)
        cook.take_order(orders)

    @staticmethod
    def deliver_order(order):
        """
        deliver_order(order: Order)

        Allows deliveryman to deliver orders.
        """
        if order.order_status == 'prepared':
            print(f'Delivering order № {order.order_id}...')
            print(f'Order № {order.order_id} was delivered to the address {order.address}.')
            order.order_status = 'delivered'


class Cook(Employee):
    """
    Cook class.

    Represents the restaurant cook.
    """
    def __init__(self, employee_id, employee_name, employee_experience):
        super().__init__(employee_id, employee_name, 'cook', employee_experience)
        self.taken_orders = []

    def take_order(self, orders):
        """
        take_order(orders: Order[])

        Allows cook to receive orders from employees.
        """
        self.taken_orders += orders
        for order in orders:
            print(f'Order № {order.order_id} is taken.')
            order.order_status = 'preparing'
        self.prepare_all_orders()

    def prepare_all_orders(self):
        """
        prepare_all_orders()

        Prepares all taken orders.
        """
        for order in self.taken_orders:
            if order.order_status == 'preparing':
                self.prepare_order(order)

    @staticmethod
    def prepare_order(order):
        """
        prepare_order(order: Order)

        Prepares an order.
        """
        print(f'Preparing order № {order.order_id}...')
        print(f'Order № {order.order_id} is ready.')
        order.order_status = 'prepared'


class Customer(ABC):
    """
    Customer class.

    Abstract class. Represents a restaurant customer.
    """
    def __init__(self, customer_id, customer_cash):
        self.customer_id = customer_id
        self.customer_cash = customer_cash

    def cancel_order(self, order):
        """
        cancel_order(order: Order)

        Cancels the order.
        """
        if order.customer == self:
            order.order_status = 'canceled'

    def pay(self, order):
        """
        pay(order)

        Allows customer to pay for orders.
        """
        if self.customer_cash >= order.order_price:
            self.customer_cash -= order.order_price
            order.order_status = 'paid'
            print(f'Customer № {self.customer_id} paid the bill for the order № '
                  f'{order.order_id} ({order.order_price} UAH).')
            print(f'Current cash: {self.customer_cash} UAH.')


class CustomerIn(Customer):
    """
    CustomerIn class.

    Represents a customer inside the restaurant.
    """
    def __init__(self, customer_id, customer_cash, table):
        super().__init__(customer_id, customer_cash)
        table.add_customer(self.customer_id)
        self.table_id = table.table_id

    def make_order(self, employee, menu_items):
        """
        make_order(employee: Waiter, menu_items: str[])

        Allows customer to make orders in restaurant.
        """
        employee.take_order(self, self.table_id, menu_items)


class CustomerOut(Customer):
    """
    CustomerOut class.

    Represents a remote customer.
    """

    def make_order(self, employee, address, distance, menu_items):
        """
        make_order(employee: Deliveryman, address: str, distance: float, menu_items: str[])

        Allows customer to make delivery orders.
        """
        employee.take_order(self, address, distance, menu_items)


class Order(ABC):
    """
    Order class.

    Abstract class. Represents an order.
    """
    _id_counter = count(1)

    def __init__(self, customer, menu_items):
        self.order_id = next(self._id_counter)
        self.customer = customer
        self.menu_items = menu_items
        self.order_status = 'formed'

    @abstractmethod
    def calc_price(self):
        """
        calc_price()

        Abstract method. Implemented in inherited classes.
        """


class InRestaurantOrder(Order):
    """
    InRestaurantOrder class.

    Represents an order made in restaurant.
    """
    def __init__(self, customer, table_id, menu_items):
        super().__init__(customer, menu_items)
        self.table_id = table_id
        self.order_price = self.calc_price()

    def calc_price(self):
        """
        calc_price() -> float

        Calculates the cost of an order made in restaurant.
        """
        price = 0
        for item in self.menu_items:
            price += menu[item]
        return price


class DeliveryOrder(Order):
    """
    DeliveryOrder class.

    Represents a delivery order.
    """
    def __init__(self, customer, address, distance, menu_items):
        super().__init__(customer, menu_items)
        self.address = address
        self.distance = distance
        self.order_price = self.calc_price()

    def calc_price(self):
        """
        calc_price() -> float

        Calculates the delivery order cost.
        """
        price = 0
        for item in self.menu_items:
            price += menu[item]
        return price + self.distance*0.025


class Table:
    """
    Table class.

    Represents table in restaurant.
    """
    def __init__(self, table_id, table_capacity):
        self.table_id = table_id
        self.table_capacity = table_capacity
        self.is_available = True
        self.table_customers = []

    def add_customer(self, customer_id):
        """
        add_customer(customer_id: int)

        Adds customer to a table.
        """
        if self.is_available:
            self.table_customers.append(customer_id)
            self.table_capacity -= 1
            if self.table_capacity == 0:
                self.is_available = False
        else:
            print('There are no empty seats on this table.')

    def remove_customer(self, customer_id):
        """
        remove_customer(customer_id: int)

        Removes customer from table.
        """
        if customer_id in self.table_customers:
            self.table_customers.remove(customer_id)
            self.table_capacity += 1
            self.is_available = True
        else:
            print('This table does not have such customer.')

    def remove_all_customer(self):
        """
        remove_all_customer()

        Clears the table.
        """
        for customer in self.table_customers:
            self.remove_customer(customer)


# create table
table1 = Table(1, 4)

# create employees
cook1 = Cook(1, 'Josh', '5 years')
waiter1 = Waiter(2, 'John', '2 years')
deliveryman1 = Deliveryman(3, 'Bob', '4 months')

# create customers
customer_in1 = CustomerIn(1, 400, table1)
customer_in2 = CustomerIn(2, 200, table1)
customer_out1 = CustomerOut(3, 800)

print('\n==========RESTAURANT==========\n')

# customers in restaurant make orders
customer_in1.make_order(waiter1, ['Chicken Dip', 'Coca-Cola'])
customer_in2.make_order(waiter1, ['Seared Steak', 'Caesar Salad', 'Juice'])


# waiter transfers orders to the cook
waiter1.give_orders(cook1)

print()

# waiter delivers prepared orders
for i in waiter1.orders_by_table.values():
    for j in i:
        waiter1.deliver_order(j)

print()

# customer makes another order
customer_in1.make_order(waiter1, ['Fudge Cake'])

# waiter transfers order to the cook
waiter1.give_orders(cook1)

print()

# waiter delivers prepared orders
for i in waiter1.orders_by_table.values():
    for j in i:
        waiter1.deliver_order(j)

print()

# customers pay for orders
for i in waiter1.orders_by_table.values():
    for j in i:
        waiter1.request_payment(j)

print('\n==========DELIVERY==========\n')

# customer out of restaurant makes order
customer_out1.make_order(deliveryman1, 'Pushkinskaya st. 12/10', 1000,
                         ['Boneless Wings', 'Seared Steak', 'Seared Steak',
                          'Chicken Salad', 'Coca-Cola', 'Coca-Cola'])

# deliveryman transfers order to the cook
deliveryman1.give_orders(cook1)

print()

# deliveryman delivers prepared orders
for i in deliveryman1.order_by_address.values():
    for j in i:
        deliveryman1.deliver_order(j)

print()

# customer pay for order
for i in deliveryman1.order_by_address.values():
    for j in i:
        deliveryman1.request_payment(j)
