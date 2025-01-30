class customer:
    def __init__(self,first_name,customer_id,phone):
        self.first_name= first_name
        self.customer_id= customer_id
        self.phone= phone
    
    def display_customer_details(self):
        return f"Name of customer {self.first_name}, Customer ID: {self.customer_id}, phone num: {self.phone}"
    
customer_instance = customer("Vaish", 64973, 9876543210)
print(customer_instance.display_customer_details())  # Accessing customer_id