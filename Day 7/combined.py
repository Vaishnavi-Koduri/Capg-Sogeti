from Cus_details import *

customer_instance = customer("Vaish", 64973, 9876543210)
order_instance = orders( 101, "Approved", 11)
order_items_instance = order_items(1100,17,45)
transaction_instance = transaction(101,"Approved",11,1122)

# Printing the customer details by importing them using *
print(customer_instance.display_customer_details())  # Accessing customer_id
print(order_instance.display_orders())  # Accessing order_id
print(order_items_instance.display_order_items())
print(transaction_instance.display_transaction_details())  # Adding () to call the function