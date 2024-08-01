class Customer:
    def __init__(self, customer_id, name, contact):
        """
        Initialize a new customer.

        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param contact: Contact details of the customer
        """
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def __str__(self):
        """
        Return a string representation of the customer.

        :return: String representation of the customer
        """
        return f"Customer[ID={self.customer_id}, Name={self.name}, Contact={self.contact}]"

class Table:
    def __init__(self, table_id, capacity):
        """
        Initialize a new table.

        :param table_id: Unique identifier for the table
        :param capacity: Number of seats at the table
        """
        self.table_id = table_id
        self.capacity = capacity
        self.is_available = True

    def assign_to_customer(self):
        """
        Assign the table to a customer and mark it as not available.
        """
        if self.is_available:
            self.is_available = False
            print(f"Table {self.table_id} assigned to a customer.")
        else:
            print(f"Table {self.table_id} is already assigned.")

    def release(self):
        """
        Release the table and mark it as available.
        """
        if not self.is_available:
            self.is_available = True
            print(f"Table {self.table_id} is now available.")
        else:
            print(f"Table {self.table_id} is already available.")

    def __str__(self):
        """
        Return a string representation of the table.

        :return: String representation of the table
        """
        status = "Available" if self.is_available else "Assigned"
        return f"Table[ID={self.table_id}, Capacity={self.capacity}, Status={status}]"

class Order:
    def __init__(self, order_id, customer, order_type):
        """
        Initialize a new order.

        :param order_id: Unique identifier for the order
        :param customer: Customer who placed the order
        :param order_type: Type of the order (DineIn, Takeaway, Delivery)
        """
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.order_type = order_type

    def add_item(self, item):
        """
        Add an item to the order.

        :param item: Item to be added
        """
        self.items.append(item)
        print(f"Added item {item} to order {self.order_id}.")

    def remove_item(self, item):
        """
        Remove an item from the order.

        :param item: Item to be removed
        """
        if item in self.items:
            self.items.remove(item)
            print(f"Removed item {item} from order {self.order_id}.")
        else:
            print(f"Item {item} not found in order {self.order_id}.")

    def calculate_total(self):
        """
        Calculate the total price of the order.

        :return: Total price
        """
        total = sum(item['price'] for item in self.items)
        return total

    def cancel_order(self):
        """
        Cancel the order.
        """
        self.items = []
        print(f"Order {self.order_id} has been canceled.")

    def __str__(self):
        """
        Return a string representation of the order.

        :return: String representation of the order
        """
        return f"Order[ID={self.order_id}, Customer={self.customer.name}, Type={self.order_type}, Items={self.items}]"

class DineInOrder(Order):
    def __init__(self, order_id, customer, table=None):
        super().__init__(order_id, customer, "DineIn")
        self.table = table

    def assign_table(self, table):
        self.table = table
        print(f"Table {table.table_id} assigned to dine-in order {self.order_id}.")

    def __str__(self):
        table_info = f", Table={self.table.table_id}" if self.table else ""
        return f"DineInOrder[ID={self.order_id}, Customer={self.customer.name}, Items={self.items}{table_info}]"

class TakeawayOrder(Order):
    def __init__(self, order_id, customer, pickup_time=None):
        super().__init__(order_id, customer, "Takeaway")
        self.pickup_time = pickup_time

    def schedule_pickup(self, pickup_time):
        self.pickup_time = pickup_time
        print(f"Pickup time {pickup_time} scheduled for takeaway order {self.order_id}.")

    def __str__(self):
        pickup_info = f", Pickup Time={self.pickup_time}" if self.pickup_time else ""
        return f"TakeawayOrder[ID={self.order_id}, Customer={self.customer.name}, Items={self.items}{pickup_info}]"

class DeliveryOrder(Order):
    def __init__(self, order_id, customer, delivery_address=None, delivery_time=None):
        super().__init__(order_id, customer, "Delivery")
        self.delivery_address = delivery_address
        self.delivery_time = delivery_time

    def schedule_delivery(self, delivery_address, delivery_time):
        self.delivery_address = delivery_address
        self.delivery_time = delivery_time
        print(f"Delivery scheduled to {delivery_address} at {delivery_time} for order {self.order_id}.")

    def __str__(self):
        delivery_info = f", Delivery Address={self.delivery_address}, Delivery Time={self.delivery_time}" if self.delivery_address and self.delivery_time else ""
        return f"DeliveryOrder[ID={self.order_id}, Customer={self.customer.name}, Items={self.items}{delivery_info}]"

# Main Menu
def main_menu():
    customers = {}
    tables = {1: Table(1, 4), 2: Table(2, 4), 3: Table(3, 2)}
    orders = {}

    while True:
        try:
            print("\nRestaurant Management System")
            print("1. Add Customer")
            print("2. Remove Customer")
            print("3. Edit Customer")
            print("4. View Customers")
            print("5. Assign Table to Customer")
            print("6. Add Order")
            print("7. Remove Order")
            print("8. Cancel Order")
            print("9. View Orders")
            print("10. Exit")
            choice = input("Enter your choice: ")

            if choice == '':
                raise ValueError("Input cannot be blank.")
            choice = int(choice)

            if choice == 1:
                add_customer(customers)
            elif choice == 2:
                remove_customer(customers)
            elif choice == 3:
                edit_customer(customers)
            elif choice == 4:
                view_customers(customers)
            elif choice == 5:
                assign_table_to_customer(customers, tables)
            elif choice == 6:
                add_order(customers, orders, tables)
            elif choice == 7:
                remove_order(orders)
            elif choice == 8:
                cancel_order(orders)
            elif choice == 9:
                view_orders(orders)
            elif choice == 10:
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def add_customer(customers):
    try:
        customer_id = input("Enter customer ID: ")
        if customer_id == '':
            raise ValueError("Customer ID cannot be blank.")
        name = input("Enter customer name: ")
        if name == '':
            raise ValueError("Customer name cannot be blank.")
        contact = input("Enter customer contact: ")
        if contact == '':
            raise ValueError("Customer contact cannot be blank.")
        customers[customer_id] = Customer(customer_id, name, contact)
        print(f"Customer {name} added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while adding the customer: {e}")

def remove_customer(customers):
    try:
        customer_id = input("Enter customer ID to remove: ")
        if customer_id == '':
            raise ValueError("Customer ID cannot be blank.")
        if customer_id in customers:
            del customers[customer_id]
            print(f"Customer {customer_id} removed successfully.")
        else:
            print(f"Customer {customer_id} not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while removing the customer: {e}")

def edit_customer(customers):
    try:
        customer_id = input("Enter customer ID to edit: ")
        if customer_id == '':
            raise ValueError("Customer ID cannot be blank.")
        if customer_id in customers:
            name = input("Enter new customer name: ")
            if name == '':
                raise ValueError("Customer name cannot be blank.")
            contact = input("Enter new customer contact: ")
            if contact == '':
                raise ValueError("Customer contact cannot be blank.")
            customers[customer_id].name = name
            customers[customer_id].contact = contact
            print(f"Customer {customer_id} updated successfully.")
        else:
            print(f"Customer {customer_id} not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while editing the customer: {e}")

def view_customers(customers):
    try:
        if customers:
            for customer in customers.values():
                print(customer)
        else:
            print("No customers found.")
    except Exception as e:
        print(f"An error occurred while viewing customers: {e}")

def assign_table_to_customer(customers, tables):
    try:
        customer_id = input("Enter customer ID to assign a table: ")
        if customer_id == '':
            raise ValueError("Customer ID cannot be blank.")
        if customer_id in customers:
            table_id = input("Enter table ID: ")
            if table_id == '':
                raise ValueError("Table ID cannot be blank.")
            table_id = int(table_id)
            if table_id in tables and tables[table_id].is_available:
                tables[table_id].assign_to_customer()
                print(f"Table {table_id} assigned to customer {customer_id}.")
            else:
                print(f"Table {table_id} is not available or does not exist.")
        else:
            print(f"Customer {customer_id} not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while assigning the table: {e}")

def add_order(customers, orders, tables):
    try:
        order_id = input("Enter order ID: ")
        if order_id == '':
            raise ValueError("Order ID cannot be blank.")
        customer_id = input("Enter customer ID: ")
        if customer_id == '':
            raise ValueError("Customer ID cannot be blank.")
        if customer_id in customers:
            order_type = input("Enter order type (DineIn, Takeaway, Delivery): ")
            if order_type == '':
                raise ValueError("Order type cannot be blank.")
            if order_type == "DineIn":
                table_id = input("Enter table ID: ")
                if table_id == '':
                    raise ValueError("Table ID cannot be blank.")
                table_id = int(table_id)
                if table_id in tables and tables[table_id].is_available:
                    tables[table_id].assign_to_customer()
                    orders[order_id] = DineInOrder(order_id, customers[customer_id], tables[table_id])
                else:
                    print(f"Table {table_id} is not available or does not exist.")
            elif order_type == "Takeaway":
                orders[order_id] = TakeawayOrder(order_id, customers[customer_id])
            elif order_type == "Delivery":
                delivery_address = input("Enter delivery address: ")
                if delivery_address == '':
                    raise ValueError("Delivery address cannot be blank.")
                delivery_time = input("Enter delivery time: ")
                if delivery_time == '':
                    raise ValueError("Delivery time cannot be blank.")
                orders[order_id] = DeliveryOrder(order_id, customers[customer_id], delivery_address, delivery_time)
            else:
                print("Invalid order type.")
            add_items_to_order(orders[order_id])
            print(f"Order {order_id} added successfully.")
        else:
            print(f"Customer {customer_id} not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while adding the order: {e}")

def add_items_to_order(order):
    try:
        while True:
            item_name = input("Enter item name (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            if item_name == '':
                raise ValueError("Item name cannot be blank.")
            item_price = input("Enter item price: ")
            if item_price == '':
                raise ValueError("Item price cannot be blank.")
            item_price = float(item_price)
            order.add_item({'name': item_name, 'price': item_price})
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while adding items to the order: {e}")

def remove_order(orders):
    try:
        order_id = input("Enter order ID to remove: ")
        if order_id == '':
            raise ValueError("Order ID cannot be blank.")
        if order_id in orders:
            del orders[order_id]
            print(f"Order {order_id} removed successfully.")
        else:
            print(f"Order {order_id} not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while removing the order: {e}")

def cancel_order(orders):
    try:
        order_id = input("Enter order ID to cancel: ")
        if order_id == '':
            raise ValueError("Order ID cannot be blank.")
        if order_id in orders:
            orders[order_id].cancel_order()
            print(f"Order {order_id} canceled successfully.")
        else:
            print(f"Order {order_id} not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred while canceling the order: {e}")

def view_orders(orders):
    try:
        if orders:
            for order in orders.values():
                print(order)
        else:
            print("No orders found.")
    except Exception as e:
        print(f"An error occurred while viewing orders: {e}")

if __name__ == "__main__":
    main_menu()
