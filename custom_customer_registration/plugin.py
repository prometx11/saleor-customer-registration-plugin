from typing import Any
from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField
from saleor.account.models import Address

class CustomCustomerRegistration(BasePlugin):
    PLUGIN_ID = "plugin.customCustomerRegistration"  # plugin identifier
    PLUGIN_NAME = "Custom Customer Registration"  # display name of plugin
    PLUGIN_DESCRIPTION = "Enables customer registration with address."
    
    def customer_updated(self, customer: "User", previous_value: Any) -> Any:
        print("CustomCustomerRegistration customer_updated hook invoked...",customer.metadata)
        # customer.first_name = "test132"
        # update_fields = ["first_name"]
        # customer.save(update_fields=update_fields)
        if(customer.is_active): 
            print("customer active with metadata type", type(customer.metadata))
            print("address in metadata?", "address" in customer.metadata)
            if("address" in customer.metadata):
                print("customer has billing address in metadata")
                addr = Address()
                addr.first_name = customer.metadata["firstName"]
                addr.last_name=  customer.metadata["lastName"]
                addr.street_address_1 = customer.metadata["street"]
                addr.city =customer.metadata["city"]
                addr.postal_code = customer.metadata["postalCode"]
                addr.country = customer.metadata["country"]
                addr.save()
                addr.user_addresses.add(customer)
                customer.addresses.add(addr)
                customer.default_shipping_address = addr
                customer.default_billing_address = addr
            if("shipping_address" in customer.metadata):
                print("customer has extra shipping address metadata")                      
                sAddr = Address()
                sAddr.first_name = customer.metadata["shipping_firstName"]
                sAddr.last_name=  customer.metadata["shipping_lastName"]
                sAddr.street_address_1 = customer.metadata["shipping_street"]
                sAddr.city =customer.metadata["shipping_city"]
                sAddr.postal_code = customer.metadata["shipping_postalCode"]
                sAddr.country = customer.metadata["shipping_country"]
                sAddr.save()
                
                customer.default_shipping_address = sAddr
                sAddr.user_addresses.add(customer)
                customer.addresses.add(sAddr)
        