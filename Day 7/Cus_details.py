class customer:
    def __init__(self,first_name,customer_id,phone):
        self.first_name= first_name
        self.customer_id= customer_id
        self.phone= phone
    
    def display_customer_details(self):
        return f"Name of customer {self.first_name}, Customer ID: {self.customer_id}, phone num: {self.phone}"

class orders(customer):
    def __init__(self,order_id,order_status,staff_id):
        self.order_id= order_id
        self.order_status= order_status
        self.staff_id= staff_id

    def display_orders(self):
        return f"Order ID:  {self.order_id}, Order status: {self.order_status}, Staff ID: {self.staff_id}"

class order_items(customer):
    def __init__(self,item_id,quantity,discount):
        self.item_id= item_id
        self.quantity= quantity
        self.discount= discount
    
    def display_order_items(self):
        return f"Item ID: {self.item_id}, Quantity: {self.quantity}, Discount: {self.discount}"
    
class transaction(orders):
    def __init__(self, order_id,order_status,staff_id,transaction_id):
        # super().__init__(customer_id, name,phone,state)
        super().__init__(order_id,order_status,staff_id)
        self.transaction_id= transaction_id

    def display_transaction_details(self):
        return f"Order ID: {self.order_id}, Order Status: {self.order_status}, Transaction ID: {self.transaction_id}"
    

# Creating instances with correct parameters
customer_instance = customer("Vaish", 64973, 9876543210)
order_instance = orders( 101, "Approved", 11)
order_items_instance = order_items(1100,17,45)
transaction_instance = transaction(101,"Approved",11,1122)

# Printing details
print(customer_instance.display_customer_details())  # Accessing customer_id
print(order_instance.display_orders())  # Accessing order_id
print(order_items_instance.display_order_items())
print(transaction_instance.display_transaction_details())  # Adding () to call the function