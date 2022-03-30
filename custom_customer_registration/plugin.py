from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField

class CustomCustomerRegistration(BasePlugin):
    
    def customer_updated(self, customer: "User"):
        print("CustomCustomerRegistration customer_updated hook invoked...",customer)
        